from area import circle_area_module as ac, rect_area_module as ar, square_area_module as sq, tri_area_module as at

flag=1
while flag:
    flag=int(input('enter:\n1 for square area\n2 for rect area\n3 for cir area\n4 for tri area\n0 for exit\n'))
    if flag==1:
        side=float(input('enter side length: '))
        print(sq.squ(side))
    elif flag==2:
        l=float(input('enter length: '))
        b=float(input('enter breadth: '))
        print(ar.rect(l,b))
    elif flag==3:
        r=float(input('enter radius: '))
        ac.cir(r)
    elif flag==4:
        side1=float(input('enter side length: '))
        side2=float(input('enter side length: '))
        side3=float(input('enter side length: '))
        print(at.tri(side1,side2,side3))
'''

output:

30.25
33.75
38.465
6.573799795399918

'''
