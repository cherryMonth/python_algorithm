# coding=utf-8


class ElemType:

    def __init__(self, elem, carry):
        self.elem_name = elem
        self.carry = carry


class BiTNode:

    def __init__(self, name, carry):
        self.data = ElemType(name, carry)  # 数据元素
        self.l_child = None  # 左孩子
        self.r_child = None  # 右孩子

    @staticmethod
    def bi_tree_empty(tree):  # 判断二叉树是否为空
        return True if tree != None else False

    def pre_order_traverse(self):
        pass

    def in_order_traverse(self):
        pass

    def post_order_traverse(self):
        pass



