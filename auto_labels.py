import os

# Path dataset to create name to labels
direktori = '../dataset/train' 

# Get a list of folder names in natural order in the file system
nama_folder = sorted([folder for folder in os.listdir(direktori) if os.path.isdir(os.path.join(direktori, folder))])

# create labels
with open('labels.txt', 'w') as file:
    file.write('\n'.join(nama_folder))

