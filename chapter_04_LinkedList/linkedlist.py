class LinkedList:
    class _Node:
        def __init__(self, e=None, node_next=None):
            self.e = e
            self.next = node_next

        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        self.add(0, e)

    def add_last(self, e):
        self.add(self._size, e)

    def add(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError('Add failed. Illegal index.')
        prev = self._dummy_head
        for i in range(index):
            prev = prev.next
        node = self._Node(e)
        node.next = prev.next
        prev.next = node
        self._size += 1

    def getter(self, index):
        if index < 0 or index >= self._size:
            raise ValueError('Get failed. Illegal index.')
        curr = self._dummy_head.next
        for i in range(index):
            curr = curr.next
        return curr.e

    def get_first(self):
        return self.getter(0)

    def get_last(self):
        return self.getter(self._size - 1)

    def setter(self, index, e):
        if index < 0 or index >= self._size:
            raise ValueError('Set failed. Illegal index.')
        curr = self._dummy_head.next
        for i in range(index):
            curr = curr.next
        curr.e = e

    def contains(self, e):
        curr = self._dummy_head.next
        while curr:
            if curr.e == e:
                return True
            curr = curr.next
        return False

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise ValueError('Remove failed. Illegal index.')
        prev = self._dummy_head
        for i in range(index):
            prev = prev.next
        ret = prev.next
        prev.next = ret.next
        ret.next = None
        self._size -= 1
        return ret.e

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def __str__(self):
        curr = self._dummy_head.next
        data = []
        while curr:
            data.append(str(curr.e))
            curr = curr.next
        return '<chapter_03_LinkedList.linkedlist.LinkedList>: (Head) ' + \
            ' -> '.join(data) + ' (Tail)'

    def __repr__(self):
        return self.__str__()

    def reverse1(self, res):
        """
        链表的逆序操作
        :param res:
        :return:
        """
        root = self._dummy_head.next
        self._helper(res, root)

    def _helper(self, res, node):
        # 链表的逆向，使用递归方式实现
        if node.next == None:
            res.append(node.e)   # 这里需要添加一个
            return
        self._helper(res, node.next)
        res.append(node.e)

    def reverse2(self, res):
        """
        链表的逆序操作
        :param res:
        :return:
        """
        head = self._dummy_head.next
        while head != None:
            res.insert(0, head.e)
            head = head.next
        return res

    def removeRepeatNode(self):
        """
        将单向链表里面连续的节点给删除掉， 非连续的重复的节点不进行删除
        :return:
        """
        head = self._dummy_head
        while head.next and head.next.next:
            if head.next.e == head.next.next.e:
                deleteNode = head.next.next   # 将删除节点指向重复的第二个节点， 这样删除的时候就会把第一个节点也进行删除
                while deleteNode.next and deleteNode.e == deleteNode.next.e:
                    deleteNode = deleteNode.next
                head.next = deleteNode.next   # 头指针的下一个节点指向被删除节点的下一个节点

            else:
                head = head.next

    def bianli(self):
        """
        遍历链表
        :return:
        """
        head = self._dummy_head
        dataList = []
        size = 0
        head = head.next
        while head:
            dataList.append(head.e)
            head = head.next
            # 测试循环列表， 查看循环链表的入口节点
            size += 1
            if size > self._size:
                break
        return dataList


    def getReverseNumK(self, k):
        """
        获取倒数第k个节点
        :return:
        """
        head = self._dummy_head
        if k > self._size:
            return None
        while k:
            head = head.next
            k = k - 1
        headB = self._dummy_head
        while head:
            head = head.next
            headB = headB.next
        return headB

    def createCirclelist(self):
        """
        构造循环链表， 注意构建了循环链表后之前的遍历链表的方式都不能生效了
        :return:
        """
        head = self._dummy_head
        while head.next:
            head = head.next
        tail = head
        size = self._size
        half = size//2
        head = self._dummy_head
        while half:
            head = head.next
            half -= 1
        halfNode = head
        tail.next = halfNode

    """
    1--2--3--4--5--6--7--8--9--10
                   |            |
                   |            |
                   --------------
    第一步： 假设是在7这个节点两者进行相等。
    设1-6段为x, 设6-7这段为y, 设环的长度6-10的长度为r, 快指针走了n圈环 
    第一次相等的时候快慢指针走的距离为分别为x+y+nr, x+y
    因为快慢指针的速度差为2
    x+y+nr = 2x+2y
    解方程得到：
    nr = x+y， 那么慢指针再从新从头开始走， 同时快指针在y处开始走
    慢指针走x快指针也是走x, 则快指针就会有x+y正好会走一个圈的起始地点。就是入口处了
      
    """
    def getCircleEntry(self):
        """
        寻找单向链表的环
        :return:
        """
        slow = self._dummy_head
        fast = self._dummy_head
        # 使用快慢指针的方式实现， 快慢指针一定会在某一个节点进行重复，
        # 且循环链表里面是不存在next为None的节点的, 下面的这种方式不能得到结果
        # slow = self._dummy_head
        # fast = self._dummy_head.next.next
        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next.next
        # slow = self._dummy_head
        # while id(slow) != id(fast):
        #     slow = slow.next
        #     fast = fast.next
        # return slow

        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not slow or not fast:    # 这里注意判断
            return None
        slow = self._dummy_head
        while id(slow) != id(fast):
            slow = slow.next
            fast = fast.next
        return slow

    def mergeTwoOrderList(self, list1, list2):

        len1 = list1._size
        len2 = list2._size
        if len1 == 0 and len2 == 0:
            return -1
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1

        head1 = list1._dummy_head.next
        head2 = list2._dummy_head.next

        self._dummy_head = self._Node(-1)
        head = self._dummy_head
        while head1 and head2:
            if head1.e > head2.e:
                head.next = self._Node(head2.e)
                head = head.next
                head2 = head2.next
            else:
                head.next = self._Node(head1.e)
                head = head.next
                head1 = head1.next
        # 把剩余的直接连接起来即可， 不用再继续遍历下去了
        if not head1:
            head.next = head2

        if not head2:
            head.next = head1
        self._size = len1 + len2

    def joinExistList(self, existList):
        """
        将一个已有的链表添加到
        :param existList:
        :return:
        """
        if existList._size == 0:
            return
        existHead = existList._dummy_head.next
        head = self._dummy_head
        while head.next:
            head = head.next
        head.next = existHead
        self._size = self._size + existList._size

    def findFirstCommonNode(self, list1, list2):
        """
        查找两个链表额第一个公共节点
        :param list1:
        :param list2:
        :return:
        """
        listLen1 = list1._size
        listLen2 = list2._size

        if listLen1 == 0 or listLen2 == 0:
            return -1
        listHead1 = list1._dummy_head
        listHead2 = list2._dummy_head
        dLen = abs(listLen1-listLen2)
        if listLen1 > listLen2:
            while dLen:
                listHead1 = listHead1.next
                dLen = dLen - 1
        if listLen1 < listLen2:
            while dLen:
                listHead2 = listHead2.next
                dLen -= 1
        while listHead1 != listHead2 and listHead1 and listHead2:
            listHead1 = listHead1.next
            listHead2 = listHead2.next

        if listHead1 and listHead2:
            return listHead2
        else:
            return None




if __name__ == '__main__':
    linkedlist = LinkedList()
    print(linkedlist.get_size())
    linkedlist.add_first(1)
    linkedlist.add_first(2)
    linkedlist.add_first(4)
    linkedlist.add_first(5)
    reverse_list = []
    linkedlist.reverse1(reverse_list)
    print(reverse_list)
    reverse_list2 = []
    print(linkedlist.reverse2(reverse_list2))

    # print(linkedlist.get_size())
    # print(linkedlist)
    # print(linkedlist.getter(3))
    # print(linkedlist.get_first())
    # print(linkedlist.get_last())
    #
    # print(linkedlist)
    # linkedlist.remove(2)
    # linkedlist.remove_first()
    # linkedlist.remove_last()
    # print(linkedlist)

    """
    测试删除链表里面连续重复的节点
    """
    repeatList = LinkedList()
    for i in [1,2,3,4,5,5,5,6,6,6,7,7,8]:
        repeatList.add_last(i)
    print("获取链表的倒数第k个节点为:{}".format(repeatList.getReverseNumK(10)))
    print("链表的遍历为: {}".format(repeatList.bianli()))
    repeatList.removeRepeatNode()
    print("删除重复的链表后的节点为: {}".format(repeatList.bianli()))


    circleList = LinkedList()
    for i in range(21):
        circleList.add_last(i)
    print("创建循环链表前的遍历{}".format(circleList.bianli()))
    circleList.createCirclelist()
    print("循环链表的遍历， 最后一个节点是入口节点{}".format(circleList.bianli()))
    print(circleList.getCircleEntry().e)

    firstList = LinkedList()
    secondList = LinkedList()
    for i in range(0, 10, 2):
        firstList.add_last(i)
    for i in range(1, 20, 2):
        secondList.add_last(i)
    print("偶数链表遍历为: {}".format(firstList.bianli()))
    print("奇数链表遍历为: {}".format(secondList.bianli()))
    mergeList = LinkedList()
    mergeList.mergeTwoOrderList(firstList, secondList)
    print("合并后的奇偶数链表遍历为: {}".format(mergeList.bianli()))


    """
    测试两个链表的第一个公共节点
    """
    firstList = LinkedList()
    for i in range(0, 10):
        firstList.add_last(i)
    secondList = LinkedList()
    for i in range(5, 10):
        secondList.add_last(i)
    commonList = LinkedList()
    for i in range(10, 15):
        commonList.add_last(i)
    firstList.joinExistList(commonList)
    secondList.joinExistList(commonList)
    print("第一个链表为: {}".format(firstList.bianli()))
    print("第二个链表为: {}".format(secondList.bianli()))
    firstCommonNode = firstList.findFirstCommonNode(firstList, secondList)
    print("第一个公共节点为: {}".format(firstCommonNode.e if firstCommonNode else None))
    # 测试非存在公共节点的两个链表
    singleList = LinkedList()
    for i in range(20, 25):
        singleList.add_last(i)
    firstCommonNode = firstList.findFirstCommonNode(firstList, singleList)
    print("第一个公共节点为: {}".format(firstCommonNode.e if firstCommonNode else None))


