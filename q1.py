n = int(input())
for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end='')
    print()

