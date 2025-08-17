a = 3.5
print(type(3.5))
print(type(a))

print(7 % 3)
print(2 ** 3)

a = "Hello"
b = "!"
print(a + b)
print(a + " " + b)

text = "Python"
print(text[0])
print(text[0:3])
print(text[::-1])

print("apple".upper())
print("APPLE".lower())
print("banana".replace("a", "A"))

name = input("이름: ")
print(f"Hi! I'm {name}")

numbers = [1, 2, 3]
print(numbers)
print(len(numbers))
for n in numbers:
    print(n)
print(*numbers)

fruits = []
item = input("추가할 과일: ")
fruits.append(item)
print(fruits)

rm = input("삭제할 과일: ")
if rm in fruits:
    fruits.remove(rm)
print(fruits)

t = (1, 2)
s = {1, 2}

student = {"name": "Taeyeon"}
print(student["name"])
student["age"] = 17
student["name"] = "Hana"
del student["age"]

students = [{"name": "A"}]
students.append({"name": "B"})
students.append({"name": "C"})

for stu in students:
    print(stu["name"])

target = "C"
idx = -1
for i in range(len(students)):
    if students[i]["name"] == target:
        idx = i
        break
if idx != -1:
    del students[idx]

print("123" + str(123))
print(int("123") + 123)
