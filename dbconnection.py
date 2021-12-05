import mysql.connector


class DbConnection:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd='0000',
            database="forbes"
        )

        self.mycursor = self.db.cursor()

    def createDatabase(self):
        self.mycursor.execute('DROP TABLE IF EXISTS TopForbes')
        self.mycursor.execute(
            "CREATE TABLE TopForbes (personID int PRIMARY KEY AUTO_INCREMENT, rankForbes smallint UNSIGNED, name VARCHAR(50), netWorth VARCHAR(10), age smallint UNSIGNED, sourceOfWealth VARCHAR(50), category VARCHAR(50), selfMadeScore smallint UNSIGNED, philanthropyScore smallint UNSIGNED, residence VARCHAR(50), citizenship VARCHAR(50), maritalStatus VARCHAR(50), children smallint UNSIGNED, education VARCHAR(250))")

    def insertIntoDatabase(self, stats):
        for i in range(200):
            self.mycursor.execute(
                "INSERT INTO TopForbes (rankForbes, name, netWorth, age, sourceOfWealth, category, selfMadeScore, philanthropyScore, residence, citizenship, maritalStatus, children, education) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    stats[0][i], stats[1][i], stats[2][i], stats[3][i], stats[4][i], stats[5][i], stats[6][i],
                    stats[7][i], stats[8][i], stats[9][i], stats[10][i], stats[11][i], stats[12][i]
                )
            )

        self.db.commit()

    def top10CeleMaiTineri(self):
        # O functie care sa returneze top 10 cele mai tinere persoane din forbes
        self.mycursor.execute("select name from topforbes order by age is null, age limit 10")
        result = [row[0] for row in self.mycursor.fetchall()]
        return result

    def cetatenieAmericana(self, american):
        # O functie care sa retuneze cate persoane au cetatenie americana sau nu
        if american:
            self.mycursor.execute("select count(*) from topforbes where citizenship='United States'")
        else:
            self.mycursor.execute("select count(*) from topforbes where citizenship!='United States'")
        result = self.mycursor.fetchall()[0][0]
        return result

    def top10Filantropi(self):
        # O functie care sa returneze top 10 cel mai mare scor filantropic.
        self.mycursor.execute("select name from topforbes order by philanthropyScore desc limit 10")
        result = [row[0] for row in self.mycursor.fetchall()]
        return result
