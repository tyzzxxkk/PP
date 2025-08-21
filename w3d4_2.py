for num in range(2, 21):  # 2부터 20까지 검사
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):  # 소수 판별
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:   # 소수를 찾으면
        print("첫 소수:", num)
        break       # 바로 반복 종료