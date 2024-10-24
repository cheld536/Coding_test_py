#list 2

from random import randint
# n = []
# a = [randint(1,10) for _ in range(10)]
# for _ in range(10):
#      n.append(randint(1,10))
# print(n)
# n.sort() # 오름차순으로 정렬
# print(n)
# n.sort(reverse=True)
# print(n)
# print('The sum is',sum(n)) #리스트 안의 모든 값을 더하는 하수
# print(f'The sum is {sum(n)}.')

# n = [randint(1,10) for _ in range(10)]
# print(n)
# k = list(map(int,input().split()))
# for ele in k:
#     if ele in n: print(f'{ele} is in the list')
#     else: print(f'{ele} is not in the list')

# a = int(input())
# print(n.count(a),'occurrences of', a)


# k = list(map(int,input().split()))
# for ele in k:
#     if ele in n: print(f'{ele} is in n[{n.index(ele)}]')
#     else: print(f'{ele} is not in the list')
#
# b = list(map(int,input().split()))
# for i in b:
#     ans = []
#     for j in range(len(n)):
#         if i == n[j]:
#             ans.append(j)
#     if ans == []:
#         print(f'{i} is not in the list')
#     else: print(f'{i} is in the following locations {ans}')

## 2차원 리스트

# li =[[0]*5]*3 # 이렇게 하면 [0, 0, 0, 0, 0] 이거 3개 복사하는 느낌
# li = [[0 for _ in range(5)]for _ in range(3)]
#
# print(li)
# li[0][0] = 1
# print(li)

# a = [[0 for i in range(5)]for _ in range(3)]
# print(a)
# a[0][0] = 1
# b = [ele[:] for ele in a] # a의 모든 서브 리스트에서 각가을 복사해라 ele[:]-> 1차원 배열 복사
# b[0][0] = 2
# print('a:',a)
# print('b:', b)

# a = [[5*i+j+1 for j in range(5)]for i in range(3)]
# print(a)

# a = [[randint(1,100) for _ in range(2)]for _ in range(5)]
# print(a)

# a = [[3,1],[1,2],[2,2],[1,1],[2,1]]
# print(a)
# a.sort()                #오름차순 정렬
# print(a)
# a.sort(reverse=True)    #내림 차순 정렬
# print(a)
#
# a.sort(key=lambda x: x[1]) #뒤에 부터 먼저 오름 차순으로 정렬하고 앞에 껄 내림 차순으로 정렬 -> 레빗트 솔트 (보조키 먼저 정렬 후 주키 정렬)
# print(a)
# a.sort(key=lambda x: x[0], reverse=True)
# print(a)

# a = [['3','1'],['1','2'],['2','2'],['1','1'],['2','1']]
# a.sort(key=lambda x: x[1])
# a.sort(key=lambda x: x[0], reverse=True)
# print(a)

### SET 공부!!