https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j] :
                    nums[i],nums[j]=nums[j],nums[i]
        n=nums.count(0)
        for i in range(n,len(nums)):
            x.append(nums[i])
        for i in range(n):
            x.append(0)
        return(x)
        
