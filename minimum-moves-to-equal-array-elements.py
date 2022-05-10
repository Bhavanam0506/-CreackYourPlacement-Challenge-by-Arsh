class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = min(nums)
        moves = 0
        for x in nums:
            moves += (x - n)
        return moves
