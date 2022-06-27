import sys
class File_Handler:
	file_directory = None

	def __init__(self, directory_path):
		self.file_directory = directory_path

	def read(self, file_name):
		absolute_path = self.file_directory + "/" + file_name
		file = None
		try:
			file = open(absolute_path, "r")

			for line in file:
				print("Line read from file => ", line)			
		except:
			print("File is not present in ", self.file_directory)
		finally:
			if file is not None:
				file.close()							


	def write(self, file_name):
		absolute_path = self.file_directory + "/" + file_name
		file = None
		try:
			file = open(absolute_path, "a")
			file.write("It is written via python code...")
			print("Data successfully written to file.")
		except:
			print("File is not present in ", self.file_directory)
		finally:
			if file is not None:
				file.close()							


file_name = sys.argv[1]
# Write the file
log_object = File_Handler("/Users/divang/Desktop/data")
log_object.write(file_name)

# Reading the above written file
log_object.read(file_name) 
