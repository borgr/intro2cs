#############################################################
# FILE : ex9.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex9 200132014
# DESCRIPTION: compression
#############################################################
'''
This module contains several function for compress and decompress data, using
the Huffman code algorithm.
'''
LEFT = 0
RIGHT = 1
LENGTH = 0
ORIGIN = 1
MAGIC = b"i2cshcfv1"
EPSILON = 0.000000000000001
import collections


def symbol_count(data):
    """ returns how frequent the each char is.
    Args
    data- an iterable
    """
    return collections.Counter(char for char in data)


def make_huffman_tree(counter):
    """
    Returns a tuple of tuples representing the huffman
    tree for the given frequencies.

    Args
    counter - a dictinary of chars andnumbers

    Note: will not work will for more than
    10**16 items in counter
    
    >>> make_huffman_tree({3: 1, 2: 1, 1: 1, 0: 1})
    ((0, 1), (2, 3))
    >>> make_huffman_tree({2: 1, 1: 2, 0: 1})
    ((0,2), 1)
    >>> make_huffman_tree({0: 2, 130: 2, 70: 2, 200: 2, 10: 3, 140: 1, 80: 2,
    20: 3, 150: 1, 90: 4, 220: 1, 30: 1, 160: 3, 100: 4, 230: 3, 40: 1, 170: 1,
    110: 2, 240: 1, 50: 4, 180: 2, 60: 3, 190: 2})
    (((((70, 80), (110, 130)), ((180, 190), 50)),
    ((90, 100), ((200, 30), 10))),
    (((20, 60), (160, 230)), (((40, 140), (150, 170)), ((220, 240), 0))))
    """
    if counter == dict():
        return
    counter = collections.Counter(counter)
    tree = None
    frequent = 1
    item = 0
    eps = EPSILON  # used to remember order
    while len(counter) - 1:
        eps += EPSILON
        common = counter.most_common()
        common = sorted(common, key=lambda key: (-key[frequent], key[item]))

        # choose the two to make a tuple from
        rare = common[-1]
        rarer = common[-2]
        
        # make a tuple
        frequency = rare[frequent] + rarer[frequent] + eps
        sub_tree = ((rarer[item], rare[item]), -frequency)

        # Replace with new tuple
        counter.subtract(dict((rare, rarer, sub_tree)))
        counter = +counter
        
    tree = (next(iter(counter)))
    if len(counter):
        return tree


def build_codebook(huff_tree):
    """ buils a codebook for the compression
    Return
    a dictionary from the chars
    to tuples of representation - (char:(length in bits, number)}
    
    Arg
    huff_tree - a tuple representing the tree formation of
    the chars, result of the make_huffman_tree function
    >>> build_codebook(make_huffman_tree(symbol_count("dgfbd")))
    {'f': (2, 1), 'g': (2, 2), 'd': (2, 3), 'b': (2, 0)}
    >>> build_codebook(make_huffman_tree(symbol_count("dgfbdhhhh")))
    {'f': (3, 3), 'g': (3, 5), 'd': (3, 7), 'b': (3, 1), 'h': (1, 0)}
    >>> build_codebook(make_huffman_tree(symbol_count("dgfbdhhh")))
    {'f': (2, 0), 'g': (3, 5), 'd': (2, 2), 'b': (3, 1), 'h': (2, 3)}
    """

    if huff_tree is not None and type(huff_tree) is not tuple:
        return {huff_tree: (1, 0)}
    return rec_build_codebook(huff_tree)


def rec_build_codebook(huff_tree, bits=""):
    """
    builds the codebook recursivle
    Returns
    codebook
    Args
    bits - bits to start with
    huff_tree - a tuple representing the tree formation of
    the chars, result of the make_huffman_tree function
    """
    codebook = dict()
    if type(huff_tree) is tuple:
        codebook.update(rec_build_codebook(huff_tree[LEFT],
                                           bits + str(LEFT)))
        codebook.update(rec_build_codebook(huff_tree[RIGHT],
                                           bits + str(RIGHT)))
    elif huff_tree is not None:
        codebook[huff_tree] = (len(bits),
                               (sum(int(bits[-place-1]) * 2**place
                                    for place in range(len(bits)))))

    return codebook


def build_canonical_codebook(codebook):
    """builds a canonical codebook
    Returns
    a canonical codebook
    Args
    codebook - a dictionary like the one given by build_codebook()
    """
    if not codebook:
        return {}
    canonical = ([(key, codebook[key][LENGTH]) for key in sorted(
        codebook, key=lambda key: (codebook[key][LENGTH], key))])
    return tuples_to_code(canonical)


