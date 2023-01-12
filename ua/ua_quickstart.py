#TODO: (optional: more complex example? BQ? CF?)
#TODO: optional: colab???

""""Hello Analytics Reporting API V4."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os

file_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "../sandbox", "adswerve-ts-content-marketing-sa.json"))

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = file_path
VIEW_ID = '146223021'


def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.
  Source: https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics

# EXAMPLE 1 STARTS
# Google's example
def get_report_example_1_sessions_by_country(analytics):
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
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:country'}]
        }]
      }
  ).execute()
# EXAMPLE 1 ENDS

# # EXAMPLE 2 STARTS
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
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'yesterday'}],
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
# EXAMPLE 2 ENDS

# EXAMPLE 3 STARTS
# query a segment
def get_report_example_3_ga_segment(analytics):
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
          # 'dateRanges': [{'startDate': '2022-09-01', 'endDate': '2022-09-30'}],
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:pageviews'},{'expression': 'ga:uniquePageviews'}],
          'dimensions': [{'name': 'ga:pageTitle'}, {'name': 'ga:segment'}],
          "orderBys": [
            {
              "orderType": "VALUE",
              "sortOrder": "DESCENDING",
              "fieldName": "ga:pageviews"
            }
          ],
          "segments": [{"segmentId": "gaid::-13"}]
        }]
      }
  ).execute()
# EXAMPLE 3 ENDS

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
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print(header + ': ', dimension)

      for i, values in enumerate(dateRangeValues):
        print('Date range:', str(i))
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print(metricHeader.get('name') + ':', value)
      print("\n")
def main():
  analytics = initialize_analyticsreporting()
  # response = get_report_example_1_sessions_by_country(analytics)
  response = get_report_example_2_metrics_by_page_title(analytics)
  # response = get_report_example_3_ga_segment(analytics)
  print_response(response)

if __name__ == '__main__':
  main()

