import sys
class File_Handler:
	log_directory = None

	def __init__(self, directory_path):
		self.log_directory = directory_path

	def read(self, file_name):
		absolute_path = self.log_directory + "/" + file_name

		file = open(absolute_path, "r")

		for line in file:
			print("Line read from file => ", line)			

log_file_name = sys.argv[1]

# Creation of a OBJECT via Class File_Handler
try:
	log_object = File_Handler("/Users/divang/Desktop/logs")
	log_object.read(log_file_name)
	print("File found in log folder")
	sys.exit(1)
except:
	print("...... Looks like you have supplied the data file not the log file .....")

try:	
	data_object = File_Handler("/Users/divang/Desktop/data")
	data_object.read(log_file_name)
	print("File found in data folder")
except:
	print("Looks like you have supplied the neither log nor data file")

