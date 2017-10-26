#!/usr/bin/env python3

json = 'window.MNIST_TRAINED_MODEL = ['

for i in range(10):
	f = open('w' + str(i), 'r')
	json += '[' + ', '.join(f.read().splitlines())
	if i < 9:
		json += '], '

json += ']'

print(json)