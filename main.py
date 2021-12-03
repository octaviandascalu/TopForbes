import time
from bs4 import BeautifulSoup

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"SeleniumDrivers\chromedriver.exe")
driver.implicitly_wait(10)
url = 'https://www.forbes.com/billionaires/'

driver.get(url)
driver.find_element_by_id('truste-consent-button').click()

# time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'lxml')

table = soup.find('div', attrs={'class': 'table'})

data = []

urls = []
rank = []
name = []
netWorth = []
age = []
source = []
category = []

for group in table.find_all('div', attrs={'class': 'table-row-group'}):
    for row in group.find_all('div', attrs={'class': 'table-row'}):
        urls.append("https://www.forbes.com/profile/" + row.get('id') + "/?list=billionaires")
        rank.append(row.find('div', attrs={'class': 'rank'}).get_text())
        name.append(row.find('div', attrs={'class': 'personName'}).get_text())
        netWorth.append(row.find('div', attrs={'class': 'netWorth'}).get_text())
        age.append(row.find('div', attrs={'class': 'age'}).get_text())
        source.append(row.find('div', attrs={'class': 'source'}).get_text())
        category.append(row.find('div', attrs={'class': 'category'}).get_text())

data.extend([urls, rank, name, netWorth, age, source, category])

for field in data:
    print(field)

# for i in range(1):
# driver.get(urls[i])
#     #time.sleep(1)

driver.quit()
