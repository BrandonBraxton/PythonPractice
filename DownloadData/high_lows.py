import csv

filename = '/Users/brandon/git/PythonPractice/DownloadData/sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    