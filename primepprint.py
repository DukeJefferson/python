N=int(input())
m=int(input())
for x in range(N,m+1):
  for a in range(2,x):
    if(x%a!=0 and x%x==0):
      b[a]=x
print(*b)    
     
