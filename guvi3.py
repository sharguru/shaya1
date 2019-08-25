s=str(input())
ss=str(input())
if len(s)<len(ss):
  print(ss.find(s,0,-1)+1)
elif len(s)>len(ss):
  print(s.find(ss,0,-1)+1)