def tuples_to_code(canonical):
    """creates a codebook out of ordered tuples
    of keys and lengths
    """
    if not canonical:
        return {}
    
    # transform to a new dict
    canon = dict()
    
    # code is increamented in one each time
    # so in order to start from the begginning (0)
    # you need the first counting to be -1
    code = -1
    key = LENGTH  # when switching key should be in the normal length place
    new_length = ORIGIN  # the length should be in the key place
    last_len = canonical[0][new_length]
    for char in canonical:
        code += 1
        code = 2**(char[new_length] - last_len) * code
        canon[char[key]] = (char[new_length], code)   
        last_len = char[new_length]       
    return canon


def build_decodebook(codebook):
    """creates a decode book
    Return
    dictionary that maps bits to the correct chars
    Args
    codebook - an output of build_codebook
    >>> build_decodebook({25: (1, 0)})
    {(1, 0): 25}
    """
    return dict([(value, key) for key, value in codebook.items()]) 


def compress(corpus, codebook):
    """compresses a file
    Yields
    bits of the compressed string in int
    Args
    corpus - iterable containing chars
    codebook - a result of build_codebook() function
    """
    num = 1 
    for char in corpus:
        code = codebook[char]
        bits = bin(code[num])[2:].zfill(code[LENGTH])
        for bit in bits:
            yield int(bit)


def decompress(bits, decodebook):
    """decompresses a file
    Yields
    letters of the decompressed file
    Args
    bits - an iterator with bits in ints,
    representing a compressed file
    decodebook - a result of build_decodebook() function
    """
    check = 0
    bits_num = 0
    for bit in bits:
        check = check*2 + bit
        bits_num += 1
        if (bits_num, check) in decodebook:
            yield decodebook[(bits_num, check)]
            check = 0
            bits_num = 0


def pad(bits):
    """adds 1 to the end and zeros
    until it is in bytes

    Yield
    bytes - 0 - 255 ints.
    the last one ends with 1 and then zeroes
    Args
    bits - an iterator with bits
    >>> list(pad([0,0,0,0,0,1,1,0]))
    [6, 128]
    >>> list(pad([0,0,0,0,0,0,1,0]))
    [2, 128]
    >>> list(pad([0,0,0,0,0,0,1]))
    [3]
    """
    byte = 0
    counter = 7  # the last bit in the byte
    for bit in bits:
        byte += 2**counter * bit
        if counter == 0:
            yield byte
            byte = 0
            counter = 8  # number of bits in byte
        counter -= 1
    byte += 2**counter * 1  # if it was exact it will still send a full byte
    yield byte


def unpad(byteseq):
    """ reverse the pad() function

    Yields
    bits - 0 or 1 without the 1 and 0s in the end
    Args
    byteseq - iterator of bytes
    >>> list(unpad(pad([0,0,0,0,0,1,1,0])))
    [0, 0, 0, 0, 0, 1, 1, 0]
    >>> list(unpad(pad([0,0,0,0,0,1,1])))
    ['0', '0', '0', '0', '0', '1', '1']
    >>>
    """
    # return all the bits
    bits = None
    for byte in byteseq:
        if bits is not None:        
            for bit in bits:
                yield int(bit)
                
        # Turn it into a byte (8 bits) and delete
        # the addition of bin()
        bits = bin(byte)[2:].zfill(8)
        
    # return the last bits without the addition
    # find where the sequence of 0 ends (LEFT to right)
    r_index = 1
    while r_index != 8 and bits[-r_index] != "1":
        r_index += 1

    # yield the remaining bits without the sequence
    for bit in bits[:-r_index]:
        yield int(bit)


def join(data, codebook):
    """yields bytes of canonical codebook + coded data

    Yields
    bytes of canonical codebook and then coded data
    Args
    codebook - a canonical codebook a result of
    the function build_canonical_codebook()
    data - a string
    >>> list(join("gggdfddf",build_codebook(
    make_huffman_tree(symbol_count("gggdfddf")))))
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g', 'g', 'g', 'd', 'f',
    'd', 'd', 'f']
    """
    for index in range(256):
        if index in codebook:
            yield codebook[index][LENGTH]
        else:
            yield 0
    for byte in data:
        yield byte


def split(byteseq):
    """splits join results into a tuple

    returns
    a tuple (codebook, data) where codebook is
    a general expression for a codebook,
    and data is an iterator on bytes.
    Args
    byteseq - the output of join
    """
    byteseq = list(byteseq)
    codebook = [(key, byte) for key,
                byte in enumerate(byteseq[:256]) if byte > 0]
    codebook = sorted(codebook,
                      key=lambda key: (key[ORIGIN], key[LENGTH]))
    data = byteseq[256:]
    return ((byte for byte in data), tuples_to_code(codebook))


def padington(reapeats=10, length=10000, input=False):
    """
    compares pad and unpad
    """
    import random
    for i in range(reapeats):
        x = list()
        for k in range(random.randint(1, length)):
            x.append(random.randint(0, 1))
        if input:
            print(x)
        print(x == list(unpad(pad(x))))
