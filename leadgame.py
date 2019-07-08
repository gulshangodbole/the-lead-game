
c=input("enter rounds")
e=[]
f=[]
s=[]
h=[]
for i in range(1,c+1):
    a=input("enter scores of player 1")
    e.append(a)
    
for i in range(1,c+1):
    d=input("enter scores of player 2")
    f.append(d)

print e
print f

for i in range(1,c+1):
    if(e[i]>f[i]):
      g=e[i]-f[i]
      s.append(g)

      print  max(s)
      print "player 1 wons"
      break
    else:
      k=f[i]-e[i]
      h.append(k)
      print  max(h)
      print "player 2 wons"
      break

    
