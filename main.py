#word counting program 
count =  dict()
print('Enter your file or words Here')
line = input('')
words = line.split()
print('Words:', words)
print('Counting the word...')
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)
print('successfully completed')


