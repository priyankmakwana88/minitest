#!/usr/bin/env python3

from xlrd import open_workbook
wb = open_workbook('sample.xls')
#print ((wb.sheets()[0].cell(0,0).value))

for s in wb.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
    print (values)

