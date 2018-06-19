#!/usr/bin/env python3

from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("sample.xls")
wb = copy(rb)

s = wb.get_sheet(0)
s.write(2,0,2)
wb.save('sample.xls')
