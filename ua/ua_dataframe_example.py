
""""
Load UA data into dataframe
Sources:
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
https://medium.com/analytics-for-humans/submitting-your-first-google-analytics-reporting-api-request-cdda19969940

"""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os
import pandas as pd

file_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "../sandbox", "adswerve-ts-content-marketing-sa.json"))

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = file_path
VIEW_ID = '146223021'


def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.


  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


# our example
def get_report_example_2_metrics_by_page_title(analytics):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          # 'dateRanges': [{'startDate': '2022-09-16', 'endDate': '2022-09-22'}],
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:pageviews'},{'expression': 'ga:uniquePageviews'}],
          'dimensions': [{'name': 'ga:pageTitle'}],
          "orderBys": [
            {
              "orderType": "VALUE",
              "sortOrder": "DESCENDING",
              "fieldName": "ga:pageviews"
            }
          ]
        }]
      }
  ).execute()

# https://stackoverflow.com/questions/47203801/google-analytics-reporting-api-v4-sort-results

def parse_response(response):
    response_data = response.get('reports', [])[0]

    """Parses and prints the Analytics Reporting API V4 response
    Source: 
    https://medium.com/analytics-for-humans/submitting-your-first-google-analytics-reporting-api-request-cdda19969940
    Parse the response of API
    """
    # Initialize results, in list format because two dataframes might return
    result_list = []

    # Initialize empty data container for the two date ranges (if there are two that is)
    data_csv = []
    data_csv2 = []

    # Initialize header rows
    header_row = []

    # Get column headers, metric headers, and dimension headers.
    columnHeader = response_data.get('columnHeader', {})
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    dimensionHeaders = columnHeader.get('dimensions', [])

    # Combine all of those headers into the header_row, which is in a list format
    for dheader in dimensionHeaders:
      header_row.append(dheader)
    for mheader in metricHeaders:
      header_row.append(mheader['name'])

    # Get data from each of the rows, and append them into a list
    rows = response_data.get('data', {}).get('rows', [])
    for row in rows:
      row_temp = []
      dimensions = row.get('dimensions', [])
      metrics = row.get('metrics', [])
      for d in dimensions:
        row_temp.append(d)
      for m in metrics[0]['values']:
        m = pd.to_numeric(m)  # conver to numeric
        row_temp.append(m)
      data_csv.append(row_temp)

      # In case of a second date range, do the same thing for the second request
      if len(metrics) == 2:
        row_temp2 = []
        for d in dimensions:
          row_temp2.append(d)
        for m in metrics[1]['values']:
          row_temp2.append(m)
        data_csv2.append(row_temp2)

    # Putting those list formats into pandas dataframe, and append them into the final result
    result_df = pd.DataFrame(data_csv, columns=header_row)
    result_df.columns = result_df.columns.str.replace(':', '')

    result_list.append(result_df)
    if data_csv2 != []:
      result_list.append(pd.DataFrame(data_csv2, columns=header_row))
      result_list[1] = result_df.columns.str.replace(':', '')

    return result_list




def main():
  analytics = initialize_analyticsreporting()

  response = get_report_example_2_metrics_by_page_title(analytics)

  df_list = parse_response(response)
  df = df_list[0]
  print(df.head(100))

if __name__ == '__main__':
  main()

