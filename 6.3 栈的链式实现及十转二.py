# 栈的链式实现 及 十转二
# coding:utf-8


class Node(object):  # 定义 节点 类
    def __init__(self, init_data=None):
        self.data = init_data
        self.next = None  # 初始设置下一节点为空


class SingleLinkStack(object):  # 创建 链式栈，并 实现 其应有的功能
    def __init__(self):
        head_node = Node()
        self.__head = head_node

    def is_empty(self):  # 判断 链式栈 是否为空
        return self.__head.next is None

    def length(self):  # 得到 链式栈 的 长度
        # 用 cur 游标，用来 遍历 链式栈
        cur = self.__head
        # 用 count 来 记录数量
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 遍历 链式栈
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
            print(cur.data, end='')
        print("\n")

    def push(self, item):  # 头部添加元素
        new_node = Node(item)
        new_node.next = self.__head.next
        self.__head.next = new_node

    def pop(self):  # 弹出 栈顶 元素，并删除 栈顶。
        if self.__head.next is None:
            raise IndexError
        else:
            topValue = self.__head.next.data
            self.__head.next = self.__head.next.next
            return topValue

    def getTop(self):
        if self.__head.next is None:
            raise IndexError
        else:
            topValue = self.__head.next.data
            return topValue


if __name__ == "__main__":
    #scoreList = SingleLinkStack()
    #print(scoreList.is_empty())
    #print(scoreList.length())

    #scoreList.push(700)
    #scoreList.push(615)
    #scoreList.push(630)
    #scoreList.push(627)
    #scoreList.travel()
    #scoreList.pop()
    #scoreList.travel()

    def ten_to_two(value):  # 十进制转二进制
        NumStack = SingleLinkStack()  # 先创建一个链式栈
        left_value = value
        if value != 0:  # 先排除是0的情况
            while left_value > 0:
                Num = left_value % 2  # 除2取余
                NumStack.push(int(Num))
                left_value = left_value / 2
                left_value = int(left_value)  # 这一步需要保证最后一步得到的不是小数，故用int函数可以向下取整。
            NumStack.travel()
        else:
            print("After transforming: 0")


    ten_to_two(32)
    ten_to_two(16)
    ten_to_two(9)
    ten_to_two(8)
    ten_to_two(0)
