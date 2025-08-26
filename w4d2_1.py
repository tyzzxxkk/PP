def sum_numbers(*args, **kwargs):
    total = sum(args)  # 위치 인자 합계
    total += sum(kwargs.values())  # 키워드 인자 값도 합계
    return total

print(sum_numbers(1, 2, 3))                 # 6
print(sum_numbers(10, 20, a=5, b=15))       # 50

# *args
# **임의 개수의 위치 인자(순서대로 들어오는 값)**를 한꺼번에 받을 때 사용.
# 함수 안에서 **튜플(tuple)**로 모아진다.

# **kwargs
# **임의 개수의 키워드 인자(이름=값 형태)**를 한꺼번에 받을 때 사용.
# 함수 안에서 **딕셔너리(dict)**로 모아진다.