#Name: T.Sai krishna
#Lab:02
#Task:03
#Program:Keywords as Variable names
for=5
True=10
#for=5
#   ^
#SyntaxError: invalid syntax
#True=10
#    ^
#SyntaxError: cannot assign to True
#Name: T.Sai krishna
#Lab:02
#Task:02
#Program:Python keyword checker
import keyword
print(keyword.iskeyword("if"))
print(keyword.iskeyword("False"))
print(keyword.iskeyword("async"))
print(keyword.iskeyword("name"))
print(keyword.iskeyword("student"))
print(keyword.iskeyword("def"))
#Name: T.Sai krishna
#Lab:02
#Task:01
#Program:Python keywords list
import keyword
print(keyword.kwlist)
print("Total number of keywords:",len(keyword.kwlist))
print("Soft keywors:",keyword.softkwlist)
print("Total no of Soft Keywords:",len(keyword.softkwlist))
#Name: T.Sai krishna
#Lab:02
#Task:Challenge
#Program:printing soft keywords
import keyword
print(keyword.softkwlist)
print(len(keyword.softkwlist))
