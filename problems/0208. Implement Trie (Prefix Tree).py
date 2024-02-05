class Trie:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        d = self.d
        for char in word:
            if char in d:
                d = d[char]
                continue
            else:
                d[char] = {}
                d = d[char]

        # set mark which means the end of the word
        d["fin"] = 0

    def search(self, word: str) -> bool:
        d = self.d
        for char in word:
            if char not in d:
                return False
            else:
                d = d[char]
        
        if "fin" in d:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        d = self.d
        for char in prefix:
            if char not in d:
                return False
            else:
                d = d[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)