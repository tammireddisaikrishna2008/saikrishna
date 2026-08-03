#Name: T.Sai krishna
#Program:Full Name Operations
#Task:A2.1-Strings
first_name=input("Enter your first name\n")
last_name=input("Enter your last name\n")
full_name=first_name+" "+last_name
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
len=len(full_name)
print("Length of your name is:",len)
print("First charcter of your name is :",full_name[0])
print("Last charcter of your name is :",full_name[len-1])
#output
#Enter your first name
#sai krishna
#Enter your last name


#sai krishna
#sai krishna
#Length of your name is: 28
#First charcter of your name is : S
#Last charcter of your name is : a


#Name:t.Sai krishna
#Program:First Name Extraction
#Task:A2.2-String Slicing
full_name=input("Enter your full name\n")
print("Your First name is :",full_name[:full_name.rindex(" ")])
#output
#Enter your full name
#sai krishna
#Your First name is : Sai krishna