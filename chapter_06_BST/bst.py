from collections import deque


class BST:
    """这里的BST实现不包括重复元素（为了演示原理方便）"""
    class _Node:
        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        self._root = self._add(self._root, e)

    def _add(self, node, e):
        # # 递归终止条件
        # if node.e == e:
        #     return
        # elif node.e > e and not node.left:
        #     node.left = self._Node(e)
        #     self._size += 1
        #     return
        # elif ndoe.e < e and not node.right:
        #     node.right = self._Node(e)
        #     self._size += 1
        #     return
        # # 递归条件
        # if node.e > e:
        #     self._add(node.left, e)
        # else:
        #     self._add(node.right, e)

        # 另外一种简洁写法
        if not node:
            self._size += 1
            return self._Node(e)
        if node.e == e:
            return node
        elif node.e > e:
            node.left = self._add(node.left, e)
        else:
            node.right = self._add(node.right, e)
        return node

    def contains(self, e):
        """以root为根有没有e"""
        return self._contains(self._root, e) 

    def _contains(self, node, e):
        """以node为根有没有e"""
        if not node:
            return False
        if node.e == e:
            return True
        elif node.e > e:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right, e)

    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, node):
        """前序遍历以node为根的BST"""
        if not node:
            return
        print(node.e)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_order_NR(self):
        """非常好的DFS例子"""
        stack = []
        stack.append(self._root)
        while stack:
            curr = stack.pop()
            print(curr.e)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    def in_order(self):
        return self._in_order(self._root)

    def _in_order(self, node):
        if not node:
            return
        self._in_order(node.left)
        print(node.e)
        self._in_order(node.right)

    def post_order(self):
        """一个应用是释放内存"""
        return self._post_order(self._root)

    def _post_order(self, node):
        if not node:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.e)

    def level_order(self):
        """非常好的BFS例子"""
        queue = deque()
        queue.append(self._root)
        while queue:
            curr = queue.popleft()
            print(curr.e)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def minimum(self):
        if self.is_empty():
            raise ValueError('BST is empty!')
        self._minimum(self._root)

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self.is_empty():
            raise ValueError('BST is empty!')
        self._maximum(self._root)

    def _maximum(self, node):
        if not node.right:
            return node
        return self._maximum(node.right)

    def remove_min(self):
        ret = self.minimum()
        # 用单链表来验证
        self._root = self._remove_min(self._root)
        return ret

    # 删除掉以node为根的BST中的最小节点
    # 返回删除节点后新的BST的根
    def _remove_min(self, node):
        # 递归终止
        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node

    def remove_max(self):
        ret = self.maximum()
        # 用单链表来验证
        self._root = self._remove_max(self._root)
        return ret

    # 删除掉以node为根的BST中的最大节点
    # 返回删除节点后新的BST的根
    def _remove_max(self, node):
        # 递归终止
        if not node.right:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node
        node.right = self._remove_max(node.right)
        return node

    def remove(self, e):
        self._root = self._remove(self._root, e)

    # 删除以node为根的BST中值为e的节点，递归算法
    # 返回删除节点后的新的BST的根
    def _remove(self, node, e):
        # 递归终止
        if not node:
            return
        # 递归条件
        if node.e > e:
            node.left = self._remove(node.left, e)
            return node
        elif node.e < e:
            node.right = self._remove(node.right, e)
        else: # node.e == e
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node
            if not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node
            # 如果左右子树均不为空
            # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor

    def _generate_depth_string(self, depth):
        res = ''
        for i in range(depth):
            res += '--'
        return res

    def _generate_BST_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth) + 'None\n')
            return
        res.append(self._generate_depth_string(depth) + str(node.e) + '\n')
        self._generate_BST_string(node.left, depth + 1, res)
        self._generate_BST_string(node.right, depth + 1, res)

    def __str__(self):
        res = []
        self._generate_BST_string(self._root, 0, res)
        return '<chapter_06_BST.bst.BST>:\n' + ''.join(res)

    def __repr__(self):
        return self.__str__()

    def _buildTreePreIno(self, preorder, inorder):
        """
        返回构造的 TreeNode 根结点
        使用前序和中序构建二叉树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 在编码过程中，一定要保证 len(pre) == len(tin)，否则逻辑一定不正确
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            # 这里要返回结点，而不是返回具体的数
            self._size += 1
            return self._Node(preorder[0])
        root = self._Node(preorder[0])
        self._size += 1
        # 直接得到在中序遍历中的位置，下面算好偏移量就好了，如果容易算错，记得拿具体例子
        pos = inorder.index(preorder[0])
        root.left = self._buildTreePreIno(preorder[1:pos + 1], inorder[:pos])
        root.right = self._buildTreePreIno(preorder[pos + 1:], inorder[pos + 1:])
        return root

    def buildTreePreIno(self, preorder, inorder):
        # 使用前序和中序生成二叉树
        self._root = self._buildTreePreIno(preorder, inorder)

    def buildTreeInoPost(self, inorder, postorder):
        # 使用中序、后续生成一个二叉树
        self._root = self._buildTreeInoPost(inorder, postorder)

    def _buildTreeInoPost(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            self._size += 1
            return self._Node(postorder[-1])
        root = self._Node(postorder[-1])
        root_in_inorder_position = inorder.index(postorder[-1])
        root.left = self._buildTreeInoPost(inorder[:root_in_inorder_position], postorder[:root_in_inorder_position])
        root.right = self._buildTreeInoPost(inorder[root_in_inorder_position+1:], postorder[root_in_inorder_position: -1])
        return root

    def _findNode(self, value, node):
        """
        查找二叉树中的某一个节点
        :return:
        """
        if not node or node.e == None:
            return None
        if node.e == value:
            return node
        target = self._findNode(value, node.left)
        if target:
            return target
        target = self._findNode(value, node.right)
        if target:
            return target
        return None

    def findNode(self, value):
        # 查找节点， 需要将查找节点的父节点也一起返回回去
        node = self._root
        return self._findNode(value, node)

    def findInorderNextNode(self, value):
        # 查找中序遍历后的下一个节点,
        """
        思路是直接找到中序遍历的第一个节点， 然后分情况进行讨论
        :param value:
        :return:
        """
        node = self.findNode(value)
        if not node:
            return None
        if node.right:
            # 根据中序遍历的顺序，只要存在右子树那么找出右子树的左或根即可， 左存在就找左， 不存在则为根
            node = node.right
            if node.left:
                while node.left:
                    node = node.left
                return node
            else:
                return node
        # 如果所查节点不存在右子树， 那么就向上查父节点
        # else:
        #     while father:
        #         if father.left == node:
        #             return father
        #         father

    def findPreOrderNextNode(self, val):
        node = self.findNode(val)
        if node.left:
            return node.left
        return node.right

    def findPostOrderNextNode(self, val):
        """
        求二叉树的后续遍历的下一个节点
        :param val:
        :return:
        """
        node = self.findNode(val)
        father = node.father
        if father:
            node = father.left
            while node.right:
                node = node.right
            return node
        else:
            return father

    def findCommonAnsentor(self, q, p):
        root = self._root
        node = self.__findCommonAnsentor(root, q, p)
        return node

    def __findCommonAnsentor(self, root, q, p):
        if root is None:
            return None
        if root.val == q or root.val == p:
            return root

        left = self.__findCommonAnsentor(root.left, q, p)
        right = self.__findCommonAnsentor(root.right, q, p)
        if left and right:
            return root
        if left:
            return root.left
        if right:
            return root.right
        return None

    def mirrorBinary(self):
        root = self._root
        self._mirrorBinary(root)

    def _mirrorBinary(self, root):
        """
        先序遍历构建镜像二叉树
        :param root:
        :return:
        """
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self._mirrorBinary(root.left)
        self._mirrorBinary(root.right)

    def levelMirrorBinary(self):
        """
        通过层序构建镜像二叉树
        :return:
        """
        root = self._root
        self._levelMirrorBinary(root)

    def _levelMirrorBinary(self, root):
        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def upDownBinary(self):
        """
        从上往下, 从左往右层序打印二叉树
        :return:
        """
        root = self._root
        res = self._upDownBinary(root)
        return res

    def _upDownBinary(self, root):
        if root is None:
            return None
        queue = []
        queue.append(root)
        res = []
        while queue:
            node  = queue.pop(0)
            res.append(node.e)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def upDownSplitBinary(self):
        root = self._root
        res = self._upDownSplitBinary(root)
        return res

    def _upDownSplitBinary(self, root):
        """
        层序遍历二叉树， 每一个等级都要分开进行打印
        :param root:
        :return:
        """
        if root is None:
            return None

        queue = []
        queue.append(root)
        res = []
        while queue:
            queueLen = len(queue)
            levelRes = []
            while queueLen:
                node = queue.pop(0)
                levelRes.append(node.e)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queueLen -= 1
            res.append(levelRes)
        return res

    def upDownLevelZhiBinary(self):
        root = self._root
        res = self._upDownLevelZhiBinary(root)
        return res

    def _upDownLevelZhiBinary(self, root):
        if root is None:
            return None

        queue = []
        queue.append(root)
        turnLeft = False
        res = []
        while queue:
            queueLen = len(queue)
            levelList = []
            while queueLen:
                node = queue.pop(0)
                if turnLeft:
                    levelList.insert(0, node.e)
                else:
                    levelList.append(node.e)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queueLen -= 1
            turnLeft = ~turnLeft
            res.append(levelList)
        return res

    def findNumK(self, k):
        root = self._root
        if root is None:
            return None
        self.k = k
        node = self._findNumK(root)

        return node

    def _findNumK(self, root):
        """
        获取二叉树第k大的数
        分析： 如果可以实现右中左的遍历顺序那就可以很快得到答案啦
        :param root:
        :param k:
        :return:
        """
        if root is None:
            return None
        node = self._findNumK(root.right)
        if node:
            return node
        self.k -= 1
        if self.k == 0:
            return root
        node = self._findNumK(root.right)
        if node:
            return node

    def depthOfBST(self):
        """
        求二叉树的深度
        :return:
        """
        root = self._root
        depth = self._depthOfBST(root)
        return depth

    def _depthOfBST(self, root):
        if root is None:
            return 0
        """
        # 方法一: 遍历二叉树的高度
        queue = []
        queue.append((1, root))
        depthMax = 1  # 需要一个最大层级的变量来比较， 否则左右节点加一会出错
        while queue:
            depth, node = queue.pop(0)
            depthMax = max(depthMax, depth)
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
        return depthMax
        """

        queue = []
        queue.append(root)
        depthMax = 0  # 需要一个最大层级的变量来比较， 否则左右节点加一会出错
        while queue:
            curLen = len(queue)
            depthMax += 1
            while curLen:
                curLen -= 1
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depthMax




class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def buildTree(self, preorder, inorder):
#         """
#         返回构造的 TreeNode 根结点
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         # 在编码过程中，一定要保证 len(pre) == len(tin)，否则逻辑一定不正确
#         if len(preorder) == 0:
#             return None
#         if len(preorder) == 1:
#             # 这里要返回结点，而不是返回具体的数
#             return self._Node(preorder[0])
#         root = TreeNode(preorder[0])
#         # 直接得到在中序遍历中的位置，下面算好偏移量就好了，如果容易算错，记得拿具体例子
#         pos = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
#         root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
#         return root


