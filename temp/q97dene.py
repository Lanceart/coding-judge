import os
import sys
# Print the current working directory
print("Current working directory:", os.getcwd())


print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)


import subprocess

# The command you want to execute, e.g., 'dir' to list directory contents on Windows.
command = ["javac", "-version"]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the standard output of the command
print("Output:")
print(result.stdout)

# Print the standard error of the command, if any
if result.stderr:
    print("Errors:")
    print(result.stderr)