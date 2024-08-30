class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        c = 0
        for x in range(len(nums)):
            if bin(x)[2:].count('1') == k:
                c += nums[x]
        return c
