import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq

class Node(object):
    def __init__(self, data, next_node = None):
        self.data = data # データ
        self.next = next_node # 次のNodeを指す参照変数(ポインタ)

class LinkedList(object):
    def __init__(self, head = None) -> None:
        self.head = head # インスタンス化した時にNoneをいれておく。



if __name__ == "__main__":
    ...
    # n = int(input())
    # n,k = map(int,input().split())
    # A = list(map(int,input().split()))
    # S = list(str(input()))