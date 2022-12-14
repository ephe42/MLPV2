#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import numpy as np


class UsefulFunction:
    def __init__(self):
        pass

    def normalization(self, x):
        return (x - np.min(x)) / (np.max(x) - np.min(x))

    def vectorized_result(self, i, size):
        e = np.zeros((size, 1))
        e[int(i)] = 1.0
        return e

    def data_spliter(self, x, y, proportion):
        c = list(zip(x, y))
        np.random.shuffle(c)
        x, y = zip(*c)
        x_train, x_validation = np.split(x, [int(proportion * len(x))])
        y_train, y_validation = np.split(y, [int(proportion * len(y))])
        return (x_train, x_validation, y_train, y_validation)


class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start <= other <= self.end
