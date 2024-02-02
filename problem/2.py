n = input()
numlist = list(map(int, input().split()))
sum = sum(numlist)
maxnum = max(numlist)

print(sum * 100 / maxnum/ int(n))