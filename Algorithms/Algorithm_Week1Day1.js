// Rotate Array
// Implement rotateArr(arr, shiftBy), a function that accepts an array and a number to shift it by. Shift arr's values to the right by that amount. 'Wrap around' any values that shift off array's end to the other side, so that no data is lost, and operate in-place - do not return a new array, but modify the array passed in. If the shiftBy value is longer than the array length, that's okay - it can wrap around, then wrap again and again and again.

function rotateArray(arr, shiftBy){
var count = 0;
if(shiftBy < 0){
count = shiftBy;
    while(count < 0){
        arr.push(arr[0]);
        arr.shift();
        count++
    }

} else {
    while(count < shiftBy){
        arr.unshift(arr[arr.length-1]);
        arr.pop();
        count++;
    }
}
return arr;
}

console.log(rotateArray([1,2,3,4,5], 2));