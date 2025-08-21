count = 0

while count < 3 : 
    password = int(input("비밀번호를 입력하세요 : "))
    
    if password == 1234:
        print("해제")
        break
    else:
        print("틀렸습니다.")
        count += 1  

if count == 3: 
    print("잠금")
