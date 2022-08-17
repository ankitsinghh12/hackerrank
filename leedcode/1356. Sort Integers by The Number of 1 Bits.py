class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_counter = {}
        
        heap = []
        
        for num in arr:
            num_binary = bin(num)[2:]            
            bit_count = num_binary.count('1')            
            heapq.heappush(heap, (bit_count, num))

        results = []
        for _ in range(len(heap)):
            results.append(heapq.heappop(heap)[1])
                
        return results