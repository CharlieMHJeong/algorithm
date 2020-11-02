# frequency_histogram.py
# 1. Asks the user for the input file's name;
# 2. Read the file (if possible ensure that you enable the file error handling with strerror()) and counts all the Latin letters( lower- and upper-case letters are treated as equal)
# 3. The histogram should be sent to a file the same name as the input one, but with the suffix '.hist'). 

from os import strerror

try:
    file_name = input("Please enter a file name to read [enter for text.txt]: ", ) or "text.txt"
    s = open(file_name, "rt")
    sw = open("{}.hist".format(file_name),"wt")

except IOError as e:
    print(strerror(e.errno))

cha_dict = {}

for i in s.read():
    #Unicode:  32 == Space, 10 == LineFeed
    if ord(i) == 32 or ord(i) == 10:
        continue
    i = i.lower()
    if i != " ":
        cha_dict[i] = cha_dict.get(i,0) + 1

for k, v in cha_dict.items():
    # print("{} --> {}".format(k, v))
    sw.write("{} --> {}\n".format(k, v))

s.close()
sw.close()

