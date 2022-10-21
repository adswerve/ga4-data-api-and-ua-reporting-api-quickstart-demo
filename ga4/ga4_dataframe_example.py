"""
Query Data API (GA4) and parse response into a dataframe
Sources:
https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
https://medium.com/analytics-for-humans/submitting-your-first-google-analytics-reporting-api-request-cdda19969940
"""


from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
import pandas as pd
import os
KEY_FILE_LOCATION = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "../sandbox", "adswerve-ts-content-marketing-sa.json"))
#  TODO(developer): replace with your Google Analytics 4 property ID before running the sample.
PROPERTY_ID = "206551716"



def sample_run_report_example_metrics_by_page(property_id="YOUR-GA4-PROPERTY-ID", credentials_json_path=KEY_FILE_LOCATION):
    """Runs a simple report on a Google Analytics 4 property."""

    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient().from_service_account_json(credentials_json_path)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pageTitle")],
        metrics=[Metric(name="screenPageViews"),Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2022-09-16", end_date="2022-09-22")],
    )
    response = client.run_report(request)

    return response
def parse_response(response):
    """
    Parses Data API response to a dataframe
    Based on this example: 
    https://medium.com/analytics-for-humans/submitting-your-first-google-analytics-reporting-api-request-cdda19969940
    
    """
    # Initialize results, in list format because two dataframes might return
    result_list = []

    # Initialize empty data container for the two date ranges (if there are two that is)
    data_csv = []
    data_csv2 = []

    # Initialize header rows
    header_row = []

    # Get metric headers, and dimension headers.

    for column in response.dimension_headers:
        header_row.append(column.name)

    for column in response.metric_headers:
        header_row.append(column.name)

    # Get data from each of the rows, and append them into a list
    for row in response.rows:
        row_temp = []

        for i in range(0, len(row.dimension_values)):
            # print(row.dimension_values[i].value)
            row_temp.append(row.dimension_values[i].value)

        for i in range(0, len(row.metric_values)):
            # print(row.metric_values[i].value)
            row_temp.append(pd.to_numeric(row.metric_values[i].value)) # convert to numeric

        data_csv.append(row_temp)

    # Putting those list formats into pandas dataframe, and append them into the final result
    result_df = pd.DataFrame(data_csv, columns=header_row)

    return result_df


def main():

  response = sample_run_report_example_metrics_by_page(property_id=PROPERTY_ID)
  df = parse_response(response)
  print(df.head(100).to_string())

if __name__ == '__main__':
  main()