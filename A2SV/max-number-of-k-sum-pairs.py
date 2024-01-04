class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #time: O(nlogn)
        #space: O(1)

        nums.sort()
        i = 0
        j = len(nums) - 1
        count  = 0
        while i < j and j > 0:
            if nums[i] + nums[j] > k:
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
    
        return count


        