# Time and Space Complexity Analysis

The key to this problem is that if the array is divided into two separate arrays each iteration (leftHalf, rightHalf), one of them will always be sorted, and hence can be searched with the find_sorted function. 
Since, one of the arrays is sorted, it can easily be found if the value would reside in the sorted array by checking the first and last value. If the value, instead lies in the unsorted array, the process can then 
be repeated, whereby the unsorted array is again divided to produce one sorted array and one unsorted.

Since in each iteration the array space is divided by 2, the time complexity is O(logn) and the space complexity is O(1).

