"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution:
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def new_number(n):
            total = 0
            while n:
                n,rem = divmod(n,10)
                total += rem ** 2
            return total        
        
        visited = set()

        while True:
            _new = new_number(n)
            if _new == 1:
                return True
            if _new in visited:
                return False
            visited.add(_new)
            n = _new


class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square(num):
            return num ** 2
        
        
        def get_digits(num):
            res = []
            while num:
                res.append(num % 10)
                num //= 10
            return res
                
        
        visited = set([n])
        
        while True:
            n = sum(map(square, get_digits(n)))
            if n == 1:
                return True
            else:
                if n not in visited:
                    visited.add(n)
                else:
                    return False
            
         
        
            
            