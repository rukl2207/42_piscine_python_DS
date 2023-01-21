class Research:
    def __init__(self):
        self.filename = '../ex00/data.csv'

    def file_reader(self) -> str:
        with open(self.filename, 'r') as in_file:
            return in_file.read()


if __name__ == '__main__':
    print(Research().file_reader())
