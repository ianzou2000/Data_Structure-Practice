# 面向对象(OOP) 三大特点：数据封装 继承 多态
# Class & Instance 类和实例 类是抽象的概念，实例则是具体的


class Student(object):
    def __init__(self, name, score):  # __init__方法可以绑定对象的属性。
        self.name = name
        self.score = score

    def print_score(self):  # 在class中创建函数，第一个参数永远是self，外部调用时python解释器会自动调用，不需额外传递。
        print('%s 的分数是 %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=80:
            return 'B'
        else:
            return 'C'


ian = Student('ian', 100)
trump = Student('trump', 0)

ian.print_score()
trump.print_score()
print('ian 的等级是', ian.get_grade(), sep=' ')