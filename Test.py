from random import randint,uniform
L = ['              Landed','             On time','             Arrived']
inputFile = open('inputfile','w')
s = ''
for test in range(0,10000) :
	s = s + str(randint(10000,100000)) + L[randint(0,2)] + str('{0:.4f}'.format(uniform(10000,20000)))
inputFile.write(s)	
