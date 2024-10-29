n=int(input("Enter a Number:"))
#Initialization
a=0
b=1
for i in range(0,n+1,1):
    print(a, " ")
    a,b=b,a+b



#f(0)=0   a
#f(1)=1   b
#F(n) = F(n-1) + F(n-2)
#f(2)=1
#f(3)=1+1=2
#f(4)=1+2=3
