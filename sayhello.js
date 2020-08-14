class Person {
  constructor(altura, color) {
    this.altura = altura
    this.color = color
  }
  sayHello(name) {
    alert(`Hello ${name}! My height is ${this.altura} and my color is ${this.color}.`)
  }
}

const pricilla = new Person(155, "white")
const marcus = new Person(176, "green")

console.log(pricilla)
console.log(marcus)
