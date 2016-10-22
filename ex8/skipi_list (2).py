from sllist import SkipiNode as Node

class SkipiList:
    """
    This class represents a special kind of a doubly-linked list
    called a SkipiList. A SkipiList is composed of Nodes (SkipiNode from
    sllist).cIn addition to the data, each Node has one pointer to the
    next Node in the list, and another pointer to the prev-prev Node in the 
    list (hence the name "skipi"). The only data members the class contains 
    are the head and the tail of the list.
    """
    def __init__(self):
        """Constructs an empty SkipiList."""
        "*** YOUR CODE HERE ***"
        
    def add_first(self, data):
        """
        Adds an item to the beginning of a list.
        data - the item to add
        """
        "*** YOUR CODE HERE ***"
    
    def remove_first(self):
        """
        Removes the first Node from the list and return its data.
        Returns that data of the removed node
        """
        "*** YOUR CODE HERE ***"

    def add_last(self, data):
        """
        Adds an item to the end of a list.
        data - the item to add
        """
        "*** YOUR CODE HERE ***"
        
    def remove_last(self):
        """
        Removes the last Node from the list and return its data.
        The data of the removed node
        """
        "*** YOUR CODE HERE ***"
    
    def remove_node(self, node):
        """
        Removes a given Node from the list, and returns its data. 
        Assumes the given node is in the list. Runs in O(1).
        """
        "*** YOUR CODE HERE ***"
         

    def __getitem__(self, k):
        """
        Returns the data of the k'th item of the list.
        If k is negative return the data of k'th item from the end of the list.
        If abs(k) > length of list raise IndexError.
        "*** YOUR CODE HERE ***"
 
