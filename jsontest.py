import os
file_path = '/home/sushi/demofile3.json'

print(os.stat(file_path).st_size)

if os.stat(file_path).st_size == 1:
    print('File is empty')
else:
    print('File is not empty')
