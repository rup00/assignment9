x=int(input("enter how many multipul you want"))
n=int(input("enter the n number which multipuls u want"))
ch=x*x
count=1
i=1
while i<=ch:
    if count<=x:
        if(i%n==0):
            print(i)
            count+=1
            i+=1
        else:
            i+=1
    
