import numpy as np
import pandas as pd
import itertools
import math 
import sys
from functools import lru_cache
import bisect
import heapq
from collections import deque, defaultdict


def main():
    # N (整数)
    # n = int(input())
    
    # N K (整数)
    # n,k = map(int,input().split())
    
    # N M (整数)
    # n,m = map(int,input().split())
    
    # W H (整数)
    h,w = map(int,input().split())
    
    # A1 A2 A3 ... An (整数)
    # A = list(map(int,input().split()))
    
    # B1 B2 B3 ... Bn (整数)
    # B = list(map(int,input().split()))
    
    # S (文字列)
    # S = list(str(input()))
    
    # S1 S2 S3 ... Sn (文字列)
    S = []
    where_s = []
    for i in range(h):
        s = list(input())
        for j in range(w):
            if s[j] == 's':
                where_s.append([i,j])
        S.append(s)
        
    que = []
    
    for s in where_s:
        
        i = s[0]
        j = s[1]
        
        if i>0:
            if S[i-1][j] == 'n':
                que.append([[i-1,j],'u'])
        if i<h-1:
            if S[i+1][j] == 'n':
                que.append([[i+1,j],'d'])
        if j>0:
            if S[i][j-1] == 'n':
                que.append([[i,j-1],'l'])
        if j<w-1:
            if S[i][j+1] == 'n':
                que.append([[i,j+1],'r'])
        
        if i>0 and j>0:
            if S[i-1][j-1] == 'n':
                que.append([[i-1,j-1],'ul'])
        if i>0 and j<w-1:
            if S[i-1][j+1] == 'n':
                que.append([[i-1,j+1],'ur'])
        if i<h-1 and j>0:
            if S[i+1][j-1] == 'n':
                que.append([[i+1,j-1],'dl'])
        if i<h-1 and j<w-1:
            if S[i+1][j+1] == 'n':
                que.append([[i+1,j+1],'dr'])

    nuke = list('nuke')
    
    for q in que:
        i = q[0][0]
        j = q[0][1]
        direction = q[1]
        succes = True
        
        if direction == 'u':
            for k in range(4):
                ii = i-k
                jj = j
                if ii < 0:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
            
            if succes:
                for x in range(5):
                    print(i+1-x+1,j+1)
                return
            
        elif direction == 'd':
            for k in range(4):
                ii = i+k
                jj = j
                if ii >= h:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
            
            if succes:
                for x in range(5):
                    print(i-1+x+1,j+1)
                return
            
        elif direction == 'l':
            for k in range(4):
                ii = i
                jj = j-k
                if jj < 0:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
                
            if succes:
                for x in range(5):
                    print(i+1,j+1-x+1)
                return
            
        elif direction == 'r':
            for k in range(4):
                ii = i
                jj = j+k
                if jj >= w:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
                
            if succes:
                for x in range(5):
                    print(i+1,j-1+x+1)
                return
            
        elif direction == 'ul':
            for k in range(4):
                ii = i-k
                jj = j-k
                if ii <0 or jj <0:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
                
            if succes:
                for x in range(5):
                    print(i+1-x+1,j+1-x+1)
                return
            
        elif direction == 'ur':
            for k in range(4):
                ii = i-k
                jj = j+k
                if ii <0 or jj >=w:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
                
            if succes:
                for x in range(5):
                    print(i+1-x+1,j-1+x+1)
                return
            
        elif direction == 'dl':
            for k in range(4):
                ii = i+k
                jj = j-k
                if ii >=h or jj <0:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
                    
            if succes:
                for x in range(5):
                    print(i-1+x+1,j+1-x+1)
                return
            
        elif direction == 'dr':
            for k in range(4):
                ii = i+k
                jj = j+k
                if ii >=h or jj >=w:
                    succes = False
                    break
                if S[ii][jj] != nuke[k]:
                    succes = False
                    break
            
            if succes:
                for x in range(5):
                    print(i-1+x+1,j-1+x+1)
                return
    
    # A (二次元配列)
    # A = []
    # for _ in range(m):
    #     A.append(list(map(int,input().split())))
    ...
    
    
    

if __name__ == "__main__": 
    main()