import GA
import pandas as pd

def get_day_report(day):
    analyticsReport = GA.get_day_report(day)
    report = get_dict(analyticsReport)
    df = pd.DataFrame(report)
    return df

def print_report(rep):
    for report in rep.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

        for row in report.get('data', {}).get('rows', []):
            print('\n')

            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                print('  ' + header + ': ' + dimension)

            for i, values in enumerate(dateRangeValues):
                print('    Date range: ' + str(i))
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    print('    ' + metricHeader.get('name') + ': ' + value)


def get_dict(response):
    gaReport = []
    # gaReport format
    #   date, channel grouping, source / medium, campaign
    #   sessions, new users, users, transactions, revenue, totalsc
    #   cost, roi, roas

    for report in response.get('reports', []):

        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

        for row in report.get('data', {}).get('rows', []):
            rowData = \
                {
                    'ga:date': ''
                    , 'ga:channelGrouping': ''
                    , 'ga:sourceMedium': ''
                    , 'ga:campaign': ''
                    , 'ga:sessions': ''
                    , 'ga:newUsers': ''
                    , 'ga:users': ''
                    , 'ga:transactions': ''
                    , 'ga:transactionRevenue': ''
                    , 'ga:metric2': ''
                    , 'cost': ''
                    , 'roi': ''
                    , 'roas': ''
                }

            # print('\n')

            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                # print('  ' + header + ': ' + dimension)
                rowData[header] = dimension

            for i, values in enumerate(dateRangeValues):
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    # print('    ' + metricHeader.get('name') + ': ' + value)
                    rowData[metricHeader.get('name')] = value

            gaReport.append(rowData)

    return gaReport