# # 쓰기
# with open("data.txt", "w", encoding="utf-8") as f:
#     f.write("안녕하세요\n")

# # 읽기
# with open("data.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

f = None
try:
    f = open("data.txt", "a", encoding="utf-8")
    f.write("추가 내용\n")
except OSError as e:
    print("파일 오류:", e)
finally:
    if f is not None:
        f.close()  # 반드시 닫아줌
