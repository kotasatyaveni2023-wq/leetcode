class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num: abs(num - x))        
        result = arr[:k]
        result.sort()
        return result
