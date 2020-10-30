def create_file():
    with open('letter.txt','w') as file1:
        n = int(input('enter no. of lines of text: '))
        for i in range n:
            a = input('enter line: ')
            file1.write(a)
            file1.write('\n')

def read_file():
    file = input('enter file name: ')
    with open(file,'r') as file2:
        return file2.readlines()
list1 = read_file()
def read_file_vowel():
    file=input('enter file name: ')
    
    for i in list1:
        count = 0
        print('vowel count in line',index(i),': ')
        for j in i:
            if j in 'aeiouAEIOU':
                count+=1
    return count

def reverse_display():
    list2=[]
    for i in list1:
        a = ''
        for j in range(len(i)-1,-1,-1):
            a+= i[j]
        list2.append(a)
    for i in list2:
        print(i)

def copy_file():
    file = input('enter file name: ')
    with open(file,'w') as file3:
        for i in list1:
            file3.write(i)
            file3.write('\n')

while flag !=0:
    flag= int(input('0 for end loop, 1 for creating, 2 for reading, 3 for counting vowels, 4 for reverse, 5 for copy: '))
    if flag == 1:
        create_file()
    elif flag==2:
        list1=read_file()
    elif flag == 3:
        read_file_vowel()
    elif flag ==4:
        reverse_display()
    elif flag ==5:
        copy_file()
        
        
        
        
        
    
    



        
            
        
            
