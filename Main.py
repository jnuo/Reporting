import Reporter
import datetime
import timedelta
import Helper.Data as dt

today = datetime.datetime.now().date()
yesterday = today - timedelta.Timedelta( days = 1 )

#gaReport = Reporter.get_day_report(yesterday)

#x = gaReport[0]
#print(x)


dt.go()