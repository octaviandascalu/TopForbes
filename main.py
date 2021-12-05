import time
from crawler import Crawler
from dbconnection import DbConnection
# from esantionDateCrawler import stats

start = time.time()
crawler = Crawler()
crawler.start()
stop = time.time()
print("Timp:", int(stop - start) // 60, "minute ", round(stop - start) % 60, "secunde\n")

db_conn = DbConnection()
db_conn.createDatabase()
db_conn.insertIntoDatabase(crawler.exportExtractedStats())

print("Top 10 tineri din Forbes:")
print(*db_conn.top10CeleMaiTineri(), sep=",")
print()
print("Top 10 filantropi din Forbes:")
print(*db_conn.top10Filantropi(), sep=",")
print()
print("In top 200 Forbes sunt", db_conn.cetatenieAmericana(True), "de cetateni americani.\n")
