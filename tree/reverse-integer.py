class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        nums = list(str(x))
        for num in range(len(nums) / 2):
            end = len(nums) - 1 - num
            tmp = nums[num]
            nums[num] = nums[end]
            nums[end] = tmp

        result = 0
        for num in nums:
            if num == "-":
                result *= -1
                break
            result = result * 10 + int(num)
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result

