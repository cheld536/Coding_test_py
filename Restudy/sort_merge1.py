"""
병합 정렬
분할 정복을 활용하여 기준점으로 각 배열을 나눈다음 정렬후 병합하는 과정

"""
import sys
input = sys.stdin.readline
print = sys.stdout.write


#병합 정렬 구현
def Merge(s,e): #s: 시작점, e: 종료지점
    if e - s < 1 : return
    m = int(s+(e-s) / 2) #중간점
    Merge(s,m)          # 중간점을 기준으로 왼쪽 정렬
    Merge(m+1,e)        # 중간점을 기준으로 오른쪽 정렬
    for i in range(s,e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <=e: # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 +=1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m: # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        A[k] = tmp[index1]
        k += 1
        index1 +=1
    while index2 <= e:
        A[k] = tmp[index2]
        k+=1
        index2 +=1



N =int(input())
A = [0] * int(N+1)
tmp = [0] * int(N+1)

for i in range(1,N+1):
    A[i] = int(input())

Merge(1,N)

for i in range(1,N+1):
    print(str(A[i])+ '\n')