// js object
let myObj = {
  car: "mercedies",
  color: "red",
  weight: "5674 kg",
};

console.log(myObj);
console.log(myObj.car);
console.log(myObj["weight"]);

// nested objects
myObj = {
  car: (main = {
    name: "ankit car",
    weight: "123",
  }),
  eye: (maineye = {
    ramroEye: "no name",
  }),
};

console.log(myObj);
console.log();
console.log(myObj.car);
console.log();
console.log(myObj["car"]["name"]); //ankit car
console.log(myObj.car.name); // ankit car
console.log(myObj.car.weight);
console.log();

// function inside object

let myObj2 = {
  ankit: "bhattarai",
  ujjwal: "bhandari",
  prabesh: "rayamajhi",
  homeFun: function () {
    return this.ankit + " " + this.homeFun;
  },
};

console.log(myObj2.homeFun());
