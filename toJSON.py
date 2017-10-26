#!/usr/bin/env python3

json = 'model = ['

for i in range(10):
	f = open('w' + str(i), 'r')
	json += '[' + ', '.join(f.read().splitlines())
	if i < 9:
		json += '], '

json += ']'

print(json)