#!/usr/bin/env python3
"""1. FIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Class that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """Method for initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Method that puts a key and value in cache"""
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                key = list(self.cache_data.keys())[0]
                del self.cache_data[key]
                print('DISCARD: {}'.format(key))

    def get(self, key):
        """Method that gets a value from cache by key given"""
        if key:
            return self.cache_data.get(key)
        return None
