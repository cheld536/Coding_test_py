import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #n 리스트 크기, m 질의 수
A = [[0] * (n + 1)]              # A 원본 리스트
D = [[0] * (n + 1) for _ in range(n + 1)] # D 합 배열


for i in range(n):  # 원본 리스트 데이터 저장
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        #합 배열 구하기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    X1, Y1, X2, Y2 = map(int, input().split())
    #구간 합 배열로 질의에 응답
    result = D[X2][Y2] - D[X1-1][Y2] - D[X2][Y1 - 1] + D[X1-1][Y1 - 1]
    print(result)


