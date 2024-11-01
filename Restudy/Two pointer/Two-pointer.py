"""
#연속된 자연수의 합 구하기
-> 연속된 자연수의 합의 가지수를 구하는 문제
백준 2018
입력: 15, 출력 : 4
sum > N : sum = sum - start_index: start_index ++;
sum < N: end_index++; sum = sum + end_index;
sum ==N : end_index++; sum = sum + end_index; count++:
"""

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count +=1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum = sum - start_index
        start_index +=1
    else:
        end_index += 1
        sum += end_index

print(count)