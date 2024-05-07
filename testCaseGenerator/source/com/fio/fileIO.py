#######################################################################################################################
### This class provides a wrapper around File IO
class FileIO:
    ###################################################################################################################
    ### Constructor
    def __init__(self):
        self.readMode = 'r'
        self.writeMode = 'w'

    ###################################################################################################################
    ### Reads in the data for the specified file and returns the data to the caller
    def read(self, fileName):
        # Initialize local variable
        fileData = ""

        # Read the File to the local variable
        # If the file does not exist then throw an error
        try:
            with open(fileName, self.readMode) as file:
                fileData = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {fileName}")

        # Return the data read from the
        return fileData
    
    ###################################################################################################################
    ### Writes the specified data to the specified file.
    def write(self, fileName, fileData):
        # Attempt to open the file to write the data
        # If the file does not exist then throw an error
        try:
            with open(fileName, self.writeMode) as file:
                # If the data is in list format then write each item as a separate line
                if isinstance(fileData, list):
                    file.writelines(fileData)
                # Otherwise the data is just a blob. Write the whole contents
                else:
                    file.write(fileData)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {fileName}")
