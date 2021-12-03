import mysql.connector

# Esantion testare BD
name = ['Jeff Bezos ', 'Elon Musk ', 'Bernard Arnault & family ', 'Bill Gates ', 'Mark Zuckerberg ', 'Warren Buffett ',
        'Larry Ellison ', 'Larry Page ', 'Sergey Brin ', 'Mukesh Ambani ', 'Amancio Ortega ',
        'Francoise Bettencourt Meyers & family ', 'Zhong Shanshan ', 'Steve Ballmer ', 'Ma Huateng ',
        'Carlos Slim Helu & family ', 'Alice Walton ', 'Jim Walton ', 'Rob Walton ', 'Michael Bloomberg ',
        'Colin Zheng Huang ', 'MacKenzie Scott ', 'Daniel Gilbert ', 'Gautam Adani & family ', 'Phil Knight & family ',
        'Jack Ma ', 'Charles Koch ', 'Julia Koch & family ', 'Masayoshi Son ', 'Michael Dell ',
        'Tadashi Yanai & family ', 'François Pinault & family ', 'David Thomson & family ',
        'Beate Heister & Karl Albrecht Jr. ', 'Wang Wei ', 'Miriam Adelson ', 'He Xiangjian ', 'Dieter Schwarz ',
        'Zhang Yiming ', 'Giovanni Ferrero ', 'Alain Wertheimer ', 'Gerard Wertheimer ', 'Li Ka-shing ',
        'Qin Yinglin & family ', 'William Lei Ding ', 'Len Blavatnik ', 'Lee Shau Kee ', 'Jacqueline Mars ',
        'John Mars ', 'Yang Huiyan & family ', 'Alexey Mordashov & family ', 'Robin Zeng ', 'Hui Ka Yan ',
        'Susanne Klatten ', 'Vladimir Potanin ', 'Dietrich Mateschitz ', 'Pang Kang ', 'Klaus-Michael Kuehne ',
        'Vladimir Lisin ', 'Wang Xing ', 'German Larrea Mota Velasco & family ', 'Leonardo Del Vecchio & family ',
        'Takemitsu Takizaki ', 'Leonard Lauder ', 'Thomas Peterffy ', 'Vagit Alekperov ', 'Leonid Mikhelson ',
        'Jim Simons ', 'Jiang Rensheng & family ', 'Gina Rinehart ', 'Rupert Murdoch & family ', 'Shiv Nadar ',
        'Zhang Zhidong ', 'Iris Fontbona & family ', 'Lei Jun ', 'Zhang Yong ', 'Richard Qiangdong Liu ',
        'Gennady Timchenko ', 'Stephen Schwarzman ', 'Goh Cheng Liang ', 'Stefan Quandt ', 'Li Xiting ',
        'Pierre Omidyar ', 'Stefan Persson ', 'Abigail Johnson ', 'R. Budi Hartono ', 'Andrew Forrest ', 'Ray Dalio ',
        'Michael Hartono ', 'Li Shufu ', 'Zhong Huijuan ', 'Xu Hang ', 'Lui Che Woo & family ', 'Emmanuel Besnier ',
        'Laurene Powell Jobs & family ', 'Eric Schmidt ', 'Sun Piaoyang ', 'Theo Albrecht, Jr. & family ',
        'Alisher Usmanov ', 'Robert Pera ', 'Wu Yajun ', 'Fan Hongwei & family ', 'Dhanin Chearavanont ', 'Peter Woo ',
        'Chen Bang ', 'Andrey Melnichenko ', 'Dustin Moskovitz ', 'Su Hua ', 'Donald Newhouse ', 'Petr Kellner ',
        'Lee Man Tat ', 'Pavel Durov ', 'James Ratcliffe ', 'Jorge Paulo Lemann & family ', 'Reinhold Wuerth & family ',
        'Charlene de Carvalho-Heineken & family ', 'Radhakishan Damani ', 'Wang Chuanfu ', 'Steve Cohen ',
        'Ken Griffin ', 'Chen Zhiping ', 'Ernest Garcia, II. ', 'Uday Kotak ', 'Carl Icahn ',
        'Suleiman Kerimov & family ', 'Thomas Frist, Jr. & family ', 'Lukas Walton ', 'Mikhail Fridman ',
        'Wei Jianjun & family ', 'Zuo Hui ', 'Zhou Qunfei & family ', 'Donald Bren ', 'Hinduja brothers ',
        'Lakshmi Mittal ', 'Georg Schaeffler ', 'Eric Yuan & family ', 'Wang Jianlin ', 'Kwong Siu-hing ', 'Robin Li ',
        'Pallonji Mistry ', 'Eduardo Saverin ', 'Roman Abramovich ', 'David Tepper ', 'Gong Hongjia & family ',
        'Mike Cannon-Brookes ', 'John Menard, Jr. ', 'Seo Jung-jin ', 'Cheng Yixiao ', 'Liang Wengen ',
        'Scott Farquhar ', 'Finn Rausing ', 'Jorn Rausing ', 'Kirsten Rausing ', 'Brian Chesky ', 'Joseph Lau ',
        'David Duffield ', 'Charoen Sirivadhanabhakdi ', 'Kim Jung-ju ', 'Robert & Philip Ng ', 'Zhang Bangxin ',
        'Anders Holch Povlsen ', 'Wang Wenyin ', 'Wang Liping & family ', 'Tatyana Bakalchuk ', 'Michael Platt ',
        'Huang Shilin ', 'Ricardo Salinas Pliego & family ', 'Kumar Birla ', 'Dang Yanbao ', 'Cyrus Poonawalla ',
        'Robert Kuok ', 'Hank & Doug Meijer ', 'Jack Dorsey ', 'Lu Zhongfang ', 'Ma Jianrong & family ', 'Zhang Tao ',
        'Nathan Blecharczyk ', 'John Doerr ', 'Joe Gebbia ', 'Forrest Li ', 'Yu Renrong ', 'Liu Yonghao & family ',
        'Gordon Moore ', 'Jeff Yass ', 'Bobby Murphy ', 'Patrick Drahi ', 'Jensen Huang ', 'Alexander Otto ',
        'Cen Junda ', 'Joseph Tsai ', 'Aliko Dangote ', 'Marcel Herrmann Telles ', 'Mikhail Prokhorov ',
        'Jorge Moll Filho & family ', 'Viktor Rashnikov ', 'Harry Triguboff ', 'Leonid Fedun & family ', 'Eyal Ofer ',
        'Evan Spiegel ', 'Luis Carlos Sarmiento ']
