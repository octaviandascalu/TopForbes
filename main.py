import time
from crawler import Crawler
from dbconnection import DbConnection

# from esantionDateCrawler import stats

start = time.time()
crawler = Crawler()
crawler.start()
crawler.stop()
stop = time.time()
print("Timp:", (stop - start) // 60, "minute ", (stop - start) % 60, "secunde")

db_conn = DbConnection()
db_conn.createDatabase()
db_conn.insertIntoDatabase(crawler.exportExtractedStats())

print("Top 10 tineri din Forbes:", db_conn.top10CeleMaiTineri())
print("Top 10 filantropi din Forbes:", db_conn.top10Filantropi())
print("In top 200 Forbes sunt", db_conn.cetatenieAmericana(True), "de cetateni americani.")
