//Always Hungry
console.log("***********Always Hungry************")
function alwaysHungry(arr) {
    var count=0
    for (var i=0;i<arr.length;i++){
        if(arr[i]=="food"){
            console.log("yummy")
            count++
        }
    }
    if(count==0){
        console.log("I'm hungry")
    }
}
alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]);
//High Pass Filter
console.log("********High Pass Filter***********")
function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i =0;i<arr.length;i++){
        if(arr[i]>cutoff){
             filteredArr.push(arr[i]);
        }

    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]


//Better than average
console.log("**********Better than average********")

function betterThanAverage(arr) {
    var sum = 0;
    var count = 0
    for(var i=0;i<arr.length;i++){
        sum=sum+arr[i]
    }
   
    var count = 0
    var avg =sum/arr.length
    for(var j=0;j<arr.length;j++){
        if(arr[j]>avg){
            count++
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4

//Array Reverse
console.log("**************Array Reverse**********")


function reverse(arr) {
    var start =0;
    var end=arr.length-1
    while(start<end/2){
        var reverse =arr[start]
        arr[start]=arr[end]
        arr[end]=reverse
        start++
        end--

    }
    return arr;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]


//Fibonacci Array
console.log("*************Fibonacci Array*************")


function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    for(var i=2;i<n;i++){
        fibArr.push(fibArr[i-2]+fibArr[i-1])

    }
    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
