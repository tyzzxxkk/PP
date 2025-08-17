# 숫자형 자료형 (int, float 확인)
a = 3.5
print(type(3.5))    # float
print(type(a))      # float

# 연산자 실습 (나머지, 거듭제곱)
print(7 % 3)        # 1
print(2 ** 3)       # 8

# 문자열 기본 (연결하기)
a = "Hello"
b = "!"
print(a + b)        # Hello!
print(a + " " + b)  # Hello !

# 문자열 인덱싱, 슬라이싱, 거꾸로 출력
text = "Python"
print(text[0])      # 'P'
print(text[0:3])    # 'Pyt'
print(text[::-1])   # 'nohtyP'

# 문자열 함수
print("apple".upper())                # 'APPLE'
print("APPLE".lower())                # 'apple'
print("banana".replace("a", "A"))     # 'bAnAnA'

# 문자열 포맷 (f-string)
name = input("이름: ")
print(f"Hi! I'm {name}")

# 리스트 생성 및 활용
numbers = [1, 2, 3]
print(numbers)           # [1, 2, 3]
print(len(numbers))      # 리스트 길이 (3)
for n in numbers:        # 리스트 순회
    print(n)
print(*numbers)          # 1 2 3 (언패킹 출력)

# 리스트 메서드 (append, remove)
fruits = []
item = input("추가할 과일: ")
fruits.append(item)       # 입력받은 과일 추가
print(fruits)

rm = input("삭제할 과일: ")
if rm in fruits:
    fruits.remove(rm)     # 리스트에서 해당 과일 삭제
print(fruits)

# 튜플과 세트
t = (1, 2)     # 튜플: 수정 불가
s = {1, 2}     # 세트: 중복 없음, 순서 없음

# 딕셔너리 기초
student = {"name": "Taeyeon"}
print(student["name"])    # key로 접근
student["age"] = 17       # 새로운 key-value 추가
student["name"] = "Hana"  # 값 수정
del student["age"]        # key 삭제

# 리스트 안의 딕셔너리 (복합 자료형)
students = [{"name": "A"}]
students.append({"name": "B"})
students.append({"name": "C"})

for stu in students:
    print(stu["name"])    # 각각의 name 출력

# 리스트 안 딕셔너리에서 특정 요소 삭제
target = "C"
idx = -1
for i in range(len(students)):
    if students[i]["name"] == target:
        idx = i
        break
if idx != -1:
    del students[idx]

# 자료형 변환 실습
print("123" + str(123))   # 문자열 + 문자열 → "123123"
print(int("123") + 123)   # 정수 + 정수 → 246
