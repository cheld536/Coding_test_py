"""
퀵정렬!!!
기준 값을 선정해 해당 값보다 작은 데이터와 큰데이터로 분류하는 것을 반복해 정렬하는 알고리즘.
1) 데이터를 분할하는 피벗을 선정한다
2) 피벗을 기준으로 다음 a~e 과정을 거쳐 데이터를 2개의 집합으로 분리한다.
 2-a) S(start)가 가리키는 데이터가 피벗이 가리키는 데이터보다 작으면 start를 오른쪽으로 1칸 이동한다.
 2-b) end가 가르키는 데이터가 피벗이 가리키는 데이터보다 크면 end를 왼쪽으로 1칸 이동한다.
 2-c) start가 가르키는 데이터가 피벗이 가르키는 데잍 보다 크고, end가 가르키는 데이터가 피벗이 가르키는 데이터보다 작으면 start, end가
      가르키는 데이터를 swap하고 start는 오른쪽, end는 왼쪽으로 1칸씩 이동한다.
 2-d) start와 end가 만날 때까지 a~c반복
 2-e) start와 end가 만나면 만난 지점에서 가리키는 데이터와 피벗이 가르키는 데이터를 비교하여 피벗이 가리키는 데이터가 크면 만난 지점의 오른쪽
      에, 작으면 만난 지점의 왼쪽에 피벗이 가리키는 데이터를 삽입한다.
3) 분리 집합에서 각각 다시 피버을 선정한다.
4) 분리 집합이 1개 이하가 될 때까지 과정을 반복
"""
import sys
from turtledemo.sorting_animate import partition

input = sys.stdin.readline

N, K = map(int,input().split()) #데이터 개수, K번째 수
A = list(map(int,input().split())) #정렬을 할 배열 입력

pivot = 0 # 피벗 위치를 저장
start, end = 0 #시작 위치와 끝위치를 정하는 변수

def quickSort(S,E,K):
    global A
    if S < E:
        pivot = partition(S,E)
        if pivot == K :     # k번째 수가 피벗이면 더는 구할 필요가 없음
            return
        elif K < pivot:     # K번째 수가 피벗보다 작으면 왼쪽 그룹만 정렬
            quickSort(S,pivot-1,K)
        else:               # K번째 수가 피벗보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot+1,E,K)

def swap(i,j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partions(S,E):
    global A

    if S + 1 == E : #시작 위치 바로 다음이 끝이라면
        if A[S] > A[E]:
            swap(S,E)
        return E

    M = (S + E) // 2 # 중앙값 착찾고
    swap(S,M)
    pivot = A[S]
    i = S + 1
    j = E

    while i<=j:
        while pivot < A[j] and j > 0: #피벗보다 작은 수가 나올 때까지 j 감소
            j = j - 1
        while pivot > A[i] and i < len(A) - 1: #피벗보다 큰 수가 나올 때까지 i증가
            i = i + 1
        if i <= j:      #찾은 i와 j 데이터를 swap
            swap(i,j)
            i = i + 1
            j = j - 1
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정
    A[S] = A[j]    # 피벗 데이터를 나뉜 두 그룹의 경계 index에 저장하기
    A[j] = pivot
    return j        # 경계 인덱스 리턴

quickSort(0, N-1, K-1) #선언한 배열 보다 하나 작게
print(A[K-1]) #퀵 정렬을 구현하고 주어진 수를 오름차순으로 정렬하고 K 번째 수 출력