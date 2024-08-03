
a = []
for i in range (12):
    n = int(input ("enter your salary"))
    a.append(n)
    
b=0  
for i in range(len(a)):
    b+=a[i]
print(b)