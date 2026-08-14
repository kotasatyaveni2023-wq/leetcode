class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=dict()
        for num in arr:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        s1=set()
        for (k,v) in d.items():
            if v in s1:
                return False
            else:
                s1.add(v)
        return True

        