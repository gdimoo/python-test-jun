"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        result = 1
        if number < 0:
            return 'number can not be negative'
        else:
            for i in range(1,number+1):
                result *= i
                
            count_zero = 0
            
            for j in str(result)[::-1]:
                if j == '0':
                    count_zero += 1
                else:
                    return count_zero
