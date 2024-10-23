##print('Hyundai')
##print("Let's go.")
#print('He said,"go!"')
##print('he said, "let \'s go !".')


# input 연습
"""
a = input()
print(a)
"""
"""
a,b = input().split()
print(a,b)
"""
"""
a,b = input().split(':')
print(a+'h'+b+'m')
"""
"""
a = input()
print(a*5)
"""

# print('*'*10+'#'*10)

#스트링 출력

# a = "Hyundai Motors"
# print(a[0:4]+a[8:10])
# print(a[10:14])

# 숫자

# a = int(input())
# print(a*5)

# a,b = map(int, input().split())
# print(a/b)
# print(f'{a/b:.2f}')

# a,b = map(int, input().split())
# print(a//b, a%b)

# range 함수 사용
# for i in range(0,10):
#     print(i,end='')

# for i in range(1,11):
#     print(i,end='')

# for i in range(1,10,2):
#     print(i,end=' ')
#
# for i in range(9,0,-2):
#     print(i,end=' ')

#리스트

# a = ['*']*10
# a = ['*' for _ in range(10)]
# print(a)

# a = ['*' for _ in range(10)]
# a[1] = '1'
# a[2] = 2
# a[3] = 3.0
# print(a)

# a = ['*' for _ in range(10)]
# for i in range(1,10,2):
#     a[i] = i

# a = [i for i in range(10)]
# even = a[0:10:2]
# odd = a[1:10:2]
# print(odd+even)
# print(a)

# l1 = [i for i in range(10)]
# l2 = l1.copy()
# #l2 = l1[:]
# print(l2)
# l3 = l1[::-1]
# print(l3)
#
# print(l1[::-1])
# l1.reverse()

# a = input().split() # 그냥 입력하면 리스트 생성

# a = list(map(int,input().split())) # map은 리스트가 안됨 따라서 list 형변환 필요
# print(a)
# b = input()
# a.append(b)
# print(a)
# 맨 뒤에서 제거 할거면 pop()

# a = list(map(int,input().split()))
# print(a)
# #a.remove(20) #시간 복잡도가 엄청 올라감...
# del a[1] # 10 30 40 50
# print(a)
# #a.remove(40) #코테에서 쓰면 ㄹㅇ ㅈ됨 ㅋㅋㅋ
# del a[2] # 10 30 50
# ## 중요! 따라서 del 쓸거면 뒤에서 부터 지우기 -> 뒤에서 부터 지우면 인덱스 변화가 없기 때문
# print(a)

a = list(map(int,input().split()))
a.insert(0,input()) # 0번 위치에 입력을 받아서 저장
print(a)
