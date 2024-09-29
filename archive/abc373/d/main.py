import numpy as np
import math 
import sys
from functools import lru_cache
import itertools
class Graph:
    
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.G = [[] for _ in range(self.nodes)]
        
    def add_edge(self, node1: int, node2: int, weight: int) -> None:
        
        self.G[node1].append([node2,w])
        self.G[node2].append([node1,-w])
        
    # 深さ優先探索
    def dfs(self, start: int, nodes: list) -> list:

        stack = [start]

        while stack:
            current_node = stack.pop()

            for next_node, weight in self.G[current_node]:
                if nodes[next_node] == '':
                    stack.append(next_node)
                    nodes[next_node] = nodes[current_node] + weight
                    
                elif nodes[next_node] == nodes[current_node]+weight:
                    pass
                
                else:
                    nodes[current_node] = nodes[next_node] - weight
                    self.dfs(current_node,nodes)

        return nodes
    
    # 木の直径
    def diameter(self) -> int:
        
        tmp = max(enumerate(self.dfs(0)),key=lambda x: x[1])[0]
        
        return max(self.dfs(tmp))
    
    

# n = int(input())
n,m = map(int,input().split())
# A = list(map(int,input().split()))

Graph = Graph(n)

for i in range(m):
    u,v,w = map(int,input().split())
    if v<u:
        u,v = v,u
        w = -w
    Graph.add_edge(u-1,v-1,w)
    
nodes = [''] * n

for i in range(n):
    if nodes[i] == "":
        nodes[i] = 0
    Graph.dfs(i,nodes)
    
print(*nodes)