# 树节点类构建
class TreeNode(object):
    def __init__(self, data):  # 这里的data分为两部分，对应于下面的freChar()函数return的结果，为一个元组(string, priority)
        self.val = data[0]  # 取元组的第一个元素，即string
        self.priority = data[1]  # 取元组的第二个元素，即优先度
        self.leftChild = None  # 默认左子树为空
        self.rightChild = None  # 默认右子树为空
        self.code = ""  # 默认编码为空


# 创建树节点队列函数
def createnodeQ(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q


# 为队列添加节点元素，并保证优先度从小到大排列
def addQ(queue, nodeNew):
    if len(queue) == 0:  # 增强了算法的稳健性
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:  # 对元素的优先度进行比较
            return queue[:i] + [nodeNew] + queue[i:]  # 若第i个节点的优先度大于nodeNew，则将nodeNew放到第i个节点的前面
    return queue + [nodeNew]  # 此种情况说明：newNode的优先度比之前所有节点的优先度都高


# 节点队列类定义
class nodeQueue(object):

    def __init__(self, code):
        self.que = createnodeQ(code)  # 属性1：队列
        self.size = len(self.que)  # 属性2：队列长度，即元素个数

    def addNode(self, node):  # 方法：添加节点
        self.que = addQ(self.que, node)
        self.size += 1

    def popNode(self):  # 方法：弹出节点
        self.size -= 1
        return self.que.pop(0)


# 各个字符在字符串中出现的次数，即计算优先度
def freChar(string):
    d = {}
    for c in string:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return sorted(d.items(), key=lambda x: x[1])  # 返回一个频率由小到大排列的列表元组，每个元组中第一个元素是字符串，第二个元素是频率


# 创建哈夫曼树
def createHuffmanTree(nodeQ):  # 以节点队列为参数，利用队列数据先进先出的特点
    while nodeQ.size != 1:
        node1 = nodeQ.popNode()  # 选择优先度最小的节点，弹出
        node2 = nodeQ.popNode()  # 选择优先度第二笑的节点，弹出
        r = TreeNode([None, node1.priority + node2.priority])  # 将两个节点优先度求和，形成新的树节点
        r.leftChild = node1  # 左子树放第一个节点
        r.rightChild = node2  # 右子树放第二个节点
        nodeQ.addNode(r)  # 将优先度求和后的新的树节点按优先度添加到队列中
    return nodeQ.popNode()  # 循环后将队列中最后一个节点弹出，即为所求的哈夫曼树


codeDic1 = {}
codeDic2 = {}


# 由哈夫曼树得到哈夫曼编码表
def HuffmanCodeDic(head, x):  # 这里的x在使用时为''
    """使用中序遍历，左根右"""
    global codeDic, codeList  # 对函数声明：这里改变的是全局变量而不是局部变量
    if head:  # 如果节点存在的话，则执行
        HuffmanCodeDic(head.leftChild, x + '0')  # 对该节点的左孩子标"0"
        head.code += x  # 并将节点的编码存储到code的属性中
        if head.val:  # 如果节点的val存在的话，则执行
            codeDic2[head.code] = head.val
            codeDic1[head.val] = head.code
        HuffmanCodeDic(head.rightChild, x + '1')  # 对该节点的右孩子标"1"


# 字符串编码
def TransEncode(string):
    global codeDic1
    transcode = ""
    for c in string:
        transcode += codeDic1[c]  # 利用以string为键的codeDic1字典，取出对应的编码
    return transcode


# 字符串解码
def TransDecode(StringCode):
    global codeDic2
    code = ""
    ans = ""
    for ch in StringCode:
        code += ch
        if code in codeDic2:
            ans += codeDic2[code]  # 利用以编码为键的codeDic2字典，取出对应的string
            code = ""  # 找完一个之后初始化code
    return ans


# 举例
fin = open('')
string = "AAGGDCCCDDDGFBBBFFGGDDDDGGGEFFDDCCCCDDFGAAA"
t = nodeQueue(freChar(string))
tree = createHuffmanTree(t)
HuffmanCodeDic(tree, '')
print('codeDic1:%s' % codeDic1, '\n', 'codeDic2:%s' % codeDic2)
a = TransEncode(string)
print(a)
aa = TransDecode(a)
print(aa)
print(string == aa)
