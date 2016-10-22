#############################################################
# FILE : ex8.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex8 200132014
# DESCRIPTION: node - lists functions
#############################################################
from sllist import List, Node


def update_merge(nod, first):
    """updates the first value to the nod
    and returns next nodes from both"""
    if nod is None:
        nod = Node(first.get_data())
    else:
        nod.set_next(Node(first.get_data()))
        nod = nod.get_next()
    first = first.get_next()
    return nod, first


def update_sort(nod, first):
    """updates the first to be the nod
    and returns next nodes from both"""
##    print("update sort in, nod", nod.get_data(), "first", first.get_data())
    nod.set_next(first)
    nod = nod.get_next()
    first = first.get_next()
    return nod, first


def merger(first, second, nod, update_merge=update_merge,
           leng_first=float("inf"), leng_second=float("inf"),
           doubles=False):
    """merges two sorted node lists in the given length to the nod,
    using update_merge to update nodes
    returns the begginning of the node list
    if doubles if True include double nodes twice
    this function is complex but avoids repetition...
    """
    start = nod
    # look for the smaller values
    while ((first is not None and second is not None) and
           (leng_first > 0 and leng_second > 0)):
        if first is second and doubles:
            first = first.get_next()
            leng_first -= 1
        elif first.get_data() > second.get_data():
            nod, second = update_merge(nod, second)
            leng_second -= 1
        else:
            nod, first = update_merge(nod, first)
            leng_first -= 1

    # keep on with the list the is not empty
    while first is not None and leng_first > 0:
##        print("empty first", first.get_data())
        nod, first = update_merge(nod, first)
        leng_first -= 1
    while second is not None and leng_second > 0:
##        print("empty second", second.get_data())
        nod, second = update_merge(nod, second)
        leng_second -= 1
    return start


def check_int(sll):
    """checks that the list is integer only"""
    nod = sll.head
    while nod is not None:
        if type(nod.get_data()) != int and (type(nod.get_data()) != float):
            return False
        nod = nod.get_next()
    return True


def check_sorted(sll):
    """checks that the list is sorted"""
    nod = sll.head
    while nod is not None and nod.get_next() is not None:
        if nod.get_data() > nod.get_next().get_data():
            return False
        nod = nod.get_next()
    return True


def merge_lists(first_list, second_list, doubles=True):
    """
    Merges two sorted (in ascending order) lists into one new sorted list in
    an ascending order. The resulting new list is created using new nodes
    (copies of the nodes of the given lists). Assumes both lists are sorted in
    ascending order. The original lists should not be modified.
    """
    sll = List()
    sll.head = Node("unrelevant")
    nod = sll.head
    merger(first_list.head, second_list.head, nod) 

    # Get rid of the head, it is just faster
    # than making an exception for the first time.
    sll.head = sll.head.get_next()

    return sll


def contains_cycle(sll):
    """
    Checks if the given list contains a cycle. 
    A list contains a cycle if at some point a Node in the list points to 
    a Node that already appeared in the list. Note that the cycle does not 
    necessarily contain all the nodes in the list. The original list should 
    not be modified.
    Returns true if the list contains a cycle

    >>> x = Node(1)
    >>> y = Node(2)
    >>> x.set_next(y)
    >>> z = List()
    >>> z.head = x
    >>> contains_cycle(z)
    False
    >>> y.set_next(x)
    >>> contains_cycle(z)
    True
>>> 
    """
    node_sll = sll.head
    node_test = sll.head
    while node_test is not None and node_test.get_next() is not None:
        node_sll = node_sll.get_next()
        node_test = node_test.get_next().get_next()
        if node_sll is node_test:
            return True
    return False


def reverse(sll):
    """
    Reverses the given list (so the head becomes the last element, and every 
    element points to the element that was previously before it). Runs in O(n). 
    No new object is created or returned in default .
    >>> sll = List()
    >>> sll.add_first(1)
    >>> sll.add_first(2)
    >>> reverse(sll)
    >>> sll.head.get_data()
    1
    >>> sll.head.get_next().get_data()
    2
    >>> sll.head.get_next().get_next()
    >>> 
    """

    current = sll.head
    if current is None:
        return
    after = current.get_next()
    current.set_next(None)
    while after is not None:
        before = after.get_next()
        after.set_next(current)
        current = after
        after = before
    sll.head = current

    
