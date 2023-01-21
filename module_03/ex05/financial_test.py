#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
import os
import pytest

# returned tuple in test_main_ok may change when checking. be careful with parameter 'expect'


@pytest.mark.parametrize(
	'arg_1, arg_2, expect',
	[
		['MSFT', 'Total Revenue', ('Total Revenue', '198,270,000', '198,270,000', '168,088,000', '143,015,000', '125,843,000')],
		['MSFT', 'EBITDA', ('EBITDA', '100,239,000', '-', '-', '-', '-')],
		['MSFT', 'Tax Rate for Calcs', ('Tax Rate for Calcs', '0', '0', '0', '0', '0')],
		['GOOG', 'Gross Profit', ('Gross Profit', '157,827,000', '146,698,000', '97,795,000', '89,961,000', '77,270,000')],
		['GOOG', 'Basic EPS', ('Basic EPS', '-', '5.69', '2.96', '2.48', '2.21')],
	]
)
def test_main_ok(arg_1, arg_2, expect):
	result = main(arg_1, arg_2)
	assert expect == result and type(result) == tuple


def test_main_connection_negative_1():
	with pytest.raises(ConnectionError) as excinfo:
		main("wrong_ticker", 'Total Revenue')
	assert str(excinfo.value) == "Connection error to url"


def test_main_connection_negative_2():
	with pytest.raises(ConnectionError, match="Connection error to url"):
		main("MSFTr", 'Total Revenue')


def test_main_wrong_field_negative_1():
	with pytest.raises(ValueError) as excinfo:
		arg_1 = 'MSFT'
		arg_2 = 'wrong_field'
		main(arg_1, arg_2)
	assert str(excinfo.value) == f"The field '{arg_2}' does not exist in '{arg_1}'"


def test_main_wrong_field_negative_2():
	with pytest.raises(ValueError) as excinfo:
		arg_1 = 'MSFT'
		arg_2 = 'Total RevenueW'
		main(arg_1, arg_2)
	assert str(excinfo.value) == f"The field '{arg_2}' does not exist in '{arg_1}'"


def main(ticker: str, field: str) -> tuple:
	url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
	response = requests.get(url, headers={'User-Agent': 'Noname'})
	if not response.ok or response.url != url:
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
	return tuple(result)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		raise AttributeError(
			f"Wrong number of arguments.\n"
			f"Usage: {os.path.basename(__file__)} 'ticker_symbol' 'table_ﬁeld'\n"
			f"Example: {os.path.basename(__file__)} MSFT 'Total Revenue'")
	print(main(sys.argv[1], sys.argv[2]))

# cd
