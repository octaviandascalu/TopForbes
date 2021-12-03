import mysql.connector
from esantionDateCrawler import stats

def convertToInteger(value):
    if value is None:
        return value
    else:
        return int(value)


def convertToString(value):
    if value is None:
        return value
    else:
        return str(value)


def top10CeleMaiTineri():
    # O functie care sa returneze top 10 cele mai tinere persoane din forbes
    mycursor.execute("select name from topforbes order by age is null, age limit 10")
    result = [row[0] for row in mycursor.fetchall()]
    return result


def cetatenieAmericana(american):
    # O functie care sa retuneze cate persoane au cetatenie americana sau nu
    if american:
        mycursor.execute("select count(*) from topforbes where citizenship='United States'")
    else:
        mycursor.execute("select count(*) from topforbes where citizenship!='United States'")
    result = mycursor.fetchall()[0][0]
    return result


def top10Filantropi():
    # O functie care sa returneze top 10 cel mai mare scor filantropic.
    mycursor.execute("select name from topforbes order by philanthropyScore desc limit 10")
    result = [row[0] for row in mycursor.fetchall()]
    return result


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

for i in range(200):
    mycursor.execute(
        "INSERT INTO TopForbes (name, age, sourceOfWealth, selfMadeScore, philanthropyScore, residence, citizenship, maritalStatus, children, education) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            convertToString(stats[0][i]), convertToInteger(stats[1][i]), convertToString(stats[2][i]),
            convertToInteger(stats[3][i]), convertToInteger(stats[4][i]),
            convertToString(stats[5][i]), convertToString(stats[6][i]),
            convertToString(stats[7][i]), convertToInteger(stats[8][i]), convertToString(stats[9][i])
        )
    )

db.commit()

print("Top 10 tineri din Forbes:", top10CeleMaiTineri())
print("Top 10 filantropi din Forbes:", top10Filantropi())
print("In top 200 Forbes sunt", cetatenieAmericana(True), "de cetateni americani.")
