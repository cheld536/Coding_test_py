"""
버블 정렬 프로그램1

"""

N = int(input())

A = []

for i in range(N):
    A.append((int(input()),i))

MAX = 0
sorted_A = sorted(A) # 정렬해서 저장하는 리스트 index

for i in range(N):
    if MAX < sorted_A[i][1] - i: #정렬 전 index - 정렬 후 index 계산의 최댓값 저장
        MAX = sorted_A[i][1] - i

print(MAX + 1)