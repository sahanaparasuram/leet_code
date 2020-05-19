ch1='P'
ch2='B'
def charscope():
     ch1='M'
     if(ord(ch1)>70):
         ch1=ch1+ch2
     print(ch1,ch2,sep=":")
#main()
print(ch1,ch2,sep=':')
charscope()
print(ch1,ch2,sep=':')

'''
'P':'B'
'MB:B'
'P':'B'
'''
