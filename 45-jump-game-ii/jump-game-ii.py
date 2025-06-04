# Farzan Ali Faisal
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # We can use a BFS approach where we check the
        # biggest jump we can take "level" by "level"
        l, r = 0, 0
        count = 0

        while r < len(nums) - 1:
            # farthest computes the greatest jump you can take
            # in this step which is used as the new right pointer.
            farthest = nums[l] + l
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            count += 1
            l = r + 1
            r = farthest
        return count