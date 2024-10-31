"""
주몽의 명령
예제 입력
6
9
2 7 4 1 5 3

출력 2

두 재료의 번호의 합 -> 크기를 비교, 값을 정렬하면 문제를 좀 더 쉽게 풀수 있다.


1 재료 데이터를 리스트 A에 저장한 후 오픔차순 정렬합니다>
2. 투 포인터 i, j를 양쪽 끝에 위치시킨 후 문제의 조건에 적합한 포인터 이동 원칙을 활요해 탐색을 수행합니다. .

투포인터 이동 원칙
1) A[i] + A[j] > M: j--;
2) A[i] + A[j] < M: i++;
3) A[i] + A[j] == M: i++; j--; count++;

"""
import sys
input = sys.stdin.readline

n = int(input()) # 재료의 갯수
m = int(input()) # 갑옷 이 완성되는 번호의 합
A = list(map(int,input().split()))
A.sort() # A 배열 정렬
i = 0 #시작 인덱스
j = n-1 # 종료 인덱스
count = 0

while i<j:
    if A[i] + A[j] < m:
        i += 1
    elif A[i] + A[j] > m:
       j -= 1
    else:
        count += 1
        i +=1
        j -=1


print(count)
