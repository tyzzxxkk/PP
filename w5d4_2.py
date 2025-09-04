try :
    s = "123a" # 숫자가 아닌 문자열
    num = int(s) # int() 변환 시 ValueError 발생
    print("정수로 변환할 수 없는 문자열입니다.")
else :
    print("변환 성공 : ", num)