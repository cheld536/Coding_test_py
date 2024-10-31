"""
#카드 게임

N장의 카드가 있다. 가각의 카드는 차례로 1~N까지의 번호가 붙어 있으며, 1번카드가 먼저 가장 위 N 번카드가 가장 아래인 상태로 놓여있다.

"""
from collections import deque

N = int(input())
myqueue = deque()

#큐에 1~N까지 저장
for i in range(1,N+1):
    myqueue.append(i)

while len(myqueue) > 1:
    myqueue.popleft()
    myqueue.append(myqueue.popleft())

print(myqueue[0])