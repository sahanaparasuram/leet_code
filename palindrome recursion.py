def create(n,list):
    for i in range(0,n):
        name=input('enter name: ')
        list.append(name)

def display(n,list):
    for i in range(0,n):
        print(list[i])

        

def sort(n,list):
    def innersort(a,b,c):
        
        if len(a)>len(b) and c+1<=len(b):
            if a[c]>b[c]:
                a,b=b,a
                print(a,b)
            if a[c]==b[c]:
                innersort(a,b,c+1)
        elif len(a)<len(b) and c+1<=len(a):
            if a[c]>b[c]:
                a,b=b,a
            if a[c]==b[c]:
                innersort(a,b,c+1)
    for j in range(0,n):   
        for i in range(0,n-1):
            if list[i][0]>list[i+1][0]:
                list[i],list[i+1]=list[i+1],list[i]
            if list[i][0]==list[i+1][0]:
                innersort(list[i],list[i+1],1)
    print('The names in alphabetical order are: ')
    for i in range(0,n ):
        print(list[i])


def search(a,x,list):
    find=False
    for i in range(0,x):
        if list[i]==a:
            print('Name found in position : ',i+1)
            find=True
    if not(find):
        print('Name not found')

        

def reverse(x,list):
    for i in range(0,x):
        list[i]=list[i][::-1]
    print('The reverse of each name: ')
    for i in range(0,x):
        print(list[i])
        
    
for i in range(0,5):
    menu=input('Enter 1 to create, 2 to display, 3 to sort, 4 to search, 5 to reverse : ')
    if menu=='1':
        n=int(input('enter number of students:'))
        listname=[]
        create(n,listname)
        print(listname) 
    if menu=='2':
        display(n,listname)
    if menu=='3':
        sort(n,listname)  
    if menu=='4':
        num=int(input('Enter number of names to be searched : '))
        for k in range(0,num):
            name=input('Enter name to be searched : ')
            search(name,n,listname)
    if menu=='5':
        reverse(n,listname)
