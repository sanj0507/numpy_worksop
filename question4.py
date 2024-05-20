#write a program to find the sum of digits of a given number'
n=int(input("Enter a number"))
sum=0
while(n>0):
    num=n%10
    sum+=num
    n=n//10
print(sum)

