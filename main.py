from crawler import Crawler
from dbconnection import DbConnection
from esantionDateCrawler import stats

# crawler = Crawler()
# crawler.start()
# crawler.stop()

db_conn = DbConnection()
db_conn.createDatabase()
db_conn.insertIntoDatabase(stats)

print("Top 10 tineri din Forbes:", db_conn.top10CeleMaiTineri())
print("Top 10 filantropi din Forbes:", db_conn.top10Filantropi())
print("In top 200 Forbes sunt", db_conn.cetatenieAmericana(True), "de cetateni americani.")