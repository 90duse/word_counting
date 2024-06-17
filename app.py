# this program will the biggest word or longest word in your file and how many
# time that word is in the file. also it will tell you total words in in your file
try:
    name = input('Enter your file ')
    handle  = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1


    bigword = None
    numberOftime = None

    for word, tiro in counts.items():
        if bigword is None or str(tiro) > bigword:
            bigword = word
            numberOftime = tiro
    print(bigword,numberOftime)
        
    totalwords = sum(counts.values())
    print('Total words in this file are: ', totalwords)

except :
      print('Unkown error is found in the code ',)
    

# dealing files this code will get you any special word that you may want 
# to search inside a file. in the exaple we are using legacy.txt file which it
# has some pragraphs









    