# 파일에서 쓰기
with open("hello.txt", "w", encoding="utf-8") as f :
    f.write("안녕하세요\n")

# 파일에서 읽기  
with open("hello.txt", "r", encoding="utf-8") as f :
    for line in f :
        print(line.strip())
# with 블록을 벗어나면 자동으로 f.close() 호출됨