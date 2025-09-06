import csv

students = []

while True:
    try:
        name = input("이름 입력 (종료: 엔터): ")
        if name == "":
            break

        age = int(input("나이 입력: "))
        if age < 0:
            raise AgeError("나이는 음수가 될 수 없습니다.")

        score = int(input("점수 입력: "))
        if not (0 <= score <= 100):
            raise ScoreError("점수는 0~100 사이여야 합니다.")

        students.append([name, age, score])

    except ValueError:
        print("숫자를 잘못 입력했습니다.")
    except AgeError as e:
        print("나이 오류:", e)
    except ScoreError as e:
        print("점수 오류:", e)
