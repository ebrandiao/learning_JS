// função normal

function sayHi () {
    console.log(" Eu sou a funcção comum - hello world")
}
sayHi()

// Arrow function

const sayHi1 = () => {
    console.log("Eu sou a arrow funtion - hello world")
}
sayHi1()
// As arrow functions facilitam as declarações de funções anônimas como callbacks
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];

const dobro = numbers.map(function(number) {
    return number * 2;
});

console.log(dobro)

const doubles = numbers.map(number => number * 2);

console.log(doubles)