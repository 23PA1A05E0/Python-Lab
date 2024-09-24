import csv

data = [['s.no','name'],[1,'bharath'],[2,'balaji']]


f = open('table.csv','w')
w= csv.writer(f)
w.writerows()
f.close()

f = open('table.csv','r')
r = csv.reader(f)
for row in r:
    print(row)
