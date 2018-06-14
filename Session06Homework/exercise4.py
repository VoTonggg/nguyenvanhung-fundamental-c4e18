from pymongo import MongoClient

import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"


client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db['customers']

all_customers = customers.find()

labels = ["events", "wom", "ads"]
event_ref = 0
wom_ref = 0
ads_ref = 0
for customer in all_customers:
    if customer['ref'] == "events":
        event_ref += 1
    elif customer['ref'] == "wom":
        wom_ref += 1
    elif customer['ref'] == "ads":
        ads_ref += 1
values = [event_ref, wom_ref, ads_ref]
print(event_ref + wom_ref + ads_ref)
pyplot.pie(values,
           labels = labels)

pyplot.axis("equal")

pyplot.show()
