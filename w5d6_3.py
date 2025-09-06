with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이", "점수"])  # 헤더
    writer.writerows(students)
