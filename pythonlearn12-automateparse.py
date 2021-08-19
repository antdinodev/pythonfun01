import os

#so organize files in order

#for windows use doble backslash
#for mac use / (easier)
os.chdir("E:\\7.12.21 obs\\genshin 8.8\\kamisato vlog")

#print(os.getcwd())


for f in os.listdir():
    #print(f)
    #print(os.path.splitext(f))
    file_name, file_ext = os.path.splitext(f)
    print(file_name)
    #so if your filename has -, you can split it up using this
    print(file_name.split('-'))