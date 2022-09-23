#Lab
#Name:

# Phase 1
print('Hello Welcome to PyMat Delicacies')
day=input("Enter the day of the Week:")
day1=day.upper()
# print("TODAY'S SPECIAL :3 Tacos and Tequila")
# x1=13.45
# print('$',x1)
# quantity=int(input('How many Special do you want ?'))
# total_price=x1*quantity+(0.05*x1)+3
# print('Your Total order is $',total_price,'Thanks you for visting PyMat Delicacies')
# # print('You get a FREE Tequila....Buenos')

# phase 2
if(day1=='SUNDAY'):
    print("TODAY'S SPECIAL :3 Tacos and Tequila")
    x1=13.45
    print('$',x1)
    quantity=int(input('How many Special do you want ?'))
    total_price=x1*quantity+(0.05*quantity)+3
    print('Your Total order is $',total_price,'Thanks you for visting PyMat Delicacies')
    
elif(day1=='MONDAY'):
    print("TODAY'S SPECIAL :Pizaa and Coffee")
    x2=25.45
    print('$',x2)
    quantity1=float(input('How many Special do you want ?'))
    total_price1=x2*quantity1+(0.05*quantity1)+3
    print('Your Total order is $',total_price1,'Thanks you for visting PyMat Delicacies')
    if(total_price1>=12.99):
        print('You get a FREE Tequila....Buenos')
elif(day1=='TUESDAY'):
    print("TODAY'S SPECIAL :Chinesse and Juice")
    x3=55.45
    print('$',x3)
    quantity2=float(input('How many Special do you want ?'))
    total_price2=x3*quantity2+(0.05*quantity2)+3
    print('Your Total order is $',total_price2,'Thanks you for visting PyMat Delicacies')
    if(total_price2 >=12.99):
        print('You get a FREE Tequila....Buenos')
elif(day1=='WEDNESDAY'):
    print("TODAY'S SPECIAL :Indian and Juice")
    x4=75.45
    print('$',x4)
    quantity3=float(input('How many Special do you want ?'))
    total_price3=x4*quantity3+(0.05*quantity3)+3
    print('Your Total order is $',total_price3,'Thanks you for visting PyMat Delicacies')
    if(total_price3 >=12.99):
        print('You get a FREE Tequila....Buenos')
elif(day1=='THURSDAY'):
     print("TODAY'S SPECIAL :Indian and Mohito")
     x5=95.45
     print('$',x5)
     quantity4=float(input('How many Special do you want ?'))
     total_price4=x5*quantity4+(0.05*quantity4)+3
     print('Your Total order is $',total_price4,'Thanks you for visting PyMat Delicacies')
     if(total_price4 >=12.99):
        print('You get a FREE Tequila....Buenos')
elif(day1=='FRIDAY'):
     print("TODAY'S SPECIAL :Spagheti and Cocktail")
     x6=15.45
     print('$',x6)
     quantity5=float(input('How many Special do you want ?'))
     total_price5=x5*quantity5+(0.05*quantity5)+3
     print('Your Total order is $',total_price5,'Thanks you for visting PyMat Delicacies')
    
     

else:
     print("TODAY'S SPECIAL :Korean and Mohito")
     x7=5.45
     print('$',x7)
     quantity6=float(input('How many Special do you want ?'))
     total_price6=x7*quantity6+(0.05*quantity6)+3
     print('Your Total order is $',total_price6,'Thanks you for visting PyMat Delicacies')
     







