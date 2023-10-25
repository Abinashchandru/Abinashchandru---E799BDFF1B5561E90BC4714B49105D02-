# Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.
num=int(input("please Enter the Number you wish:")) 
if (num%4==0) :
  if(num%100==0):
    if (num%400==0):
      print("%d is a leap year"%num)
    else:
      print("%d is not"%num) 
  else:
     print("%d is a leap year"%num) 
else:
  print("%d is not"%num)