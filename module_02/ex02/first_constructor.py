import sys
import os


class Research:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = None

    def file_reader(self) -> str:
        if not os.access(self.filename, os.R_OK):
            raise FileNotFoundError("The file does not exist or cannot be read.")
        with open(self.filename, 'r') as in_file:
            self.data = in_file.read()
            tpl = tuple(self.data.split('\n'))
            if len(tpl) < 2:
                raise ValueError("The correct file must contain a header and data.")
            correct_data_row = {'0', '1'}
            for i, value in enumerate(tpl):
                row = tuple(map(str.strip, value.split(',')))
                if i == 0:
                    if not (len(row) == 2 and set(row) != correct_data_row):
                        raise ValueError(
                            f"Error in line {i + 1}. "
                            f"The correct ﬁle contains a header with two strings delimited by a comma.")
                else:
                    if not (len(row) == 2 and set(row) == correct_data_row):
                        raise ValueError(
                            f"Error in line {i + 1}. "
                            f"The line must contain either 0 or 1 and never both of them delimited by a comma.")
            return self.data


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise AttributeError(f"Error: Wrong number of arguments.\n"
                             f"Usage: python3 {os.path.basename(__file__)} <path_to_data.csv>")
    print(Research(sys.argv[1]).file_reader())
