# 쓰기
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요\n")

# 읽기
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
