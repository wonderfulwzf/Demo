class Student:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
stu1 = Student("jack", 33)
stu2 = Student("amy", 24)
stu3 = Student("lucy", 22)
stu4 = Student("lulu", 45)
print("实例化了%s个学生" % Student.count)