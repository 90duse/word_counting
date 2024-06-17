#this code will give you the top 10 longest or bigest words 

try:
    name = input('Enter your file ')
    handle  = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    handle.close()

    
    findlist = list()
    for key, val in counts.items():
        newtup = (val,key)
        findlist.append(newtup)
    findlist = sorted(findlist, reverse=True) #sorting the list and allowing to reverse the longest to shortest value
    
    for val, key in findlist[:10]: # looping the list to get the top 10 values 
        print(key , val)
    


except FileNotFoundError:
    print(f"Error: The file '{name}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access the file '{name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
    














    