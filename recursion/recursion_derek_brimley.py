def factorial(num):
    if num == 1:
        return 1
    else:
        result = factorial(num-1) * num
        return result

try:
    print(factorial(5))
except:
    print("Maximum recursion depth reached!")
try:
    print(factorial(8))
except:
    print("Maximum recursion depth reached!")
try:
    print(factorial(20))
except:
    print("Maximum recursion depth reached!")
try:
    print(factorial(100))
except:
    print("Maximum recursion depth reached!")
try:
    print(factorial(999))
except:
    print("Maximum recursion depth reached!")