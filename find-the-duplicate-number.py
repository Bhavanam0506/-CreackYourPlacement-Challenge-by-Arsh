class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=[]
        for i in nums:
            n=nums.count(i)
            if n>1:
                return(i)
