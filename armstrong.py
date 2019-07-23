num=int(input())
sum=0
while num>0 :
  digit=num%10
  sum+=digit**3
if(sum==num):
  print('Yes')
else:
  print('No')
