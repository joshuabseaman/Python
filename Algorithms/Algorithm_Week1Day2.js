// Array Balance Index
// Given an array of integers, return the index of the array item where the sum of all the items to the left of that item is equal to the sum of all the items to the right of that item are equal. For example, given the array:

// [3, 4, 9, 2, 4, -2, 3]

// we would return 2. The items to the left of index 2 (3 and 4) and the items to the right of index 2 (2, 4, -2 and 3) both add up to the same number (7). If no item in the array exists where the items to the left and right of any given item would equal the same sum, return -1 instead.

function arrayBalanceIndex(arr) {
    if ((arr.length <= 1)) {
        return -1
    }
    var left = 0;
    var right = 0;
    for(var j = 1; j < arr.length; j++){
        right += arr[j];
    }
    for(var i = 0; i < arr.length; i++){
        if (left == right){
            return i
        }
        right -= arr[i+1]
        left += arr[i]
    }
    return -1;
}

console.log(arrayBalanceIndex([3, 4, 9, 2, 4, -2, 3]));