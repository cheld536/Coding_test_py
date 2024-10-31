"""
ATM 인출 시간 계산하기

1) 삽입 정렬을 활용해서 입력된 배열의 데이터를 정렬
2) 정렬된 배열을 합 배열 변환 S[i] = S[i-1] + A[i]
3) 합배열을 모두 다 더한 뒤 결과값을 출력
"""
N = int(input()) #데이터의 크기입력을 받는 변수
A = list(map(int,input().split())) # 리스트 배열 데이터 입력
S = [0] * N #합배열 초기화

for i in range(1,N): #삽입 정렬
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1 , -1): # i - 1 부터 -1 까지 -1만큼 작아 지면서 반복 삽입 위치 찾기
        if A[j] < A[i]:             # A[j] 보다 A[i]가 더크면
            insert_point = j + 1    # 삽입 위치를 j + 1 해준다
            break
        if j == 0:                  # 만약 j면 point = 0
            insert_point = 0
    for j in range(i, insert_point, -1): # i 부터 insert_point 까지 -1 작아지면서 반복
        A[j] = A[j-1]                  # 데이터 삽입을 위해 삽입 위치에서 i까지 데이터를 한 칸씩 뒤로 밀기
    A[insert_point] = insert_value     # 삽입 할 위치에 값을 저장

S[0] = A[0]                         # S[i] = S[i-1] + A[i] / 합 집합 첫번째 칸은 S[0] = A[0] 동일

sum = 0

for i in range(1,N):
    S[i] = S[i-1] + A[i]

for _ in range(0,N):
    sum += S[_]

print(sum)