import sys

input = sys.stdin.readline
result = 0


def Merge_sort(s,e):
    global result
    if e-s < 1 : return
    m = (s+(e-s) // 2)
    Merge_sort(s,m)
    Merge_sort(m+1,e)

    for i in range(s,e+1):
        tmp[i] = A[i]

    k = s

    index1 = s
    index2 = m+1

    while index1 <= m and index2 <= e: #두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k # 뒤족 데이터 값이 더 작다면 결괏값 업데이트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 +=1
    while index1 <= m:
        A[k] = tmp[index1]
        k+=1
        index1 += 1

    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1





N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
tmp =[0] * int(N+1)
Merge_sort(1,N)
print(result)