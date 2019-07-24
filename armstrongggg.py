n=input()
n=n.split()
n=list(map(int,n))
for a in range(n[0],(n[1])+1):
  temp=a
  sum=0
  while (temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
    if (sum==a):
      print(a)
    
