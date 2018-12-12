import GoogleAnalytics
import datetime
import timedelta
import pandas as pd
# import Helper.Data as dt
import configparser

config = configparser.ConfigParser()
config.read('reporting_config.ini')

today = datetime.datetime.now().date()
yesterday = today - timedelta.Timedelta( days = 1 )

########
# ok - Get analytics

### sprint 1 Google Ads
### sprint 2 Facebook Ads
### sprint 3 Criteo
### sprint 4 output excel'i duzenle
### sprint 5 ali

# ok - out to excel
#########

# Get analytics
day_report = GoogleAnalytics.get_google_analytics_day_report(yesterday)

# rows, columns = day_report.shape
# print(rows, columns)

# Get ads


# match
# google / cpc olanlarin icindeki en cok session alana 159.87 TL yaz
googleAdRows = day_report[ day_report['ga:sourceMedium'] == "google / cpc" ]
# print( googleAdRows[['ga:sourceMedium', 'ga:campaign', 'ga:sessions', 'cost', 'ga:metric2']][ googleAdRows['ga:sessions'] == googleAdRows['ga:sessions'].max()] )

index = googleAdRows[ googleAdRows['ga:sessions'] == googleAdRows['ga:sessions'].max()].index.values[0]

# index = day_report[ day_report['ga:sourceMedium'] == "google / cpc" & day_report['ga:sessions'] == googleAdRows['ga:sessions'].max() ].index.values[0]

day_report.loc[index]['cost'] = 159.87
day_report.loc[index]['roi'] = float(day_report.loc[index]['ga:metric2']) / float(day_report.loc[index]['cost'])
day_report.loc[index]['roas'] = float(day_report.loc[index]['ga:transactionRevenue']) / float(day_report.loc[index]['cost'])

print(day_report.loc[index])

# print( googleAdRows[ googleAdRows['ga:sessions'] == googleAdRows['ga:sessions'].max()] )
# googleAdRows[ googleAdRows['ga:sessions'] == googleAdRows['ga:sessions'].max()]['cost'] = 158.98
# print( googleAdRows[['ga:sourceMedium', 'ga:campaign', 'ga:sessions', 'cost', 'ga:metric2']][ googleAdRows['ga:sessions'] == googleAdRows['ga:sessions'].max()] )

# print(googleAdRows)
# df[['ga:sourceMedium', 'ga:campaign', 'ga:metric2']][df['ga:campaign'].str.contains("remarketing", case=False) | df['ga:sourceMedium'].str.contains("criteo", case=False)]

# out to excel
filename = config.get('Output', 'filename')
writer = pd.ExcelWriter(filename)
day_report.to_excel(writer, sheet_name='Sheet1')
writer.save()
