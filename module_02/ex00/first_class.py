class Must_read:
    def __init__(self):
        filename = 'data.csv'
        with open(filename, 'r') as in_file:
            print(in_file.read())


if __name__ == '__main__':
    mr = Must_read()
