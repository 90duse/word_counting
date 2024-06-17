# this program will find you the biggest word or longest word in your file and how many
# time that word is in the file. also it will tell you total words in in your file
try:
    name = input('Enter your file ')
    handle  = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    handle.close()

    bigestWord = None
    numberOftime = None

    for word, tiro in counts.items():
        if bigestWord is None or str(tiro) > bigestWord:
            bigestWord = word
            numberOftime = tiro
    print(bigestWord,numberOftime)
    
    totalwords = sum(counts.values())
    print('Total words in this file are: ', totalwords)

except FileNotFoundError:
    print(f"Error: The file '{name}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access the file '{name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
    














    