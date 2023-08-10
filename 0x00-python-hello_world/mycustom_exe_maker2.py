import os
import sys

# Get the current working directory
current_directory = os.getcwd()

# Check for command-line arguments
if len(sys.argv) < 2:
    print("Usage: python make_executable.py <exclude_extensions>")
    sys.exit(1)

# List of file extensions to exclude (passed as command-line arguments)
exclude_extensions = sys.argv[1:]

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
