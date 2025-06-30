n = input()
even = odd = 0
for d in n:
    if int(d) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Even: {even}, Odd: {odd}")
