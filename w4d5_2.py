numbers = [1, 2, 3, 4]

# filter -> 조건을 만족하는 원소만 걸러냄
# Lambda x : x % 2 == 0 -> 짝수인 경우만 True
evens = list(filter(lambda x : x % 2 == 0, numbers))

print(even) # 짝수만 출력