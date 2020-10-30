import pickle
import os

dict={}

n=int(input('enter no. of entries: '))
for i in range(0,n):
    rec = []
    name = input('enter name: ')
    rec.append(name)
    reg_no = int(input('enter the reg no.: '))
    
    rank = int(input('enter the rank: '))
    
    rec.append(rank)
   
    
    if rank <=100 :
        sub_code = 'Comp'
    elif rank >100 and rank <=200:
        sub_code = ' Elec'
    elif rank > 200 and rank <=300:
        sub_code = 'Tele'
    else:
        sub_code = 'NO ALLOTMENT'
    rec.append(sub_code)
    
    dict[reg_no] = rec



def create_file():
    with open('cetrk.dat','wb') as file1:
        pickle.dump(dict,file1)
        
        
def copy_file():
    with open('cetrk.dat','rb') as file1:
        dict=pickle.load(file1)
        print (dict)
        
        with open('cet.dat','wb') as file2:
            dict_copy={}
            for i in dict:
                if dict[i][1]<=1000:
                    dict_copy[i]=dict[i]
            pickle.dump(dict_copy,file2)
            print (dict_copy)
                    
            
def read_file():
    name = input('enter file name: ')
    
    with open(name,'rb') as file1:
        dict=pickle.load(file1)
        
        
        print('Reg No. \t\tName \t\tRank \t\tSubject code')
        for i in dict:
            print()
            print(i,end = '\t\t')
            for j in dict[i]:
                print(j,end = '\t\t')
        return dict
    print()
            

            

def append_file(dict):
    num = int(input('enter no. of appends: '))
    with open('temp.dat','wb') as file1:
        for i in range(0,num):
            rec = []
            name = input('enter name: ')
            rec.append(name)
            reg_no = int(input('enter the reg no.: '))
    
            rank = int(input('enter the rank: '))
            rec.append(rank)
   
    
            if rank <=100 :
                sub_code = 'Comp'
            elif rank >100 and rank <=200:
                sub_code = ' Elec'
            elif rank > 200 and rank <=300:
                sub_code = 'Tele'
            else:
                sub_code = 'NO ALLOTMENT'
            rec.append(sub_code)
            dict[reg_no] = rec
        pickle.dump(dict,file1)
        
        
    os.remove('cetrk.dat')
    os.rename('temp.dat','cetrk.dat')
        
def delete_file():
    with open('tempe.dat','wb') as file1:
        dict1={}
        with open('cetrk.dat','wb') as file2:
        
            for i in dict:
                if dict[i][1]<=1500:
                    dict1[i]=dict[i]
        pickle.dump(dict1,file1)
    os.remove('cetrk.dat')
    os.rename('tempe.dat','cetrk.dat')
            
            
flag=1
while flag!=0:
    flag= int(input('0 for end loop\n1 for create\n2 for reading\n3 for append\n4 for copy\n5 for delete: '))
    if flag==1:        
        create_file()
        print()    
    elif flag==2:
        dict1=read_file()
        print()
    elif flag==3:
        append_file(dict1)
        print()
    elif flag==4:
        copy_file()
        print()
    elif flag==5:        
        delete_file()
        print()


        


    

    

    

    
