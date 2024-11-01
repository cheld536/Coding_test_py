"""
깊이 우선 탐색
1) 특징: 재귀 함수로 구현, 스택 자료구조 이용
2) 시간 복잡도: O(V+E) 노드 수: V, 에지 : E

깊이 우선 탐색 이론
1. DFS를 시작할 노드를 정한 후 사용할 자료구조 초기화하기
2. 스택에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 스택에 삽입하기
3. 스택 자료구조에 값이 없을 때까지 반복하기



"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split()) # n: 노드 개수, m: 에지 개수
A = [[] for _ in range(n+1)]   # 그래프 데이터 저장 인접 리스트 초기화
visited = [False] * (n+1)      # 방문 기록 리스트 초기화

#DFS 구현
def DFS(v):
    visited[v] = True           # 방문한 곳이니 True
    for i in A[v]:              # ex) 만약 v가 1 이고, A[1] = 2 이니
        if not visited[i]:      # ex) visited[2]는 F -> not(f) 는 T 함수 실행
            DFS(i)              # ex) 재귀함수 활용하여 DFS함수 호출 2를 넘겨줌
                                # ex) A[2] = 5, visited[2] = T, visited[5] = F 이므로 DFS(5) 실행

for _ in range(m):
    s,e = map(int, input().split())
    A[s].append(e)          # 양방향 에지이므로 양쪽에 에지를 더하기
    A[s].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:      #연결 노드 중 방분하지 않았던 노드만 탐색
        count += 1          # 탐색횟수를 증가
        DFS(i)

print(count)
