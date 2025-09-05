f = None
try:
    f = open("hello.txt", "a", encoding="utf-8")
    f.write("추가 내용입니다\n")
except OSError as e:
    print("파일 오류:", e)
finally:
    if f is not None:
        f.close()   # 반드시 닫아줌
