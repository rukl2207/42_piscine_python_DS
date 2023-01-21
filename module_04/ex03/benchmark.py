#!/usr/bin/env python3

import timeit
import sys
from functools import reduce


def loop_approach(num: int):
	total = 0
	for i in range(num + 1):
		total += i*i
	return total


def reduce_approach(num: int):
	total = reduce(lambda x, y: x + y*y, range(num + 1))
	return total


def compare_time(func_name: str, executions: str, number: str):
	try:
		executions = int(executions)
		number = int(number)
	except ValueError as err:
		print("Invalid arguments: Incorrect number of calls or number for the sum.", err)
		return
	if number < 0 or executions < 0:
		print("Invalid arguments: Incorrect number of calls or number for the sum. They must be positive.")
		return

	func = {
		"loop": loop_approach,
		"reduce": reduce_approach,
	}
	if func_name not in func:
		print("Invalid arguments: Incorrect function name.")
		return

	print(timeit.timeit(lambda: func[func_name](number), number=executions))
	# print(func[func_name](number))


if __name__ == '__main__':
	if len(sys.argv) == 4:
		compare_time(sys.argv[1], sys.argv[2], sys.argv[3])
	else:
		print("Wrong counts of argument.")
