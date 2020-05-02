# Time And Space Complexity Analysis

The time complexity of the insert operation is linear O(n) adn the search can be done in costant O(1). 

The time complexity of the find operations also depends on the length of the word O(w). The space complexity is O(1)

The space complexity of the trie, in the worst case would be the same as the space complexity of a dictionary, since it would be a flat tree. That would be O(n*w), where n is the number of words and w the length of the words.
However, on average words will have common characters and the space complexity will be reduced. The average space complexity depends of the number of paths (let's call them M) and the number of subpaths that results from the split fuinctions (let's call the average number of subpaths N) Therefore the total space consumed in a trie is M*N.

The insertion method in the RouterTrieNode was not implemented as it was not needed since defaultdicts are being used in the RouteTrie class. Also, the splitpath method in the Router class, was not implemented as
the split path is implemented in each method of the RouteTrie class

