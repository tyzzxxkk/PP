menu = {"김치찌개":9000, "제육볶음":9000, "계란말이":6000, "차돌된장찌개":10000}

menuName = input("메뉴 이름을 입력하세요 : ")

if menuName in menu: 
    print(f"{menuName} : {menu[menuName]}원")
else:
    print("없는 메뉴입니다.")

