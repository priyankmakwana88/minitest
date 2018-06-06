#!/usr/bin/env python3

import numpy as np

arr=np.array([1,2,3,4,5,6])
li=[11,22,33]
print(arr)

#METHOD 1 (save data in .npy format)
'''
np.save('data1',arr)

q=np.load('data1.npy')

print(q)
'''

#METHOD 2 (save data in txt file)
'''
#	    file_name	what_to_save		      format	  newline(\n as def)			will dislpay comments as well
np.savetxt('data.txt',  arr,		delimiter=',',fmt='%1.5e',newline=' ',		comments='#hi',footer=' ')
#np.savetxt('data.txt', arr)

ar=np.loadtxt('data.txt',dtype=float)
print(ar)
'''

#METHOD 3 (save data in txt file and similar to save function)
arr.tofile('data.txt')

ar=np.fromfile('data.txt',dtype=int)
print(ar)
