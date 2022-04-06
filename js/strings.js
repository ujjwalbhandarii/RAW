// escape sequence

// \b	Backspace
// \f	Form Feed
// \n	New Line
// \r	Carriage Return
// \t	Horizontal Tabulator
// \v	Vertical Tabulator

let x = "njsndnsdnksd";
console.log(x.length);

// slice(start, end)       -- can accept neg values
// substring(start, end)   -- cannot accept neg values
// substr(start, length)

let myName = "ujjwal bhandari";
console.log(myName.slice(0, 7)); // ujjwal

//replace() method replaces a specified value with another value in a string

let anotherName = "my name is ujjwal";
console.log(anotherName.replace("my", "his")); // his name is ujjwal

let upperCheck = "ujjwal";
let lowerCheck = "BHANDARI";
console.log(upperCheck.toUpperCase()); //UJJWAL
console.log(lowerCheck.toLowerCase());

// concat()

let text1 = "hy";
let text2 = "babe";
let text3 = "";
console.log(text3.concat(text1, " ", text2));

// trim()

let usingTrim = "           This        Is      Triming";
let testingTrim = usingTrim.trim();
console.log(testingTrim.length);
console.log("");

let strin1 = "hy this is a sring";
console.log(strin1.length);

let str2 = "this is my name.\nwhat the hell you dont know my name";
console.log(str2);

// use of new keyboard

let str12 = "ram";
let y = new String("ram");

console.log(typeof str12 + " ", typeof y); // + can also be used and ,(comma) can also be used

// Do not create Strings objects.
// The new keyword complicates the code and slows down execution speed.
// String objects can produce unexpected results:
