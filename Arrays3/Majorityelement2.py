class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        value1 = nums[0]
        value2 = -1
        count1 = 1
        count2 = 0

        for i in range(1, n):
            if nums[i] == value1:
                count1 += 1
            elif nums[i] == value2:
                count2 += 1
            elif count1 == 0:
                value1 = nums[i]
                count1 = 1
            elif count2 == 0:
                value2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        c1 = c2 = 0

        for num in nums:
            if num == value1:
                c1 += 1
            elif num == value2:
                c2 += 1

        res = []

        if c1 > n / 3:
            res.append(value1)
        if c2 > n / 3:
            res.append(value2)

        return res