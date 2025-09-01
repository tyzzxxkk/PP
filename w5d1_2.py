# 파일 열기 (읽기 모드 'r')
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip()으로 줄바꿈 제거