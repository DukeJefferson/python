e=input()
a=0
if(e[0]=="I" and e[1]=="X"):
  a+=9
elif(e[0]=="X" or e[1]=="X"):
  a+=10
elif(e[0]=="V" or e[1]=="V"):
  a+=5
elif(e[0]=="I" or e[1]=="I"):
  a+=1
elif(e[0]=="L" or e[1]=="L"):
  a+=50
print(a)
