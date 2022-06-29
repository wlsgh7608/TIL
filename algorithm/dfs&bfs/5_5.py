def factorial_function(n):
    if n == 1:
        return 1
    return n*factorial_function(n-1)

def factorial_iteractive(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print("반복적으로 구현 :",factorial_iteractive(5))
print("재귀적으로 구현 :",factorial_function(5))