#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
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
    response = requests.get(url, headers={'User-Agent': 'Noname'})
    if not response.ok or response.url != url:
        raise ConnectionError("Connection error to url")
    soup = BeautifulSoup(response.text, 'html.parser')
    values = soup.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
    result = []
    for val in values:
        if val.span.text == field:
            result.append(val.span.text)
            nums1 = val.find_all('div',
                                 class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')
            nums2 = val.find_all('div',
                                 class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)')
            for i, j in enumerate(nums2):
                nums1.insert(2 * i + 1, j)
            for num in nums1:
                result.append(num.text)
    if not result:
        raise ValueError(f"The field '{field}' does not exist in '{ticker}'")
    return tuple(result)


if __name__ == '__main__':
    sleep(5)
    print(main())
