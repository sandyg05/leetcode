"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_bound = 2**31-1
        min_bound = -2**31
        
        
        res = ""
        front_flag = True
        str = str.strip()
        sign = 1
        for char in str:
            if front_flag and (char not in ("-","+") and (char < "0" or char >"9")):
                return 0
            
            elif front_flag and char == "-":
                front_flag = False
                sign *= (-1)
            
            elif front_flag and char == "+":
                front_flag = False
            
            elif char >= "0" and char <= "9":
                front_flag = False
                res += char
            
            elif (not front_flag) and (char < "0" or char > "9"):
                break
        
        if not res:
            return 0
        elif sign > 0:
            return min(max_bound, int(res))
        elif sign < 0:
            return max(min_bound,sign * int(res))

                
            



class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        flag = ""
        str = str.strip(" ")
        if not str:
            return 0
        
        if str[0] == "-" or str[0] == "+":
            flag = str[0]
            str = str[1:]

        if not str:
            return 0
        
        if not str[0].isdecimal():
            return 0
        else:
            i,num = 0,0
            while i < len(str) and str[i].isdecimal():
                num = 10 * num + int(str[i])
                i += 1
            
            if flag == "-":
                num = - num
        
            if num > INT_MAX:
                num = INT_MAX
            elif num < INT_MIN:
                num = INT_MIN

            return num
            
        
            
        
            
        
        