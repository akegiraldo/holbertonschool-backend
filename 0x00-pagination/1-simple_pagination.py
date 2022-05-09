#!/usr/bin/env python3
"""1. Simple pagination"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int):
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function that takes two integer arguments page
        with default value 1 and page_size with default
        value 10, and returns this rows of CSV
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0

        _ = self.dataset()

        min_idx, max_idx = self.index_range(page, page_size)
        if max_idx >= len(self.__dataset):
            return []

        return self.__dataset[min_idx:max_idx]
