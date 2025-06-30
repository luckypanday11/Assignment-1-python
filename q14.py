n = input()
increasing = all(n[i] < n[i+1] for i in range(len(n) - 1))
print("Yes" if increasing else "No")
