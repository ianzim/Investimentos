def create_file(name):
    file = open(name, 'wt+')

def add_info(filename, info):
    file = open(filename, 'a+')
    file.write(info)

def read_file(filename):
    file = open(filename, 'r+')
    file = file.split(';')
    mes = file[0]
    quantia = file[1]
    for line in file:
        print(f'{line[0]<.20}{line[1]>8}')
