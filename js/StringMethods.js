// slice(start, end)
// substring(start, end)
// substr(start, length)

// slice() extracts a part of a string and returns the extracted part in a new string.
// The method takes 2 parameters: the start position, and the end position (end not included).
let string = "ujjwal bhandari ishwa";
let part = string.slice(2, 14);
console.log(part);

// JavaScript counts positions from zero.
// First position is 0.
// Second position is 1.

// **********************************************
// JavaScript String substring()

// substring() is similar to slice().
// The difference is that substring() cannot accept negative indexes.

// *************************************************
// JavaScript String substr()
// substr() is similar to slice().

// The difference is that the second parameter specifies the length of the extracted part.

//...................................................
// Replacing String Content
// The replace() method replaces a specified value with another value in a string:

let srt123 = "this is hello ";
console.log(srt123);
mod_srt123 = srt123.replace("hello", "bye");
console.log(mod_srt123);

// To replace case insensitive, use a regular expression with an /i flag (insensitive):
let text = "Please visit Microsoft!";
let newText = text.replace(/MICROSOFT/i, "W3Schools");
console.log(newText);
console.log(" ");

// To replace all matches, use a regular expression with a /g flag (global match):
let tex1t = "Please visit Microsoft and Microsoft!";
let newText1 = text.replace(/Microsoft/g, "W3Schools");
console.log(newText1);

let name = "ujjwal";
console.log(name.toUpperCase());

let bname = "BHANDARI";
console.log(bname.toLocaleLowerCase());

let text1 = "hello";
let text2 = "ji";
console.log(text1.concat(" ", text2));
console.log();

//.........................................
// ECMAScript 2017 added two String methods: padStart() and padEnd() to support padding at the beginning and at the end of a string.

// JavaScript String padStart()
// The padStart() method pads a string with another string:
let text23 = "5";
let padded = text.padStart(4, "x");
console.log(padded);

// The padStart() method is a string method.
// To pad a number, convert the number to a string first.
// See the example below.
let numb = 5;
let text11 = numb.toString();
let padded11 = text.padStart(4, "0");
console.log(padded11);

// JavaScript String padEnd()
// The padEnd() method pads a string with another string:
let text1111 = "5";
let padded111 = text.padEnd(4, "x");
console.log(padded111);

// The padEnd() method is a string method.
// To pad a number, convert the number to a string first.

// padEnd() is an ECMAScript 2017 feature.

// *************************************************
// Extracting String Characters
// There are 3 methods for extracting string characters:
// charAt(position)
// charCodeAt(position)
// Property access [ ]

// he charAt() method returns the character at a specified index (position) in a string:
text = "HELLO WORLD";
let char = text.charAt(0);
console.log(char);

// The charCodeAt() method returns the unicode of the character at a specified index in a string:
// The method returns a UTF-16 code (an integer between 0 and 65535).
text = "HELLO WORLD";
char = text.charCodeAt(0);
console.log(char);

// Property Access
// ECMAScript 5 (2009) allows property access [ ] on strings:
text = "HELLO WORLD";
char = text[0];
console.log(char);

/// ************************************************
// Converting a String to an Array

// A string can be converted to an array with the split() method:
text.split(",");
console.log(text);
