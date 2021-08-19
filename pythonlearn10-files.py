#open files
#file objects


#r will read the file
with open('python dev job desc.txt', 'r', encoding="utf8") as f:
    f_contents = f.read()
    print(f_contents)


#w will write or overwrite current file if it already exist
with open ('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0) #seek does something, A BIT CONFUSING oreplaced r with t
    f.write('R')

#try copy file

with open('python dev job desc.txt', 'r', encoding ="utf8") as rf:
    with open('test_copy.txt', 'w', encoding="utf8") as wf:
        for line in rf:
            wf.write(line)