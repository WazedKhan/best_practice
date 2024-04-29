from collections import defaultdict
from typing import List


def singleNumber(nums: List[int]):
    # create a empty dict with default dict
    counts = defaultdict(int)
    # count appears of every items in the list
    for num in nums:
        counts[num] += 1

    # check if any item appeared once
    for key, value in counts.items():
        if value == 1:
            return key
