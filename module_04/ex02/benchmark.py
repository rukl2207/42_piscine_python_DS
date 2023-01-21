#!/usr/bin/env python3

import timeit
import sys


def loop_approach(emails: list):
	new_emails = []
	for email in emails:
		if email.endswith('@gmail.com'):
			new_emails.append(email)
	# return new_emails


def comprehension_approach(emails: list):
	new_emails = [email for email in emails if email.endswith('@gmail.com')]
	# return new_emails


def map_approach(emails: list):
	new_emails = map(lambda email: email if email.endswith('@gmail.com') else None, emails)
	# return list(new_emails)


def filter_approach(emails: list):
	new_emails = filter(lambda email: email.endswith('@gmail.com'), emails)
	# return list(new_emails)


def compare_time(func_name: str, executions: str):
	try:
		executions = int(executions)
	except ValueError as err:
		print("Invalid arguments: Incorrect number of calls.", err)
		return

	func = {
		"loop": loop_approach,
		"list_comprehension": comprehension_approach,
		"map": map_approach,
		"filter": filter_approach,
	}
	if func_name not in func:
		print("Invalid arguments: Incorrect function name.")
		return

	emails = [
		'john@gmail.com',
		'james@gmail.com',
		'alice@yahoo.com',
		'anna@live.com',
		'philipp@gmail.com'
	] * 5
	print(timeit.timeit(lambda: func[func_name](emails), number=executions))


if __name__ == '__main__':
	if len(sys.argv) == 3:
		compare_time(sys.argv[1], sys.argv[2])
	# else:
	# 	print("Wrong counts of argument.")
