import random

while True:
    nums = sorted(random.sample(range(1, 46), 6))
    print("로또 번호:", *nums)
    again = input("다시 뽑을까요? (y/n) : ").strip().lower()
    if again != "y":
        print("종료합니다!")
        break