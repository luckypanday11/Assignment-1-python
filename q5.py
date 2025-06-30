n = int(input())
sum_of_cubes = sum(int(d)**3 for d in str(n))
print("Armstrong" if sum_of_cubes == n else "Not Armstrong")
