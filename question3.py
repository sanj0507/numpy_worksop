#write a program to find the factorial of a nummber
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("ENter a number"))
fact=fact(n)
print(fact)
