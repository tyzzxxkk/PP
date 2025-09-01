# "hello.txt" 파일을 쓰기 모드("w")로 열기
# encoding="utf-8" → 한글/특수문자도 정상 저장 가능

with open("hello.txt", "w", encoding="utf-8") as f:
    f.wrtie("Hello Python\n")
     # "Hello Python" + 줄바꿈 문자가 hello.txt에 저장됨