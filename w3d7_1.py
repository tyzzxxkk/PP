multiples = [n for n in range(1, 51) if n % 3 == 0]
print("3의 배수:", *multiples)
print("합계:", sum(multiples))