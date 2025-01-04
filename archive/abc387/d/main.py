import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect


if __name__ == "__main__":
    ...
    # n = int(input())
    h,w = map(int,input().split())
    # A = list(map(int,input().split()))
    
    S = []
    for i in range(h):
        
        tmp =list(str(input()))
        S.append(tmp)

        if "S" in tmp:
            s_index = (i,tmp.index("S"))
        if "G" in tmp:
            g_index = (i,tmp.index("G"))
    
    M = np.full((h,w,2), [float('inf')]).tolist()
    
    M[s_index[0]][s_index[1]] = [0, "*"]
    
    while(M[g_index[0]][g_index[1]][0] == float('inf')):
        flag = False
        for i in range(h):
            for j in range(w):
                if M[i][j][0] >= 0:
                    if i-1 >= 0 and S[i-1][j][0] != "#" and M[i][j][1] != "-":
                        if M[i-1][j][0] > M[i][j][0]+1:
                            M[i-1][j] = [M[i][j][0]+1, "-"]
                            flag = True

                    if i+1 < h and S[i+1][j][0] != "#" and M[i][j][1] != "-":
                        if M[i+1][j][0] > M[i][j][0]+1:
                            M[i+1][j] = [M[i][j][0]+1, "-"]
                            flag = True

                    if j-1 >= 0 and S[i][j-1][0] != "#" and M[i][j][1] != "|":
                        if M[i][j-1][0] > M[i][j][0]+1:
                            M[i][j-1] = [M[i][j][0]+1, "|"]
                            flag = True

                    if j+1 < w and S[i][j+1][0] != "#" and M[i][j][1] != "|":
                        if M[i][j+1][0] > M[i][j][0]+1:
                            M[i][j+1] = [M[i][j][0]+1, "|"]
                            flag = True
        if not flag:
            print(-1)
            sys.exit()

        
    print(M[g_index[0]][g_index[1]][0])