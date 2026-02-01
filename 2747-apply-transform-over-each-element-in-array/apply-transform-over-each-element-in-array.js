/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    

    const lst=[];
    for (let i =0 ; i< arr.length ;i++){
        lst[i]=fn(arr[i],i);

    }
    return lst 
};