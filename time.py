# i have to Write a program for checking the validity of a time entered by the user as a set of 3 integers,hours [0,23],minutes [0,59],seconds[0,59]

# Lwazi Somtsewu
# 31 July 2024

h =input("Enter the hours: ")
h =int(h)
m =int(input("Enter the minutes: "))
s= int(input("Enter the seconds: "))

if (0<=h<=23)and (0<=m<=59) and (0<=s<=59):
    print("Your time is valid.")

else:
    print("Your time is invalid.")