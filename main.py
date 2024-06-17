#word counting program 
#This program is a word counting program. first it ask you to enter your file or words and when you entered, it will counts your words bit by bit.You will get every word and how many times it is in your data. 
#this code can save you much time in counting words which hard in human #mind when you hava more files.


count =  dict()
print('Enter your file or words Here')
line = input('')
words = line.split()
print('Words:', words)
print('Counting the word...')
for word in words:
    count[word] = count.get(word, 0) + 1
print("counts", count)
print('successfully completed')


