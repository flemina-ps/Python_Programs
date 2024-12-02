
# Function to get sum of digits of a number
def getSum(n): 
   
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
  
n = int(input("Enter the number: "))
print("Sum of digits of the number",n,"is",getSum(n))