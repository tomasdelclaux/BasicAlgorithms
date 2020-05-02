# Time and Space Complexity Analysis

The problem was solved by iteratively reducing the set of possible solutions by limiting them into an upperbound and lowerbound range. Each iteration an estimate was set as the value in between the upperbound and lowerbound.

A while loop is used. An upperbound and lowerbound are initially set, and each iteration an estimate value is calculated as the middle value. Then, in the iteration the middle value square value is compared to the initial number, and the upper and lower limits are set accordingly for the next iteration if the square root has not been found.

Since, each time n is divided by 2 the time complexity is O(logn) and the space complexity is o(1); no datastructure used.

