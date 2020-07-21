n=int(input())
if(n%3==0 and n%5==0):
    print("zoom")
elif(n%3==0):
    print("zip")
elif(n%5==0):
    print("zap")
else:
    print("invalid")
