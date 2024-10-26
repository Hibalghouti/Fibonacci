# number of Fibonacci numbers to generate
n = int(input("Enter the number: "))

# Initialization
a, b = 0, 1

for i in range(n):
    print(a, " ")
    a, b = b, a + b  # Update to the next Fibonacci numbers


#f(0)=0   a
#f(1)=1   b
#F(n) = F(n-1) + F(n-2)
#f(2)=1
#f(3)=1+1=2
#f(4)=1+2=3