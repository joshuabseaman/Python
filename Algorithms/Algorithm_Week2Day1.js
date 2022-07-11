function arrayOddOccurances(arr){
    for (var i = 0; i < arr.length; i++){
        var count = 0;
        for(var j = 0; j< arr.length; j++){
            if (arr[i] == arr[j]){
                count ++;
            }
        }
            if (count % 2 != 0){
                return arr[i];
            }
    }
    return -1;
}

console.log(arrayOddOccurances([7,4,3,6,6,3,2,3,4,7,3]));
console.log(arrayOddOccurances([5,6,7,7,6,4,6,4,6]));
console.log(arrayOddOccurances([26,34,26]));
console.log(arrayOddOccurances([7,3,7,4,7,4,7,3,7,4,4]));