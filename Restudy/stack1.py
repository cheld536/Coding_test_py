import sys
from inspect import stack

input = sys.stdin.readline
N = int(input()) # 수열의 개수
S = [0] * N


for i in range(N):
    S[i] = int(input())

stack = [] # 스택선언
num = 1
result = True
answer = ""

for i in range(N):
    su = S[i]
    if su >= num: #현재 수열값 >= 오름차순 자연수 : 값이 같아질 때까지 append()수행
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else: #현재 수열값 < 오름차순 자연수 값
        numpop = stack.pop()
        if numpop > su:
            print("No")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)