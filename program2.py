# metaFile;
def getTableMetaData(metaFile):
	x = metaFile.read();
	x = x.split('\n');
	for i in range(len(x)):
		x[i] = x[i].split(' ');
	return x;

def readInputFile(inputFile, dataTypes):
	totalLength = 0;
	for dt in dataTypes:
		totalLength += int(dt[2]);
	x = inputFile.read();

	if len(x) % totalLength !=0:
		raise Exception('File unexpected');

	x = [x[i:i+totalLength] for i in range(0, len(x), totalLength)];
	fullX = [];
	for data in x:
		temp = [];
		lensum = 0;
		for dt in dataTypes:
			lensum += int(dt[2]);
			temp.append(data[lensum-int(dt[2]):lensum]);
		fullX.append(temp);

	for i in range(len(fullX)):
		for j in range(len(fullX[i])):
			if dataTypes[j][1] == 'C':
				fullX[i][j] = fullX[i][j].strip();
			elif dataTypes[j][1] == 'I':
				fullX[i][j] = int(fullX[i][j]);
			elif dataTypes[j][1] == 'P':
				fullX[i][j] = float(fullX[i][j]);	
	
	print(fullX);
	return fullX;
				


# def putFromInputToDataFile(inputFile, dataFile, dataTypes):


if __name__ == '__main__':
	metaFile = open('metadata','r');
	dataTypes = getTableMetaData(metaFile);
	dataFile = open('datafile','r+');
	inputFile = open('inputfile', 'r');
	dataBase = readInputFile(inputFile, dataTypes);
	while True:
		col = input();
		colPos = -1;
		for i in range(len(dataTypes)):
			if dataTypes[i][0] == col:
				colPos = i;
				break;
		if colPos == -1:
			raise Exception('Column not present');
		sumCol = 0;
		if dataTypes[colPos][1] == 'I' or dataTypes[colPos][1] == 'P':
			for dtbs in dataBase:
				sumCol += dtbs[colPos];
			print(sumCol);
		else:
			raise Exception('Not a number');



	metaFile.close();
	dataFile.close();