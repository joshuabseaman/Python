// Book Index
// Implement bookIndex(pages), a function that accepts one argument: an array of integers (pages). 
// pages is guaranteed to be in order - there's no need to try to sort it. Similarly, it's guaranteed 
// to be all integer page numbers - no need to try a special case for pages like "xii" or "1158b". 
// The output will be a string that represents those page numbers in the same way they would in a textbook index.

function bookIndex(pages) {
    var stringArray = [];
    var output = "";

    for (var i = 0; i < pages.length; i ++) {
        if (pages[i] + 1 != pages[i + 1]){
            stringArray.push(String(pages[i]));
        }
        else {
            let leftPage = pages[i];
            while (pages[i] + 1 == pages[i + 1]) {
                i ++;
            }
            let rightPage = pages[i];
            stringArray.push(`${leftPage}-${rightPage}`);
        }
    }
    for (var i = 0; i < stringArray.length; i ++) {
        output += stringArray[i];
        if (i != stringArray.length - 1) {
            output += ', ';
        }
    }
    return output;
}

console.log(bookIndex([1,2,3,6,7,9,11,12,13,17]));
console.log(bookIndex([223,224,225,226,227,231,232,233]));
console.log(bookIndex([5,8,11,21,172]));
console.log(bookIndex([41,42,43,44,45]));