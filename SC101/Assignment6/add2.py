"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur1 = l1
    cur2 = l2  # mark the first node of both linked list
    carry = 0  # if value add up from each node in each linked list exceed 10, change to 1.
    switch1 = True  # controller for l1's nodes and below is for l2
    switch2 = True
    linked_list = None  # the linked list to return for the output
    end = None  # to keep track on the last node

    while True:
        if cur1 and switch1 is True:  # if there is another node after current node the switch will be True
            val1 = cur1.val  # and then get the value for the current vnode's value
        if cur2 and switch2 is True:
            val2 = cur2.val

        if switch1 and switch2 is True:  # both node in each linked list are not the last node
            if val1 + val2 == 10:
                new_node = ListNode(0 + carry, None)
            else:
                if linked_list is None:  # condition for the first node in the output
                    new_node = ListNode(((val1 + val2) % 10), None)
                else:
                    if val1 + val2 + carry == 10:
                        new_node = ListNode(0, None)
                    else:
                        new_node = ListNode(((val1 + val2) % 10) + carry, None)

        elif switch1 is True and switch2 is False:  # condition if l1 still have next node while l2 does not for the
            if val1 + carry >= 10:  # current node in each linked list
                new_node = ListNode(0, None)
            else:
                new_node = ListNode(val1 + carry, None)

        elif switch1 is False and switch2 is True:  # condition if the current nodes in l1 doesnt have next node and l2
            if val2 + carry >= 10:  # still has.
                new_node = ListNode(0, None)
            else:
                new_node = ListNode(val2 + carry, None)

        else:
            if carry == 1:  # if the last node for the output is over 10 after add up, carry will be one and need to add
                new_node = ListNode(1, None)  # one more node which the value is 1 as the last node.
                cur = linked_list  # find the last node and add the new_node to replace it as the last one.
                while cur.next is not None:
                    cur = cur.next
                cur.next = new_node
            return linked_list

        if linked_list is None:  # add the calculated node to the linked list for output
            linked_list = new_node
            end = new_node
        else:
            end.next = new_node
            end = end.next

        if switch1 is True and switch2 is True:  # 63 to 79 is to check on 3 different conditions to decide if carry is
            if val1 + val2 + carry >= 10:        # 1 or 0 base on the val 1 and val 2 added up.
                carry = 1
            else:
                carry = 0

        elif switch1 is True and switch2 is False:
            if val1 + carry >= 10:
                carry = 1
            else:
                carry = 0

        elif switch1 is False and switch2 is True:
            if val2 + carry >= 10:
                carry = 1
            else:
                carry = 0

        if cur1.next is not None:  # uf the current node in l1 has next node, go to the next node ready to calculated
            cur1 = cur1.next  # otherwise turn off the switch and dont need to get val
        else:
            switch1 = False

        if cur2.next is not None:  # same as the above.
            cur2 = cur2.next
        else:
            switch2 = False


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
