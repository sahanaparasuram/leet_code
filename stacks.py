l=[]
top=None
def push():
    n=input('enter element: ')
    l.append(n)
    top = len(l)-1

def pop():
    if len(l)== 0:
        print('sorry :( there are no elements in this list')
    else:
        l.pop()
        top = len(l)-1

def display():
    print(l)

i = 1
while i == True:
    n=int(input('enter 1 to append\n enter 2 to pop\n enter 3 to display\nenter 0 to exit'))
    if n==1:
        push()
    elif n==2:
        pop()
    elif n==3:
        display()
