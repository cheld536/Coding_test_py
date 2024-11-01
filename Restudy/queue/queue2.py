"""
절대값 힙 구현 하기
① 배열에 정수 x를 넣는다.
② 배열에서 절대값이 가장 작은 값을 출력한 후 그 값을 배열에서 제거, 절대값이 가장 작은 값이 여러 개일 경우 그 중 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

절대값과 관련된 정렬이 필요하므로 우선순위 큐로 문제를 쉽게 해결
예제의 절대 값이 같으면 음수를 출력

x가 0일 때
큐가 비어 있을 때는 0을 출력하고 비어 있지 않을 때는 절댓값이 최소인 값을 출력한다.

x가 1일 때
put으로 큐에 새로운 값을 추가하고 우선순위 큐 정렬 기준으로 자동 정렬한다.

※ 슈도코드 작성하기

N(질의 요청 개수)
우선순위 큐 선언
- 절댓값 기준으로 정렬되도록 설정
- 단, 절댓값이 같으면 음수 우선 정렬

for N만큼 반복:
    요청이 0일 때: 큐가 비어 있으면 0, 비어 있지 않으면 큐의 front값 출력(get())
    요청이 1일 때: 새로운 데이터를 우선순위 큐에 더하기(put())

"""

from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty() :
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        #절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myQueue.put((abs(request), request))