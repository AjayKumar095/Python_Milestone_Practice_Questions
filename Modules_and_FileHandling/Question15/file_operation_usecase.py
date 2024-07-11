from file_operations import read, write, appending

filepath='Modules_and_FileHandling\Question15\sampletext.txt'
print(read(filepath=filepath))
print(write(filepath=filepath, text='This new text.'))
print(appending(filepath=filepath, text='This text need to append with old data.'))