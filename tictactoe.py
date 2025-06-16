import random
import time
def get_inp():
    r=int(input("enter the row: "))
    c=int(input("enter the column: "))
    if r>3 or c>3:
        print('you have enter a valid input')
        time.sleep(1)
        print('enter a value within 1 to 3')
        return get_inp()
    else:
        if a[r-1][c-1]=="_":
            return r-1,c-1
        else:
            print("already taken,try again")
            return get_inp()
    #ValueError

def gen_inp():
    e=random.choice([0, 1, 2])
    f=random.choice([0, 1, 2])
    if a[e][f]=="_":
        return e,f
    else:
        return gen_inp()

def display(x):
    for i in x:
        for j in i:
            print(j,end='|')
        print()

a=[["_","_","_"],
   ["_","_","_"],
   ["_","_","_"]]
while True:
    num1,num2=get_inp()
    a[num1][num2]="x"
    display(a)
    if (a[0][0]==a[0][1]==a[0][2]=="x" or a[1][0]==a[1][1]==a[1][2]=="x" or a[2][0]==a[2][1]==a[2][2]=="x" or a[0][0]==a[1][0]==a[2][0]=="x" or a[0][1]==a[1][1]==a[2][1]=="x" or a[0][2]==a[1][2]==a[2][2]=="x" or a[0][0]==a[1][1]==a[2][2]=="x" or a[0][2]==a[1][1]==a[2][0]=="x"):
        print("\n\nyou have won the match")
        break
    
    if a[0][0]!="_" and a[0][1]!="_" and a[0][2]!="_" and a[1][0]!="_" and a[1][1]!="_" and a[1][2]!="_" and a[2][0]!="_" and a[2][1]!="_" and a[2][2]!="_":
        print("\n\nlets play again, it an draw")
        break
    n1,n2=gen_inp()
    a[n1][n2]="o"
    time.sleep(2)
    print("choice made by computer",n1+1,n2+1)
    time.sleep(2)
    display(a)
    if (a[0][0]==a[0][1]==a[0][2]=="o" or a[1][0]==a[1][1]==a[1][2]=="o" or a[2][0]==a[2][1]==a[2][2]=="o" or a[0][0]==a[1][0]==a[2][0]=="o" or a[0][1]==a[1][1]==a[2][1]=="o" or a[0][2]==a[1][2]==a[2][2]=="o" or a[0][0]==a[1][1]==a[2][2]=="o" or a[0][2]==a[1][1]==a[2][0]=="o"):
        print("\n\nyou have lost the match")
        break
