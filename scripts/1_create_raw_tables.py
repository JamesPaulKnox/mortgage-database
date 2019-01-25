from app_config import *

for script in raw_scripts:
	c.executescript(open(script, 'r').read())
