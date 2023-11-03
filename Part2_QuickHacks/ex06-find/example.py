# Import libraries
import os
import time

# Insert the directory path in here
path = '/Users/dimsumpanda/Documents/Projects/learn-more-python-the-hard-way/ex5'

# Extracting all the contents in the directory corresponding to path
l_files = os.listdir(path)
print(l_files)
# # Iterating over all the files
# for file in l_files:

#     # Instantiating the path of the file. path was set earlier
#     file_path = f'{path}\\{file}'

#     # Checking whether the given file is a directory or not
#     if os.path.isfile(file_path):
#         try:
#             # Printing the file pertaining to file_path
#             # os.startfile(file_path, 'print')
#             print(f'Printing {file}')

#             # Sleeping the program for 5 seconds so as to account the
#             # steady processing of the print operation.
#             time.sleep(5)
#         except:
#             # Catching if any error occurs and alerting the user
#             print(f'ALERT: {file} is not a file, so can not be printed!')

# print('Task finished!')
