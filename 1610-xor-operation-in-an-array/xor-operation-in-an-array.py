class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        list1 = []

        for i in range(n):
            list1.append(start)
            start = start + 2

        res = list1[0]

        for i in range(1, len(list1)):
            res = res ^ list1[i]

        return res