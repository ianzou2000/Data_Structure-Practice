i = 0


class TreeNode(object):
    def __init__(self, init_data=None, left=None, right=None):
        self.data = init_data
        self.lchild = left
        self.rchild = right


class BiTree(object):
    def __init__(self):
        self.root = TreeNode()
        self.seq = input('Create a BiTree by giving a string as the pre-order.\n')

    def CreateBiTree(self, new_node):
        global i
        if self.seq[i] == '#':
            pass
            #print('#', end='')
        else:
            new_node.data = self.seq[i]
            #print(new_node.data, i, '\n')
            new_node.lchild = TreeNode()
            i += 1
            self.CreateBiTree(new_node.lchild)
            new_node.rchild = TreeNode()
            i += 1
            self.CreateBiTree(new_node.rchild)
        return 0

    def CreateBiTree2(self):
        self.CreateBiTree(self.root)

    def PreOrderTraverse(self, new_node):
        print(new_node.data, end=' ')
        if new_node.lchild is not None:
            self.PreOrderTraverse(new_node.lchild)
        if new_node.rchild is not None:
            self.PreOrderTraverse(new_node.rchild)

    def InOrderTraverse(self, new_node):
        if new_node.lchild is not None:
            self.InOrderTraverse(new_node.lchild)
        print(new_node.data, end=' ')
        if new_node.rchild is not None:
            self.InOrderTraverse(new_node.rchild)

    def PosOrderTraverse(self, new_node):
        if new_node.lchild is not None:
            self.PosOrderTraverse(new_node.lchild)
        if new_node.rchild is not None:
            self.PosOrderTraverse(new_node.rchild)
        print(new_node.data, end=' ')


if __name__ == '__main__':
    BiTree = BiTree()
    BiTree.CreateBiTree2()
    BiTree.PreOrderTraverse(BiTree.root)
    print('\n')
    BiTree.InOrderTraverse(BiTree.root)
    print('\n')
    BiTree.PosOrderTraverse(BiTree.root)