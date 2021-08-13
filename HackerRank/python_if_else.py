import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().sprit())
    check_exp = {True : "Not Weird", False : "Weird"}

    print(check_exp[n % 2 == 0 and (n in range(2, 6) or n>20)])