# 先序： 4,1,0,3,2,5
# 中序： 0,1,2,3,4,5
"""
         4
        / \
       1   5
      / \
     0   2
          \
           3


     """


class BST1:
    """这里的BST实现不包括重复元素（为了演示原理方便）"""
    class _Node:
        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None
            self.father = None       # 用于找前中后序的下一个节点

    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        self._root = self._add(self._root, e)

    def _add(self, node, e):
        # # 递归终止条件
        # if node.e == e:
        #     return
        # elif node.e > e and not node.left:
        #     node.left = self._Node(e)
        #     self._size += 1
        #     return
        # elif ndoe.e < e and not node.right:
        #     node.right = self._Node(e)
        #     self._size += 1
        #     return
        # # 递归条件
        # if node.e > e:
        #     self._add(node.left, e)
        # else:
        #     self._add(node.right, e)

        # 另外一种简洁写法
        if not node:
            if self._size == 0:
                node = self._Node(e)
                self._size += 1
                return node
            return self._Node(e)
        if node.e == e:
            return node
        elif node.e > e:
            node.left = self._add(node.left, e)
            node.left.father = node
        else:
            node.right = self._add(node.right, e)
            node.right.father = node
        return node

    def contains(self, e):
        """以root为根有没有e"""
        return self._contains(self._root, e)

    def _contains(self, node, e):
        """以node为根有没有e"""
        if not node:
            return False
        if node.e == e:
            return True
        elif node.e > e:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right, e)

    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, node):
        """前序遍历以node为根的BST"""
        if not node:
            return
        print(node.e)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_order_NR(self):
        """非常好的DFS例子"""
        stack = []
        stack.append(self._root)
        while stack:
            curr = stack.pop()
            print(curr.e)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    def in_order(self):
        return self._in_order(self._root)

    def _in_order(self, node):
        if not node:
            return
        self._in_order(node.left)
        print(node.e)
        self._in_order(node.right)

    def post_order(self):
        """一个应用是释放内存"""
        return self._post_order(self._root)

    def _post_order(self, node):
        if not node:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.e)

    def level_order(self):
        """非常好的BFS例子"""
        queue = deque()
        queue.append(self._root)
        while queue:
            curr = queue.popleft()
            print(curr.e)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def minimum(self):
        if self.is_empty():
            raise ValueError('BST is empty!')
        self._minimum(self._root)

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self.is_empty():
            raise ValueError('BST is empty!')
        self._maximum(self._root)

    def _maximum(self, node):
        if not node.right:
            return node
        return self._maximum(node.right)

    def remove_min(self):
        ret = self.minimum()
        # 用单链表来验证
        self._root = self._remove_min(self._root)
        return ret

    # 删除掉以node为根的BST中的最小节点
    # 返回删除节点后新的BST的根
    def _remove_min(self, node):
        # 递归终止
        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node

    def remove_max(self):
        ret = self.maximum()
        # 用单链表来验证
        self._root = self._remove_max(self._root)
        return ret

    # 删除掉以node为根的BST中的最大节点
    # 返回删除节点后新的BST的根
    def _remove_max(self, node):
        # 递归终止
        if not node.right:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node
        node.right = self._remove_max(node.right)
        return node

    def remove(self, e):
        self._root = self._remove(self._root, e)

    # 删除以node为根的BST中值为e的节点，递归算法
    # 返回删除节点后的新的BST的根
    def _remove(self, node, e):
        # 递归终止
        if not node:
            return
        # 递归条件
        if node.e > e:
            node.left = self._remove(node.left, e)
            return node
        elif node.e < e:
            node.right = self._remove(node.right, e)
        else: # node.e == e
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node
            if not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node
            # 如果左右子树均不为空
            # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor

    def _generate_depth_string(self, depth):
        res = ''
        for i in range(depth):
            res += '--'
        return res

    def _generate_BST_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth) + 'None\n')
            return
        res.append(self._generate_depth_string(depth) + str(node.e) + '\n')
        self._generate_BST_string(node.left, depth + 1, res)
        self._generate_BST_string(node.right, depth + 1, res)

    def __str__(self):
        res = []
        self._generate_BST_string(self._root, 0, res)
        return '<chapter_06_BST.bst.BST>:\n' + ''.join(res)

    def __repr__(self):
        return self.__str__()

    def _buildTreePreIno(self, preorder, inorder):
        """
        返回构造的 TreeNode 根结点
        使用前序和中序构建二叉树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 在编码过程中，一定要保证 len(pre) == len(tin)，否则逻辑一定不正确
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            # 这里要返回结点，而不是返回具体的数
            self._size += 1
            return self._Node(preorder[0])
        root = self._Node(preorder[0])
        self._size += 1
        # 直接得到在中序遍历中的位置，下面算好偏移量就好了，如果容易算错，记得拿具体例子
        pos = inorder.index(preorder[0])
        root.left = self._buildTreePreIno(preorder[1:pos + 1], inorder[:pos])
        root.right = self._buildTreePreIno(preorder[pos + 1:], inorder[pos + 1:])
        return root

    def buildTreePreIno(self, preorder, inorder):
        # 使用前序和中序生成二叉树
        self._root = self._buildTreePreIno(preorder, inorder)

    def buildTreeInoPost(self, inorder, postorder):
        # 使用中序、后续生成一个二叉树
        self._root = self._buildTreeInoPost(inorder, postorder)

    def _buildTreeInoPost(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            self._size += 1
            return self._Node(postorder[-1])
        root = self._Node(postorder[-1])
        root_in_inorder_position = inorder.index(postorder[-1])
        root.left = self._buildTreeInoPost(inorder[:root_in_inorder_position], postorder[:root_in_inorder_position])
        root.right = self._buildTreeInoPost(inorder[root_in_inorder_position+1:], postorder[root_in_inorder_position: -1])
        return root

    def _findNode(self, value, node):
        """
        查找二叉树中的某一个节点
        :return:
        """
        if not node or node.e == None:
            return None
        if node.e == value:
            return node
        target = self._findNode(value, node.left)
        if target:
            return target
        target = self._findNode(value, node.right)
        if target:
            return target
        return None

    def findNode(self, value):
        # 查找节点， 需要将查找节点的父节点也一起返回回去
        node = self._root
        return self._findNode(value, node)

    def findInorderNextNode(self, value):
        # 查找中序遍历后的下一个节点
        node = self.findNode(value)
        if not node:
            return None
        if node.right:
            # 根据中序遍历的顺序，只要存在右子树那么找出右子树的左或根即可， 左存在就找左， 不存在则为根
            node = node.right
            if node.left:
                while node.left:
                    node = node.left
                return node
            else:
                return node
        # 如果所查节点不存在右子树， 那么就向上查父节点
        else:
            father = node.father
            while father:
                if father.left == node:
                    return father
                node = father
                father = node.father

    def findCommonAnsentor(self, q, p):
        """
        寻找两个节点的最近的公共祖先
        :param q: 二叉树的第一个节点
        :param p: 二叉树的第二个节点
        :return: 返回为None或者是找到的最近的一个祖先
        """
        root = self._root
        node = self.__findCommonAnsentor(root, q, p)
        return node

    def __findCommonAnsentor(self, root, q, p):
        if root is None:
            return None
        if root.e == q or root.e == p:
            return root

        left = self.__findCommonAnsentor(root.left, q, p)
        right = self.__findCommonAnsentor(root.right, q, p)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None


if __name__ == '__main__':
    bst = BST()
    # nums = [5, 3, 6, 8, 4, 2, 2]
    # for num in nums:
    #     bst.add(num)
    # bst.pre_order()
    # print(bst)

    # bst.in_order()
    # bst.post_order()
    # bst.pre_order_NR()
    # bst.level_order()

    from random import randint
    for i in range(20):
        bst.add(randint(0, 5))
    # print(bst)
    bst.pre_order()
    print("******************")
    bst.in_order()
    # print('*' * 20)
    # bst.remove_min()
    # bst.remove_max()
    # bst.in_order()
    # print('*' * 20)
    # print(bst.size())

    print("使用前序和中序进行二叉树的重建\n\n\n")
    pre = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = BST()
    s.buildTreePreIno(pre, inorder)
    s.pre_order()
    print("******************")
    s.in_order()
    print("size is {}".format(s._size))
    print("使用后序和中序进行二叉树的重建\n\n\n")
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    s = BST()
    s.buildTreeInoPost(inorder, postorder)
    s.post_order()
    print("******************")
    s.in_order()
    print("size is {}".format(s._size))

    node = s.findNode(15)
    print("查找到节点为：{}".format(node.e))



    """
    中序遍历构造的二叉树
    1、 节点存在右子树
    2、 节点不存在右子树
    
    """
    print("节点不存在右子树测试\n\n\n")
    pre_data = [100, 50, 20, 70, 60, 80, 77]
    bb_tree = BST1()
    for dat in pre_data:
        bb_tree.add(dat)
    bb_tree.pre_order()
    print("*******************\n")
    bb_tree.in_order()
    next_node = bb_tree.findInorderNextNode(80)
    print("下一个节点为: {}".format(next_node.e))

    print("节点存在右子树测试\n\n\n")
    pre_data = [100, 20, 30, 70, 60, 120]
    bb_tree = BST1()
    for dat in pre_data:
        bb_tree.add(dat)
    print("30和70的公共祖先是：{}".format(bb_tree.findCommonAnsentor(30, 70).e))
    bb_tree.pre_order()
    print("*******************\n")
    bb_tree.in_order()
    next_node = bb_tree.findInorderNextNode(30)
    print("下一个节点为: {}".format(next_node.e))

    """
    测试二叉树的层序遍历
    """
    newBinaryData = [10, 5, 15, 2, 7, 12, 17, 1, 3, 6, 8, 11, 13, 16, 18]
    newBinary = BST()
    for dat in newBinaryData:
        newBinary.add(dat)
    levelList = newBinary.upDownSplitBinary()
    print("层序遍历分层列表的二叉树链表为: {}".format(levelList))

    levelList = newBinary.upDownBinary()
    print("层序遍历的二叉树链表为: {}".format(levelList))

    levelList = newBinary.upDownLevelZhiBinary()
    print("之字形层序遍历的二叉树链表为: {}".format(levelList))


    """
    寻找二叉树的第k大的数
    """
    bst = BST()
    for i in range(11):
        bst.add(i)
    node = bst.findNumK(2)
    print("二叉树第二大的节点为: {}".format(node.e if node else None))


    """
    测试二叉树的高度
    """
    bst = BST()
    for i in [8,5,7,6,9,3,4,1]:
        bst.add(i)
    depth = bst.depthOfBST()
    print("二叉树的高度为: {}".format(depth))



