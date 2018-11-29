import GA

def report_day(day):
    gaReport = GA.get_day_report(day)
    for report in gaReport.get('reports', []):
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