#슬라이딩 윈도우 알고리즘
# 2개의 포인터로 범위를 지정/ 범위를 유지한 채로 이동하며 문제를 해결

"""
입력  9 8   # 문자열의 길이, 부분 문자열의 길이
CCCTGGATTG #DNA 문자열
2 0 1 1  #부분 문자욜에 포함돼야 할 A,C,G,T의 최소 개수

"""

#전역 변수 선언
checkList =[0]*4        # 비밀번호 체크 리스트
myList = [0] * 4        # 현재 상태 리스트
checkSecrect = 0        # 몇 개의 문자와 관련된 개수를 충족 했는지 판단하는 변수

#메인코드

#함수 정의
def myadd(c): # 새로 들어오는 문자열을 처리
    global checkList, myList, checkSecrect  #전역 변수로 선언
    if c == "A":
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecrect += 1
    elif c == "C":
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecrect +=1
    elif c == "G" :
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecrect +=1
    elif c == "T":
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecrect +=1

#제거 되는 문자를 처리하는 함수
def myremove(c):
    global checkList, myList, checkSecrect
    if c =='A':
        if myList[0] == checkList[0]:
            checkSecrect -= 1
        myList[0] -= 1
    elif c =='C':
        if myList[1] == checkList[1]:
            checkSecrect -=1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecrect -= 1
        myList[2] -= 1
    elif c =='T':
        if myList[3] == checkList[3]:
            checkSecrect -= 1
        myList[3] -= 1

S,P = map(int,input().split())              #S문자열 크기, P 부분 문자열 크기
Result = 0                                  # 결과값 저장
A = list(input())                           # A 문자열 데이터
checkList = list(map(int,input().split()))  #비밀번호

for i in range(4):
    if checkList[i] == 0:
        checkSecrect += 1

for i in range(P):      # 초기 P 부분 문자열 처리 부분
    myadd(A[i])

if checkSecrect == 4: # 4자릿수와 관련된 크기가 모두 충족될 때 유요한 비밀번호
    Result += 1

for i in range(P,S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecrect == 4:
        Result += 1

print(Result)