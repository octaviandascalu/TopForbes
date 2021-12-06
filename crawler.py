# import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By


class Crawler:
    def __init__(self):
        self.urls = []
        self.rank = []
        self.name = []
        self.netWorth = []
        self.age = [None] * 200
        self.source_of_wealth = [None] * 200
        self.category = []
        self.self_made_score = [None] * 200
        self.philanthropy_score = [None] * 200
        self.residence = [None] * 200
        self.citizenship = [None] * 200
        self.marital_status = [None] * 200
        self.children = [None] * 200
        self.education = [None] * 200

    def start(self):
        driver = webdriver.Chrome(executable_path=r"SeleniumDrivers\chromedriver.exe")
        url = 'https://www.forbes.com/billionaires/'
        driver.get(url)
        driver.find_element(By.ID, 'truste-consent-button').click()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        soup = BeautifulSoup(driver.page_source, 'lxml')
        driver.quit()
        table = soup.find('div', attrs={'class': 'table'})

        # age = []
        # source = []

        for group in table.find_all('div', attrs={'class': 'table-row-group'}):
            for row in group.find_all('div', attrs={'class': 'table-row'}):
                self.urls.append("https://www.forbes.com/profile/" + row.get('id') + "/?list=billionaires")
                self.rank.append(int(row.find('div', attrs={'class': 'rank'}).get_text()[:-1]))
                self.name.append(row.find('div', attrs={'class': 'personName'}).get_text())
                self.netWorth.append(row.find('div', attrs={'class': 'netWorth'}).get_text())
                # age.append(row.find('div', attrs={'class': 'age'}).get_text())
                # source.append(row.find('div', attrs={'class': 'source'}).get_text())
                self.category.append(row.find('div', attrs={'class': 'category'}).get_text())
        self.extractFromProfiles()

    def extractFromProfiles(self):
        index = list(range(0, 200))
        with ThreadPoolExecutor(max_workers=5) as executor:
            return executor.map(self.extractStats, index, timeout=60)

    def extractStats(self, index):
        new_driver = webdriver.Chrome(executable_path=r"SeleniumDrivers\chromedriver.exe")
        new_driver.get(self.urls[index])
        new_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        soup = BeautifulSoup(new_driver.page_source, 'lxml')
        block = soup.find('div', attrs={'class': 'listuser-content__block person-stats'})
        for item in block.find_all('div', attrs={'class': 'listuser-block__item'}):
            if item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Age':
                self.age[index] = int((item.find('span', attrs={'class': 'profile-stats__text'}).get_text()))
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Source of Wealth':
                self.source_of_wealth[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Self-Made Score':
                self.self_made_score[index] = int(
                    (item.find('span', attrs={'class': 'profile-stats__text'}).get_text()))
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Philanthropy Score':
                self.philanthropy_score[index] = int(
                    (item.find('span', attrs={'class': 'profile-stats__text'}).get_text()))
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Residence':
                self.residence[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Citizenship':
                self.citizenship[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Marital Status':
                self.marital_status[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Children':
                self.children[index] = int((item.find('span', attrs={'class': 'profile-stats__text'}).get_text()))
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Education':
                self.education[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())

    def exportExtractedStats(self):
        stats = []
        stats.extend(
            [self.rank, self.name, self.netWorth, self.age, self.source_of_wealth, self.category, self.self_made_score,
             self.philanthropy_score, self.residence, self.citizenship, self.marital_status, self.children,
             self.education])
        # for field in stats:
        #     print(field)

        return stats
