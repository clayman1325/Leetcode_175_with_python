class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in list(word):
            if not trie.get(char):
                trie[char] = { }
            trie = trie[char]
        trie["*"] = ""

    def search(self, word: str) -> bool:
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    if ch == '.':
                        for x in node:
                            if x != '*' and search_in_node(word[i + 1:], node[x]):
                                return True
                    return False
                else:
                    node = node[ch]
            return '*' in node
        return search_in_node(word, self.trie)

    def search_any_words(self, trie, word):
        result = False
        for i in range(len(word)):
            char = word[i]
            if not trie.get(char):
                if char == ".":
                    for key in trie:
                        if key != "*" and self.search_any_words(trie[key], word[i+1:]):
                            return True
                return False
            else:
                trie = trie[char]
        return True




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# trie = {}

#  trie = {
#      a: {b: {}}
#  }