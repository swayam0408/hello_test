#factorial of a given number
def factorial(n):
if n<0;
return 0
elif n == 0 or n ==1;
return 1
else:
fact = 1
fact*=n
n-=n
return fact

n=5
print("factorial")
