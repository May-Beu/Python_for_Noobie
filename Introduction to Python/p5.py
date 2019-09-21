'''
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign 
'''
less_deposite=0.10
more_deposite=0.25
less=float(input('Enter the no. of one liter container or less than one liter :'))
more=float(input('Enter the no.of more than one liter of container :'))
refund=less*less_deposite + more* more_deposite
print("Thank you for being aware for nature \n"," your total refund is :$", refund)

#"the following line  is not a part of question"
# in case if a person have only cointainer which is less than one liter or one liter
#less_refund= less*less_deposite
#print("your refund for container less than one liter or one liter $",less_refund)
 #in case if a person have only cointainer which is more than one liter
#more_refund=more*more_deposite
#print("your refund for container more than one liter $",more_refund)