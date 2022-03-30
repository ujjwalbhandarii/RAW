// there are 6 primitive dataType in js
undefined;
Boolean;
Number;
String;
BigInt; // 2020 or 2019 ko echma script ma aayako theo
Symbol; // echma script 2015

let myName = "ujjwal";
console.log(typeof myName); // string

myName = 15;
console.log(typeof myName); // number

myName = 15.6;
console.log(typeof myName); // number

myName = true;
console.log(typeof myName); // boolean

myName = { firstName: "ujjwal", lastName: "bhandaeri" };
console.log(typeof myName); // object

let y = 123e5; // 12300000
let z = 123e-5; // 0.00123
console.log(y);

const myArr = ["ankit", "ujjwal", "prabesh"]; //array
console.log(myArr);
console.log(typeof myArr); // returns object
console.log(myArr[2]); // prabesh

const myObj = {
  ujjwal: "bhandari",
  ankit: "bhatarai",
  prabesh: "rayamajhi",
};

console.log(myObj);
console.log(typeof myObj); // object

// Undefined
// In JavaScript, a variable without a value, has the value undefined. The type is also undefined.
let car;
console.log(car); // undefined

car = "";
console.log(car);
console.log(typeof car);
