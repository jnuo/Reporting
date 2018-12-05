import Reporter
import datetime
import timedelta
import Helper.Data as dt
import pandas as pd

import configparser

config = configparser.ConfigParser()
config.read('reporting_config.ini')

# name = config.get('Onur','ad')
# yas = config.get('Onur', 'yas')
# print(name, yas)

today = datetime.datetime.now().date()
yesterday = today - timedelta.Timedelta( days = 1 )
gaReport = Reporter.get_day_report(yesterday)
df = pd.DataFrame(gaReport)

googles = df[['ga:sourceMedium', 'ga:campaign', 'ga:transactions' ]][ df['ga:sourceMedium'] == "google / cpc" ]

google_dyn = googles[['ga:campaign', 'ga:transactions']][ googles['ga:campaign'].str.contains("remarketing", case=False) ]
print(google_dyn)

