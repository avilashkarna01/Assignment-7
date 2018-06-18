#Question-1
def area():
    r=int(input("enter a radius: "))
    area=(22/7)*r*r
    print(area)
area()
print("\n")

#Question-2
p=[]
def perfect():
    for x in range (1,1000):
        l=[]
        s=0
        for y in range(1,x):
            if x%y==0:
                l.append(y)
        for a in l:
            s=s+a
        if s==x:
            p.append(x)
perfect()
print(p)
print("\n")


#Question-3
def table(n):
    if n>10:
        return
    else:
        print(12*n)
        table(n+1)
table(1)
print("\n")

#Question-4
def power (b,p):
	s=1
	if p==1:
		return b
	else:
		s=b*power(b,p-1)
		return s
print(power(4,7))	
print("\n")	



#Question-5
def fact (x):
    if x==1:
        return 1
    else:
        x=x*fact(x-1)
        return x
a=int(input("enter any number:"))
f=fact(a)
print(f)
d={}
d[a]=f
print(d)