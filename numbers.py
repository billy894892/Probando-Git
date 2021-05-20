def printNumbers(n):
    i=1
    for i in range(1,n+1):
        print(i)
    return
def sumNumbers(n):
    i=1;sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

print("Program to print n numbers")
printNumbers(int(input("Enter a number: ")))
num = 1
while num > 0:
    num = int(input("Enter number to calculate: "))
    print(sumNumbers(num))
print("End..")