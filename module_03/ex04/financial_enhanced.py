#!/usr/bin/env python3
import cProfile
import pstats

from bs4 import BeautifulSoup
# import requests
import httpx
import sys
import os
from time import sleep


def main():
	if len(sys.argv) != 3:
		raise AttributeError(
			f"Wrong number of arguments.\n"
			f"Usage: {os.path.basename(__file__)} 'ticker_symbol' 'table_ﬁeld'\n"
			f"Example: {os.path.basename(__file__)} MSFT 'Total Revenue'")
	ticker, field = sys.argv[1], sys.argv[2]
	url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
	# response = requests.get(url, headers={'User-Agent': 'Noname'})
	response = httpx.get(url)
	# if not response.ok or response.url != url:
	if response.status_code != 200:
		raise ConnectionError("Connection error to url")
	soup = BeautifulSoup(response.text, 'html.parser')
	values = soup.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
	result = []
	for val in values:
		if val.span.text == field:
			result.append(val.span.text)
			nums1 = val.find_all('div', class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')
			nums2 = val.find_all('div', class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)')
			for i, j in enumerate(nums2):
				nums1.insert(2 * i + 1, j)
			for num in nums1:
				result.append(num.text)
	if not result:
		raise ValueError(f"The field '{field}' does not exist in '{ticker}'")
	# sleep(5)
	return tuple(result)


if __name__ == '__main__':
	# for proﬁling-http.txt and for proﬁling-ncalls.txt
	# print(main())

	# for pstats-cumulative.txt
	pr = cProfile.Profile()
	pr.enable()
	print(main())
	pr.disable()
	sys.stdout = open('pstats-cumulative.txt', 'w')
	pstats.Stats(pr).sort_stats(pstats.SortKey.CUMULATIVE).print_stats(5)


# python3 -m cProfile -s tottime  financial_enhanced.py MSFT 'Total Revenue' > profiling-http.txt
# python3 -m cProfile -s ncalls  financial.py MSFT 'Total Revenue' > proﬁling-ncalls.txt
# ./financial_enhanced.py MSFT "Total Revenue"

# python3 -m cProfile -s calls -o 111.temp  financial_enhanced.py MSFT 'Total Revenue'
# python3 -m pstats 111.temp
# sort cumulative
# stats 5