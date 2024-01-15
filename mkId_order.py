def generate_student_id(year, college, major, clazz, student_number, gender):
    return year + college + major + clazz + student_number + gender

# 初始化学年和学院列表
years = ["2020", "2021", "2022", "2023"]
colleges = ["201", "202", "203", "204", "205", "206", "207", "208", "209"]

# 各个学院的专业个数
major_counts = {"201": 4, "202": 2, "203": 2, "204": 3, "205": 4, "206": 3, "207": 3, "208": 5, "209": 2}

# 生成学生ID并写入文件
with open("userId_20-23.txt", "w", encoding="utf-8") as file:
    for year in years:
        for college in colleges:
            for major in range(1, major_counts[college] + 1):
                for clazz in range(1, 3):
                    for student_number in range(1, 31):
                        for gender in range(2):
                            student_id = generate_student_id(
                                year, str(college), str(major),
                                str(clazz), str(student_number).zfill(2),
                                str(gender)
                            )
                            file.write(student_id + "\n")
