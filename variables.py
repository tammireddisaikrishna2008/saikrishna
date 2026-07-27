#Name: T.Sai krishna
#Lab:03
#Task:01
#Program:Variables and Data Types
name=" Sai krishna" 
age=18
height=5.3
is_student=True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
#Name: T.Sai krishna
#Lab:03
#Task:02
#Program:Multiple variable assignment
a,b,c=10,20,30
print("a =",a)
print("b =",b)
print("c =",c)
p=q=r=100
print("p =",p)
print("q =",q)
print("r =",r)
#Name: T.Sai krishna
#Lab:03
#Task:03
#Program:Swapping of two variables
#using temp variable
a=input("Enter 'a'value:")
b=input("Enter 'b' value:")
temp=a
a=b
b=temp
print("After swapping")
print("a =",a)
print("b =",b)
#Swapping by tuple unpacking
a=input("Enter 'a'value:")
b=input("Enter 'b' value:")
a,b=b,a
print("After swapping by tuple unpacking i.e a,b=b,a")
print("a =",a)
print("b =",b)
#Name: T.Sai krishna
#Lab:03
#Task:challenge
#Program:Calaculatng the area and circumfernce of a circle
radius=float(input("Enter the radius\n"))
area=(3.14*radius*radius)
circumference=(2*3.14*radius)
print("Area of circle is",area)
print("Circumference of circle is",circumference)
