import sqlite3, datetime, os

app_dir = "/run/media/james/MediaB/projects/agency_loan_level/"

db_name = "mortgage.db"

conn = sqlite3.connect(app_dir + db_name)
c = conn.cursor()

raw_scripts = [ \
	"raw_fannie_origination.sql", \
	"raw_fannie_performance.sql", \
	"raw_freddie_origination.sql", \
	"raw_freddie_performance.sql" \
	]

