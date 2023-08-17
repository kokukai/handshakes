def factorial(x):
    number = 1
    for i in range(1, x+1):
        number *= i
    return number

def handshakes(n):
    if n <= 1:
        return 0
    
    return (factorial(n)) // (factorial(2) * (factorial(n-2)))

print(handshakes(0))
