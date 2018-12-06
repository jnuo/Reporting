import GA
import datetime
import timedelta
# import Helper.Data as dt
# import pandas as pd

import configparser

# config = configparser.ConfigParser()
# config.read('reporting_config.ini')
# name = config.get('Onur','ad')
# yas = config.get('Onur', 'yas')
# print(name, yas)

today = datetime.datetime.now().date()
yesterday = today - timedelta.Timedelta( days = 1 )
day_report = GA.get_google_analytics_day_report(yesterday)

rows, columns = day_report.shape
print(rows, columns)


