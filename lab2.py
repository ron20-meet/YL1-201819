#ex1
list1 = [5,10,15,20,25]

def fun(ls):
	new_list = [ls[0],ls[-1]]
	return new_list

fun(list1)
print(fun(list1))


#ex2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
 	if i<5:
 		print(i)

#ex3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = [] 
for i in a: 
	if i in b: 
		common.append(i)
print(common)

#ex4
import tkinter as tk
from tkinter import simpledialog

number = int(simpledialog.askstring("Input", "Enter a number!", parent=tk.Tk()))
IsPrime = True
for i in range(2, number):
	if number % i == 0:
		IsPrime = False
if IsPrime:
	print("Prime")
else:
	print("Not prime")