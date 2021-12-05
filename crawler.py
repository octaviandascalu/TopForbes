import time
from bs4 import BeautifulSoup

from selenium import webdriver


class Crawler:
    def __init__(self):
        self.stats = []
        self.driver = webdriver.Chrome(executable_path=r"SeleniumDrivers\chromedriver.exe")
        self.url = 'https://www.forbes.com/billionaires/'

    def start(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('truste-consent-button').click()
        self.driver.implicitly_wait(10)

        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
        self.driver.implicitly_wait(5)
        urls, name = self.extractUrlsFromTable()
        self.extractFromProfile(urls, name)

    def extractUrlsFromTable(self):
        table = self.soup.find('div', attrs={'class': 'table'})

        # data = []

        urls = []
        # rank = []
        name = []
        # netWorth = []
        # age = []
        # source = []
        # category = []

        for group in table.find_all('div', attrs={'class': 'table-row-group'}):
            for row in group.find_all('div', attrs={'class': 'table-row'}):
                urls.append("https://www.forbes.com/profile/" + row.get('id') + "/?list=billionaires")
                # rank.append(row.find('div', attrs={'class': 'rank'}).get_text())
                name.append(row.find('div', attrs={'class': 'personName'}).get_text())
                # netWorth.append(row.find('div', attrs={'class': 'netWorth'}).get_text())
                # age.append(row.find('div', attrs={'class': 'age'}).get_text())
                # source.append(row.find('div', attrs={'class': 'source'}).get_text())
                # category.append(row.find('div', attrs={'class': 'category'}).get_text())

        # data.extend([urls, rank, name, netWorth, age, source, category])
        # for field in data:
        #     print(field)
        return urls, name

    def extractFromProfile(self, urls, name):

        age = [None] * 200
        source_of_wealth = [None] * 200
        self_made_score = [None] * 200
        philanthropy_score = [None] * 200
        residence = [None] * 200
        citizenship = [None] * 200
        marital_status = [None] * 200
        children = [None] * 200
        education = [None] * 200

        for i in range(200):
            self.driver.get(urls[i])
            # time.sleep(1)
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            block = soup.find('div', attrs={'class': 'listuser-content__block person-stats'})
            for item in block.find_all('div', attrs={'class': 'listuser-block__item'}):
                if item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Age':
                    age[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Source of Wealth':
                    source_of_wealth[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Self-Made Score':
                    self_made_score[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Philanthropy Score':
                    philanthropy_score[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Residence':
                    residence[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Citizenship':
                    citizenship[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Marital Status':
                    marital_status[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Children':
                    children[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Education':
                    education[i] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())

        self.stats.extend(
            [name, age, source_of_wealth, self_made_score, philanthropy_score, residence, citizenship, marital_status,
             children, education])

    def exportExtractedStats(self):
        # for field in self.stats:
        #     print(field)

        return self.stats

    def stop(self):
        self.driver.quit()
