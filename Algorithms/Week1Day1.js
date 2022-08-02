/* 
String: Reverse
Given a string,
return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

function reverseString(str) {   //Create a function for the reversed string
    var newString = ""    //create a variable for the new string
    for (var i = str.length - 1; i >= 0; i--) {   //create a for loop that checks the length of the string and goes to the end of the last index and iterates from the end going backwards
        newString += str[i]   //takes the value of the for loop and sets it equal to the value to the new string
    }
    return newString   //Gives you back the new string that was created
}
console.log(reverseString("creature"))   //Logging the reverse string to the terminal
console.log(reverseString("dog"))
console.log(reverseString("hello"))
console.log(reverseString(""))

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 * 
 * psuedo code # 1
 * - create a function that takes in a string
 * - turn it into an array -> split function
 * - call the reverse function
 * - call the join function
 * 
 * psuedo code # 2
 * - create a function that takes in a string
 */
// function reverseString(str) {}

/*****************************************************************************/


/* 
Acronyms
Create a function that, given a string, returns the string’s acronym 
(first letter of each word capitalized). 
Do it with .split first if you need to, then try to do it without
*/

const two_str1 = "object oriented programming";
const two_expected1 = "OOP";

// The 4 pillars of OOP
const two_str2 = "abstraction polymorphism inheritance encapsulation";
const two_expected2 = "APIE";

const two_str3 = "software development life cycle";
const two_expected3 = "SDLC";

// Bonus: ignore extra spaces
const two_str4 = "  global   information tracker    ";
const two_expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
// function acronymize(str) {}

function acronymize(str) {
    var acroArr =[]
    var acro 
    acroArr.push(str.charAt(0));
    for(var i = 0; i < str.length; i++){
        if(str.charAt(i) == " " && (i + 1) != 0) {
            acroArr.push(str.charAt(i+1));
        }
    }
    acro = acroArr.join("");
    return acro.toUpperCase();
}

console.log(acronymize(two_str1))
console.log(acronymize(two_str2))
console.log(acronymize(two_str3))
console.log(acronymize(two_str4))