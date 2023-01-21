#!/usr/bin/env python3

import os


def main():
	try:
		if not os.environ['VIRTUAL_ENV'].endswith('scornhol'):
			raise KeyError
		os.system("pip install beautifulsoup4 pytest > /dev/null ; pip freeze > requirements.txt; cat requirements.txt")
	except KeyError as err:
		print("KeyError: Wrong enviroment.", err)


if __name__ == '__main__':
	main()

# python3 -m virtualenv scornhol
# source scornhol/bin/activate
# pip freeze
# deactivate
