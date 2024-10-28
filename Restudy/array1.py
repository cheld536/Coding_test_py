#숫자의 합
num1 = int(input())
numbers = list(input())
sum = 0             #자료의 형 변환을 위해 0으로ㅓ

for j in numbers:
    sum = sum + int(j)

print(sum)