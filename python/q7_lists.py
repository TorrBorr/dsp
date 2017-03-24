# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count=0
    for word in words:
        if len(word)>1:
            if word[0] == word[(len(word)-1)]:  
                count = count+1
            else:
                pass
        else:
            pass
          
    
    return count

    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    raise NotImplementedError


def front_x(words):
    print words
    
    x_words = []
    other_words = []
    
    for word in words:
        if word.startswith('x'):
            x_words.append(word)
        else:
            other_words.append(word)
    x_words.sort()
    other_words.sort()
    
    new_list=x_words+other_words
    
    return new_list
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    raise NotImplementedError


def sort_last(tuples):
    
    def getKey(pair):
        return pair[-1]
          
    return sorted(tuples, key=getKey)
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    raise NotImplementedError


def remove_adjacent(nums):
    if len(nums)>0:
        new_list = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                new_list.append(nums[i])
            else: 
                pass
    else:
        new_list = []
    #if nums[-1] == nums[-2]:
        #pass
    #else:
        #new_list.append(nums[-1])
    return new_list

    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    raise NotImplementedError


def linear_merge(list1, list2):
    new_list = []
    list1_counter = 0
    list2_counter = 0
    
    while list1_counter<len(list1) and list2_counter<len(list2):
        if list1[list1_counter]<list2[list2_counter]:
            new_list.append(list1[list1_counter])
            list1_counter=list1_counter+1
        else:
            new_list.append(list2[list2_counter])
            list2_counter=list2_counter+1
    
    if list1_counter<len(list1):
        for counter in range(list1_counter,len(list1)):
            new_list.append(list1[counter])
    else:
        for counter in range(list2_counter,len(list2)):
            new_list.append(list2[counter])
            
    return new_list

    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    raise NotImplementedError
