'''
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
'''
acre=42460
width=float(input("Enter the weidth of field"))
length=float(input(" enter the length of field"))
area=width*length
sfeet=area/10.764 # this will turn the area into square feet
print(" area of field :",sfeet*acre,"acre")
