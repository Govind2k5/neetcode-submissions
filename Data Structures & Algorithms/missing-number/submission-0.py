class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        realsum = (n*(n-1))//2

        sumarr = 0
        for i in nums:
            sumarr+=i
        return realsum - sumarr