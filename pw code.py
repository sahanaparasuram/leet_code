pw=942
i=6
print("welcome! this is a fun code breaking game that i have designed!!")
print("the aim of the game is quite simple. you have to guess a 3 digit")
print("code based on certain clues. you will have 6 attempts to do this")
print("the first attemp is a random guess. but from the second attempt,")
print("you will get one clue for every attempt. you have 5 clues in all")
print("zero is not present ina ny place and no number repeats itself")
print("remember! the world is counting on you to crack this code!")
print()
print()
clue=1
clue1="6 8 2 : only one number is correct and well placed"
clue2='6 1 4 : only one number is correct but wrongly  placed'
clue3='2 9 6 : only two numbers are correct but wrongly placed'
clue4='7 3 8 : nothing is correct'
clue5='7 8 9 : only one number is correct but wrong placed'
while i>0:
    print()
    pin=int(input("enter the correct pin: "))
    print()
    if pin==pw:

        print("congratulations!! you cracked the code!!you haved saved everyone!")
        break
    else:
        i=i-1
        print("wrong pin! please try again")
        print(" you have",i,"attempts remaining!")
        print()
        while clue==1:
            ans=input("would you like clue 1?(yes/no): ")
            if ans=='yes':
                print()
                print(clue1)
                break
        while clue==2:
            ans=input("would you like clue 2?(yes/no): ")
            if ans=='yes':
                print()
                print(clue2)
                break
        while clue==3:
            ans=input("would you like clue 3?(yes/no): ")
            if ans=='yes':
                ()
                print(clue3)
                break
        while clue==4:
            ans=input("would you like clue 4?(yes/no): ")
            if ans=='yes':
                print()
                print(clue4)
                break
        while clue==5:
            ans=input("would you like clue 5?(yes/no): ")
            if ans=='yes':
                print()
                print(clue5)
                break
        clue=clue+1
        
else:
    print("you have run out of attempts:( your account has been locked!")
    print("the world might be in danger")
    print("talk to your programer if you would like to try again")
    
