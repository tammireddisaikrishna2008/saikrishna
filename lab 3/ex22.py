#25341a05k3  sai krishna
n=4
a=n
for i in range(0,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(0,n+1):
    print(" "*i+"*"*(2*(n-i)-1))


''' output
   *
  ***
 *****
*******
*******
 *****
  ***
   *
'''