import requests
from bs4 import BeautifulSoup


class Notice:
    def __init__(self, title, date, view):
        self.title = title
        self.date = date
        self.view = view

    def __repr__(self):
        return f'{self.title}'


url = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

tr_list = soup.select('tbody > tr')

notice_list = list()
for tr in tr_list:
    title = tr.select_one('td.tleft > a').get_text(strip=True)
    date = tr.select('td')[1].get_text(strip=True)
    view = tr.select('td')[2].get_text(strip=True)
    new_notice = Notice(title, date, view)
    notice_list.append(new_notice)


print(notice_list)
