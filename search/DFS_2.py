"""
DFS 활용
신기한 소수 찾기
"7331" 신기한 소수, 733도 소수, 73도 소수, 7도 소수
각 자리별 소수를 찾아서 계산
입력 : 자릿수 N
자리수 길이 만큼 해당하는 소수 구하기

일의 자리수 소수는 2 5 7 9
그 다음 부터 소수는 1 3 5 7 9 (홀수들)
2 -> 1(소수 x) 탐색중단,
2 -> 3(소수 0) 탐색 지속 -> 1 (소수 x) 탐색 중지
2 -> 3 -> 3 (소수 0) 지속적인 탐색

"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input()) # 자릿수 N을 입력받음

# 소수 판별 함수
def isPrime(num):
    for i in range(2,int(num/2 +1 )): #2부터 시작 num/2 하고 + 1 까지 실행
        if num % i == 0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N :
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0: # 2로 나눴을 때 나머지가 0이면 짝수이므로 소수 x
                continue
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)

# 일의자리의 소수는 4가지 이므로 4가지수에서 만 시작
DFS(2)
DFS(3)
DFS(5)
DFS(7)