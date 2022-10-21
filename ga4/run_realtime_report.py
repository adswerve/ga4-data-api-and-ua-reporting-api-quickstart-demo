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

"""Google Analytics Data API sample application demonstrating the creation of
a realtime report.

See https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runRealtimeReport
for more information.
"""
# [START analyticsdata_run_realtime_report]
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunRealtimeReportRequest

from run_report import print_run_report_response

import os

KEY_FILE_LOCATION = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "../sandbox", "adswerve-ts-content-marketing-sa.json"))
PROPERTY_ID = "206551716"

def run_sample(property_id = "YOUR-GA4-PROPERTY-ID", credentials_json_path=""):
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    run_realtime_report(property_id, credentials_json_path)


def run_realtime_report(property_id="YOUR-GA4-PROPERTY-ID", credentials_json_path=""):
    """Runs a realtime report on a Google Analytics 4 property."""
    client = BetaAnalyticsDataClient().from_service_account_json(credentials_json_path)

    request = RunRealtimeReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
    )
    response = client.run_realtime_report(request)
    print_run_report_response(response)


# [END analyticsdata_run_realtime_report]


if __name__ == "__main__":
    run_sample(property_id = PROPERTY_ID, credentials_json_path=KEY_FILE_LOCATION)