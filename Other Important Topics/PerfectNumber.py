num=int(input("Enter the number:"))
sum2=0
for x in range(1,num):
  if(num%x==0):
    sum2+=x
if(sum2==num):
  print("It is a perfect number")
else:
  print("It is not a perfect number")
