infile = open('philosophers.txt', 'r')

line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()

print(line1.strip())
print(line2.strip())
print(line3.strip())


#for line in range(5):
#    print(infile.readline())


infile.close()
