import numpy as np
import math 
import sys

x1_min, y1_min, z1_min, x1_max, y1_max, z1_max = map(int,input().split())
x2_min, y2_min, z2_min, x2_max, y2_max, z2_max = map(int,input().split())

x_min = max(x1_min, x2_min)
y_min = max(y1_min, y2_min)
z_min = max(z1_min, z2_min)
x_max = min(x1_max, x2_max)
y_max = min(y1_max, y2_max)
z_max = min(z1_max, z2_max)


x_length = x_max - x_min
y_length = y_max - y_min
z_length = z_max - z_min

# 共通部分の体積を計算（各辺の長さが正の場合）
if x_length > 0 and y_length > 0 and z_length > 0:
    print('Yes')
else:
    print('No')
        
        