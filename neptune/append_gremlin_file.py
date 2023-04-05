import sys
import csv
import os

file_path = 'vertex.csv'
id = sys.argv[1]
label = sys.argv[2]

try:
  # open with 'a' appends rows to a file
  with open(file_path, 'a', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    if os.stat(file_path).st_size == 0: #check if the file is empty and does not have headers
      header = ['~id', '~label']
      writer.writerow(header)

    data = [id, label]
    writer.writerow(data)
except Exception as e:
  print(e)