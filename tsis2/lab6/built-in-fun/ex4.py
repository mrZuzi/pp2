import math
import time

def sqrt_after_ms(num, ms):
    time.sleep(ms/1000)
    return math.sqrt(num)
  
num = int(input())
ms = int(input())
result = sqrt_after_ms(num, ms)
print(f"Square root of {num} after {ms} milliseconds is {result}")