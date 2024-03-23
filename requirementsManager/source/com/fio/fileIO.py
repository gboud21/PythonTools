#######################################################################################################################
### This class provides a wrapper around File IO
class FileIO:
    def __init__(self):
        self.readMode = 'r'
        self.writeMode = 'w'

    def read(self, fileName):
        # Initialize local variable
        fileData = ""

        # Read the File to the local variable
        # If the file does not exist then throw an error
        try:
            with open(fileName, readMode) as file:
                fileData = file.read()
        except: FileNotFoundError:
            raise FileNotFoundError(f"File not found: {fileName}")

        # Return the data read from the
        return fileData
    
    def write(self, fileName, fileData):
        # Attempt to open the file to write the data
        # If the file does not exist then throw an error
        try:
            with open(fileName, writeMode) as file:
                # If the data is in list format then write each item as a separate line
                if isInstance(fileData, list):
                    file.writelines(data)
                # Otherwise the data is just a blob. Write the whole contents
                else
                    file.write(data)
        except: FileNotFoundError:
            raise FileNotFoundError(f"File not found: {fileName}")
