#!/bin/python
import timeit
"""
Filename: Median.py
Median of a stream of integers and it's operations
"""

x = [];
last_len = 0; last_mid = -1;

"""
Find the element and delete it. If successful return True else, return False.
"""
def my_remove(val):
	global x
	hi = len(x)-1; lo = 0;
	if (val < x[lo]) or (val > x[hi]):
		return False
	elif val == x[0]:
		del x[0]
		return True
	elif val == x[hi]:
		del x[hi]
		return True
	while True:
		mid = (lo+hi)/2
		if val == x[mid]:
			del x[mid]
			return True
		elif (hi-lo) == 1 and x[hi] != val and x[lo]!=val:
			return False
		elif lo == hi:
			return False
		elif val < x[mid]:
			hi = mid-1
		elif val > x[mid]:
			lo = mid+1

"""
Find the position to insert the element and add it to the list.
"""
def my_insert(val):
	global x
	hi = len(x)-1; lo = 0;
	if (hi == -1) or (val <= x[0]):
		x.insert(0,val)
		return
	elif val >= x[hi]:
		x.append(val)
		return
	while True:
		mid = (lo+hi)/2
		if (hi-lo) <= 1:
			if val < x[lo]:
				x.insert(lo,val)
			elif val > x[hi]:
				x.insert(hi+1,val)
			else :
				x.insert(lo+1,val)
			return;
		else :
			if val == x[mid]:
				x.insert(mid,val)
				return;
			elif val < x[mid]:
				hi = mid-1
			elif val > x[mid]:
				lo = mid+1

"""
Perform the specified operation over list 'X' and value 'val'. Return the median of remaining list
"""
def median(ope, val):
	res = 0;
	global last_len, last_mid;
	# Perform operation on list as specified
	if ope  == 'a':
		# x.append(val)
		# x.sort();	# sort the array
		my_insert(val)
		last_len = last_len + 1
		# Calculate mid value and result
		if (last_len%2) != 0 :
			last_mid = last_mid + 1
			res = x[last_mid]
		else:
			res = (float)(x[last_mid] + x[last_mid + 1]) / 2
	elif ope == 'r':
		if len(x) == 0:
			return 'Wrong!'
		if my_remove(val) == False :
			return 'Wrong!'
		last_len = last_len - 1
		# Calculate mid value and result
		if last_len == 0:
			last_mid = last_mid - 1
			return 'Wrong!'
		elif (last_len%2) != 0 :
			res = x[last_mid]
		else:
			last_mid = last_mid - 1
			res = (float)(x[last_mid] + x[last_mid + 1]) / 2
	
	if (res%1) == 0:
		res = int(res)		
	return res

N = int(raw_input())
toPrint = [];
for i in range(N):
	tmp = raw_input().strip().split(' ')
	ope = tmp[0]
	val = int(tmp[1])
	toPrint.append(median(ope,val))

for i in range(len(toPrint)):
	print str(toPrint[i])