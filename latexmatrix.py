#!/usr/bin/python
import sys

w,h= None,None
h = None

values = []

for arg in sys.argv:
    if "matrix" in arg:
        pass #consume our name
    elif "-w" in arg:
        w = int(arg[arg.find("-w")+2:])
    elif "-h" in arg:
        h = int(arg[arg.find("-h")+2:])
    else:
        values.append(arg)
        
if w == None:
    w = int(raw_input("Please enter a width: "))
if h == None:
    h = int(raw_input("Please enter a height: "))

result = "\\begin{pmatrix}\n"

if len(values) == 0:
    print "Please enter all the values for one row, seperated by a space and then hit enter, repeat for each row."
for i in range(h):
    if len(values) < w:
        row = raw_input().split(" ")
    else:
        row = values[:w]
        values = values[w:]
    row = row[:w]
    for e in row:
        result += e + " & "
    result = result[:-2]
    result += "\\\\\n"

result = result[:-3]+"\n\\end{pmatrix}\n"
print result
