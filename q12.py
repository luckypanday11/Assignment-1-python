n = int(input())

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(1, n + 1):
    if is_prime(i):
        print(i, end=' ')
