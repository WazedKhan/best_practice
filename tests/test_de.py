import sys

sys.path.append(r"D:\Python\python-best-practice")


from ..code.deafault_dict.find_unique_item import singleNumber


def test_find_unique_item_of_list():
    arr = [1, 2, 2, 5, 5, 5, 6, 6, 6, 6]
    print(singleNumber(arr) == 1)
