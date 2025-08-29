numbers = [3, 1, 4, 1, 5]

# 기본 오름차순 정렬
print(sorted(numbers))

# 내림차순 정렬
print(sorted(numbers, reverse=True))

# key 함수에 abs(절대값) 적용
print(sorted(numbers, key=abs))

#key에 Lambda 사용 -> 짝수 먼저, 홀수 나중
print(sorted(numbers, key=lamda, x: x % 2))