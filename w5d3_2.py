def square_root(n: float) -> float:
    if n < 0:
        raise ValueError("n은 음수일 수 없습니다.")
    return n ** 0.5

# 사용 예시
try:
    print(square_root(9))    # 3.0
    print(square_root(-4))   # 여기서 ValueError 발생
except ValueError as e:
    print("입력값 오류:", e)
