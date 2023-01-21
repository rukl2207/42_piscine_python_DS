import os
from random import randint


class Research:
    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads, tails = tuple(map(sum, zip(*self.data)))
            return heads, tails

        def fractions(self, heads: int, tails: int):
            return (heads / (heads + tails) * 100), (tails / (heads + tails) * 100)

    class Analytics(Calculations):
        def predict_random(self, numb_predictions: int) -> [[int]]:
            result = []
            for i in range(numb_predictions):
                x = randint(0, 1)
                result.append([x, 1 - x])
            return result

        def predict_last(self):
            return self.data[-1]

        def save_report_to_file(self, data, filename, file_extension):
            with open('.'.join((filename, file_extension)), 'w') as out_file:
                out_file.write(data)

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
