class TrieNode:
    def __init__(self, data):
        self._data = data
        self._children = [None] * 26
        self._is_ending_char = False


class Trie:
    def __init__(self):
        self._root = TrieNode('/')
    
    def insert(self, text):
        