import xml.etree.ElementTree as ET
import sqlite3
from sqlite3 import Cursor
from typing import List, Optional


ARTIST_TABLE_NAME = "Artist"
GENRE_TABLE_NAME = "Genre"
ALBUM_TABLE_NAME = "Album"
TRACK_TABLE_NAME = "Track"


class Song:
    def __init__(self, element_tree: ET):
        self.genre = self._lookup(element_tree, "Genre")
        self.artist = self._lookup(element_tree, "Artist")
        self.album = self._lookup(element_tree, "Album")
        self.title = self._lookup(element_tree, "Name")
        self.len = self._lookup(element_tree, "Total Time")
        self.rating = self._lookup(element_tree, "Rating")
        self.count = self._lookup(element_tree, "Play Count")

    def _lookup(self, element_tree: ET, key: str):
        found = False
        for child in element_tree:
            if found:
                return child.text
            if child.tag == "key" and child.text == key:
                found = True

        return None

    def __repr__(self):
        return f"{{genre: {self.genre}, artist: {self.artist}, album: {self.album}, name: {self.title}, len: {self.len}, rating: {self.rating}, count: {self.count}"


def drop_table_artist(cursor: Cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist;")


def create_table_artist(cursor: Cursor):
    cursor.execute(
        f"""
        CREATE TABLE {ARTIST_TABLE_NAME} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
    """
    )


def drop_table_genre(cursor: Cursor):
    cursor.execute("DROP TABLE IF EXISTS Genre;")


def create_table_genre(cursor: Cursor):
    cursor.execute(
        """
        CREATE TABLE Genre (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
    """
    )


def drop_table_album(cursor: Cursor):
    cursor.execute("DROP TABLE IF EXISTS Album;")


def create_table_album(cursor: Cursor):
    cursor.execute(
        f"""
        CREATE TABLE {ALBUM_TABLE_NAME} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER,
            title TEXT UNIQUE NOT NULL
        );
    """
    )


def drop_table_track(cursor: Cursor):
    cursor.execute("DROP TABLE IF EXISTS Track;")


def create_table_track(cursor: Cursor):
    cursor.execute(
        """
        CREATE TABLE Track (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            album_id  INTEGER,
            genre_id  INTEGER,
            len INTEGER, rating INTEGER, count INTEGER
        );
    """
    )


def get_songs(xml_filename: str) -> List[Song]:
    parsed_xml = ET.parse(xml_filename)

    xml_songs = parsed_xml.findall("dict/dict/dict")

    songs = [Song(element) for element in xml_songs]

    return songs


def insert_artist(cursor: Cursor, name: str):
    if name is not None:
        if not artist_exists(cursor, name):
            cursor.execute(
                f"""
                INSERT INTO {ARTIST_TABLE_NAME} (name) VALUES (?);
            """,
                (name,),
            )


def artist_exists(cursor: Cursor, name: str):
    cursor.execute(
        f"""
        SELECT EXISTS(SELECT 1 from {ARTIST_TABLE_NAME} WHERE name = ?) 
    """,
        (name,),
    )

    result = cursor.fetchone()[0]

    return result == 1


def get_artist_id(cursor: Cursor, name: str) -> Optional[int]:
    cursor.execute(
        f"""
        SELECT id FROM {ARTIST_TABLE_NAME} WHERE name = ?;
    """,
        (name,),
    )

    result = cursor.fetchone()

    if result is not None:
        return result[0]
    else:
        return None


def insert_album(cursor: Cursor, artist_name: str, title: str):
    if title is not None and not album_exists(cursor, title):
        artist_id = get_artist_id(cursor, artist_name)

        cursor.execute(
            f"""
            INSERT INTO {ALBUM_TABLE_NAME} (artist_id, title) VALUES (?, ?);
        """,
            (artist_id, title),
        )


def album_exists(cursor: Cursor, title: str) -> bool:
    cursor.execute(
        f"""
        SELECT EXISTS(SELECT 1 from {ALBUM_TABLE_NAME} WHERE title = ?); 
    """,
        (title,),
    )

    result = cursor.fetchone()[0]
    return result == 1


def get_album_id(cursor: Cursor, title: str) -> Optional[int]:
    cursor.execute(
        f"""
        SELECT id FROM {ALBUM_TABLE_NAME} WHERE title = ?;
    """,
        (title,),
    )

    result = cursor.fetchone()
    if result is not None:
        return result[0]
    return None


def insert_genre(cursor: Cursor, name: str):
    if name is not None and not genre_exists(cursor, name):
        cursor.execute(
            f"""
            INSERT INTO {GENRE_TABLE_NAME} (name) VALUES (?);
        """,
            (name,),
        )


def genre_exists(cursor: Cursor, name: str) -> bool:
    cursor.execute(
        f"""
            SELECT EXISTS(SELECT 1 from {GENRE_TABLE_NAME} WHERE name = ?); 
        """,
        (name,),
    )

    result = cursor.fetchone()[0]
    return result == 1


def get_genre_id(cursor: Cursor, name: str) -> Optional[int]:
    cursor.execute(
        f"""
        SELECT id FROM {GENRE_TABLE_NAME} WHERE name = ?
    """,
        (name,),
    )

    result = cursor.fetchone()
    if result is not None:
        return result[0]
    return None


def insert_track(cursor: Cursor, song: Song):
    album_id = get_album_id(cursor, song.album)
    genre_id = get_genre_id(cursor, song.genre)

    cursor.execute(
        f"""
        INSERT INTO {TRACK_TABLE_NAME} (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?) 
    """,
        (song.title, album_id, genre_id, song.len, song.rating, song.count),
    )


if __name__ == "__main__":
    connection = sqlite3.connect("trackdb.sqlite")

    cursor = connection.cursor()

    drop_table_artist(cursor)
    create_table_artist(cursor)

    drop_table_genre(cursor)
    create_table_genre(cursor)

    drop_table_album(cursor)
    create_table_album(cursor)

    drop_table_track(cursor)
    create_table_track(cursor)

    songs = get_songs("Library.xml")

    for song in songs:
        insert_artist(cursor, song.artist)

        insert_genre(cursor, song.genre)

        insert_album(cursor, song.artist, song.album)

        insert_track(cursor, song)

    connection.commit()
