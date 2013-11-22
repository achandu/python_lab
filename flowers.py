#!/usr/bin/py

def LeastPrice(flowers,count):
	purchased = [0] * count
	price = 0; j=0;
	for flower in flowers:
		if j == count :
			j = 0
		price = price + flower * ( purchased[j] + 1)
		purchased[j] = purchased[j] + 1
		j = j+1
	return price

friends = int(raw_input().split(" ")[1])
flowers = map(int, raw_input().strip().split(" "))
flowers = sorted(flowers,reverse=True);
print str(LeastPrice(flowers,friends))