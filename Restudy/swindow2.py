#최솟값 찾기1

"""
입력
1) 숫자의 갯수 N
2) 슬라이딩 윈도우의 크기
3) N개의 A

최솟값을 구하는 버위가 i - L + 1 ~ i 까지 임으로 L이라고 생각

슬라이딩 윈도우를 덱으로 구현

!!! 덱이란? !!!
양쪽 끝에서 파일의 삽입과 추출이 가능한 자료구조
appendleft(), popleft() / append(), pop()

알고리즘
숫자 비교, 윈도우 범위 계산이 끝난 덱에서 맨 앞에 있는 노드의 숫자를 출력하기만 하면 정답이 된다.
"""

from collections import deque
N,L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

#새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # deque 제일 왼쪽에 있는 파일보다 now[i]가 클때 까지
        mydeque.pop()                           # 오른쪽에 있는 자료를 pop
    mydeque.append((now[i],i))                  # now[i] 값과, i 번째 데이터라고 알리고 입력
    if mydeque[0][1] <= i - L: #범위에서 벗어난 값은 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0],end='')
