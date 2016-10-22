
class Node:
    """
    This class represents the Node of the List.
    The Node contains the data and points to next element (Node).
    """
    def __init__(self, data, next=None):
        """
        Constructor for Node.
        data - The data the Node holds
        next - The next Node in the list
        """
        self.data = data
        self.next = next
        
    def get_next(self):
        """
        Returns the Node this Node is pointing to.
        """
        return self.next

    def get_data(self):
        """
        Returns the data of this Node.
        """
        return self.data

    def set_next(self,next):
        """
        Sets the Node that will follow this Node to the one given in the parameter.
        next - the Node that will now follow this Node
        """
        self.next = next

class List:
    """
    This class represents a single-linked list.
    The only data member the class contains is the head of the list.
    """
    def __init__(self):
        """
        Constructs an empty list.
        """
        self.head = None
    
    def add_first(self,data):
        """
        Adds a data item to the beginning of the list.
        """
        self.head = Node(data, self.head)
        
    def remove_first(self):
        """
        Removes the first node from the list and return its data or null if the list is empty.
        """
        if (self.head is None):
            return None
            
        res = self.head.data
        self.head = self.head.next
        return res

class SkipiNode:
    """
    This class represents a Node for SkipiList.
    The SkipiNode contains the data, points to next element (Node) and to
    a node that is previous to its previous node.
    """

    def __init__(self, data, next=None, skip_back=None):
        self.data = data
        self.next = next
        self.skip_back = skip_back
