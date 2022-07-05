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