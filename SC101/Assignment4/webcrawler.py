"""
File: webcrawler.py
Name: Mike
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        datas = soup.tbody.find_all("tr")
        male_number = 0
        female_number = 0
        for data in datas[:len(datas)-1]:
            td = data.find_all('td')
            # the third and the last will be the data that need to be add up.
            male_number += int(td[2].text.replace(',', ''))
            female_number += int(td[4].text.replace(',', ''))
        print('Male Number:', male_number)
        print('Female number:', female_number)


if __name__ == '__main__':
    main()
