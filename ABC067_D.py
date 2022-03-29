from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="067"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc078_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  #オイラーツアー
  def EulerTour(G, s):
      depth=[-1]*len(G)
      depth[s]=0
      done = [0]*len(G)
      Q = [~s, s] # 根をスタックに追加
      parent=[-1]*len(G)
      ET = []
      left,right=[-1]*len(G),[-1]*len(G)
      while Q:
          i = Q.pop()
          if i >= 0: # 行きがけの処理
              done[i] = 1
              ET.append(i)
              for a in G[i][::-1]:
                  if done[a]: continue
                  depth[a]=depth[i]+1
                  parent[a]=i
                  Q.append(~a) # 帰りがけの処理をスタックに追加
                  Q.append(a) # 行きがけの処理をスタックに追加
          else: # 帰りがけの処理
              ET.append(i)
      for i in range(len(G)*2):
        if ET[i]>=0 and left[ET[i]]==-1: left[ET[i]]=i
        if ET[~i]<0 and right[~ET[~i]]==-1: right[~ET[~i]]=len(G)*2-i-1
      return ET, left, right, depth, parent
  N=int(input())
  G=[[] for _ in range(N)]
  for i in range(N-1):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].append(b)
    G[b].append(a)
  ET, left, right, depth, parent=EulerTour(G,0)
  if depth[N-1]%2==0:
    p=N-1
    for i in range(depth[N-1]//2-1):
      p=parent[p]
  else:
    p=N-1
    for i in range(depth[N-1]//2):
      p=parent[p]
  if N-(right[p]-left[p])//2-1>(right[p]-left[p])//2+1: print('Fennec')
  else: print('Snuke')
  """ここから上にコードを記述"""

  print(test_case[__+1])