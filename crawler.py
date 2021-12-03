from bs4 import BeautifulSoup

from selenium import webdriver


class Crawler:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"SeleniumDrivers\chromedriver.exe")
        self.driver.implicitly_wait(1)
        self.url = 'https://www.forbes.com/billionaires/'

    def start(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('truste-consent-button').click()

        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
        urls = self.extractUrlsFromTable()
        self.extractFromProfile(urls)

    def extractUrlsFromTable(self):
        table = self.soup.find('div', attrs={'class': 'table'})

        # data = []

        urls = []
        # rank = []
        # name = []
        # netWorth = []
        # age = []
        # source = []
        # category = []

        for group in table.find_all('div', attrs={'class': 'table-row-group'}):
            for row in group.find_all('div', attrs={'class': 'table-row'}):
                urls.append("https://www.forbes.com/profile/" + row.get('id') + "/?list=billionaires")
                # rank.append(row.find('div', attrs={'class': 'rank'}).get_text())
                # name.append(row.find('div', attrs={'class': 'personName'}).get_text())
                # netWorth.append(row.find('div', attrs={'class': 'netWorth'}).get_text())
                # age.append(row.find('div', attrs={'class': 'age'}).get_text())
                # source.append(row.find('div', attrs={'class': 'source'}).get_text())
                # category.append(row.find('div', attrs={'class': 'category'}).get_text())

        # data.extend([urls, rank, name, netWorth, age, source, category])
        # for field in data:
        #     print(field)
        return urls

    def extractFromProfile(self, urls):
        stats = []
        age = []
        source_of_wealth = []
        self_made_score = []
        philanthropy_score = []
        residence = []
        citizenship = []
        marital_status = []
        children = []
        education = []

        for i in range(1):
            self.driver.get(urls[i])
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            block = soup.find('div', attrs={'class': 'listuser-content__block person-stats'})
            for item in block.find_all('div', attrs={'class': 'listuser-block__item'}):
                if item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Age':
                    age.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Source of Wealth':
                    source_of_wealth.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Self-Made Score':
                    self_made_score.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Philanthropy Score':
                    philanthropy_score.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Residence':
                    residence.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Citizenship':
                    citizenship.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Marital Status':
                    marital_status.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Children':
                    children.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
                elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Education':
                    education.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())

        stats.extend(
            [age, source_of_wealth, self_made_score, philanthropy_score, residence, citizenship, marital_status,
             children, education])

        for field in stats:
            print(field)

    def stop(self):
        self.driver.quit()
