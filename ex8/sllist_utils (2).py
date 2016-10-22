from sllist import List, Node

def prt(sll):
    x = sll.head
    while x is not None:
        print(x.data)
        x = x.next
    

def get_length(sll):
    """ Compute the length of a given list.
    Takes one argument - a list, and returns its' length. """
    
    length_sll = 0
    node = sll.head
    while node:
        length_sll += 1
        node = node.next
    return length_sll

def merge(first_list, second_list):
    """
    Merges two sorted lists (in ascending order) into one sorted list.
    The original lists can be modified to the resulting list, in an
    ascending order. Assumes both given lists are sorted.
    """
        
    first_node = first_list.head
    second_node = second_list.head
    
    #choose the merged_list head    
    if first_node and second_node:
        if first_node.data <= second_node.data:
            current_node = first_node
            first_node = first_node.next
            head = first_list.head
        else:
            current_node = second_node
            second_node = second_node.next
            head = second_list.head
    else:
        if first_node:
            current_node = first_node
        else:
            current_node = second_node
            
    while first_node and second_node:
        if first_node.data <= second_node.data:
            current_node.set_next(first_node)
            first_node = first_node.next
        else:
            current_node.set_next(second_node)
            second_node = second_node.next
        current_node = current_node.next
        
    if first_node or second_node:
        if first_node:
            current_node.set_next(first_node)
        else:
            current_node.set_next(second_node)
            
    if head.data == first_list.head.data:
        return first_list
    else:
        return second_list

def merge_lists(first_list, second_list):
    """
    Merges two sorted (in ascending order) lists into one new sorted list in
    an ascending order. The resulting new list is created using new nodes
    (copies of the nodes of the given lists). Assumes both lists are sorted in
    ascending order. The original lists should not be modified.
    """
    merged_list = List()
    first_node = first_list.head
    second_node = second_list.head
        
    while first_node and second_node:
        if first_node.data <= second_node.data:
            merged_list.add_first(first_node.data)
            first_node = first_node.next           
        else:
            merged_list.add_first(second_node.data)
            second_node = second_node.next
                
    if first_node or second_node:
        if first_node:
            while first_node:
                merged_list.add_first(first_node.data)
                first_node = first_node.next
        else:
            while second_node:
                merged_list.add_first(second_node.data)
                second_node = second_node.next
        
    ascending_merged_list = reverse(merged_list)
    return merged_list



def contains_cycle(sll):
    """
    Checks if the given list contains a cycle.
    A list contains a cycle if at some point a Node in the list points to
    a Node that already appeared in the list. Note that the cycle does not
    necessarily contain all the nodes in the list. The original list should
    not be modified.
    Returns true iff the list contains a cycle
    """
    fast_iterator_node = sll.head
    if fast_iterator_node is None:
        return False
    slow_iterator_node = sll.head

    while (fast_iterator_node.next is not None) and (fast_iterator_node.next.next is not None):
        fast_iterator_node = fast_iterator_node.next.next
        slow_iterator_node = slow_iterator_node.next
        if slow_iterator_node == fast_iterator_node:
            return True
    return False
        

def reverse(sll):
    """
    Reverses the given list (so the head becomes the last element, and every
    element points to the element that was previously before it). Runs in O(n).
    No new object is created.
    """

    length_sll = 1
    node = sll.head
    if node is None:
        return None
    #compute the length of the given list 
    while node.next:
        length_sll += 1
        node = node.next
    #save the last node for later use
    last_node = node
        
    node_location = 0
    #scen the list - each time goes to the last "pointed" node and reverse the pointing direction
    while node_location < length_sll - 1:
        previous_node = sll.head
        for val in range(length_sll - node_location - 1):
            previous_node = previous_node.get_next()
        forward_node =  sll.head
        for val in range(length_sll - node_location - 2):
            forward_node = forward_node.get_next()
        previous_node.set_next(forward_node)
        forward_node.set_next(None)
        node_location += 1
    #define the original last node as first
    sll.head = last_node


    
def is_palindrome(sll):
    """
    Checks if the given list is a palindrome. A list is a palindrome if
    for j=0...n/2 (where n is the number of elements in the list) the
    element in location j equals to the element in location n-j.
    Note that you should compare the data stored in the nodes and
    not the node objects themselves. The original list should not be modified.
    Returns true if the list is a palindrome
    """

    length_sll = 0
    node = sll.head
    #compute the length of the given list 
    while node is not None:
        length_sll += 1
        node = node.get_next()

    mid_sll = length_sll // 2
    current_node = sll.head
    for val in range(mid_sll):
        comparison_node_location = length_sll- val - 1
        comparison_node = sll.head
        for val in range(comparison_node_location):
            comparison_node = comparison_node.get_next()
        if comparison_node.get_data() != current_node.get_data():
            return False
        current_node = current_node.get_next()

    return True
        

def have_intersection(first_list, second_list):
    """
    Checks if the two given lists intersect.
    Two lists intersect if at some point they start to share nodes.
    Once two lists intersect they become one list from that point on and
    can no longer split apart. Assumes that both lists does not contain cycles.
    Note that two lists might intersect even if their lengths are not equal.
    No new object is created, and niether list is modified.
    Returns true iff the lists intersect.
    """
    first_node = first_list.head
    if first_node is None:
        return False
    #goes to the last node of the first list
    while first_node.next is not None:
        first_node = first_node.next
       
    second_node = second_list.head
    if second_node is None:
        return False
    #goes to the last node of the second list
    while second_node.next is not None:
        second_node = second_node.next
    #check if the lists intersect in some point    
    if first_node == second_node:
            return True

    return False


def get_item(sll, k):
    """
    Returns the k'th element from of the list.
    If k > list_size returns None, if k<0 returns the k element from the end.
    """
    if k is None or sll is None:
        return None
    
    current_node = sll.head
    list_size = 0
    #compute the length of the given list 
    while current_node is not None:
        current_node = current_node.next
        list_size += 1
        
    if k < 0:
        k = list_size + k
    if k >= list_size or k < 0:
        return None

    node = sll.head
    for val in range(k):
        node = node.next
    return node.data
                
    
def slice(sll, start, stop, step):
    """ Returns a new list after slicing the given list from start to stop
    with a step.
    Imitates the behavior of slicing regular sequences in python.
    slice(sll, [start], stop, [step]):
    With 4 arguments, behaves the same as using list[start:stop:step],
    With 3 arguments, behaves the same as using list[start:stop],
    With 2 arguments, behaves the same as using list[:stop],
    """
    sll = List()
    return sll


def merge_sort(sll):
    prt(sll)
    """
    Sorts the given list using the merge-sort algorithm.
    Resulting list should be sorted in ascending order. Resulting list should
    contain the same node objects it did originally, and should be stable,
    i.e., nodes with equal data should be in the same order they were in in the
    original list. You may create a constant number of new to help sorting.
    """

##    if not sll:
##        return None
    
    def merge_helper(sll):
        
        sll_length = get_length(sll)
        if sll_length >= 2:
            mid_node = sll.head
            if sll_length > 3:
                for val in range ((sll_length // 2) - 2):
                    mid_node = mid_node.next
            current_node = mid_node.next
            
            first_list = List()
            first_list.head = sll.head
            second_list = List()
            second_list.head = current_node
            mid_node.next = None
        
            first_half = merge_helper(first_list)
            second_half = merge_helper(second_list) 

            sll =  merge(first_half, second_half)
        return sll
    
    
    sll.head = merge_helper(sll).head

        
x = List()
x.add_first(5)
x.add_first(8)
