import glob2

# Recursivly search though directory for txt files
# Use with to create new file and append text
# for i in glob2.glob('./*.txt'):
#     print(i)


with open('mergedFile.txt', 'a+') as file:
    fileLst = glob2.glob('./*.txt')
    for i in fileLst:
        currentFile = open(i);
        content = currentFile.read()
        file.write(content + '\n')
        