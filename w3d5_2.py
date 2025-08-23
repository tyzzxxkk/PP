# score = int(input("점수를 입력해주세요 : "))

# if score >= 60 :
#     print("합격!")
# else :
#     print("불합격..")

score = int(input("점수를 입력해주세요 : "))

result = "합격!" if score >= 60 else "불합격.." # 한줄로 조건문 사용
print(result) 