import pandas as pd
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import configparser


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = ''
VIEW_ID = ''
config = configparser.ConfigParser()

def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
      An authorized Analytics Reporting API V4 service object.
    """
    config.read('reporting_config.ini')
    KEY_FILE_LOCATION = config.get('GA', 'KEY_FILE_LOCATION')

    credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics

def get_google_analytics_day_report(day):
    analyticsReport = get_day_report(day)
    report = get_dict(analyticsReport)
    df = pd.DataFrame(report)
    # print("df: " + df[['ga:sourceMedium', 'ga:campaign', 'ga:metric2']][df['ga:campaign'].str.contains("remarketing", case=False) | df['ga:sourceMedium'].str.contains("criteo", case=False)])
    return df


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


def get_day_report(day):
    # print('Getting report for ' + str(day))
    ga = initialize_analyticsreporting()
    rep = get_report(ga, day, day)
    #print_response(rep)
    return rep



def get_report(analytics, start, end):
    """Queries the Analytics Reporting API V4.

    Args:
      analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
      The Analytics Reporting API V4 response.
    """
    VIEW_ID = config.get('GA', 'VIEW_ID')
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': VIEW_ID,
                    'dateRanges': [{'startDate': str(start), 'endDate': str(end)}],
                    'metrics':
                        [
                            {'expression': 'ga:sessions'}
                            , {'expression': 'ga:newUsers'}
                            , {'expression': 'ga:users'}
                            , {'expression': 'ga:transactions'}
                            , {'expression': 'ga:transactionRevenue'}
                            , {'expression': 'ga:metric2'}
                        ],
                    'dimensions':
                        [
                            {'name': 'ga:date'}
                            , {'name': 'ga:channelGrouping'}
                            , {'name': 'ga:sourceMedium'}
                            , {'name': 'ga:campaign'}
                         ]
                }]
        }
    ).execute()


def print_response(response):
    """Parses and prints the Analytics Reporting API V4 response.

    Args:
      response: An Analytics Reporting API V4 response.
    """
    for report in response.get('reports', []):
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


def main():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    print_response(response)


if __name__ == '__main__':
    main()
