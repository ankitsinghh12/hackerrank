#https://medium.com/@edward.zhou/leet-code-338-counting-bits-explained-python3-solution-cda868e37d15
class Solution:
    def countBits(self, num: int) -> List[int]:
        results = [0]
        
        for i in range(1, num+1):
            results.append(results[i & (i-1)] + 1)
            
        return results