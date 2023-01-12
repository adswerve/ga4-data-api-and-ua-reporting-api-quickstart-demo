from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest

import os
file_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "../sandbox", "adswerve-ts-content-marketing-sa.json"))

KEY_FILE_LOCATION = file_path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = KEY_FILE_LOCATION
#  TODO(developer): replace with your Google Analytics 4 property ID before running the sample.
PROPERTY_ID = "206551716"

def sample_run_report_example_1_users_by_city(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a simple report on a Google Analytics 4 property.
    Source: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
    """

    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2022-10-01", end_date="today")]
    )
    response = client.run_report(request)

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


def sample_run_report_example_2_metrics_by_page(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a simple report on a Google Analytics 4 property."""

    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pageTitle")],
        metrics=[Metric(name="screenPageViews"),Metric(name="activeUsers")],
        # date_ranges=[DateRange(start_date="2023-01-05", end_date="2023-01-11")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
    )
    response = client.run_report(request)

    print("Report result:")
    for row in response.rows:
        print("\n", row.dimension_values[0].value)

        for i in range(0, len(row.metric_values)):
            print(row.metric_values[i].value)


if __name__ == "__main__":

    # sample_run_report_example_1_users_by_city(property_id=PROPERTY_ID)

    sample_run_report_example_2_metrics_by_page(property_id=PROPERTY_ID)