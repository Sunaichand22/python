num=int(input())
count=0
for fact in range(2,int((num/2))+1,1):
    if(num%fact==0):
        count=count+1
if(count!=0):
    print("yes")
else:
    print("no")
