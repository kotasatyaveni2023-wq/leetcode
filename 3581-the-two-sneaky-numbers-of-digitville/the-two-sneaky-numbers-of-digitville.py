class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d1=dict()
        for num in nums:
            if num not in d1:
                d1[num]=1
            else:
                d1[num]+=1
        res=[]
        for (k,v) in d1.items():
            if v==2:
                res.append(k)
        return res
        