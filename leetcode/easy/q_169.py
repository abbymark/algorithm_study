class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        max_count = 0
        major_num = None
        for k,v in count.items():
            if v > max_count:
                max_count = v
                major_num = k
        return major_num