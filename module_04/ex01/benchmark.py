#!/usr/bin/env python3

import timeit


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


def compare_time():
	emails = [
		'john@gmail.com',
		'james@gmail.com',
		'alice@yahoo.com',
		'anna@live.com',
		'philipp@gmail.com'
	] * 5
	executions = 900_000
	# executions = 90_000_000
	result = [
		("it is better to use a loop", timeit.timeit(lambda: loop_approach(emails), number=executions)),
		("it is better to use a list comprehension", timeit.timeit(lambda: comprehension_approach(emails), number=executions)),
		("it is better to use a map", timeit.timeit(lambda: map_approach(emails), number=executions))
	]
	result.sort(key=lambda x: x[1])
	print(result[0][0])
	print(f"{result[0][1]} vs {result[1][1]} vs {result[2][1]}")
	# print(loop_approach(emails))
	# print(comprehension_approach(emails))
	# print(map_approach(emails))


if __name__ == '__main__':
	compare_time()
