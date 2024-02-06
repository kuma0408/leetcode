class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        d = self.d
        for char in word:
            if char not in d:
                d[char] = {}
            
            d = d[char]
        
        d["fin"] = True

    def search(self, word: str) -> bool:
        d = self.d
        for idx, char in enumerate(word):
            if char == ".":
                if idx == len(word)-1:
                    return True
                else:
                    for tmp in d.values():
                        ret = self.search_dot(word[idx+1:], tmp)
                        if ret == True:
                            return True
            elif char in d:
                d = d[char]
            else:
                return False
            
        return "fin" in d

    def search_dot(self, word: str, d: dict) -> bool:
        for idx, char in enumerate(word):
            if char == ".":
                if idx == len(word)-1:
                    return True
                else:
                    for tmp in d.values():
                        ret = self.search_dot(word[idx+1:], tmp)
                        if ret == True:
                            return True
            elif char in d:
                d = d[char]
            else:
                return False        

        return "fin" in d


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)