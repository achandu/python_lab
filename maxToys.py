#!/usr/bin/py

def NumToys(toys, amount):
	count = 0; total_price = 0;
	for i in range(len(toys)):
		if (toys[i]+total_price) < amount :
			total_price = total_price + toys[i]
			count = count + 1
		else :
			return count;
	return count

amount = int(raw_input().split(" ")[1])
toys = map(int, raw_input().strip().split(" "))
toys.sort();
print str(NumToys(toys,amount))