def create_file(name):
    file = open(name, 'wt+')

def add_info(filename, info):
    file = open(filename, 'a+')
    file.write(f'{info}\n')

def read_file(filename):
    file = open(filename, 'r+')
    for line in file:
        line = line.split(';')
        line[1] = line[1].replace('\n', '')
        print(f'{line[0]:<.20}.....................{line[1]:>8}')
    file.close()
