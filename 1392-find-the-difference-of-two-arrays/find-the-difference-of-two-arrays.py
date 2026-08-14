class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[]
        s1=set(nums1)
        s2=set(nums2)
        l1=list(s1.difference(s2))
        l2=list(s2.difference(s1))
        result.append(l1)
        result.append(l2)
        return result 
        