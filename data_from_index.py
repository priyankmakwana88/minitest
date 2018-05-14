#!/usr/bin/env python

import ctypes
x=raw_input()


print id(x)
print ctypes.cast(id(x), ctypes.py_object).value
