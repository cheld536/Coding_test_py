import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001 # 만개보다 작거나 같은 수가 들어온다고 했으므로

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)