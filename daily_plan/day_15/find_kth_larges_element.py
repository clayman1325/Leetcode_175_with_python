class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def insert(heap, num):
            if len(heap) < k:
                heap.insert(0, num)
            else:
                heap[0] = num
            idx = 0
            while(idx < len(heap) - 1):
                if heap[idx] > heap[idx+1]:
                    aux = heap[idx+1]
                    heap[idx+1] = heap[idx]
                    heap[idx] = aux
                idx += 1
            return heap

        heap = []

        for num in nums:
            if len(heap) < k or num > heap[0]:
                heap = insert(heap, num)
        return heap[0]