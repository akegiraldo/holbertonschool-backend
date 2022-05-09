#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page: int, page_size: int):
    """
    Function should return a tuple of size
    two containing a start index and an end
    index corresponding to the range of
    indexes to return in a list for those
    particular pagination parameters
    """
    page = page - 1
    min_idx = 0 if page == 0 else page * page_size
    max_idx = min_idx + page_size
    return (min_idx, max_idx)
