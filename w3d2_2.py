while True:
    data = input("나이를 입력하세요: ")
    if not data.isdigit():         
        print("숫자만 입력하세요!")
        continue
    age = int(data)
    if age < 0:                     
        print("음수는 입력할 수 없습니다!")
        continue
    print("나이:", age)
    break
