class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0:
            return False
        else:
            nums = list(str(x))
            for num in range(len(nums) / 2):
                end = len(nums) - 1 - num
                tmp = nums[num]
                nums[num] = nums[end]
                nums[end] = tmp

            length = len(nums)
            new_nums = list(str(x))
            for index in range(length):
                if nums[index] != new_nums[index]:
                    return False
            return True