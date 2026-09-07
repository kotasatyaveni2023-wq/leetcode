class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        length=len(words)
        res=[]
        for i in range(length):
            if words[i].find(x)!=-1:
                res.append(i)
        return res
        