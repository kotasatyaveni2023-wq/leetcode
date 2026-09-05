class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=[]
        s1=list(s)
        positions=[]
        set1=set("aeiouAEIOU")
        for i in range(len(s)):
            if s[i] in set1:
                vowels.append(s[i])
                positions.append(i)
        vowels.sort()
        j=0
        for v in vowels:
            s1[positions[j]]=v
            j+=1
        return "".join(s1)
        