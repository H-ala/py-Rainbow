import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    answer = dict()
    for number in range(1000, 9999):
        answer[hashlib.sha256(str(number).encode()).hexdigest()] = number
    
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            passHash = row[1]
            with open(output_file_name, 'a', newline = '') as fout:
                writer = csv.writer(fout)
                writer.writerow([name, answer[passHash]])

hash_password_hack('RainbowIn.csv', 'RainbowOut.csv')