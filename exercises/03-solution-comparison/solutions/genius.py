#!/usr/bin/env python3
"""
Sudoku Solver - Genius Developer Style
Author: Claude (Anthropic) for teaching purposes
Note: This code is intentionally written in a hyper-optimized, cryptic style
      for educational comparison. It may not work perfectly.
"""

def s(g,i=0):
    if i==81:return True
    r,c=divmod(i,9)
    if g[r][c]:return s(g,i+1)
    b=(r//3)*3+(c//3)
    u=set(range(1,10))-{g[r][j]for j in range(9)}-{g[j][c]for j in range(9)}-{g[(b//3)*3+j//3][(b%3)*3+j%3]for j in range(9)}
    for n in u:
        g[r][c]=n
        if s(g,i+1):return True
    g[r][c]=0
    return False

def p(g):
    for i,r in enumerate(g):
        print(' '.join(str(c) if c else '.' for c in r[:3]),'|',' '.join(str(c) if c else '.' for c in r[3:6]),'|',' '.join(str(c) if c else '.' for c in r[6:]))
        if i in[2,5]:print('-'*21)

g=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
p(g)
print('\n'+'='*21+'\n')
s(g)
p(g)
