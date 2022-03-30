// 1. difference betweeen null and undefined?

// null
let Person = null;
console.log(Person);

// undefined
let him;
console.log(him);
console.log(typeof him);
console.log();

// what is NaN?
// not a number
let a = "hari";
let b = "ram";
c = 32;
console.log(a - b); //output will be not a number(NaN)
console.log(isNaN(a)); // true
console.log(isNaN(c)); // false
console.log();

// NaN == NaN
console.log(NaN == NaN); // false

//Number.Nan == NaN
console.log(Number.Nan == NaN); // false

// isNaN(NaN)
console.log(isNaN(NaN)); // true

// isNaN(Number.NaN == NaN)
console.log(isNaN(Number.NaN == NaN)); // false

// Number.isNaN(NaN);
console.log(Number.isNaN(NaN)); // true
