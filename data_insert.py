from db import connect_db
import pandas as pd
db = connect_db().db
data = pd.read_csv('Hotel_details.csv')
d1 = data.to_dict('records')
db.hotels.insert_many(d1)
