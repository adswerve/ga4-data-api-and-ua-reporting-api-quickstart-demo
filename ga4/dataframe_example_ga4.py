"""
Query Data API (GA4) and parse response into a dataframe
Sources:
https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
https://medium.com/analytics-for-humans/submitting-your-first-google-analytics-reporting-api-request-cdda19969940
"""

#TODO: write an example of parsing GA4 response to a dataframe

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

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value)

        for i in range(0, len(row.metric_values)):
            print(row.metric_values[i].value)


def parse_response(response):
    """Parses Data API response to a dataframe
    """
    pass

if __name__ == "__main__":

    sample_run_report_example_metrics_by_page(property_id=PROPERTY_ID)