# Các hàm trong toán học

import math
from math import *
import time

my_num = -5
def input_slow(prompt , delay = 0.05):
    for i in prompt:
        print(i , end = '' , flush = True)
        time.sleep(delay)
    return input()
# print(max(1 , 9 , 9 , 5 , 10))
name = input_slow("Nhập tên của bạn: ")
print(floor(3.5))