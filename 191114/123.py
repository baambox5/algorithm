import sys;sys.stdin = open('arrest_escaped.txt', 'r')
from collections import deque
from pprint import pprint

def move(r, c, t):
   global cnt
   if time == t: return
   q.append((r, c))
   visit[r][c] = True
   while q:
       # t += 1
       rr, cc = q.popleft()
       for dir in Move[Map[rr][cc]]:
           xr, xc = rr+dir[0], cc+dir[1]
           a, b = dir

           # c, d = Move[Map[xr][xc]][0], Move[Map[xr][xc]][1]
           if 0 <= xr < N and 0 <= xc < M:
               if Map[xr][xc] == 0: continue
               if not visit[xr][xc] and (-1 * a, -1 * b) in Move[Map[xr][xc]]:
                   # q.append((xr, xc))
                   cnt += 1
                   visit[xr][xc] = True
                   move(xr, xc, t+1)
for tc in range(2, int(input())+1):
   N, M, M_R, M_C, time = map(int, input().split())
   Map = [list(map(int, input().split())) for _ in range(N)]
   Move = {
       1: [(1, 0), (-1, 0), (0, 1), (0, -1)],
       2: [(-1, 0), (1, 0)],
       3: [(0, -1), (0, 1)],
       4: [(-1, 0), (0, 1)],
       5: [(1, 0), (0, 1)],
       6: [(1, 0), (0, -1)],
       7: [(-1, 0), (0, -1)]
   }
   q = deque()
   visit = [[False] * M for _ in range(N)]
   cnt = 1
   move(M_R, M_C, 1)
   # pprint(visit)
   print('#{} {}'.format(tc, cnt))