age = ['57', '50', '72', '66', '37', '91', '77', '48', '48', '64', '85', '68', '67', '65', '50', '81', '72', '73', '77',
       '79', '41', '51', '59', '59', '83', '57', '86', '59', '64', '56', '72', '85', '64', None, '51', '76', '79', '82',
       '37', '57', '73', '70', '93', '56', '50', '64', '93', '82', '86', '40']
source_of_wealth = ['Amazon, Self Made', 'Tesla, SpaceX, Self Made', 'LVMH', 'Microsoft, Self Made',
                    'Facebook, Self Made', 'Berkshire Hathaway, Self Made', 'software, Self Made', 'Google, Self Made',
                    'Google, Self Made', 'diversified', 'Zara, Self Made', "L'Oréal",
                    'beverages, pharmaceuticals, Self Made', 'Microsoft, Self Made', 'internet media, Self Made',
                    'telecom, Self Made', 'Walmart', 'Walmart', 'Walmart', 'Bloomberg LP, Self Made',
                    'e-commerce, Self Made', 'Amazon', 'Quicken Loans, Self Made',
                    'infrastructure, commodities, Self Made', 'Nike, Self Made', 'e-commerce, Self Made',
                    'Koch Industries', 'Koch Industries', 'internet, telecom, Self Made', 'Dell computers, Self Made',
                    'fashion retail, Self Made', 'luxury goods, Self Made', 'media', 'supermarkets',
                    'package delivery, Self Made', 'casinos', 'home appliances, Self Made', 'retail',
                    'TikTok, Self Made', 'Nutella, chocolates', 'Chanel', 'Chanel', 'diversified, Self Made',
                    'pig breeding, Self Made', 'online games, Self Made', 'music, chemicals, Self Made',
                    'real estate, Self Made', 'candy, pet food', 'candy, pet food', 'real estate']
