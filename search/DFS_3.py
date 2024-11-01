"""
백준 13023번
친구 관계 파악하기


아래의 친구 관계를 만족하는 경우의수 출력
A - B
B - C
C - D
D - E

입력은 N M (노드 갯수, 에지 개수)
"""

import sys

from search.DFS_1 import visited

sys.setrecursionlimit(10000)
input = sys.stdin.readline


N,M = map(int,input().split()) #N 시작 노드, M은 엣지 갯수
visited = [False] * (N+1) #방문 기록 저장 리스트

#DFS 구현
def DFS(s,e):




s,e = list(map(int,input().split()))
