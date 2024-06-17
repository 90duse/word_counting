# this code will get you any special word that you may want 
# to search inside a file. in the example we are using legacy.txt file which
# has some words and if you want to use it in you file you can, all you need is to have the file and upload it. 

try:
    name = input('Enter your file: ')
    handle  = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    handle.close() # this will close the file after reading it to free the system in some resources
    bigword = input('Enter the word you want to fine inside the file: ').strip()
    if bigword in counts:
        total = counts[bigword]
        print('your word ', bigword , 'apears in the file times', total)
    else:
        print('Not there')
      
      
        
   

        
  

except FileNotFoundError:
    print(f"Error: The file '{name}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access the file '{name}'.")
except Exception as e:
    print(f"An error occurred: {e}")