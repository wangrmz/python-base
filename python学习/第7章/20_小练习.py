'''
***********学生管理************
1.添加学生
2.删除学生
3.查看所有学生
4.录入成绩
5.退出
请输入操作序号

'''

from datetime import datetime

class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

# 学生
class Student(Person):
    # 计数器
    count = 0

    def __init__(self, name, age,gender):
        super().__init__(name,age,gender)
        Student.count += 1
        self.scores = {}
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'

    # 给当前学生添加成绩
    def add_score(self,subject,score):
            self.scores[subject] = score
    def calcu_avg(self):
        if self.scores :
            return sum(self.scores.values()) /len(self.scores)
        else:
            return 0
    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender},成绩是:{self.scores},平均分:{self.calcu_avg()}'


# 管理
class Manager(Person):
    def __init__(self):
        self.stu_list=[] # 学生列表

    # 添加学生
    def add_stu(self):
        name=input('请输入姓名:')
        age =int(input('请输入年龄:'))
        gender = input('请输入性别:')
        stu = Student(name,age,gender)
        self.stu_list.append(stu)
        print(f'添加成功，学号是:{stu.stu_id}')

    # 删除学生
    def del_stu(self):
        # 遍历学生
        sid = input('请输入学号:')
        target = None
        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
        if target :
            self.stu_list.remove(target)
        else:
            print('学号有误，删除失败')

    # 展示所有学生
    def show_all_stu(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)

    # 设置成绩
    def set_score(self):
        sid = input('请输入学号:')
        target = None
        for stu in self.stu_list:
            if stu.stu_id == sid:
                # 输入成绩
                score_str=input('请输入成绩（学科-分数，学科-分数）')
                score_list = score_str.replace('，', ',').split(',')
                for item in score_list:
                    subject,score = item.split('-')
                    subject=subject.strip()
                    score=float(score.strip())
                    stu.add_score(subject,score)
                print('添加成功')
                return
        print('学号有误')

    def run(self):
        while True:
            print('***********学生管理************')
            print('1.添加学生')
            print('2.删除学生')
            print('3.查看所有学生')
            print('4.录入成绩')
            print('5.退出')
            # 用户选择
            choice = input('请输入操作编号:')
            if choice == '1':
                self.add_stu()
            elif choice == '2':
                self.del_stu()
            elif choice == '3':
                self.show_all_stu()
            elif choice == '4':
                self.set_score()
            elif choice == '5':
                print('再见')
                break
            else:
                print('输入有误')



# s1 = Student('张三',18,'男')
# print(s1.__dict__) #{'name': '张三', 'age': 18, 'gender': '男', 'scores': {}, 'stu_id': '2026001'}
# s1.add_score('数学',90)
# s1.add_score('语文',80)
# s1.add_score('英语',77)


m1=Manager()
m1.run()