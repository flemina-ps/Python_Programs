#Spy Number
n=int(input("Enter the number : "))
sum=0
pro=0
while n>0:
  d=n%10
  sum+=d
  pro*=d
  n//=1
  if n==0:
    n=pro
    pro=1
if sum==pro:
  print(n,"is a spy number")
else:
  print(n,"is not a spy number")