class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        heap=[(-freq,char)for char,freq in counter.items()]
        heapq.heapify(heap)
        result=''
        while heap:
            freq,char=heapq.heappop(heap)
            result+=char*-freq
        return result