self_made_score = ['8', '8', None, '8', '8', '8', '9', '8', '9', None, None, None, None, '6', None, None, '1', '2', '4',
                   '8', None, '3', '8', None, '8', None, '5', '1', None, '8', None, None, None, None, None, '2', None,
                   None, None, '4', None, None, None, None, None, '9', None, '2', '2', None]
philanthropy_score = ['1', '1', None, '4', '2', '5', '1', '1', '1', None, None, None, None, '2', None, None, '2', '1',
                      '1', '4', None, '2', '1', None, '2', None, '2', '2', None, '2', None, None, None, None, None,
                      None, None, None, None, None, None, None, None, None, None, '2', None, None, None, None]
residence = ['Seattle, Washington', 'Austin, Texas', 'Paris, France', 'Medina, Washington', 'Palo Alto, California',
             'Omaha, Nebraska', 'Lanai, Hawaii', 'Palo Alto, California', 'Los Altos, California', 'Mumbai, India',
             'La Coruna, Spain', 'Paris, France', 'Hangzhou, China', 'Hunts Point, Washington', 'Shenzhen, China',
             'Mexico City, Mexico', 'Fort Worth, Texas', 'Bentonville, Arkansas', 'Bentonville, Arkansas',
             'New York, New York', 'Shanghai, China', 'Seattle, Washington', 'Franklin, Michigan', 'Ahmedabad, India',
             'Hillsboro, Oregon', 'Hangzhou, China', 'Wichita, Kansas', 'New York, New York', 'Tokyo, Japan',
             'Austin, Texas', 'Tokyo, Japan', 'Paris, France', 'Toronto, Canada', 'Germany', 'Shenzhen, China',
             'Las Vegas, Nevada', 'Foshan, China', 'Neckarsulm, Germany', 'Beijing, China', 'Brussels, Belgium',
             'New York, New York', 'New York, New York', 'Hong Kong', 'Nanyang, China', 'Hangzhou, China',
             'London, United Kingdom', 'Hong Kong, Hong Kong', 'The Plains, Virginia', 'Jackson, Wyoming',
             'Foshan, China']
citizenship = ['United States', 'United States', 'France', 'United States', 'United States', 'United States',
               'United States', 'United States', 'United States', 'India', 'Spain', 'France', 'China', 'United States',
               'China', 'Mexico', 'United States', 'United States', 'United States', 'United States', 'China',
               'United States', 'United States', 'India', 'United States', 'China', 'United States', 'United States',
               'Japan', 'United States', 'Japan', 'France', 'Canada', 'Germany', 'China', 'United States', 'China',
               'Germany', 'China', 'Italy', 'France', 'France', 'Hong Kong', 'China', 'China', 'United States',
               'Hong Kong', 'United States', 'United States', 'China']
marital_status = ['In Relationship', 'In Relationship', 'Married', 'Divorced', None, 'Widowed, Remarried',
                  'In Relationship', 'Married', 'Married', 'Married', 'Married', 'Married', None, 'Married', 'Married',
                  'Widowed', 'Divorced', 'Married', 'Married', 'In Relationship', None, 'Married', 'Married', 'Married',
                  'Married', 'Married', 'Married', 'Widowed', 'Married', 'Married', 'Married', 'Married', 'Divorced',
                  None, None, 'Widowed', 'Married', 'Married', None, 'Married', 'Married', 'Married', 'Widowed',
                  'Married', None, 'Married', 'Divorced', 'Divorced', 'Married', 'Married']
children = ['4', '6', '5', '3', '2', '3', '4', '1', '3', '3', '3', '2', None, '3', None, '6', None, '4', '3', '2', None,
            '4', '5', '2', '3', None, '2', '3', '2', '4', '2', '3', '4', None, None, '5', '3', '2', None, '2', '3', '2',
            '2', None, None, None, '5', '3', '3', None]
