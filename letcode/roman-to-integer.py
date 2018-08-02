class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_key = dict()
        int_key['I'] = 1
        int_key['V'] = 5
        int_key['X'] = 10
        int_key['L'] = 50
        int_key['C'] = 100
        int_key['D'] = 500
        int_key['M'] = 1000
        int_key['IV'] = 4
        int_key['IX'] = 9
        int_key['XL'] = 40
        int_key['XC'] = 90
        int_key['CD'] = 400
        int_key['CM'] = 900

        number = s
        result = 0
        num_list = list(number)
        length = len(num_list)
        index = 0
        while index < length:
            if index < length - 1:
                tmp = num_list[index] + num_list[index+1]
                if tmp in int_key.keys():
                    index += 1
                else:
                    tmp = num_list[index]
            else:
                tmp = num_list[index]
            index += 1
            result += int_key[tmp]
        return result