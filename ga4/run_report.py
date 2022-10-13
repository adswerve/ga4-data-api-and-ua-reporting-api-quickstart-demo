"""
Source:
https://developers.google.com/analytics/devguides/reporting/data/v1/basics
https://github.com/googleapis/python-analytics-data/blob/main/samples/snippets/run_report.py
"""

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import MetricType
from google.analytics.data_v1beta.types import RunReportRequest


import os
file_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "../sandbox", "adswerve-ts-content-marketing-sa.json"))

KEY_FILE_LOCATION = file_path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = KEY_FILE_LOCATION

PROPERTY_ID = "206551716"

def run_sample(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    run_report(property_id)


def run_report(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report of active users grouped by country."""
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-09-01", end_date="2020-09-15")],
    )
    response = client.run_report(request)
    print_run_report_response(response)


def print_run_report_response(response):
    """Prints results of a runReport call."""
    print(f"{response.row_count} rows received")
    for dimensionHeader in response.dimension_headers:
        print(f"Dimension header name: {dimensionHeader.name}")
    for metricHeader in response.metric_headers:
        metric_type = MetricType(metricHeader.type_).name
        print(f"Metric header name: {metricHeader.name} ({metric_type})")

    print("Report result:")
    for row in response.rows:
        for dimension_value in row.dimension_values:
            print(dimension_value.value)

        for metric_value in row.metric_values:
            print(metric_value.value)

if __name__ == "__main__":

    run_sample(property_id=PROPERTY_ID)
