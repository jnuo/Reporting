import Reporter
import datetime
import timedelta

today = datetime.datetime.now().date()
yesterday = today - timedelta.Timedelta( days = 1 )

#gaReport = Reporter.get_day_report(yesterday)

#x = gaReport[0]
#print(x)


# kelimeler = ['onur','busra']
#
# for kelime in kelimeler:
#     if 'ur' in kelime:
#         print(kelime)

evciler = \
    [
        {
            'name': 'onur',
            'age': 32
        },
        {
            'name': 'urfa',
            'age': 4000000
        },
        {
            'name': 'busra',
            'age': 28
        }
    ]

#evcidf = pd.DataFrame(evciler, index)
