#구간 합의 핵심 이론

# 합 배열 S[i] = S[i-1] + A[i]

# 구간 합 배열 : S[j] - S[i-1]

import sys

input = sys.stdin.readline

suNo, quiNo = map(int,input().split()) # 숫자 개수, 질의 개수 변수선언
numbers = list(map(int,input().split())) # 숫자 배열 입력
prefix_sum = [0]                        # 합 배열 변수
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quiNo):
    s,e = map(int,input().split())
    print(prefix_sum[e]-prefix_sum[s-1])