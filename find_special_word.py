# this code will get you any special word that you may want 
# to search inside a file. in the example we are using legacy.txt file which it
# has some words.  all you need is to have the file. 

try:
    name = input('Enter your file ')
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
      
      
        
   

        
  

except :
      print('Unkown error is found in the code ',)