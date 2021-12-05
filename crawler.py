# import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver


class Crawler:
    def __init__(self):
        self.stats = []

        self.urls = []
        self.name = []
        self.age = [None] * 200
        self.source_of_wealth = [None] * 200
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
        driver.find_element_by_id('truste-consent-button').click()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        soup = BeautifulSoup(driver.page_source, 'lxml')
        # self.driver.implicitly_wait(5)
        table = soup.find('div', attrs={'class': 'table'})

        # rank = []
        # netWorth = []
        # age = []
        # source = []
        # category = []

        for group in table.find_all('div', attrs={'class': 'table-row-group'}):
            for row in group.find_all('div', attrs={'class': 'table-row'}):
                self.urls.append("https://www.forbes.com/profile/" + row.get('id') + "/?list=billionaires")
                # rank.append(row.find('div', attrs={'class': 'rank'}).get_text())
                self.name.append(row.find('div', attrs={'class': 'personName'}).get_text())
                # netWorth.append(row.find('div', attrs={'class': 'netWorth'}).get_text())
                # age.append(row.find('div', attrs={'class': 'age'}).get_text())
                # source.append(row.find('div', attrs={'class': 'source'}).get_text())
                # category.append(row.find('div', attrs={'class': 'category'}).get_text())

        driver.quit()
        self.extractFromProfiles()

    def extractStats(self, index):
        new_driver = webdriver.Chrome(executable_path=r"SeleniumDrivers\chromedriver.exe")

        new_driver.get(self.urls[index])
        new_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        soup = BeautifulSoup(new_driver.page_source, 'lxml')
        block = soup.find('div', attrs={'class': 'listuser-content__block person-stats'})
        for item in block.find_all('div', attrs={'class': 'listuser-block__item'}):
            if item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Age':
                self.age[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Source of Wealth':
                self.source_of_wealth[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Self-Made Score':
                self.self_made_score[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Philanthropy Score':
                self.philanthropy_score[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Residence':
                self.residence[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Citizenship':
                self.citizenship[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Marital Status':
                self.marital_status[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Children':
                self.children[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
            elif item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Education':
                self.education[index] = (item.find('span', attrs={'class': 'profile-stats__text'}).get_text())

    def extractFromProfiles(self):

        # for i in range(2):
        #     self.extractStats(i)
        self.set_up_threads()

        self.stats.extend(
            [self.name, self.age, self.source_of_wealth, self.self_made_score, self.philanthropy_score, self.residence,
             self.citizenship, self.marital_status, self.children, self.education])

    def set_up_threads(self):
        index = list(range(0, 200))
        with ThreadPoolExecutor(max_workers=5) as executor:
            return executor.map(self.extractStats, index, timeout=60)

    def exportExtractedStats(self):
        for field in self.stats:
            print(field)

        return self.stats
