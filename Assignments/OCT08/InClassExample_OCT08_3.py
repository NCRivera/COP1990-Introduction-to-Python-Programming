file = input('What is the name of your file (add the extension, like .txt): ')

infile = open(file, 'r')


for line in range(5):
    print(infile.readline(0.))

infile.close()
