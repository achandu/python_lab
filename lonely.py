#!/usr/bin/py
# Head ends here
def lonelyinteger(a):
	answer = 0
	for element in a:
		answer = element ^ answer
	return answer
	
# Tail starts here
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)