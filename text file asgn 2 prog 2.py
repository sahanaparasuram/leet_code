import os

def create_file():
    with open("letter.txt", "w") as file1:
        num = int(input("enter number of lines: "))
        for i in range (0, num):
            n = input("enter line: ")
            file1.write(n)
            file1.write('\n')
        file1.close()
            
      

                
def read_file():
    file = input("enter file name: ")
    with open(file, "r") as file1:
        all_file_lines = file1.readlines()
        new_file_lines = []
        i=1
        for file_line in all_file_lines:
           
            str = ''
            for file_letter in file_line:
                if ord(file_letter)>= 97 and ord(file_letter) <=122:
                    num_file_letter = ord(file_letter)
                    str+=chr(num_file_letter-32)
                    file_letter = chr(num_file_letter)
                elif ord(file_letter) >=65 and ord(file_letter) <= 90:
                    num_file_letter = ord(file_letter)
                    str+=chr(num_file_letter+32)
                    file_letter = chr(num_file_letter)
                else:
                    str+=file_letter
            new_file_lines.append(i)
            print(i,'.',str)
            i+=1
    


    
def word_search():
    with open("letter.txt", "r") as file1:
        all_file_lines = file1.readlines()
        search_word = input("enter word to be searched")
        for line in all_file_lines:
            words = line.split()
            count = 0
            
            for word in words:
                
                if word == search_word:
                    count += 1
                    
            print("number of occurences of ",search_word,"is ",count)

def update_file():
    file = input("enter file name")
    with open(file, "r") as file1:
        all_file_lines = file1.readlines()
        new_file_lines = []
        for file_line in all_file_lines:
            newline = ""
            for file_letter in file_line:
                if file_letter in "AEIOUaeiou":
                    newline+="*"
                else:
                    newline+=file_letter
            
            new_file_lines.append(newline)
    with open("tmp.txt", "w") as file2:
        for i in new_file_lines:
            file2.write(i)
            file2.write("\n")
            
    os.remove('letter.txt')
    os.rename('tmp.txt', "letter.txt")

    with open("letter.txt", "r") as file3:
        lines= file3.readlines()
        for i in lines:
            print(i)
         

for i in range(0,4):
    flag = int(input("Enter 1 for create file, enter 2 for read and Uppercase/Lower case, enter 3 for word search, enter 4 for update file, enter 0 for exit: "))
    if flag == 1:
        create_file()
    if flag == 2:
        read_file()
    if flag == 3:
        word_search()
    if flag == 4:
        update_file()

               
