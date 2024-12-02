#digit along with place value in words
number={0:'zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
pos_num={0:'Ones',1:'Tens',2:'Hundreds',3:'Thousands',4:'Ten Thousand',5:'Lakhs'}
n=input("Enter the number : ")
res=''
l=len(n)-1
for i in n:
    key=int(i)
    value=number[key]
    res=res+' '+value+' '+pos_num[l]
    l-=1
print("The number is ",n)
print("The place value is",res)