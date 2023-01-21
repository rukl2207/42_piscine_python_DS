import sys


def letter_starter():
    if len(sys.argv) != 2:
        print("Error: Wrong number of arguments. Usage: python3 letter_starter.py <email>")
        return
    with open('employees.tsv', 'r') as in_file:
        lines = in_file.readlines()
        for line in lines:
            line = line.split('\t')
            if line[2].rstrip('\n') == sys.argv[1]:
                print(
                    f"Dear {line[0]}, welcome to our team. We are sure that it will be a pleasure to work with you."
                    f" That’s a precondition for the professionals that our company hires.")
                break
        else:
            print(f"The email {sys.argv[1]} not found in the mailing")


if __name__ == '__main__':
    letter_starter()
