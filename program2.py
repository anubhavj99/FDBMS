# metaFile;
def getTableMetaData(metaFile):
	x = metaFile.read();
	x = x.split('\n');
	for i in range(len(x)):
		x[i] = x[i].split(' ');
	return x;

def readInputFile(inputFile, dataTypes):
	# x = inputFile.read();
	# x = x.split('\n');
	# for i in range(len(x)):
	# 	x[i] = x[i].split(' ');
	# for dt in dataTypes:
	# 	if dt[0] not in x[0]:
	# 		print('error');
	# 		return False;
	# for i in range(1, len(x)):
	# 	for j in range(len(dataTypes)):
	# 		if dataTypes[j][1] == 'I' and len(x[i][j]) < int(dataTypes[j][2]):
	# 			for k in x[i][j]:
	# 				if ord(k) not in range(48, 58):
	# 					return false;
	# 				else:
	# 					print(k, end="I ");
	# 		elif dataTypes[j][1] == 'C' and len(x[i][j]) < int(dataTypes[j][2]):
	totalLength = 0;
	for dt in dataTypes:
		totalLength += int(dt[2]);
	x = inputFile.read();
	x = [x[i:i+totalLength] for i in range(0, len(x), totalLength)];
	fullX = [];
	for data in x:
		temp = [];
		lensum = 0;
		for dt in dataTypes:
			lensum += int(dt[2]);
			temp.append(data[lensum-int(dt[2]):lensum]);
		fullX.append(temp);
	print(fullX)

				


# def putFromInputToDataFile(inputFile, dataFile, dataTypes):


if __name__ == '__main__':
	metaFile = open('metadata','r');
	dataTypes = getTableMetaData(metaFile);
	# print(dataTypes);
	dataFile = open('datafile','r+');
	# getTableData(dataFile, dataTypes);
	inputFile = open('inputfile', 'r');
	readInputFile(inputFile, dataTypes);
	# putFromInputToDataFile(inputFile, dataFile, dataTypes);
	metaFile.close();
	dataFile.close();