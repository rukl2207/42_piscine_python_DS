#!/usr/bin/env python3


import timeit
import random
from collections import Counter


def list_to_dict(lst: list):
	dct = {}
	for elem in lst:
		if elem in dct:
			dct[elem] += 1
		else:
			dct[elem] = 1
	return dct


def most_common(lst: list, num: int):
	dct = list_to_dict(lst)
	return sorted(dct.items(), key=lambda item: item[1], reverse=True)[:num]


def main():
	random_list = [random.randint(0, 100) for _ in range(1_000_000)]
	# z = [1, 1, 2, 1, 3, 4, 4, 3, 2, 1, 5]
	print(f"my function: {timeit.timeit(lambda: list_to_dict(random_list), number=1)}")
	print(f"Counter: {timeit.timeit(lambda: Counter(random_list), number=1)}")
	print(f"my top: {timeit.timeit(lambda: most_common(random_list, 10), number=1)}")
	print(f"Counter's top: {timeit.timeit(lambda: Counter(random_list).most_common(10), number=1)}")
	# print(list_to_dict(random_list) == Counter(random_list))
	# print(most_common(random_list, 10) == Counter(random_list).most_common(10))
	# print(list_to_dict(random_list))
	# print(list_to_dict(most_common(random_list, 10)))


if __name__ == '__main__':
	main()
