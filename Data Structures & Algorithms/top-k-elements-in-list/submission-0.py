from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  
        pair = []
        for num, freq in count.items():
            pair.append((freq, num))

        pair.sort(reverse = True)
        res = []
        for freq, num in pair[:k]:
            res.append(num)
        return res      
