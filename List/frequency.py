#Find the frequency of each element in a list
a=[]
a1=int(input("Enter the max count of elements in list : "))
for i in range(0,a1):
    a2=input(f"Enter the number {i+1} in list_1 : ")
    a.append(a2)
print("List : ",a)
fr = [None] * len(a);  
visited = -1;  
   
for i in range(0, len(a)):  
    count = 1;  
    for j in range(i+1, len(a)):  
        if(a[i] == a[j]):  
            count = count + 1;  
            #To avoid counting same element again  
            fr[j] = visited;  
              
    if(fr[i] != visited):  
        fr[i] = count;  
   
#Displays the frequency of each element present in array  

print(" Element | Frequency");  
 
for i in range(0, len(fr)):  
    if(fr[i] != visited):  
        print("    " + str(a[i]) + "    |    " + str(fr[i]));  

