

import csv
fields = ['admno','name','grade','sec']
rows = [['1234','jishnu','12','a'],['4567','vinay','11','b'],['8912','rahul','12','a']]
with open('atd_det.csv','w') as newFile:
    csvwriter = csv.writer(newFile)
    csvwriter.writerow(field)
    for row in rows:
        csvwriter.writerow(row)
    
