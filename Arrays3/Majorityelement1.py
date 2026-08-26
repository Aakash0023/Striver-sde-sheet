class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = nums[0]
        count = 1
        ranges = len(nums)
        for i in range (1,ranges):
            if nums[i] == value:
                count = count + 1
            else:
                if count == 0:
                    value = nums[i]
                    count = 1
                else:
                    count = count -1
        return value


        