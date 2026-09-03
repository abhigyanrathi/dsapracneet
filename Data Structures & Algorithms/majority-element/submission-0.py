class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        counts = Counter(nums)
        for num, count in counts.items():
            if count > n//2:
                return num