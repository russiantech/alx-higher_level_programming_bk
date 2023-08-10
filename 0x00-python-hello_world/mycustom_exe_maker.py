import os

# List of file extensions to exclude (adjust as needed)
exclude_extensions = ["txt", "md"]

# Get the current working directory
current_directory = os.getcwd()

# Iterate through the files in the directory
for filename in os.listdir(current_directory):
    if os.path.isfile(filename):
        # Get the file extension
        file_extension = filename.split(".")[-1]

        # Check if the extension is in the exclude list
        if file_extension in exclude_extensions:
            print(f"Excluding file: {filename}")
        else:
            # Make the file executable
            os.chmod(filename, os.stat(filename).st_mode | 0o111)
            print(f"Made executable: {filename}")
