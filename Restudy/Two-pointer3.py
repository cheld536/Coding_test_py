"""
#"좋은수" 구하기

주어진 N 개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면 그 수를 '좋은 수'라고 한다. N개의 수중 좋은 수가 총 몇개인지 출력하라

예시 입력
10
1 2 3 4 5 6 7 8 9 10
예시 출력
8

알고리즘 !
1) 수를 입력받아 리스트에 저장한 후 정렬
2)투포인터 이동원칙 활용해서 이동
    - A[i] + A[j] > k: j--;
    - A[i] + A[j] < k: i++;
    - A[i] + A[j] ==k: count ++;
3) 2단계를 리스트의 모든 수에 대하여 반복합니다. K가 N이 될 때까지 반복하며 좋은 수가 몇 개 인지 센다
"""

N = int(input()) # 주어진 N 개의 수 입력
Result = 0 #결과값 저장
A = list(map(int,input().split())) #리스트 데이터 입력
A.sort() # 정렬

for K in range(N):
    find = A[K]
    i = 0
    j = N-1
    while i<j:
        if A[i] + A[j] == find:
            if i != K and j != K: #i 나 j가 K가 아닐때 Result ++
                Result += 1
                break
        elif A[i] + A[j] > K:
            j -= 1
        else :
            i +=1

print(Result)