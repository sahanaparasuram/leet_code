import csv

def Create_file():
    with open('coun.csv','w',newline='') as file1:
        n=int(input('enter no.of records: '))
        fields = ['Country id','Country name','region id']
        csvwriter=csv.writer(file1)
        csvwriter.writerow(fields)
        for i in range(0,n):
            print('enter the details of record',i+1,' in the form of a list:',end=' ')
            rec= eval(input())
            csvwriter.writerow(rec)

def Read_file():
    with open('coun.csv','r',newline='') as file2:
        csvreader=csv.reader(file2)
        for  lines in file2:
            print(lines)


def Search_file():
    with open('coun.csv','r',newline='') as file2:
        csvreader=csv.reader(file2)
        search=input('enter country id to be searched:  ')
        for  line in file2:
            if line[0]==search:
                print('The details of country id',search,'is:',end=' ')
                for i in line:
                    print(i,end=' ')
                print()

flag=1
while flag !=0:
    flag= int(input('0 for end loop\n1 for create\n2 for reading\n3 for search: '))
    if flag == 1:
        Create_file()
    elif flag==2:
        Read_file()        
    elif flag == 3:
        Search_file()


            
    
