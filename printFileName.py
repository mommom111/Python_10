import glob
files = glob.glob('data//*.csv')
print(files)

# from pathlib import Path
# data_path = './data'
# csv_files = Path(data_path).glob('*.csv')
# for file in csv_files:
#   print(file)