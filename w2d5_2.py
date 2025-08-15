myName = {"name" : "Taeyeon"}
print(myName["name"]) #반드시 문자열

# # 추가
# myName = {"name": "Taeyeon"}
# myName["age"] = 17  # 새로운 key와 값 추가
# print(myName)  # {'name': 'Taeyeon', 'age': 17}

# # 수정
# myName["name"] = "Hana"  # 값 변경
# print(myName)  # {'name': 'Hana', 'age': 17}

# # 삭제
# del myName["age"]  # key 삭제
# print(myName)  # {'name': 'Hana'}

# # pop으로 삭제 (값 반환)
# removed_value = myName.pop("name")
# print(removed_value)  # 'Hana'
# print(myName)  # {}
