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

# for field in data:
#     print(field)

stats = []
age = []
source_of_wealth = []
self_made_score = []
philantropy_score = []
residence = []
citizenship = []
marital_status = []
children = []
education = []

for i in range(200):
    driver.get(urls[i])
    soup = BeautifulSoup(driver.page_source, 'lxml')
    block = soup.find('div', attrs={'class': 'listuser-content__block person-stats'})
    # print(block)
    for item in block.find_all('div', attrs={'class': 'listuser-block__item'}):
        if(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Age'):
            age.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Source of Wealth'):
            source_of_wealth.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Self-Made Score'):
            self_made_score.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Philanthropy Score'):
            philantropy_score.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Residence'):
            residence.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Citizenship'):
            citizenship.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Marital Status'):
            marital_status.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Children'):
            children.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
        elif(item.find('span', attrs={'class': 'profile-stats__title'}).get_text() == 'Education'):
            education.append(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())

        # print(item.find('span', attrs={'class': 'profile-stats__title'}).get_text())
        # print(item.find('span', attrs={'class': 'profile-stats__text'}).get_text())
    # time.sleep(1)

stats.extend([age, source_of_wealth, self_made_score, philantropy_score, residence, citizenship, marital_status, children, education])

for field in stats:
    print(field)

# div class="listuser-content__block person-stats"
# div class="listuser-block__item"
# span class="profile-stats__text"

driver.quit()

# ['57', '50', '72', '66', '37', '91', '77', '48', '48', '64', '85', '68', '67', '65', '50', '81', '72', '73', '77', '79', '41', '51', '59', '59', '83', '57', '86', '59', '64', '56', '72', '85', '64', '51', '76', '79', '82', '37', '57', '73', '70', '93', '56', '50', '64', '93', '82', '86', '40', '56', '52', '63', '59', '60', '77', '65', '84', '65', '42', '68', '86', '76', '88', '77', '71', '66', '83', '68', '67', '90', '76', '49', '78', '51', '51', '47', '69', '74', '94', '55', '70', '54', '74', '59', '80', '60', '72', '82', '58', '60', '55', '92', '51', '58', '66', '63', '70', '68', '43', '57', '54', '82', '75', '56', '49', '37', '39', '92', '37', '68', '82', '86', '67', '66', '55', '65', '53', '45', '64', '62', '85', '55', '83', '35', '57', '57', '89', '71', '57', '51', '67', '92', '53', '92', '39', '55', '64', '56', '42', '81', '64', '37', '64', '41', '66', '61', '69', '40', '70', '81', '77', '53', '41', '49', '53', '55', '46', '53', '54', '66', '54', '48', '80', '98', '45', '79', '57', '49', '38', '70', '40', '43', '55', '70', '92', '63', '33', '58', '58', '54', '57', '57', '64', '71', '56', '76', '73', '88', '65', '71', '31', '88']
# ['Amazon, Self Made', 'Tesla, SpaceX, Self Made', 'LVMH', 'Microsoft, Self Made', 'Facebook, Self Made', 'Berkshire Hathaway, Self Made', 'software, Self Made', 'Google, Self Made', 'Google, Self Made', 'diversified', 'Zara, Self Made', "L'Oréal", 'beverages, pharmaceuticals, Self Made', 'Microsoft, Self Made', 'internet media, Self Made', 'telecom, Self Made', 'Walmart', 'Walmart', 'Walmart', 'Bloomberg LP, Self Made', 'e-commerce, Self Made', 'Amazon', 'Quicken Loans, Self Made', 'infrastructure, commodities, Self Made', 'Nike, Self Made', 'e-commerce, Self Made', 'Koch Industries', 'Koch Industries', 'internet, telecom, Self Made', 'Dell computers, Self Made', 'fashion retail, Self Made', 'luxury goods, Self Made', 'media', 'supermarkets', 'package delivery, Self Made', 'casinos', 'home appliances, Self Made', 'retail', 'TikTok, Self Made', 'Nutella, chocolates', 'Chanel', 'Chanel', 'diversified, Self Made', 'pig breeding, Self Made', 'online games, Self Made', 'music, chemicals, Self Made', 'real estate, Self Made', 'candy, pet food', 'candy, pet food', 'real estate', 'steel, investments, Self Made', 'batteries, Self Made', 'real estate, Self Made', 'BMW, pharmaceuticals', 'metals, Self Made', 'Red Bull, Self Made', 'soy sauce, Self Made', 'shipping', 'steel, transport, Self Made', 'e-commerce, Self Made', 'mining', 'eyeglasses, Self Made', 'sensors, Self Made', 'Estee Lauder', 'discount brokerage, Self Made', 'oil, Self Made', 'gas, chemicals, Self Made', 'hedge funds, Self Made', 'vaccines, Self Made', 'mining', 'newspapers, TV network', 'software services, Self Made', 'internet media, Self Made', 'mining', 'smartphones, Self Made', 'restaurants, Self Made', 'e-commerce, Self Made', 'oil, gas, Self Made', 'investments, Self Made', 'paints, Self Made', 'BMW', 'medical devices, Self Made', 'eBay, PayPal, Self Made', 'H&M', 'money management', 'banking, tobacco', 'mining, Self Made', 'hedge funds, Self Made', 'banking, tobacco', 'automobiles, Self Made', 'pharmaceuticals, Self Made', 'medical devices, Self Made', 'casinos/hotels, Self Made', 'cheese', 'Apple, Disney', 'Google, Self Made', 'pharmaceuticals, Self Made', "Aldi, Trader Joe's", 'steel, telecom, investments, Self Made', 'wireless networking gear, Self Made', 'real estate, Self Made', 'petrochemicals, Self Made', 'diversified', 'real estate', 'hospitals, Self Made', 'coal, fertilizers, Self Made', 'Facebook, Self Made', 'video streaming, Self Made', 'media', 'finance, telecommunications, Self Made', 'food', 'messaging app, Self Made', 'chemicals, Self Made', 'beer, Self Made', 'fasteners, Self Made', 'Heineken', 'retail, investments, Self Made', 'batteries, automobiles, Self Made', 'hedge funds, Self Made', 'hedge funds, Self Made', 'e-cigarettes, Self Made', 'used cars, Self Made', 'banking, Self Made', 'investments, Self Made', 'investments, Self Made', 'hospitals, Self Made', 'Walmart', 'oil, banking, telecom, Self Made', 'automobiles, Self Made', 'real estate services, Self Made', 'smartphone screens, Self Made', 'real estate, Self Made', 'diversified', 'steel', 'auto parts', 'Zoom Video Communications, Self Made', 'real estate, Self Made', 'real estate', 'internet search, Self Made', 'construction', 'Facebook, Self Made', 'steel, investments, Self Made', 'hedge funds, Self Made', 'video surveillance, Self Made', 'software, Self Made', 'home improvement stores, Self Made', 'biotech, Self Made', 'video streaming app, Self Made', 'construction equipment, Self Made', 'software, Self Made', 'packaging', 'packaging', 'packaging', 'Airbnb, Self Made', 'real estate, Self Made', 'business software, Self Made', 'alcohol, real estate, Self Made', 'online games, Self Made', 'real estate', 'education, Self Made', 'fashion retail', 'mining, copper products, Self Made', 'hydraulic machinery, Self Made', 'ecommerce, Self Made', 'hedge funds, Self Made', 'batteries, Self Made', 'retail, media', 'commodities', 'coal, Self Made', 'vaccines', 'palm oil, shipping, property, Self Made', 'supermarkets', 'Twitter, Square, Self Made', 'education, Self Made', 'textiles, apparel, Self Made', 'e-commerce, Self Made', 'Airbnb, Self Made', 'venture capital, Self Made', 'Airbnb, Self Made', 'gaming, Self Made', 'semiconductors, Self Made', 'agribusiness, Self Made', 'Intel, Self Made', 'trading, investments, Self Made', 'Snapchat, Self Made', 'telecom, Self Made', 'semiconductors, Self Made', 'real estate', 'pharmaceuticals, Self Made', 'e-commerce, Self Made', 'cement, sugar, Self Made', 'beer, Self Made', 'investments, Self Made', 'hospitals, Self Made', 'steel, Self Made', 'real estate, Self Made', 'oil, Self Made', 'real estate, shipping', 'Snapchat, Self Made', 'banking, Self Made']
# ['8', '8', '8', '8', '8', '9', '8', '9', '6', '1', '2', '4', '8', '3', '8', '8', '5', '1', '8', '2', '4', '9', '2', '2', '5', '10', '8', '5', '8', '8', '3', '8', '2', '6', '8', '8', '5', '8', '8', '9', '9', '7', '1', '8', '8', '8', '9', '8', '8', '3', '8', '8', '8', '8', '8', '8', '8', '8', '8']
# ['1', '1', '4', '2', '5', '1', '1', '1', '2', '2', '1', '1', '4', '2', '1', '2', '2', '2', '2', '2', '3', '1', '3', '1', '2', '3', '2', '3', '1', '2', '1', '3', '2', '2', '2', '1', '2', '1', '2', '3', '2', '1', '2', '2', '2', '2', '5', '1', '1', '1']
# ['Seattle, Washington', 'Austin, Texas', 'Paris, France', 'Medina, Washington', 'Palo Alto, California', 'Omaha, Nebraska', 'Lanai, Hawaii', 'Palo Alto, California', 'Los Altos, California', 'Mumbai, India', 'La Coruna, Spain', 'Paris, France', 'Hangzhou, China', 'Hunts Point, Washington', 'Shenzhen, China', 'Mexico City, Mexico', 'Fort Worth, Texas', 'Bentonville, Arkansas', 'Bentonville, Arkansas', 'New York, New York', 'Shanghai, China', 'Seattle, Washington', 'Franklin, Michigan', 'Ahmedabad, India', 'Hillsboro, Oregon', 'Hangzhou, China', 'Wichita, Kansas', 'New York, New York', 'Tokyo, Japan', 'Austin, Texas', 'Tokyo, Japan', 'Paris, France', 'Toronto, Canada', 'Germany', 'Shenzhen, China', 'Las Vegas, Nevada', 'Foshan, China', 'Neckarsulm, Germany', 'Beijing, China', 'Brussels, Belgium', 'New York, New York', 'New York, New York', 'Hong Kong', 'Nanyang, China', 'Hangzhou, China', 'London, United Kingdom', 'Hong Kong, Hong Kong', 'The Plains, Virginia', 'Jackson, Wyoming', 'Foshan, China', 'Moscow, Russia', 'Ningde, China', 'Shenzhen, China', 'Bad Homburg, Germany', 'Moscow, Russia', 'Fuschl am See, Austria', 'Foshan, China', 'Schindellegi, Switzerland', 'Moscow, Russia', 'Beijing, China', 'Mexico City, Mexico', 'Milan, Italy', 'Osaka, Japan', 'New York, New York', 'Palm Beach, Florida', 'Moscow, Russia', 'Moscow, Russia', 'East Setauket, New York', 'Chongqing, China', 'Perth, Australia', 'New York, New York', 'Delhi, India', 'Shenzhen, China', 'Santiago, Chile', 'Beijing, China', 'Singapore, Singapore', 'Beijing, China', 'Moscow, Russia', 'New York, New York', 'Singapore, Singapore', 'Frankfurt, Germany', 'Shenzhen, China', 'Honolulu, Hawaii', 'Stockholm, Sweden', 'Milton, Massachusetts', 'Kudus, Indonesia', 'Perth, Australia', 'Greenwich, Connecticut', 'Kudus, Indonesia', 'Hangzhou, China', 'Shanghai, China', 'Shenzhen, China', 'Hong Kong, Hong Kong', 'Laval, France', 'Palo Alto, California', 'Atherton, California', 'Lianyungang, China', 'Mulheim an der Ruhr, Germany', 'Moscow, Russia', 'San Jose, California', 'Beijing, China', 'Wujiang, China', 'Bangkok, Thailand', 'Hong Kong, Hong Kong', 'Changsha, China', 'Moscow, Russia', 'San Francisco, California', 'Beijing, China', 'New York, New York', 'Dubai, United Arab Emirates', 'London, United Kingdom', 'Zurich, Switzerland', 'Kuenzelsau, Germany', 'London, United Kingdom', 'Mumbai, India', 'Shenzhen, China', 'Greenwich, Connecticut', 'Chicago, Illinois', 'Shenzhen, China', 'Tempe, Arizona', 'Mumbai, India', 'Indian Creek, Florida', 'Moscow, Russia', 'Nashville, Tennessee', 'Jackson, Wyoming', 'London, United Kingdom', 'Baoding, China', 'Hong Kong, Hong Kong', 'Newport Beach, California', 'London, United Kingdom', 'London, United Kingdom', 'Herzogenaurach, Germany', 'Santa Clara, California', 'Beijing, China', 'Hong Kong, Hong Kong', 'Beijing, China', 'Mumbai, India', 'Singapore, Singapore', 'Moscow, Russia', 'Palm Beach, Florida', 'Hong Kong, Hong Kong', 'Sydney, Australia', 'Eau Claire, Wisconsin', 'Seoul, South Korea', 'Beijing, China', 'Changsha, China', 'Sydney, Australia', 'London, United Kingdom', 'Surrey, United Kingdom', 'Newmarket, United Kingdom', 'San Francisco, California', 'Hong Kong, Hong Kong', 'Incline Village, Nevada', 'Bangkok, Thailand', 'Seoul, South Korea', 'Singapore, Singapore', 'Beijing, China', 'Aarhus, Denmark', 'Shenzhen, China', 'Changzhou, China', 'Moscow region, Russia', 'Geneva, Switzerland', 'Ningde, China', 'Mexico City, Mexico', 'Mumbai, India', 'Yinchuan, China', 'Pune, India', 'Hong Kong, Hong Kong', 'Grand Rapids, Michigan', 'San Francisco, California', 'Tonghua, China', 'Ningbo, China', 'Beijing, China', 'San Francisco, California', 'Woodside, California', 'San Francisco, California', 'Singapore, Singapore', 'Ningbo, China', 'Chengdu, China', 'Woodside, California', 'Haverford, Pennsylvania', 'Venice, California', 'Zermatt, Switzerland', 'Los Altos, California', 'Hamburg, Germany', 'Lianyungang, China', 'Hong Kong, Hong Kong', 'Lagos, Nigeria', 'Sao Paulo, Brazil', 'Moscow, Russia', 'Rio de Janeiro, Brazil', 'Magnitogorsk, Russia', 'Sydney, Australia', 'Moscow, Russia', 'Monte Carlo, Monaco', 'Los Angeles, California', 'Bogota, Colombia']
# ['United States', 'United States', 'France', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'India', 'Spain', 'France', 'China', 'United States', 'China', 'Mexico', 'United States', 'United States', 'United States', 'United States', 'China', 'United States', 'United States', 'India', 'United States', 'China', 'United States', 'United States', 'Japan', 'United States', 'Japan', 'France', 'Canada', 'Germany', 'China', 'United States', 'China', 'Germany', 'China', 'Italy', 'France', 'France', 'Hong Kong', 'China', 'China', 'United States', 'Hong Kong', 'United States', 'United States', 'China', 'Russia', 'Hong Kong', 'China', 'Germany', 'Russia', 'Austria', 'China', 'Germany', 'Russia', 'China', 'Mexico', 'Italy', 'Japan', 'United States', 'United States', 'Russia', 'Russia', 'United States', 'China', 'Australia', 'United States', 'India', 'China', 'Chile', 'China', 'Singapore', 'China', 'Russia', 'United States', 'Singapore', 'Germany', 'Singapore', 'United States', 'Sweden', 'United States', 'Indonesia', 'Australia', 'United States', 'Indonesia', 'China', 'China', 'Hong Kong', 'Hong Kong', 'France', 'United States', 'United States', 'China', 'Germany', 'Russia', 'United States', 'China', 'China', 'Thailand', 'Hong Kong', 'China', 'Russia', 'United States', 'China', 'United States', 'Czechia', 'Hong Kong', 'Russia', 'United Kingdom', 'Brazil', 'Germany', 'Netherlands', 'India', 'China', 'United States', 'United States', 'China', 'United States', 'India', 'United States', 'Russia', 'United States', 'United States', 'Russia', 'China', 'China', 'Hong Kong', 'United States', 'United Kingdom', 'India', 'Germany', 'United States', 'China', 'Hong Kong', 'China', 'Ireland', 'Brazil', 'Russia', 'United States', 'Hong Kong', 'Australia', 'United States', 'South Korea', 'China', 'China', 'Australia', 'Sweden', 'Sweden', 'Sweden', 'United States', 'Hong Kong', 'United States', 'Thailand', 'South Korea', 'Singapore', 'China', 'Denmark', 'China', 'China', 'Russia', 'United Kingdom', 'China', 'Mexico', 'India', 'China', 'India', 'Malaysia', 'United States', 'United States', 'China', 'China', 'China', 'United States', 'United States', 'United States', 'Singapore', 'China', 'China', 'United States', 'United States', 'United States', 'France', 'United States', 'Germany', 'China', 'Canada', 'Nigeria', 'Brazil', 'Russia', 'Brazil', 'Russia', 'Australia', 'Russia', 'Israel', 'United States', 'Colombia']
# ['In Relationship', 'In Relationship', 'Married', 'Divorced', 'Widowed, Remarried', 'In Relationship', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Divorced', 'Married', 'Married', 'In Relationship', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Married', 'Married', 'Divorced', 'Widowed', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Divorced', 'Divorced', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Single', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed, Remarried', 'Divorced', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Married', 'Single', 'Divorced', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Single', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Divorced', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Single', 'Divorced', 'Married', 'Married', 'Married', 'Married', 'Divorced', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Single', 'Divorced', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married', 'Widowed', 'Married', 'Single', 'Married', 'Married', 'Married', 'In Relationship', 'Married', 'Married', 'Married', 'Married', 'Single', 'Married', 'Married', 'Married', 'Married', 'Divorced', 'Married', 'Single', 'Married', 'Married', 'Married', 'Married', 'Married', 'Married']
# ['4', '6', '5', '3', '2', '3', '4', '1', '3', '3', '3', '2', '3', '6', '4', '3', '2', '4', '5', '2', '3', '2', '3', '2', '4', '2', '3', '4', '5', '3', '2', '2', '3', '2', '2', '5', '3', '3', '7', '2', '3', '7', '1', '3', '6', '2', '3', '1', '2', '3', '1', '4', '6', '1', '3', '2', '3', '3', '3', '1', '3', '3', '2', '3', '3', '4', '4', '5', '3', '2', '1', '1', '1', '5', '3', '2', '3', '4', '5', '2', '5', '3', '5', '3', '7', '3', '2', '2', '3', '3', '5', '7', '2', '4', '3', '1', '4', '4', '4', '1', '7', '3', '2', '2', '6', '2', '1', '2', '6', '10', '5', '2', '4', '4', '6', '3', '1', '8', '2', '2', '2', '2', '4', '4', '3', '3', '2', '5', '2', '2', '2', '4', '2', '5']
# ['Bachelor of Arts/Science, Princeton University', 'Bachelor of Arts/Science, University of Pennsylvania', 'Bachelor of Arts/Science, Ecole Polytechnique de Paris', 'Drop Out, Harvard University', 'Drop Out, Harvard University', 'Master of Science, Columbia University; Bachelor of Arts/Science, University of Nebraska Lincoln', 'Drop Out, University of Chicago; Drop Out, University of Illinois, Urbana-Champaign', 'Master of Science, Stanford University; Bachelor of Arts/Science, University of Michigan', 'Master of Science, Stanford University; Bachelor of Arts/Science, University of Maryland, College Park', 'Drop Out, Stanford University; Bachelor of Science in Engineering, University of Mumbai', 'Bachelor of Arts/Science, Harvard University; Drop Out, Stanford University', 'Bachelor of Arts/Science, Shenzhen University', 'Bachelor of Arts/Science, Universidad Nacional Autonoma de Mexico', 'Bachelor of Arts/Science, Trinity University', 'Bachelor of Arts/Science, University of Arkansas', 'Doctor of Jurisprudence, Columbia University; Bachelor of Arts/Science, University of Arkansas', 'Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Johns Hopkins University', 'Master, University of Wisconsin Madison; Bachelor of Arts/Science, Zhejiang University', 'Bachelor of Arts/Science, Princeton University', 'Bachelor of Arts/Science, Michigan State University; LLB, Wayne State University', 'Master of Business Administration, Stanford Graduate School of Business; Bachelor of Arts/Science, University of Oregon', "Bachelor of Arts/Science, Hangzhou Teacher's Institute", 'Bachelor of Arts/Science, Massachusetts Institute of Technology; Master of Science, Massachusetts Institute of Technology', 'Bachelor of Arts/Science, University of California, Berkeley', 'Drop Out, The University of Texas at Austin', 'Bachelor of Arts/Science, Waseda University', 'Drop Out, High School', 'Master of Arts, University of Cambridge', 'Bachelor of Science, Hebrew University Jerusalem', 'Bachelor of Engineering, Nankai University', 'Drop Out, High School', 'Bachelor of Arts/Science, University of Electronic Science and Technology of China', 'Master of Science, Columbia University; Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Moscow State University', 'Bachelor of Arts/Science, Bryn Mawr College', 'Diploma, The Hotchkiss School; Bachelor of Arts/Science, Yale University', 'Bachelor of Arts/Science, Ohio State University', 'Bachelor of Arts/Science, Leningrad Institute of Economics; Master of Business Administration, University of Northumbria', 'Doctorate, Chinese Academy of Social Sciences', 'Bachelor of Arts/Science, Wuhan U of  Science & Tec', 'Master of Business Administration, International Institute for Management and Development', 'Bachelor of Arts/Science, Moscow Institute of International Relations', 'Master of Business Administration, University of Vienna', 'Doctorate, Russian Academy of Economics; Bachelor of Arts/Science, Siberian Metallurgical Institute', 'Graduate, Tsinghua University', 'Bachelor of Arts/Science, University of Pennsylvania', 'Drop Out, New York University', 'Bachelor of Science in Engineering, Azerbaijan Institute of Oil and Chemistry', 'Bachelor of Arts/Science, Kuybyshev Engineering and Construction Institute', 'Bachelor of Arts/Science, Massachusetts Institute of Technology; Doctorate, University of California, Berkeley', 'Associate in Arts/Science, Guilin Medical University', 'Bachelor of Arts/Science, Oxford University; Master of Arts, Oxford University', 'Bachelor of Arts/Science, PSG College of Technology', 'Bachelor of Arts/Science, Shenzhen University; Master of Arts, South China University of Technology', 'Bachelor of Science in Engineering, Wuhan University', 'Bachelor of Arts/Science, Renmin University of China', 'Bachelor of Arts/Science, Leningrad Mechanical Institute', 'Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Yale University', 'Associate in Arts/Science, Technical University of Karlsruhe', 'Bachelor of Science, University of Science and Technology of China', 'Bachelor of Arts/Science, Tufts University', 'Associate in Arts/Science, University of Stockholm', 'Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Hobart and William Smith', 'Bachelor of Arts/Science, University of Western Australia', 'Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Long Island University', 'Master of Science, Yanshan University', 'EMBA, Nanjing University', 'EMBA, Ceibs; Bachelor of Engineering, Tsinghua University; Master of Science in Engineering, Tsinghua University', 'Master of Business Administration, Stanford Graduate School of Business; Bachelor of Arts/Science, University of Pennsylvania, The Wharton School', 'Bachelor of Arts/Science, Princeton University; Doctorate, University of California, Berkeley; Master of Science, University of California, Berkeley', 'Bachelor of Arts/Science, China Pharmaceutical University; Doctorate, Nanjing University', 'Master, Finance Academy under the Government of the Russian Federation; Master of Laws, Moscow Institute of International Relations', 'Bachelor of Arts/Science, University of California, San Diego; Master of Science, University of California, San Diego', 'Bachelor of Engineering, Northwestern Polytechnical University', 'Master of Business Administration, Columbia Business School', 'Master of Business Administration, Hunan University', 'Master of Science, Plekhanov Russian University of Economics', 'Drop Out, Harvard University', 'Bachelor of Science, Tsinghua University', 'Drop Out, Syracuse University', 'Bachelor of Arts/Science, University of Economics in Prague', 'Master of Science, Saint Petersburg State University', 'Bachelor of Arts/Science, Harvard University', 'Bachelor of Arts/Science, Rijnlands Lyceum Wassenaar; Doctor of Jurisprudence, University of Leiden', 'Master of Science, Beijing Non-Ferrous Research Institute; Bachelor of Arts/Science, Central South Industrial University of Technology', 'Bachelor of Arts/Science, University of Pennsylvania, The Wharton School', 'Bachelor of Arts/Science, Harvard University', 'Master, China Europe International Business School; Bachelor of Arts/Economics, Tongji University', 'Bachelor of Science, Stanford University', 'Bachelor of Arts/Science, University of Mumbai; Master of Business Administration, University of Mumbai', 'Drop Out, New York University; Bachelor of Arts/Science, Princeton University', 'Bachelor of Arts/Science, Dagestan State University', 'Bachelor of Arts/Science, Vanderbilt University; Medical Doctor, Washington University', 'Bachelor of Arts/Science, Colorado College', 'Bachelor of Arts/Science, Moscow Institute of Steel and Alloys', 'Bachelor of Arts/Science, Hebei Province', 'Bachelor of Arts/Science, University of Washington', "Bachelor of Arts/Science, St Xavier's College Calcutta", 'Master of Engineering Management, China University of Mining and Technology; Bachelor of Engineering, Shandong Institute of Business and Technology', 'Liaoning University', 'Bachelor of Arts/Science, Peking University; Master of Arts, University at Buffalo', 'Bachelor of Arts/Science, Harvard University', 'Bachelor of Arts/Science, Moscow State Law Academy', 'Master of Business Administration, David A. Tepper School of Business; Bachelor of Arts/Science, University of Pittsburgh', 'Bachelor of Arts/Science, Huazhong University of Science and Technology', 'Bachelor of Arts/Science, University of New South Wales', 'Bachelor of Arts/Science, University of Wisconsin, Eau Claire', 'Bachelor of Arts/Science, Konkuk University; Master of Science, Konkuk University', 'Bachelor of Arts/Science, Central South University', 'Bachelor of Arts/Science, University of New South Wales', 'Bachelor of Arts/Science, Rhode Island School of Design', 'Bachelor of Engineering, Cornell University; Master of Business Administration, Samuel Curtis Johnson Graduate School of Management', 'Doctorate, Korea Advanced Institute of Science and Technology; Master of Science, Korea Advanced Institute of Science and Technology; Bachelor of Arts/Science, Seoul National University', 'EMBA, China Europe International Business School', 'Bachelor of Science, State University of Management', 'Bachelor of Arts/Science, London School of Economics; Bachelor of Arts/Science, London School of Economics', 'Bachelor of Technology, Hefei University of Technology', 'Master of Business Administration, A. B. Freeman School of Business; Bachelor of Arts/Science, Tecnológico de Monterrey', 'Master of Business Administration, London Business School; Bachelor of Arts/Science, University of Mumbai', 'Master of Business Administration, Peking University', 'Bachelor of Arts/Science, Pune University; Doctorate, Pune University', 'Bachelor of Arts/Science, Raffles College', 'Drop Out, New York University', 'Master of Business Administration, The Wharton School of the University of Pennsylvania', 'Bachelor of Arts/Science, Harvard University', 'Master of Business Administration, Harvard University; Bachelor of Arts/Science, Rice University; Master of Science, Rice University', 'Bachelor of Arts/Science, Rhode Island School of Design', 'Bachelor of Engineering, Shanghai Jiaotong University; Master of Business Administration, Stanford Graduate School of Business', 'Bachelor of Science in Engineering, Tsinghua University', 'Doctorate, California Institute of Technology; Bachelor of Arts/Science, University of California, Berkeley', 'Bachelor of Science, SUNY Binghamton', 'Bachelor of Arts/Science, Stanford University', 'Bachelor of Science in Engineering, Oregon State University; Master of Science in Engineering, Stanford University', 'Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Harvard College', 'Doctorate, Zhejiang University', 'Bachelor of Arts/Science, Yale University; Doctor of Jurisprudence, Yale University', 'Bachelor of Arts/Science, Al-Azhar University', 'Bachelor of Arts/Science, Universidade Federal do Rio de Janeiro', 'Bachelor of Arts/Science, Moscow Institute of Finance', 'Masters of Public Health, Universidade Federal do Rio de Janeiro', 'Bachelor of Science in Engineering, Magnitogorsk Mining\xa0and Metallurgical Institute', 'Bachelor of Arts/Science, University of Leeds', 'Master of Science, Military Academy F.E.Dzerzhinsky', 'Bachelor of Science, Stanford University', 'Bachelor of Arts/Science, National University of Colombia']

# lungimi
# 192
# 200
# 59
# 50
# 197
# 200
# 163
# 134
# 144
