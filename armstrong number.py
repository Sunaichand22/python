a=int(input("Enter start index"))
b=int(input("Enter last index"))
def cdigit(x):
    count=0
    while x!=0:
        x=x//10
        count+=1
    return count
        
for i in range(a,b):
    n=i
    sum=0
    c=cdigit(i)
    while(n!=0):
        rem = n % 10
        sum = sum + rem ** c
        n = n // 10
    if(i==sum):
        print(i)
    
    
