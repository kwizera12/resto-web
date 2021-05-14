a=[][]
val=1
for i in range(1):
 for j in range(2):
   a[i][j]=val
   val=val+1
for j in range(2):
 for i in range(1):
   print(a[i][j])
