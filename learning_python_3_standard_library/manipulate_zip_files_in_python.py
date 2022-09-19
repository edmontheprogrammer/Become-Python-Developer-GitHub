# Note 1: Archive.zip file is deleted to avoid commit issues to git-github
# Zipfile Module
import zipfile

# Open and List
zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist())

# Metadata in the zip folder
for meta in zip.infolist():
    print(meta)

info = zip.getinfo('purchased.txt')
print(info)


# Access to files in zip folder
print(zip.read("wishlist.txt"))
with zip.open('wishlist.txt') as f:
    print(f.read())

# Extracting files
zip.extract("purchased.txt")

# Closing the zip
zip.extractall()
