def create_file(): 

    with open('letr.txt','w') as file1: 

        n = int(input('enter no. of lines of text: ')) 

        for i in range (0,n): 

            a = input('enter line: ') 

            file1.write(a) 

            file1.write('\n') 

  

def read_file(): 

    file = input('enter file name: ') 

    with open(file,'r') as file2: 

        return file2.readlines()
    



def read_file_vowel(): 

    file=input('enter file name: ') 

     

    for i in list1: 

        count = 0 

         

        for j in i: 

            if j in 'aeiouAEIOU': 

                count+=1
        
        print('vowel count in line',list1.index(i)+1,': ',count)
     

  

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
            j=i.split()
            for a in j:
                if j[j.index(a)][0] in 'aeiouAEIOU':
            

                    file3.write(a) 

                    file3.write('\n') 

  
flag = 1
while flag !=0: 

    flag= int(input('0 for end loop, 1 for creating, 2 for reading, 3 for counting vowels, 4 for reverse, 5 for copy: ')) 

    if flag == 1: 

        create_file() 

    elif flag==2: 

        list1=read_file()
        for i in list1:
            print(i)

    elif flag == 3: 

        read_file_vowel() 

    elif flag ==4: 

        reverse_display() 

    elif flag ==5: 

        copy_file() 
