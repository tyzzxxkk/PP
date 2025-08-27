count = 0  # 전역 변수

def counter():
    global count   # 전역 변수 사용 선언
    count += 1
    return count

# 실행 테스트
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3