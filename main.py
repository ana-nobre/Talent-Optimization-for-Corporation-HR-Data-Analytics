from src import functions as f
from src import queries as q

import os
from dotenv import load_dotenv
load_dotenv() 

csv = f.files()
f.exploracion(csv)
                
password = os.getenv("password")
f.create_schema_and_tables(q.create_schema , password)