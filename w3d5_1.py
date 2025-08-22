# list = [x**2 for x in range(1, 11)]
# print(list) #거듭제곱 리스트 출력

list = [x for x in range(1, 11) if x % 2 == 0]
print(list)