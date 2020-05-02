# Time and Space Complexity

The solution follows the principle of placing all the 0 at the start of the array and the 2 at the end, so the 1 will be then in the middle.
The time complexity is O(n) and the space complexity is O(1), since it is in place.

Initial positions are set for 0 and 2 in an array, where the initial position for 0 is the first position and for 2 the last one. 
These positions get incremented in their respective directions (right for 0 and left for 2), meaning that 1 are automatically sorted
into the middle:
        next_pos_0 = 0
        next_pos_2 = len(input_list) - 1
