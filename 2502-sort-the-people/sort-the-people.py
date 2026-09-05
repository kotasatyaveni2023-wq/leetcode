class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if heights[i] < heights[j]:
                    temp = names[i]
                    names[i] = names[j]
                    names[j] = temp
                    t = heights[i]
                    heights[i] = heights[j]
                    heights[j] = t
        return names