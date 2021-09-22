"""
Given 2 arrays, create a function that let's a user know (true/false)
whether these two arrays contain any common items
For Example:
const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
should return false.
-----------
Const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
should return true.

2 parameters - arrays - no size limit
return true or false
"""


def common_items1(array1, array2):
    """
    Finding if any items in each array have similar inputs
    :param array1:
    :param array2:
    :return: True or False
    """

    # Create Dictionary of array1 -
    # Time Complexity O(n)
    # Space Complexity O(n)
    dict1 = {}
    for item in array1:
        if item in dict1:
            updated_value = dict1[item]
            updated_value += 1
            dict1[item] = updated_value
        else:
            dict1[item] = 1

    # Compare every element of n to dict
    # Time Complexity O(m)
    for item in array2:
        if item in dict1:
            return True

    # Overall Time Complexity  O(n + m)
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array1 = ['a', 'b', 'c', 'x']
    array2 = ['z', 'y', 'a']
    array3 = ['z', 'y', 'i']
    print(common_items1(array1, array2))  # return True
    print(common_items1(array1, array3))  # return False
