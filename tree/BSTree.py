# coding=utf-8


class BSTree:

    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.key = key

    @staticmethod
    def add(root, key):

        """
        按引用传递和按指针传递不一样 有时间看起来引用比指针方便 但是长远看起来指针要灵活的多
        此处我们对root进行修改时并不能改变原结果 因为传递进来的只是引用而不是指针
        :param root:
        :param key:
        :return:
        """

        temp = dict()
        child = BSTree(key)
        child.left_child = child.right_child = None
        if BSTree.search(root, key, temp):
            return False
        else:
            if child.key < temp['parent'].key:
                temp['parent'].left_child = child
            else:
                temp['parent'].right_child = child
            return True

    @staticmethod
    def postorder_traversal(root):

        if root is None:
            return
        BSTree.postorder_traversal(root.left_child)
        BSTree.postorder_traversal(root.right_child)
        print root.key

    @staticmethod
    def preorder_traversal(root):
        if root is None:
            return
        print root.key
        BSTree.postorder_traversal(root.left_child)
        BSTree.postorder_traversal(root.right_child)

    @staticmethod
    def inorder_traversal(root):
        """
        对二叉排序树进行中序遍历会生成一个有序数组
        :param root:
        :return:
        """
        if root is None:
            return
        BSTree.inorder_traversal(root.left_child)
        print root.key, root.height
        BSTree.inorder_traversal(root.right_child)

    @staticmethod
    def quick_search(root, key):

        if root is None or root.key == key:
            return root
        elif key < root.key:
            return BSTree.quick_search(root.left_child, key)
        else:
            return BSTree.quick_search(root.right_child, key)

    @staticmethod
    def search(root, key, temp):

        """

        :param root:
        :param key:
        :param temp:
        :return:
        """

        if root is None:  # 若找不到符合要求的节点返回父节点
            temp['result'] = temp['parent']
            return False
        elif root.key == key:
            temp['result'] = root
            return True
        elif key < root.key:
            temp['parent'] = root
            return BSTree.search(root.left_child, key, temp)
        else:
            temp['parent'] = root
            return BSTree.search(root.right_child, key, temp)

    @staticmethod
    def find_min(root):
        if root.left_child is None:
            return root
        return BSTree.find_min(root.left_child)

    @staticmethod
    def DeleteBST(root, key):
        if root is None:
            return None
        elif key < root.key:
            root.left_child = BSTree.DeleteBST(root.left_child, key)
        elif key > root.key:
            root.right_child = BSTree.DeleteBST(root.right_child, key)
        else:
            if root.left_child and root.right_child:
                tmp = BSTree.find_min(root.right_child)  # 找到后继结点
                root.key = tmp.key
                root.right_child = BSTree.DeleteBST(root.right_child, tmp.key)  # 删除后继结点
            else:
                if root.left_child is None:
                    root = root.right_child
                elif root.right_child is None:
                    root = root.left_child
                else:
                    root = None
        return root


if __name__ == '__main__':
    root = BSTree(1)
    L = list()
    import numpy as np
    import time

    count = 100
    number = 0
    range_number = 10000
    test_number = 100
    begin = time.time()
    for j in range(count):
        for i in range(range_number):
            number += 1
            temp = np.random.randint(1, range_number)
            L.append(temp)
            root.add(root, temp)
        try:
            for k in range(np.random.randint(1, test_number)):
                root = root.DeleteBST(root, L[np.random.randint(0, range_number)])
        except Exception as e:
            print e, L, j
            break
        L = list()
        root = BSTree(1)

    end = time.time()
    print "success, time is %ds, total number is %d, pass number is %d, success rate is %.2f " % (
    end - begin, count * range_number, number, number / count / range_number)
