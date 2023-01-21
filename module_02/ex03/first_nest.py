import sys
import os


class Research:
    class Calculations:
        def counts(self, data: [[int]]):
            heads, tails = tuple(map(sum, zip(*data)))
            return heads, tails

        def fractions(self, heads: int, tails: int):
            return (heads / (heads + tails) * 100), (tails / (heads + tails) * 100)

    def __init__(self, filename: str):
        self.filename = filename
        self.data = None

    def file_reader(self, has_header=True) -> [[int]]:
        if not os.access(self.filename, os.R_OK):
            raise FileNotFoundError("The file does not exist or cannot be read.")
        with open(self.filename, 'r') as in_file:
            self.data = in_file.read()
            tpl = tuple(self.data.split('\n'))
            result = []
            correct_data_row = {'0', '1'}
            header = tuple(map(str.strip, tpl[0].split(',')))
            if len(header) != 2:
                raise ValueError("The correct ﬁle contains a header with two strings delimited by a comma.")
            if set(header) == correct_data_row:
                has_header = False
            else:
                tpl = tpl[1:]
            if has_header and len(tpl) < 1:
                raise ValueError("The correct file must contain a header and data.")
            if not has_header and len(tpl) < 1:
                raise ValueError("The correct file must contain data.")
            for i, value in enumerate(tpl):
                row = tuple(map(str.strip, value.split(',')))
                if not (len(row) == 2 and set(row) == correct_data_row):
                    raise ValueError(
                        f"Error in line {i + 1}. "
                        f"The line must contain either 0 or 1 and never both of them delimited by a comma.")
                result.append(list(map(int, row)))
            return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise AttributeError(f"Error: Wrong number of arguments.\n"
                             f"Usage: python3 {os.path.basename(__file__)} <path_to_data.csv>")
    research = Research(sys.argv[1])
    reader = research.file_reader()
    print(reader)
    calculations = research.Calculations()
    heads_count, tails_count = calculations.counts(reader)
    print(heads_count, tails_count)
    heads_fraction, tails_fraction = calculations.fractions(heads_count, tails_count)
    print(heads_fraction, tails_fraction)
