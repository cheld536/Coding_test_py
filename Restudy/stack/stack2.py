"""
오큰수 구하기
크기가 N인 수열 A이 있다.
각 수열의 A(i) 의 오큰수를 구하라.

1) 스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수
2) 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력

"""

N = int(input())  #수열 개수
ans =[0] * N
A = list(map(int,input().split()))
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]]< A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""

for i in range(N):
    result += str(ans[i])+" "

print(result)