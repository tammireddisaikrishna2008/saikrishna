#25341a05k3 sai krishna
n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print(n*"* ")
    else:
        print("*"+" "*(n+2)+"*")

''' output
* * * * * 
*       *
*       *
*       *
* * * * * 
'''