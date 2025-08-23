# menu = {"김치찌개":9000, "제육볶음":9000, "계란말이":6000, "차돌된장찌개":10000}

# menuName = input("메뉴 이름을 입력하세요 : ")

# if menuName in menu: 
#     print(f"{menuName} : {menu[menuName]}원")
# else:
#     print("없는 메뉴입니다.")

balance = 0  # 처음 잔액은 0원

while True:  
    print("\n=== ATM 메뉴 ===")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액 확인")
    print("4. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        money = int(input("입금할 금액: "))
        balance += money
        print(f"{money}원이 입금되었습니다. 현재 잔액: {balance}원")

    elif choice == "2":
        money = int(input("출금할 금액: "))
        if money <= balance:
            balance -= money
            print(f"{money}원이 출금되었습니다. 현재 잔액: {balance}원")
        else:
            print("잔액이 부족합니다.")

    elif choice == "3":
        print(f"현재 잔액은 {balance}원입니다.")

    elif choice == "4":
        print("ATM을 종료합니다.")
        break  

    else:
        print("잘못된 입력입니다. 1~4 사이 숫자를 입력하세요.")
