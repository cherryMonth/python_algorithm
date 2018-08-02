# coding=utf-8

"""
社会的ALV 旋转 跳跃
"""


class ALVNode:

    def __init__(self, key):
        self.key = key
        self.height = 0
        self.right_child = None
        self.left_child = None


def R_Rotate(p):
    """
    以p为根的二叉树作右旋处理
    父节点成为左子树的右子树
    左子树的右子树成为父节点的左子树
    并记录当前根节点的平衡因子
    :param p:
    :return:
    """

    lc = p.left_child  # lc指向p的左子树根节点
    p.left_child = lc.right_child  # lc的右子树挂接p的左子树
    lc.right_child = p
    p.height = max(get_length(p.right_child), get_length(p.left_child)) + 1
    lc.height = max(get_length(lc.right_child), get_length(lc.left_child)) + 1
    return lc


def L_Rotate(p):
    """
    以p为根的二叉树左旋转处理
    父节点成为右子树的左子树
    原左子树的左子树成为父节点的右子树
    :param p:
    :return:
    """

    rc = p.right_child
    p.right_child = rc.left_child
    rc.left_child = p
    p.height = max(get_length(p.right_child), get_length(p.left_child)) + 1
    rc.height = max(get_length(rc.right_child), get_length(rc.left_child)) + 1
    return rc


def L_R_Rotate(root):
    """
    双旋转 先右旋转然后左旋转
    LR旋转是向左子树插入时出现的情况, 此时无法通过一次旋转解决问题 然后我们需要先对左子树重新构建
    然后重新构建整棵树

    我们先对左子树进行左旋转，因为此时插入结点在左子树的右孩子，当平衡之后由于左
    子树要比右子树要高，所以要对树进行右旋转

    :param root:
    :return:
    """

    root.left_child = L_Rotate(root.left_child)
    return R_Rotate(root)


def R_L_Rotate(root):
    """
    双旋转 先右旋转然后左旋转
    RL旋转是向右子树插入时出现的情况, 此时无法通过一次旋转解决问题 然后我们需要先对右子树重新构建
    然后重新构建整棵树

    双旋转解决的是两种特殊情况
    当插入结点在左子树的右孩子或在右子树的左孩子时会出现一此无法均衡的情况

    我们先对右子树进行右旋转，因为此时插入结点在右子树的左孩子，当平衡之后由于右
    子树要比左子树要高，所以要对树进行左旋转

    :param root:
    :return:
    """

    root.right_child = R_Rotate(root.right_child)
    return L_Rotate(root)


def get_length(root):
    """
    得到每一个结点的平衡因子
    :param root:
    :return:
    """

    return -1 if root is None else root.height


def insert(root, key):
    if root is None:
        return ALVNode(key)

    if key < root.key:
        root.left_child = insert(root.left_child, key)
        if get_length(root.left_child) - get_length(root.right_child) == 2:
            # 当插入结点在左子树的左孩子时直接插入即可
            if key < root.left_child.key:
                root = R_Rotate(root)  # LL
            else:
                # 当插入结点在左子树的右孩子时需要双旋转
                root = L_R_Rotate(root)  # LR
    elif key > root.key:
        root.right_child = insert(root.right_child, key)
        if get_length(root.right_child) - get_length(root.left_child) == 2:
            # 当插入结点在右子树的右孩子时直接插入即可
            if key > root.right_child.key:
                root = L_Rotate(root)  # LL
            else:
                # 当插入结点在右子树的左孩子时需要双旋转
                root = R_L_Rotate(root)  # RL
    root.height = max(get_length(root.right_child), get_length(root.left_child)) + 1  # 更新当前结点的平衡因子
    return root


def find_min(root):
    """
    和BST树一样，当删除结点时需要找到后继结点
    :param root:
    :return:
    """
    if root is None:
        return None
    if root.left_child is None:
        return root
    return find_min(root.left_child)


def remove(root, key):
    """
    删除算法类似于BST树，对左，右子树的处理类似于添加的逆运算
    :param root:
    :param key:
    :return:
    """

    if root is None:
        return None

    if key < root.key:
        root.left_child = remove(root.left_child, key)  # 递归处理得到左子树
        if get_length(root.right_child) - get_length(root.left_child) == 2:
            # 当左子树删除之后若比右子树低两个平衡因子，那么要对右子树进行旋转
            right = root.right_child
            if get_length(right.left_child) > get_length(right.right_child):
                # 若右子树的左孩子大于右孩子的深度，则和添加算法一样，需要双旋转
                root = R_L_Rotate(root)
            else:
                root = L_Rotate(root)
    elif key > root.key:
        root.right_child = remove(root.right_child, key)  # 递归处理得到右子树
        if get_length(root.left_child) - get_length(root.right_child) == 2:
            # 当右子树删除之后若比左子树低两个平衡因子，那么要对左子树进行旋转
            left = root.left_child
            if get_length(left.right_child) > get_length(left.left_child):
                # 若左子树的右孩子大于左孩子的深度，则和添加算法一样，需要双旋转
                root = L_R_Rotate(root)
            else:
                root = R_Rotate(root)
    else:

        # 此处进行结点的删除操作，类似于BST
        if root.right_child and root.left_child:
            # 当有左、右子树时删除后继结点
            root.key = find_min(root.right_child).key
            root.right_child = remove(root.right_child, root.key)
        else:
            # 若是单边树则直接删除即可
            root = root.left_child if root.left_child else root.right_child
    if root:
        root.height = max(get_length(root.right_child), get_length(root.left_child)) + 1
    return root


if __name__ == "__main__":
    root = None
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
            root = insert(root, temp)
        try:
            for k in range(np.random.randint(1, test_number)):
                root = remove(root, L[np.random.randint(0, range_number)])
        except Exception as e:
            print e, L, j
            exit(0)
        L = list()
        root = None
    end = time.time()
    print "success, time is %ds, total number is %d, pass number is %d, success rate is %.2f " % (
        end - begin, count * range_number, number, number / count / range_number)
