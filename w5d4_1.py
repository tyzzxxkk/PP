try :
    a = 10
    b = 0
    result = a / b # 0으로 나누면 예외 발생
except ZeroDivisionError :
    print("0으로는 나눌 수 없습니다") 
else p:
    print("결과 : ", result)
finally :
    print("나눗셈 시도 완료")