class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set1=set(nums[0])
        for row in nums:
            set1=set1.intersection(set(row))
        l1=list(set1)
        l1.sort()
        return l1