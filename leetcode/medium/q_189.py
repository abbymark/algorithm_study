class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## Time limit exceeded
        # for j in range(k):
        #     tmp = nums[-1]
        #     for i in range(0, len(nums)):
        #         tmp2 = nums[i]
        #         nums[i] = tmp
        #         tmp = tmp2
        k = k % len(nums)
        tmp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = tmp
                