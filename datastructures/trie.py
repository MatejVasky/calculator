from typing import TypeVar, Generic, Dict, Optional

T = TypeVar('T')

class TrieNode(Generic[T]):
    """A generic trie implementation"""

    def __init__(self, value : Optional[T] = None):
        """Creates a trie node"""
        self.value = value
        self.__children : Dict[str, 'TrieNode[T]'] = {}

    def __getitem__(self, c : str) -> 'Optional[TrieNode[T]]':
        """Finds the child node corresponding to a given character. Returns None if key is not found."""
        # Type check
        if not isinstance(c, str):
            raise TypeError("Trie key must be of type str")
        # Index must be of length 1
        if len(c) != 1:
            raise KeyError("Trie key must be of length 1")
        # Look node up and return
        if c in self.__children:
            return self.__children[c]
        return None
    
    def __setitem__(self, c : str, node : 'TrieNode[T]') -> None:
        """Sets the child node corresponding to a given character"""
        # Type check
        if not isinstance(c, str):
            raise TypeError("Trie key must be of type str")
        # Index must be of length 1
        if len(c) != 1:
            raise KeyError("Trie key must be of length 1")
        # Set node
        self.__children[c] = node
    
    def __contains__(self, key : str) -> None:
        """Returns True, if the trie contains key"""
        # Type check
        if not isinstance(key, str):
            raise TypeError("Trie key must be of type str")
        # Traverse the trie
        node = self
        for c in key:
            node = node[c]
            # If you leave the trie, return False
            if not node:
                return False
        # Check if the node contains a value. If yes, then the value is contained, otherwise, it is not
        return node.value != None
    
    def append_key(self, key : str, val : T) -> None:
        """Adds key to the trie and sets its value to val"""
        # Type check
        if not isinstance(key, str):
            raise TypeError("Trie key must be of type str")
        # Traverse the trie
        node = self
        for c in key:
            new_node = node[c]
            # If you leave the trie, create a new node
            if not new_node:
                new_node = TrieNode()
                node[c] = new_node
            # Move down
            node = new_node
        # Set value
        node.value = val

    def find_longest_match(self, s : str, start : int = 0, end : Optional[int] = None, step : int = 1) -> tuple[int, T]:
        """Finds the longest substring of s, that this trie contains as a key. Returns the index of the end (i.e. the index of the first character not contained in the match) and the match's value.
        start (inclusive), end (exclusive, defaults to len(s) if left as None) and step specify the part of the string, that should be matched"""
        # Check arguments
        if end == None:
            end = len(s)
        if not isinstance(s, str):
            raise TypeError("s must be of type str")
        if not isinstance(start, int):
            raise TypeError("start must be of type int")
        if not isinstance(end, int):
            raise TypeError("end must be of type int")
        if not isinstance(step, int):
            raise TypeError("step must be of type int")
        if step == 0:
            raise ValueError("step must not be zero")
        
        # Variable initialization
        trie_node = self
        match_end = start
        match_val = None

        # Main loop
        for i in range(start, end, step):
            # If you run out of letters, end the loop
            if i < -len(s) or i >= len(s):
                break
            # Move down the trie
            trie_node = trie_node[s[i]]
            # If you leave the trie, end
            if trie_node == None:
                break
            # If the node contains a value, increase the length of the longest match
            if trie_node.value != None:
                match_end = i + step
                match_val = trie_node.value

        # Return
        return match_end, match_val
        