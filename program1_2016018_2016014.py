import timeit 
if __name__ == '__main__':
	start = timeit.default_timer();
	inputFile = open('inputfile', 'r');
	x = inputFile.read()
	x = [x[i:i+35] for i in range(0,len(x),35)]
	fullX = []
	for data in x : 
		temp = []
		temp.append(int(data[0:5]))
		temp.append(data[5:25].strip())
		temp.append(float(data[25:35]))
		fullX.append(temp)
	# print(fullX)	
	col = 'ID';
	colPos = -1;
	if col == 'ID' :
		colPos = 0
	elif col == 'STATUS' :
		colPos = 1
	elif col == 'PRICE' :
		colPos = 2		
	if colPos == -1:
		raise Exception('Column not present');
	sumCol = 0;
	
	if colPos==0 or colPos==2 :
		for dtbs in fullX :
			sumCol += dtbs[colPos]
		print(sumCol);
	else:
		raise Exception('Not a number');
	inputFile.close()	
	stop = timeit.default_timer();
	print(stop-start);
