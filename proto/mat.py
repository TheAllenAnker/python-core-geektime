# Author: Allen Anker
# Created by Allen Anker on 2019-09-23


class Matrix(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])
