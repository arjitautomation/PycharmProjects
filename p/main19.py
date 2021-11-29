# a file named "geek", will be opened with the reading mode.
import os

#to get the current working directory
directory = os.getcwd()

print(directory)
file = open('geek.txt', 'r')
for each in file:
	print (each)
