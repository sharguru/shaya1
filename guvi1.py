na,ka=map(int,input().split())
ll=list(map(int,input().split()))
for i in range(0,na):
    if ll[i]==ka:
        print("yes "+str(ll.count(ka)))
        break
    else:
        print("no")
        break
