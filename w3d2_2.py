# 숫자만 허용, 음수 금지, 재입력 루프
while True:
    data = input("나이를 입력하세요: ")
    if not data.isdigit():           # 숫자가 아닌 경우
        print("숫자만 입력하세요!")
        continue
    age = int(data)
    if age < 0:                      # 음수인 경우
        print("음수는 입력할 수 없습니다!")
        continue
    print("나이:", age)
    break
