s=str(input())
ss=str(input())
if len(s)<len(ss):
  print(ss.find(s)+1)
elif len(s)>len(ss):
  print(s.find(ss)+1)
else:
  print("no")