education = ['Bachelor of Arts/Science, Princeton University', 'Bachelor of Arts/Science, University of Pennsylvania',
             'Bachelor of Arts/Science, Ecole Polytechnique de Paris', 'Drop Out, Harvard University',
             'Drop Out, Harvard University',
             'Master of Science, Columbia University; Bachelor of Arts/Science, University of Nebraska Lincoln',
             'Drop Out, University of Chicago; Drop Out, University of Illinois, Urbana-Champaign',
             'Master of Science, Stanford University; Bachelor of Arts/Science, University of Michigan',
             'Master of Science, Stanford University; Bachelor of Arts/Science, University of Maryland, College Park',
             'Drop Out, Stanford University; Bachelor of Science in Engineering, University of Mumbai', None, None,
             None, 'Bachelor of Arts/Science, Harvard University; Drop Out, Stanford University',
             'Bachelor of Arts/Science, Shenzhen University',
             'Bachelor of Arts/Science, Universidad Nacional Autonoma de Mexico',
             'Bachelor of Arts/Science, Trinity University', 'Bachelor of Arts/Science, University of Arkansas',
             'Doctor of Jurisprudence, Columbia University; Bachelor of Arts/Science, University of Arkansas',
             'Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Johns Hopkins University',
             'Master, University of Wisconsin Madison; Bachelor of Arts/Science, Zhejiang University',
             'Bachelor of Arts/Science, Princeton University',
             'Bachelor of Arts/Science, Michigan State University; LLB, Wayne State University', None,
             'Master of Business Administration, Stanford Graduate School of Business; Bachelor of Arts/Science, University of Oregon',
             "Bachelor of Arts/Science, Hangzhou Teacher's Institute",
             'Bachelor of Arts/Science, Massachusetts Institute of Technology; Master of Science, Massachusetts Institute of Technology',
             None, 'Bachelor of Arts/Science, University of California, Berkeley',
             'Drop Out, The University of Texas at Austin', 'Bachelor of Arts/Science, Waseda University',
             'Drop Out, High School', 'Master of Arts, University of Cambridge', None, None,
             'Bachelor of Science, Hebrew University Jerusalem', None, None,
             'Bachelor of Engineering, Nankai University', None, None, None, 'Drop Out, High School', None,
             'Bachelor of Arts/Science, University of Electronic Science and Technology of China',
             'Master of Science, Columbia University; Master of Business Administration, Harvard Business School; Bachelor of Arts/Science, Moscow State University',
             None, 'Bachelor of Arts/Science, Bryn Mawr College',
             'Diploma, The Hotchkiss School; Bachelor of Arts/Science, Yale University',
             'Bachelor of Arts/Science, Ohio State University']


def convertToInteger(value):
    if value is None:
        return value;
    else:
        return int(value)


def convertToString(value):
    if value is None:
        return value;
    else:
        return str(value)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='0000',
    database="forbes"
)

mycursor = db.cursor()
mycursor.execute('DROP TABLE TopForbes')
mycursor.execute(
    'CREATE TABLE TopForbes (rankID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age smallint UNSIGNED, sourceOfWealth VARCHAR(50), selfMadeScore smallint UNSIGNED, philanthropyScore smallint UNSIGNED, residence VARCHAR(50), citizenship VARCHAR(50), maritalStatus VARCHAR(50), children smallint UNSIGNED, education VARCHAR(250))')

for i in range(50):
    mycursor.execute(
        "INSERT INTO TopForbes (name, age, sourceOfWealth, selfMadeScore, philanthropyScore, residence, citizenship, maritalStatus, children, education) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            convertToString(name[i]), convertToInteger(age[i]), convertToString(source_of_wealth[i]),
            convertToInteger(self_made_score[i]), convertToInteger(philanthropy_score[i]),
            convertToString(residence[i]), convertToString(citizenship[i]),
            convertToString(marital_status[i]), convertToInteger(children[i]), convertToString(education[i])
        )
    )

db.commit()
