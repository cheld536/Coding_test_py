"""
수 정렬하기 1 with 버블 정렬


"""

N = int(input())
A = [0] * N

for _ in range(N):
    A[_] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            swap = A[j]
            A[j] = A[j+1]
            A[j+1] = swap

for _ in range(N):
    print(A[_])