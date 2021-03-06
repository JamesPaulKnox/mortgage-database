from app_config import *
import glob, string

#####

def populate(table, columns):
	
	print(current)
	
	for row in open(current):
		row = row.translate(str.maketrans("", "", "'"))
		row = row.split("|")
		
		while len(row) < columns:
			row.append("")
		
		data = "'" + "','".join(map(str, row)) + "'"

		sql_str = "INSERT INTO " + table + " VALUES (" + data + ");"
		
		# ~ print(sql_str)
		
		c.execute(sql_str)

		

	conn.commit()

#####

files = glob.glob(app_dir + "import/*/*.txt")

for current in files:
	if "Acquisition_" in current and not "HARP" in current:
		populate("raw_fannie_origination", 25)
	if "Performance_" in current and not "HARP" in current:
		populate("raw_fannie_performance", 31)
	if "historical_data1_time_" in current and not "harp" in current:
		populate("raw_freddie_performance", 26)
	elif "historical_data1_" in current and not "harp" in current:
		populate("raw_freddie_origination", 27)
