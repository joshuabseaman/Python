// Bubble Sort
// Given an array of integers, perform a bubble sort: for each pair of items in the array, determine which item is
// larger, then move that item to the right. Once the largest possible item is at the end of the array, perform the
// same operation again, and again, until the entire array is sorted. There's technically no need to return anything
// in many cases, but for this example, go ahead and return the array once it's sorted - the test cases are expecting it.

export function bubbleSort(arr) {
    var temp = 0;
    for (var i = 0; i < arr.length-1; i++){
        for (var j = 0; j <arr.length-1; j++){
            if (arr[j] > arr[j+1]){
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
    return arr
}