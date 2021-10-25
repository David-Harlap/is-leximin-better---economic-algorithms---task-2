from doctest import testmod


def is_leximin_better(x: list, y: list) -> bool:
    """

    :param x: list that should be better then y
    :param y: basic list.
    :return: True if x is better leximin-order than y, False if not.

    >>> is_leximin_better([1],[1,1,1])    # not the same len. should e false
    False
    >>> is_leximin_better([1,1,1],[1,1,1])    # the same list should be false
    False
    >>> is_leximin_better([1,2,3],[3,2,1])    # diff order but still same lists.
    False

    >>> is_leximin_better([50,100],[50,50]) # from class
    True
    >>> is_leximin_better([3,1,3],[2,99,1]) #from class
    True

    >>> is_leximin_better([1],[4])
    False
    >>> is_leximin_better([4],[1])
    True

    >>> is_leximin_better([2,2,8,5],[5,1,8,2]) # first num diff
    True
    >>> is_leximin_better([1,5,8,7],[7,1,5,9]) # last num diff len = 4
    False
    >>> is_leximin_better([2,1,8,4],[1,2,3,8]) # 3nd diff
    True


    >>> is_leximin_better([2,2,2,2],[1,100,45,2])
    True
    >>> is_leximin_better([1,2,3,4],[5,6,7,8])
    False
    >>> is_leximin_better([1,1.1,1.2,1.3],[1,1,1,1]) # not integer
    True
    >>> is_leximin_better([2,1.2,5,7,10,2.5],[7,8,1.2,7,2,55])
    False

    """

    if len(x) != len(y):
        return False
    x.sort()
    y.sort()
    if x > y:
        return True
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testmod(name='is_leximin_better', verbose=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
