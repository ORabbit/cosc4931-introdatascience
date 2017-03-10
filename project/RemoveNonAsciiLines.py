import sys

def removeNonAsciiLines():
	if (len(sys.argv) != 2):
		print('ERROR: Invalid input arguments must be removeNonAsciiLines [filename]')
		exit()
	filename = sys.argv[1]
	
	fileR = open(filename, 'r')
	fileW = open('Ascii-' + filename, 'w')

	for line in fileR:
		try:
			line.decode('ascii')
			fileW.write(line)
		except UnicodeDecodeError:
			continue
	fileR.close()
	fileW.close()

removeNonAsciiLines()
	
