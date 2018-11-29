import Reporter
import datetime
import timedelta

today = datetime.datetime.now().date()
yesterday = today - timedelta.Timedelta( days = 1 )

Reporter.report_day(yesterday)

