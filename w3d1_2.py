user_id = input("아이디 입력: ")
user_pw = input("비밀번호 입력: ")

if user_id == "admin":                
    if user_pw == "1234":            
        print("로그인 성공!")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("존재하지 않는 아이디입니다.") 
