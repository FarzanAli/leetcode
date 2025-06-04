class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l, r = 0, 0
        count = 0

        while r < len(nums) - 1:
            farthest = nums[l] + l
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            count += 1
            l = r + 1
            r = farthest
        return count