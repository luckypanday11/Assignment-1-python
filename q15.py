num = input()
n = int(input())
if n <= len(num):
    print(num[-n])
else:
    print("Not enough digits")
