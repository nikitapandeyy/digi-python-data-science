'''total =0
while(input("enter")=="y"):
    num=int(input("enter number"))
    total +=num
print(f"total{total}")
'''
'''
total =0
while 1:
    num=input("enter a number")
    if( not num):
        break
    if(num.isnumeric):
        total+=int(num)
print(total)'''
even=0
odd =0
while True:
    num=input("enter a number")
    if not num:
        break
    if not num.isnumeric():
        continue
    num=int(num)
    if num%2==0:
        even+=num
    else:
        odd+=num

print(even)
print(odd)