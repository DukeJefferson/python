n=int(input())
m=int(input())
for a in range(n,m+1):
  temp=a
  sum=0
  while (temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
    if (sum==a):
      print(a)
    
