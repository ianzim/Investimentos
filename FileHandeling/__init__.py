def create_file(name):
    file = open(name, 'wt+')

def add_info(filename, info):
    file = open(filename, 'a+')
    file.write(info)

def read_file(filename):
    file = open(filename, 'r+')
    for line in file:
        line = line.split(';')
        line[2] = line[2].replace('\n', '')
        print(f'{line[0]:.<30}{line[1]} >> {line[2]:>8}')
    file.close()
