import sys
input = sys.stdin.readline #문자열로 입력을 받는다.

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*n
C = [0]*m
S[0] = A[0]
answer = 0

for i in range(1, n): # 1~n까지
    S[i] = S[i-1] + A[i] #합배열 저장

for i in range(n): #n까지
    remainder = S[i] % m # 각 합배열 인덱스를 주워진 값에 따라 나머지 계산
    if remainder == 0:   # 0~i까지 구간 합 자체가 0일때 정답 +1
        answer += 1
    C[remainder] += 1    # 나머지가 같은 인덱스의 개수값 증가 시키기

for i in range(m):
    #나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * ( C[i] - 1 ) // 2)  # / 연산은 소수 점까지 나오므로 // 연산으로 정수까지만 계산


print(answer)