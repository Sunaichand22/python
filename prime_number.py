a=int(input("Enter greateer than 1"))
b=int(input())
for num in range(a,b):
    flag=0
    if(num>1):
        for fact in range(2,int(num/2)+1,1):
            if(num%fact==0):
                flag+=1
        if(flag==0):
            print(num)

    
 
