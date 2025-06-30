n = int(input())
sum_digits = sum(int(d) for d in str(n))
print("Yes" if n % sum_digits == 0 else "No")
