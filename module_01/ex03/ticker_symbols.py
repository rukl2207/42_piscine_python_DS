import sys


def get_key(dct: dict, value: str) -> str:
	for k, v in dct.items():
		if v == value:
			return k


def ticker_symbols():
	companies = {
		'Apple': 'AAPL',
		'Microsoft': 'MSFT',
		'Netflix': 'NFLX',
		'Tesla': 'TSLA',
		'Nokia': 'NOK'
	}

	stocks = {
		'AAPL': 287.73,
		'MSFT': 173.79,
		'NFLX': 416.90,
		'TSLA': 724.88,
		'NOK': 3.37
	}

	if len(sys.argv) == 2:
		ticker = sys.argv[1].upper()
		if ticker in stocks.keys() and ticker in companies.values():
			print(get_key(companies, ticker), stocks[ticker])
		else:
			print("Unknown ticker")


if __name__ == '__main__':
	ticker_symbols()
