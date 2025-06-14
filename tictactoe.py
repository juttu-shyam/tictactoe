import random
def inp():
    c=int(input("1: "))
    d=int(input("2: "))
    if a[c-1][d-1]==" ":
        return c-1,d-1
    else:
        print("already taken,try again")
        return inp()
    #implement out of range

def com():
    e=random.choice([0, 1, 2])
    f=random.choice([0, 1, 2])
    #print(e,f)
    if a[e][f]==" ":
        return e,f
    else:
        return com()

a=[[" "," "," "],[" "," "," "],[" "," "," "]]
"""n1=random.choice([0, 1, 2])
n2=random.choice([0, 1, 2])
print(n1,n2)"""
while True:
    num1,num2=inp()
    a[num1][num2]="x"
    print(a[0],a[1],a[2],sep="\n")
    if (a[0][0]==a[0][1]==a[0][2]=="x" or a[1][0]==a[1][1]==a[1][2]=="x" or a[2][0]==a[2][1]==a[2][2]=="x" or a[0][0]==a[1][0]==a[2][0]=="x" or a[0][1]==a[1][1]==a[2][1]=="x" or a[0][2]==a[1][2]==a[2][2]=="x" or a[0][0]==a[1][1]==a[2][2]=="x" or a[0][2]==a[1][1]==a[2][0]=="x"):
        print("\n\nwin")
        break

    if a[0][0]!=" " and a[0][1]!=" " and a[0][2]!=" " and a[1][0]!=" " and a[1][1]!=" " and a[1][2]!=" " and a[2][0]!=" " and a[2][1]!=" " and a[2][2]!=" ":
        print("\n\ndraw")
        break
    n1,n2=com()
    a[n1][n2]="o"
    print("my choice in ",n1+1,n2+1)
    print(a[0],a[1],a[2],sep="\n")
    if (a[0][0]==a[0][1]==a[0][2]=="o" or a[1][0]==a[1][1]==a[1][2]=="o" or a[2][0]==a[2][1]==a[2][2]=="o" or a[0][0]==a[1][0]==a[2][0]=="o" or a[0][1]==a[1][1]==a[2][1]=="o" or a[0][2]==a[1][2]==a[2][2]=="o" or a[0][0]==a[1][1]==a[2][2]=="o" or a[0][2]==a[1][1]==a[2][0]=="o"):
        print("\n\nloss")
        break

