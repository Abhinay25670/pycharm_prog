with open('test1.txt','w') as f:
    f.write("hello world")
with open('test1.txt','r') as f:
    for line in f:
        print(line)