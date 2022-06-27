class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(N log N) time and O(1) space
        hq = []
        heapq._heapify_max(stones)
        while len(stones)>=2:
            max1 = heapq._heappop_max(stones)
            max2 = heapq._heappop_max(stones)
            if max1-max2>0:
                heapq.heappush(stones,max1-max2)
                heapq._heapify_max(stones)
            else:
                if len(stones)==0:
                    return max1-max2
        return heapq._heappop_max(stones)