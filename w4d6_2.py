def average(scores) :
    # sum(scores) -> 리스트 합계
    # len(scores) -> 리스트 원소 개수
    return sum(scores) /  len(scores) # 평균

scores = [80, 90, 70, 100]
print("평균 점수 : ", average(scores))
