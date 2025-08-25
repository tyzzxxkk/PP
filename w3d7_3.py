balance = 0
history = []

def to_int(msg):
    s = input(msg)
    if not s.isdigit():
        return None
    return int(s)

while True:
    print("\n[ATM] 1.입금 2.출금 3.잔액 4.내역 5.종료")
    menu = input("선택: ").strip()

    if menu == "1":
        money = to_int("입금액: ")
        if money is None or money <= 0:
            print("올바른 금액을 입력하세요.")
            continue
        balance += money
        history.append(("입금", money, balance))
        print(f"입금 완료. 잔액 {balance}원")

    elif menu == "2":
        money = to_int("출금액: ")
        if money is None or money <= 0:
            print("올바른 금액을 입력하세요.")
            continue
        if money > balance:
            print("잔액 부족.")
            continue
        balance -= money
        history.append(("출금", money, balance))
        print(f"출금 완료. 잔액 {balance}원")

    elif menu == "3":
        print(f"현재 잔액: {balance}원")

    elif menu == "4":
        if not history:
            print("거래 내역이 없습니다.")
        else:
            for t, m, b in history:
                print(f"{t}: {m}원 → 잔액 {b}원")

    elif menu == "5":
        print("ATM 종료.")
        break
    else:
        print("메뉴를 다시 선택하세요.")
