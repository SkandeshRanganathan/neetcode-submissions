class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq = {}
        heap = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for key,value in freq.items():
            heapq.heappush(heap , (value , key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count , num in heap]