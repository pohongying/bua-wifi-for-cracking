# 学号规律：2022 207 52 101
# 年份 + 学院 + 专业+班级+ 学号+性别

import random

# 写账号
def generate_student_id():
    year = random.choice(["2018", "2019", "2020", "2021", "2022", "2023"])
    college = random.choice(["201", "202", "203", "204", "205", "206", "207", "208", "209"])

    # 用字典表示每个学院的专业个数
    major_counts = {"201": 4, "202": 2, "203": 2, "204": 3, "205": 4, "206": 3, "207": 3, "208": 5, "209": 2}

    major = str(random.randint(1, major_counts[college])).zfill(2)  # 专业
    clazz = str(random.randint(1, 2))  # 班级
    student_number = str(random.randint(1, 25)).zfill(2)  # 学号
    gender = str(random.randint(0, 1))  # 性别

    student_id = year + college + major + clazz + student_number + gender
    return student_id


# 生成学生ID的数量
num_students = 10

# 生成学生ID并写入文件
with open("userId.txt", "w", encoding="utf-8") as file:
    while 1:
        student_id = generate_student_id()
        if not student_id:
            break
        file.write(student_id + "\n")


