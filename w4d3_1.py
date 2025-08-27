num = 10

def test_variable():
    num = 20   # 지역 변수 (함수 안에서만 사용됨)
    print("함수 안 지역 변수 num =", num)

print("함수 밖 전역 변수 num =", num)
test_variable()
print("함수 호출 후 전역 변수 num =", num)
실행 결과