import sys


def get_key(dct: dict, value: str) -> str:
    for k, v in dct.items():
        if v == value:
            return k
    return ""


def all_stocks():
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
        parameters = sys.argv[1].split(',')
        for index, elem in enumerate(parameters):
            parameters[index] = elem.strip()
            if not parameters[index]:
                print()
                return
        for elem in parameters:
            ticker = companies.get(elem.capitalize())
            if ticker and ticker in stocks.keys():
                print(f"{elem.capitalize()} stock price is {stocks[ticker]}")
                continue
            company = get_key(companies, elem.upper())
            if company:
                print(f"{elem.upper()} is a ticker symbol for {company}")
                continue
            print(f"{elem} is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    all_stocks()