def length_node(start, end=None):
    """returns the length of the list between two nodes"""
    length = 1
    while start.get_next() is not end:
        start = start.get_next()
        length = length + 1
    return length, start


def is_palindrome(sll):
    """
    Checks if the given list is a palindrome. A list is a palindrome if 
    for j=1...n/2 (where n is the number of elements in the list) the 
    element in location j equals to the element in location n-j. 
    Note that you should compare the data stored in the nodes and 
    not the node objects themselves. The original list should not be modified.
    Returns true if the list is a palindrome
    >>> sll = List()
    >>> ll = sll
    >>> sll.add_first(3)
    >>> sll.add_first(4)
    >>> sll.add_first(3)
    >>> is_palindrome(sll)
    True
    >>> sll = List()
    >>> sll.add_first(3)
    >>> sll.add_first(3)
    >>> sll.add_first(2)
    >>> sll.add_first(3)
    >>> sll.add_first(3)
    >>> is_palindrome(sll)
    True
    >>> sll = List()
    >>> is_palindrome(sll)
    True
    >>> sll = List()
    >>> sll.add_first(3)
    >>> is_palindrome(sll)
    True
    """
    end = sll.head
    if end is None:
        return True
    leng, end = length_node(end)

    start = sll.head
    middle = start
    for index in range(leng//2):
        middle = middle.get_next()
    rev = List()
    rev.head = middle
    reverse(rev)
    boolean = True
    while end is not None:
        if end.get_data() != start.get_data():
            boolean = False
        end = end.get_next()
        start = start.get_next()
    reverse(rev)
    return boolean


def have_intersection(first_list, second_list):
    """
    Checks if the two given lists intersect. 
    Two lists intersect if at some point they start to share nodes. 
    Once two lists intersect they become one list from that point on and 
    can no longer split apart. Assumes that both lists does not contain cycles. 
    Note that two lists might intersect even if their lengths are not equal. 
    No new object is created, and niether list is modified.
    Returns true if the lists intersect.
    
    >>> x = Node(1)
    >>> y = Node(2)
    >>> w = Node(4)
    >>> z = Node(3)
    >>> w.set_next(x)
    >>> z.set_next(y)
    >>> y.set_next(w)
    >>> first = List()
    >>> second = List()
    >>> have_intersection(first,second)
    False
    >>> first.head, second.head = w, z
    >>> have_intersection(first,second)
    True
    """
    first = first_list.head
    if first is not None:
        while first.get_next() is not None:
            first = first.get_next()
    second = second_list.head
    if second is not None:
        while second.get_next() is not None:
            second = second.get_next()
    return first is second and first is not None


def get_item(sll, k):
    """
    Returns the k'th element from of the list. 
    If k > list_size returns None, if k<0 returns the k element from the end.

    >>> sll = List()
    >>> sll.add_first(1)
    >>> sll.add_first(2)
    >>> sll.add_first(3)
    >>> sll.add_first(4)
    >>> sll.add_first(5)
    >>> get_item(sll,0)
    5
    >>> get_item(sll,1)
    4
    >>> get_item(sll,-2)
    2
    >>> sll.head.get_next().get_data()
    4
    >>> get_item(sll,6)
    >>> get_item(sll,5)
    >>> get_item(sll,4)
    1
    >>> get_item(sll,-1)
    1
    """
    if k < 0:
        return get_end(sll, -k)
    return get_start(sll, k)


def get_end(sll, k):
    """
    Returns the k'th element from of the end of the list
    Returns None if does not exist
    """
    node_data = sll.head 
    node_end = sll.head
    node_end = steps(node_end, k-1)
    if node_end is None:
        return
    node_end = node_end.get_next()
    while node_end is not None:
        node_end = node_end.get_next()
        node_data = node_data.get_next()
    return node_data and node_data.get_data()


def get_start(sll, k):
    """
    Returns the k'th element from of the list
    Returns None if does not exist
    """
    node_sll = sll.head
    node_sll = steps(node_sll, k)
    if node_sll is not None:
        return node_sll.get_data()


def steps(node, step):
    """ gets a node and steps as many steps as wished
    and returns the node, or None if the list ended"""
    if node is None:
            return
    for index in range(step):
        node = node.get_next()
        if node is None:
            return
    return node


def length(sll):
    """returns the length of the sll"""
    node = sll.head
    leng = 0
    while node is not None:
        leng += 1
        node = node.get_next()
    return leng


def printn(sll):
    """ prints all the data in the sll"""
    node = sll.head
    count = 0
    while node is not None:
        print(node.get_data(), end=" ")
        node = node.get_next()
        count += 1
        if count % 6 == 0:
            print()


def create(n):
    x = List()
    for i in range(n, 0, -1):
        x.add_first(i)
    return x


def copy_sll(sll):
    """
    """
    node_sll = sll.head
    nod = Node(node_sll.get_data())
    sll = List()
    sll.head = nod
    while node_sll is not None:
        nod.set_next(Node(node_sll.get_data()))
        nod = nod.get_next()
        node_sll = node_sll.get_next()
    return sll


def slice_forward(sll, start, stop, step):
    """Returns a new list after slicing the given list from start to stop
    with a positive step"""
    node = sll.head
    ret_sll = List()

    # get to the start
    node = steps(node, start)
    if node is None:
        return ret_sll
    stop -= start
    if stop > 0:
        ret_sll.head = Node(node.get_data())
        ret_end = ret_sll.head

    # start creating the list step by step
    stop -= step
    while stop > 0 and node is not None:
        stop -= step
        node = steps(node, step)
        if node is None:
            return ret_sll
        ret_end.set_next(Node(node.get_data()))
        ret_end = ret_end.get_next()
    return ret_sll


def slice_backwards(sll, start, stop, step):
    """Returns a new list after slicing the given list from start to stop
    with a negative step"""
    # do not include stop and initiate vars
    # for efficiency it actually goes forward,
    # but calculates so it will look like backwards     
    start, stop = stop, start
    if start < 0:
        start = -1
        no_stop = True
    else:
        no_stop = False
    start += 1
    start += (stop-start) % step
    node = sll.head
    ret_sll = List()

    # get to the start
    node = steps(node, start)
    if node is None:
        return ret_sll
    stop = stop - start
    if stop >= 0 or no_stop:
        ret_sll.add_first(node.get_data())

    # now step by step
    while stop > 0 and node is not None:
        stop = stop - step
        node = steps(node, step)
        if node is None:
            return ret_sll
        ret_sll.add_first(node.get_data())
    return ret_sll


def slice(sll, start, stop=None, step=1):
    """ Returns a new list after slicing the given list from start to stop
    with a step.
    Behaves the same as using list[start:step:stop], so stop is not in the
    returned list.
    """
    if stop is None:
        stop = start
        start = 0
    if step == 0:
        return
    
    # replace minuses with plus
    leng = length(sll)
    if stop < 0:
        stop += leng
        if stop < 0:
            if step > 0:
                stop = 0
            else:
                stop -= leng
        
    if start < 0:
        start += leng
        if start < 0:
            if step > 0:
                start = 0
            if step < 0:
                return List()
    if start >= leng and step < 0:
        start = leng - 1
    # choose which way to go
    if step > 0:
        return slice_forward(sll, start, stop, step)
    else:
        return slice_backwards(sll, start, stop, -step)


def merge_sort(sll):
    """
    Sorts the given list using the merge-sort algorithm. 
    Resulting list should be sorted in ascending order. Resulting list should 
    contain the same node objects it did originally, and should be stable, 
    i.e., nodes with equal data should be in the same order they were in in the 
    original list. You may create a constant number of new to help sorting.
    """
    if sll.head is None:
        return None
    leng = length(sll)
    sll.head = recursive_merge(sll.head, leng)
    end = steps(sll.head, leng-1)
    end.set_next(None)


def recursive_merge(start, leng):
    if leng < 2:
        return start
    
    step = (leng-1) // 2  # Number of steps to the right to end left
    mid = steps(start, step)
    left_leng = step + 1 
    right_leng = leng - left_leng
    right_start = mid.get_next()
    left = recursive_merge(start, left_leng)
    right = recursive_merge(right_start, right_leng)

    if left.get_data() > right.get_data():
        start = right
        right = right.get_next()
        right_leng -= 1
    else:
        start = left
        left = left.get_next()
        left_leng -= 1
    start = merger(left, right, start, update_sort, left_leng, right_leng)
    return start
