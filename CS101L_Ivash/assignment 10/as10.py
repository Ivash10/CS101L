# initialize punctuations string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
word_counts = dict()
while True:
    file_name = input("Enter the name of the file to open ")
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
        break

    except:
        print("Could not open file ", file_name)
        print("Please Try again\n")


for line in lines:
    for x in line:
        if x in punctuations:
            line = line.replace(x, "")
            words = line.lower().split()

for word in words:
     if len(word) > 3:
        if word not in word_counts.keys():
            word_counts[word] = 1
        else:
            word_counts[word] += 1
            
word_count_tuple = [(word, count) for word, count in sorted(
word_counts.items(), key=lambda item: item[1], reverse=True)[:10]]
print("Most frequently used words")
print("#\t" + "Word".rjust(10) + "\t\tFreq.".rjust(2))
print("=====================================")

for i, (key, value) in enumerate(word_count_tuple):
    print(str(i) + '\t' + key.rjust(10) + '\t\t' + str(value).rjust(4))
    print()


one_occurence = sum(count == 1 for count in word_counts.values())
print("There are " + str(one_occurence) + " words that occur only once")


print("There are " + str(len(word_counts)) + " unique words in the document")