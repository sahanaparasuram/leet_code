
list=eval(input('Enter an array:'))

    
def fun_sort(a):
    l=len(list)
    for i in range(0,l):
        for j in range(1,l-i):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]

    
    print('The elements after sorting in ascending order are:', a)



def fun_search(a):
    l=len(list)
    n=int(input('Element to be searched: '))
    for i in range(0,l):
       
        
        if a[i] == n:
            print('The element is present',i+1,'position')
            break
    else:
        print('The element is not present in the list')

def fun_binary_search(a): 
    low = 0
    high = len(a)
    x = int(input('Enter a number to be searched: '))
     
    while high > low: 
  
        mid = (high + low) // 2

        if a[mid] == x: 
             
            break

        elif a[mid] > x:
            high = mid-1
             
        else:
            low = mid 
            
  
    else: 
        
        mid= 0
    
      
    if mid>0: 
        print('The element is present in',mid+1,'position') 
    else: 
        print('The element is not present in the list')
  
fun_sort(list)
print()
print('Linear search:')
print()
fun_search(list)
fun_search(list)
print('Binary search:')
print()
fun_binary_search(list)
fun_binary_search(list)

 
         
     
    

    
    
