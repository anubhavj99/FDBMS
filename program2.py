# metaFile;
def getTableMetaData(metaFile):
	x = metaFile.read();
	x = x.split('\n');
	for i in range(len(x)):
		x[i] = x[i].split(' ');
	return x;

def getTableData(dataFile, dataTypes):
	x = dataFile.read();
	x = x.split('\n');
	for i in range(len(x)):
		x[i] = x[i].split(' ');
	for dt in dataTypes:
		if dt[0] not in x[0]:
			print('error');
			return False;
	return x;

def putFromInputToDataFile(inputFile, dataFile, dataTypes):
	

if __name__ == '__main__':
	metaFile = open('metadata','r');
	dataTypes = getTableMetaData(metaFile);
	# print(dataTypes);
	dataFile = open('datafile','r+');
	getTableData(dataFile, dataTypes);
	inputFile = open('inputfile', 'r');
	putFromInputToDataFile(inputFile, dataFile, dataTypes)
	metaFile.close();
	dataFile.close();