// post increment:: a++
// pre increment::  ++a   prefix

// post decrement:: a--
// pre decrement::  --a

let num = 12;
let newNum = num++;
console.log(num); // 13
console.log(newNum); // 12
console.log();

newNum = --num;
console.log(newNum); //12
console.log(num); //12
console.log();

newNum = num--;
console.log(newNum); // 12
console.log(num); //11

num = 12;
num++;
console.log(num); // 13
