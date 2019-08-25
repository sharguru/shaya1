def cc(s):
    if s!=s.lower() and s!=s.upper() and "_" not in s:
        print("yes")
    else:
        print("no")
cc(str(input()))
