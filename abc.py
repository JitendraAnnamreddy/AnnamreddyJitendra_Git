def isleap(n):
    if((n%400==0)or(n%4==0 and n%100!=0)):
        return True
    return False
n=int(input("enter the year"))
while(isleap(n)==False):
    n+=1
l=list(range(n,n+16,4))
print(l)
    
