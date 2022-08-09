/* 
Given a string,
return a new string with the duplicates excluded
Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    newStr = ""
    for(i=0;i<str.length;i++){
        if(str.charAt(i) !== str.charAt(i + 1)){
            newStr += str.charAt(i)
        }else if(str.charAt(i) == str.charAt(i + 1)){
            continue
        }
    }
    return newStr
}

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));


/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/

const str_1 = "hello";
const expecte_1 = "olleh";

const str_2 = "hello world";
const expecte_2 = "olleh dlrow";

const str_3 = "abc def ghi";
const expected_3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(string) {
    let str = ''
    for (let i = string.length-1; i >= 0; i--) {
        str+=string[i]
    }return str
}

console.log(reverseWords(str_1));
console.log(reverseWords(str_2));
console.log(reverseWords(str_3));


/* 
Reverse Word Order
Given a string of words (with spaces)
return a new string with words in reverse sequence.
*/

const str_one = "This is a test";
const expected_one = "test a is This";

const str_two = "hello";
const expected_two = "hello";

const str_three = "   This  is a   test  ";
const expected_three = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(string) {
    let arr = string.split(' ')
    let newStr = []
    for (let i = arr.length-1; i >= 0; i--) {
        newStr.push(arr[i])
    }
    return newStr.join(' ')
}

console.log(reverseWordOrder(str_one));
console.log(reverseWordOrder(str_two));
console.log(reverseWordOrder(str_three));