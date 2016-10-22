#############################################################
# FILE : ex8.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex8 200132014
# DESCRIPTION: skipi list
#############################################################
from sllist import SkipiNode as Node


def printn(sll):
    """ prints all the data in the sll"""
    node = sll.head
    count = 0
    while node is not None:
        print(node.data, end=" ")
        node = node.next
        count += 1
        if count % 6 == 0:
            print()


def create(n):
    """ creates a list with 1...n  datas"""
    x = SkipiList()
    for i in range(n, 0, -1):
        x.add_first(i)
    return x


class SkipiList:
    """
    This class represents a special kind of a doubly-linked list
    called a SkipiList. A SkipiList is composed of Nodes (Node from
    sllist).cIn addition to the data, each Node has one pointer to the
    next Node in the list, and another pointer to the prev-prev Node in the 
    list (hence the name "skipi"). The only data members the class contains 
    are the head and the tail of the list.
    """
    def __init__(self):
        """Constructs an empty SkipiList."""
        self.head = None
        self.tail = None
        
    def add_first(self, data):
        """
        Adds an item to the beginning of a list.
        data - the item to add
        """
        self.head = Node(data, self.head)
        if self.head.next is None:
            self.tail = self.head
        if (self.head.next is not None and
                self.head.next.next is not None):
            self.head.next.next.skip_back = self.head
    
    def remove_first(self):
        """
        Removes the first Node from the list and return its data.
        Returns that data of the removed node
        """
        if self.head is None:
            return
        if self.head is self.tail:
            self.tail = None
            data = self.head.data
            self.head = None
            return data
        data = self.head.data
        self.head = self.head.next
        self.head.skip_back = None
        if self.head.next is not None:
            self.head.next.skip_back = None
        return data

    def add_last(self, data):
        """
        Adds an item to the end of a list.
        data - the item to add
        """
        if self.head is None:
            self.tail = Node(data, None)
            self.head = self.tail
        else:
            if self.tail.skip_back is not None:
                self.tail.next = Node(data, None,
                                      self.tail.skip_back.next)
            elif self.head is self.tail:
                self.tail.next = Node(data, None)
            else:
                self.tail.next = Node(data, None, self.head)
            self.tail = self.tail.next

    def remove_last(self):
        """
        Removes the last Node from the list and return its data.
        The data of the removed node
        """
        if self.tail is None:
            return
        data = self.tail.data
        if self.tail.skip_back is not None:
            self.tail = self.tail.skip_back.next
            self.tail.next = None
        elif self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.head.next = None
            self.tail = self.head
        return data
    
    def remove_node(self, node):
        """
        Removes a given Node from the list, and returns its data. 
        Assumes the given node is in the list. Runs in O(1).
        """
        data = node.data
        if self.head == node:
            return self.remove_first()
        if self.tail == node:
            return self.remove_last()
        else:
            if node.skip_back is not None:
                node.skip_back.next.next = node.next
            else:
                self.head.next = node.next
            if node.next is not None:
                node.next.skip_back = node.skip_back
                if node.next.next is not None:
                    if node.skip_back is not None:
                        node.next.next.skip_back = node.skip_back.next
                    else:
                        node.next.next.skip_back = self.head
        return data

    def __getitem__(self, k):
        """
        Returns the data of the k'th item of the list.
        If k is negative return the data of k'th item from the end of the list.
        If abs(k) > length of list raise IndexError.
        """
        if k >= 0:
            node = self.head
        else:
            node = self.tail
            k += 1

        # go up or down until you get there, skippi is 2 down
        while k != 0:
            if node is None:
                raise IndexError
            elif k > 0:
                node = node.next
                k -= 1
            elif k == -1 and node is not self.head and node is self.head.next:

                return self.head.data
            else:

                node = node.skip_back
                k += 2
        # check for the last time and return
        if node is None:
                raise IndexError
        return node.data
