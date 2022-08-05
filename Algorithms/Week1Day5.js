/* 
Zip Arrays into Map
Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
*/

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
// const expected1 = {
//   abc: 42,
//   3: "wassup",
//   yo: true,
// };

const keys2 = [];
const vals2 = [];
// const expected2 = {};

// Bonus
const bonus_keys1 = [["abc", "def"], 3, "yo"];
const bonus_vals1 = [42, "wassup", true];
// const bonus_expected1 = {
//   abc: 42,
//   def: 42,
//   3: "wassup",
//   yo: true,
// };

const bonus_keys2 = ["abc", 3, "yo", 'something'];
const bonus_vals2 = [42, "wassup", true];
// const bonus_expected2 = {
//   abc: 42,
//   3: "wassup",
//   yo: true,
//   something: null // undefined
// };

// **posibility
// const bonus_keys3 = ["abc", 3, "yo"];
// const bonus_vals3 = [42, "wassup", true, 'something'];
// const bonus_expected3 = {
//   abc: 42,
//   3: "wassup",
//   yo: true,
//   something : 'something'
// };

const bonus_keys3 = ["abc", 3, "yo"];
const bonus_vals3 = [42, "wassup", true, 'something'];
// const bonus_expected3 = False


/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {
    const hashMap = {};

    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        const val = values[i];

        hashMap[key] = val;
    }
    return hashMap;
}

console.log(zipArraysIntoMap(keys1, vals1));
console.log(zipArraysIntoMap(keys2, vals2));
console.log(zipArraysIntoMap(bonus_keys1, bonus_vals1));
console.log(zipArraysIntoMap(bonus_keys2, bonus_vals2));
console.log(zipArraysIntoMap(bonus_keys3, bonus_vals3));


/* 
Invert Hash
A hash table / hash map is an obj / dictionary
Given an object / dict,
return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

// edge cases
const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something: "dicey", computer: "dicey" };
const two_expected2 = { Zaphod: "name", high: "charm", dicey: ["morals", "something", 'computer'] };

const two_obj3 = { name: "Zaphod", charm: "high", morals: "dicey", something: '', airplane: ''};
const two_expected3 = { Zaphod: "name", high: "charm", dicey: "morals", something: 'something', airplane: 'airplane'};
// const two_expected3 = { Zaphod: "name", high: "charm", dicey: "morals", undefined: ['something', 'airplane']};

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {}