m,n=input().strip().split(" ")
m=int(m)
n=int(n)

#print(m,n)

l=[[int(i)for i in input().rstrip().split(' ')] for j in range(m)]          
#print (l)
def count(a):
    b=0
    while a!=0:
        b+=1
        a=a//10
    return b

def rev(a):
    p=0
    while a!=0:
        b=a%10
        p=p*10+b
        a=a//10
    return p 


def rlr(l,m,n):
    s=0
    for i in range(m):
        if i%2==0:
            for j in range(n):
                a=count(l[i][j])
                s=s*pow(10,a)+l[i][j]            
        else:            
            for j in range(n-1,-1,-1):        
                a=count(l[i][j])
                s=s*pow(10,a)+rev(l[i][j])            
    #print(s)                    
    return s

def lrl(l,m,n):
    s=0
    c=0
    for i in range(m-1,-1,-1):
        if c % 2==0:
            for j in range(n-1,-1,-1):
                a=count(l[i][j])
                s=s*pow(10,a)+rev(l[i][j])
            c+=1    
        else:
            for j in range(n):
                a=count(l[i][j])
                s=s*pow(10,a)+l[i][j]
            c=c+1
    #print(s)                    
    return s

def dud(l,m,n):
    s=0
    for j in range(n):
        if j%2==0:
            for i in range(m):
                a=count(l[i][j])
                s=s*pow(10,a)+l[i][j]
        else:
            for i in range(m-1,-1,-1):
                a=count(l[i][j])
                s=s*pow(10,a)+l[i][j]
    #print(s)            
    return s

def udu(l,m,n):
    s=0
    c=0
    for j in range(n-1,-1,-1):
        if c%2==0:
            for i in range(m-1,-1,-1):
                a=count(l[i][j])
                s=s*pow(10,a)+rev(l[i][j])
            c=c+1
        else:
            for i in range(m):
                a=count(l[i][j])
                s=s*pow(10,a)+l[i][j]
            c=c+1
    #print(s)        
    return s

a=[rlr(l,m,n),lrl(l,m,n),dud(l,m,n),udu(l,m,n)]
#print(a)
print (max(a))
                
