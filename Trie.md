# Time and Space Complexity of a Trie

The time complexity of the insert operation is linear O(n) adn the search can be done in costant O(1). 

The time complexity of the suffix operation depends on the size of the Trie, as all the subtree of a particular prefix must be traversed. If the size of the subtree is n then the time complexity is O(n).

The space complexity of the trie, in the worst case would be the same as the space complexity of a dictionary, since it would be a flat tree. That would be O(n*w), where n is the number of words and w the length of the words.
However, on average words will have common characters and the space complexity will be reduced. The average space complexity depends of the number of words (let's call them M) and the length of those words (let's call the average length of the word N) Therefore the total space consumed in a trie is M*N.

The insertion method in the TrieNode was not implemented as it was not needed since defaultdicts are being used in the Trie class.