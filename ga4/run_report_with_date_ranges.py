#!/usr/bin/env python

# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Data API sample application demonstrating the usage of
date ranges in a report.

See https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport#body.request_body.FIELDS.date_ranges
for more information.
"""

import os
KEY_FILE_LOCATION = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "../sandbox", "adswerve-ts-content-marketing-sa.json"))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = KEY_FILE_LOCATION
#  TODO(developer): replace with your Google Analytics 4 property ID before running the sample.
PROPERTY_ID = "206551716"

# [START analyticsdata_run_report_with_date_ranges]
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest

from run_report import print_run_report_response


def run_sample(property_id = "YOUR-GA4-PROPERTY-ID"):
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    run_report_with_date_ranges(property_id)


def run_report_with_date_ranges(property_id="YOUR-GA4-PROPERTY-ID"):
    """Runs a report using two date ranges."""
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[
            DateRange(start_date="2019-08-01", end_date="2019-08-14"),
            DateRange(start_date="2020-08-01", end_date="2020-08-14"),
        ],
        dimensions=[Dimension(name="platform")],
        metrics=[Metric(name="activeUsers")],
    )
    response = client.run_report(request)
    print_run_report_response(response)


# [END analyticsdata_run_report_with_date_ranges]


if __name__ == "__main__":
    run_sample(property_id=PROPERTY_ID)