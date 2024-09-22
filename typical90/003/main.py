import numpy as np
import math 
import sys
from functools import lru_cache
import itertools

class Graph:
    
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.G = [[] for _ in range(self.nodes)]
        
    def add_edge(self, node1: int, node2: int) -> None:
        
        self.G[node1].append(node2)
        self.G[node2].append(node1)
        
    # 深さ優先探索
    def dfs(self, start: int = 0) -> list:

        dist = [-1] * self.nodes
        dist[start] = 0

        stack = [start]

        while stack:
            current_node = stack.pop()

            for next_node in self.G[current_node]:
                if dist[next_node] == -1:
                    stack.append(next_node)
                    dist[next_node] = dist[current_node] + 1

        return dist
    
    # 木の直径
    def diameter(self) -> int:
        
        tmp = max(enumerate(self.dfs(0)),key=lambda x: x[1])[0]
        
        return max(self.dfs(tmp))


n = int(input())

Graph = Graph(n)

for _ in range(n-1):
    a, b = map(int,input().split())
    a-=1
    b-=1
    Graph.add_edge(a,b)
    
print(Graph.diameter()+1)