class Trie:
    def __init__(self):
        self.terminal_value =  "*"
        self.trie = {}


    def insert(self, word: str) -> None:
        branch = self.trie
        response = branch

        for char in word:
            if(not branch.get(char)):
                branch[char] = {}
            branch = branch[char]
        branch = "*"
        self.trie = response

    def search(self, word: str) -> bool:
        test = self.trie
        for char in word:
            if(not test.get(char)): return False
            test = test[char]

        return True