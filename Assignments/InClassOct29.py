def main2():
    name = ''

    names_file = open('names.txt', 'w')

    while name != '0':
        name = input("Type a name you want to add to the file or type '0' to exit: ")
        if name != '0':
            names_file.write(name + '\n')
        else:
            break

    names_file.close()

def main():
    line = ''
    counter = 0

    fileObject = open('names.txt', 'r')

    line = fileObject.readline()

    while line != '':
        counter = counter + 1
        print(counter, " ", line)
        line = fileObject.readline()


    fileObject.close()

main2()
main()