def f(sum):
    for a in range(1,sum):
        for b in range(a,sum-a):
            c = sum-a-b
            if a**2+b**2==c**2:
                return a,b,c

sum=1000
p=1
t=f(sum)
if t:
    a,b,c=t
    p=a*b*c
    print("The numbers are:",a,',',b,',',c,)
else:
    print("Numbers not found")
