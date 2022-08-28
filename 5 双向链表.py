# 双向链表的实现
# coding:utf-8


class Node(object):  # 定义 节点 类
    def __init__(self, init_data=None):
        self.data = init_data
        self.next = None  # 初始设置下一节点为空
        self.prior = None


class DoubleLinkList(object):  # 创建 双向链表，并 实现 其应有的功能
    def __init__(self):
        head_node = Node()
        self.__head = head_node

    def is_empty(self):  # 判断 双向链表 是否为空
        return self.__head.next is None

    def length(self):  # 得到 双向链表的 长度
        # 用 cur 游标，用来 遍历 链表
        cur = self.__head
        # 用 count 来 记录数量
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 正向、反向 遍历 双向链表
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
            print(cur.data, end=' ')
        print("\n")
        print(cur.data, end=' ')
        while cur.prior is not self.__head:
            cur = cur.prior
            print(cur.data, end=' ')
        print("\n")

    def add(self, item):  # 头部添加元素
        new_node = Node(item)
        new_node.prior = self.__head
        new_node.next = self.__head.next
        self.__head.next = new_node
        self.__head.next.next.prior = new_node

    def append(self, item):  # 尾部添加元素
        """找到当前链表的最后一个，再进行修改"""
        new_node = Node(item)
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        # 退出循环后，即找到了最后一个，cur指向最后一个元素。
        cur.next = new_node
        new_node.prior = cur

    def insert(self, pos, item):  # 在指定位置插入元素
        if pos <= 0 or pos > self.length() + 1:
            raise IndexError
        else:
            new_node = Node(item)
            """要先找到前一个，再实行添加操作。这里不能遍历，需要计算个数，于是要用cur和count。"""
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 退出循环后，cur指向 第pos-1个 元素
            new_node.next = cur.next
            new_node.prior = cur
            cur.next.prior = new_node
            cur.next = new_node

    def remove(self, item):  # 删除 data为item的 节点
        cur = self.__head.next  # cur初始指向头结点的下一个，用来 判断
        pre = self.__head  # pre指向头结点，用来 修改地址
        while cur is not None:  # 这里的cur指存储地址，只要cur这里非空，就满足条件。
            if cur.data == item:
                pre.next = cur.next  # 让 前一个 指向 cur的下一个节点。
                cur.next.prior = pre
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):  # 查找 data为item的节点 是否存在
        cur = self.__head.next  # 这里可以直接跳过头结点，表示第一个元素。若这里指向下一个的话，下面的循环就不能用cur.next当条件。
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

    scoreList = DoubleLinkList()
    print(scoreList.is_empty())
    print(scoreList.length())

    scoreList.append(627)
    scoreList.append(630)
    scoreList.append(615)
    scoreList.append(700)

    #   scoreList.add(700)
    #   scoreList.add(615)
    #   scoreList.add(630)
    #   scoreList.add(627)

    scoreList.travel()
    scoreList.insert(2, 618)
    scoreList.travel()
    print(scoreList.length())
    scoreList.remove(615)
    scoreList.travel()
    print("元素: {item} 的位置是: {pos}".format(item="630", pos=scoreList.search(630)))