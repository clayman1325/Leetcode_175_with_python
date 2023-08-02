class Trie:
    def __init__(self):
        self.terminal_value =  "*"
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie["*"] = ""

    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            if char in trie:
                trie = trie[char]
            else:
                return False
        return  "*" in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# insert:
# if the char is not present in root, add char to root children
# if cur word is in trie key move to next word and append when the word is not find or reach finish of the branch

# search
# look for coincidence in the cur_word and trie current key until find finish

# { a: {p: {p: {l: {e: * }}}





# cat car celu  dog diamante

#      {
#          c: [{e:{l:{u:{}}}}, {a: [{r: {}}, {t:{}}}
#          d: [{i:{a:{]}}}, {o: {g: {}}}]
#     }