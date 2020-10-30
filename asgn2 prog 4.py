import pickle
import os

dict={}
t_type = 'no transaction'
t_amt=0
c_b = 1000
cur=[]
n=int(input('enter no. of entries: '))
for i in range(0,n):
    rec=[]
    name = input('enter name: ')
    rec.append(name)
    acc_no = (input('enter the account no.: '))
    
    rec.append(None)
    
    
    
    
    rec.append(None)
    c_b=int(input('enter the current balance: '))
    rec.append(c_b)
    cur.append(c_b)

    dict[acc_no]= rec

def create():
    with open('accnt.dat','wb') as file1:
        pickle.dump(dict,file1)

def read():
    with open('accnt.dat','rb') as file2:
        dict=pickle.load(file2)

        return dict

def update(dict):
    
    

    

    # acc_no:[name,None,None,c_b]
    n=int(input('enter no. of customers: '))
    for i in dict:
        dict[i][1]= 'notrans'
        dict[i][2]=0
    for j in range(0,n):
        a = input('enter account  number: ')
        if a not in dict:
            print('does not exist')
            
            continue
        
        b = input('enter type of tranaction: ')
        dict[a][1]=b
        
        c = int(input('enter tranaction ammount: ') )
        dict[a][2]=c
        orig=dict
        for i in dict:
        
            
            if i==a:
                if dict[i][1]=='CREDIT' or dict[i][1]=='credit':
                    dict[i][3]+=dict[i][2]
                    print('money has been added')
                    
                elif dict[i][1]=='DEBIT' or dict[i][1]=='debit':
                    if (dict[i][3]-dict[i][2])>=1000:
                        dict[i][3]-=dict[i][2]
                        break
                    else:
                        print('transaction not possible :(')
                        break
    print('acc_no\t\tname\t\ttr. type\t\ttr. amt.\t\tcurrent balance')
    flag=0
    for i in dict:
        
        if len(dict[i][0])>8:
            
            print(i,'\t\t',orig[i][0],'\t',orig[i][1],'\t\t',orig[i][2],'\t\t',cur[flag],'\t\t')
        else:
            print(i,'\t\t',orig[i][0],'\t\t',orig[i][1],'\t\t',orig[i][2],'\t\t',cur[flag],'\t\t')
        flag+=1              

    print()
    print('after updation')
    print()
    print('acc_no\t\tname\t\ttr. type\t\ttr. amt.\t\tcurrent balance')
    for i in dict:
        
        if len(dict[i][0])>8:
            
            print(i,'\t\t',dict[i][0],'\t',dict[i][1],'\t\t',dict[i][2],'\t\t',dict[i][3],'\t\t')
        else:
            print(i,'\t\t',dict[i][0],'\t\t',dict[i][1],'\t\t',dict[i][2],'\t\t',dict[i][3],'\t\t')
        
    with open('temp.dat','wb') as file3:
        pickle.dump(dict,file3)
    os.remove('accnt.dat')
    os.rename('temp.dat','accnt.dat')
              
              
        
flag=1
while flag !=0:
    flag= int(input('0 for end loop\n1 for create\n2 for reading\n3 for updation: '))
    if flag == 1:
        create()
    elif flag==2:
        dict=read()        
    elif flag == 3:
        update(dict)
    

        
'''
Account_noNameCurrent     Balance
SB_1234   Sudhakar K    10000
SB_3425   Malathi V      12000
SB_5432   Suhumar J      12000
SB_7654   Vijay H          15500
SB_8765   Suresh           10500
SB_7889   Raghu             20000

                
    
    '''
        
        
        
