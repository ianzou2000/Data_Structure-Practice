# coding:utf-8


class Node(object):  # 定义 节点 类
    def __init__(self, init_data=None):
        self.data = init_data
        self.next = None  # 初始设置下一节点为空


class LinkQueue(object):  # 创建 链队列，并 实现 其应有的功能
    def __init__(self):
        head_node = Node()
        self.front = head_node  # front的下一个是队头
        self.rear = head_node  # rear指的是队尾

    def is_empty(self):  # 判断 链队列 是否为空
        return self.front.next is None

    def length(self):  # 得到 链队列的 长度
        # 用 cur 游标，用来 遍历 链表
        cur = self.front
        # 用 count 来 记录数量
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 遍历 链队列
        cur = self.front
        while cur.next is not None:
            cur = cur.next
            print(cur.data, end=' ')
        print("\n")

    def enqueue(self, item):  # 队尾插入一个元素
        new_node = Node(item)
        self.rear.next = new_node  # 原来的队尾指向它
        self.rear = new_node  # 它变成新的队尾

    def dequeue(self):  # 删除队头，并弹出队头的值
        front_node = self.front.next
        if front_node is not None:
            self.front.next = front_node.next
        else:
            raise ValueError
        if front_node.next is None:
            self.rear = self.front
        return front_node.data

    def search(self, item):  # 查找 data为item的节点 是否存在
        cur = self.front.next  # 这里可以直接跳过头结点，表示第一个元素。若这里指向下一个的话，下面的循环就不能用cur.next当条件。
        count = 1  # 用count来进行计数，因为cur的起始是第一个元素，所以这里是1。
        while cur is not None:
            if cur.data == item:
                """返回位置"""
                return count  # 找到该元素时，返回count，即为其位置。
            else:
                count += 1  # 当没有找到时，count+1。
                cur = cur.next
        return 0


if __name__ == "__main__":

    scoreList = LinkQueue()
    print(scoreList.is_empty())
    print(scoreList.length())

    scoreList.enqueue(700)
    scoreList.enqueue(615)
    scoreList.enqueue(630)
    scoreList.enqueue(627)
    scoreList.travel()

    print(scoreList.dequeue())
    scoreList.travel()

    print(scoreList.dequeue())
    scoreList.travel()

    print(scoreList.dequeue())
    scoreList.travel()

    print(scoreList.length())