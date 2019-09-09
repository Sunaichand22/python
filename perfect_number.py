a=int(input())
b=int(input())
for num in range(a,b):
    sum1=0
    for fact in range(1,int((num/2))+1):
        if(num%fact==0):
            sum1=sum1+fact
    if(sum1==num):
        print(num)

