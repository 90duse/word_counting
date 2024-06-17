#word counting program 
try:
    name = input('Enter your file: ')
    with open(name, 'r', encoding='utf-8') as handle:
        count = dict()
        for line in handle:
            words = line.split()
            for word in words:
                count[word] = count.get(word, 0) + 1

    print('Counting the words...')
    print('Successfully completed.')
    print('Word counts:')
    print(count)

    total_words = sum(count.values())
    print('Total words in this file:', total_words)

except FileNotFoundError:
    print(f"Error: The file '{name}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access the file '{name}'.")
except Exception as e:
    print(f"An error occurred: {e}")




