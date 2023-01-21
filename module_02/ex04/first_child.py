import sys
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

    def __init__(self, filename: str):
        self.filename = filename
        self.data = None

    def file_reader(self, has_header=True) -> [[int]]:
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
                             f"Usage: python3 {sys.argv[0]} <path_to_data.csv>")
    research = Research(sys.argv[1])
    reader = research.file_reader()
    print(reader)

    # calculations = research.Calculations(reader)
    # heads_count, tails_count = calculations.counts()
    # print(heads_count, tails_count)
    # heads_fraction, tails_fraction = calculations.fractions(heads_count, tails_count)
    # print(heads_fraction, tails_fraction)

    heads_count_, tails_count_ = research.Analytics(reader).counts()
    print(heads_count_, tails_count_)
    heads_fraction_, tails_fraction_ = research.Analytics(reader).fractions(heads_count_, tails_count_)
    print(heads_fraction_, tails_fraction_)

    predict_random_lst = research.Analytics(reader).predict_random(3)
    print(predict_random_lst)
    predict_last_lst = research.Analytics(reader).predict_last()
    print(predict_last_lst)
