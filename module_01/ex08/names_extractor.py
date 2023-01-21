import sys


def name_extractor():
    if len(sys.argv) != 2:
        print("Error: Wrong number of arguments. Usage: python3 names_extractor.py <path_to_input_file>")
        return
    with open(sys.argv[1], 'r') as in_file, open('employees.tsv', 'w') as out_file:
        out_file.write("Name\tSurname\tEmail\n")
        for line in in_file:
            if "@" not in line or "." not in line.split('@')[0]:
                continue
            lst = line.split('@')
            if not lst[1].rstrip('\n'):
                continue
            name, surname = lst[0].split('.')
            if not name or not surname:
                continue
            out_file.write(f"{name.capitalize()}\t{surname.capitalize()}\t{line}")


if __name__ == '__main__':
    name_extractor()
