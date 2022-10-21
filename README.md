# Gooogle Analytics Reporting API v4 (UA) and Google Analytics Data API (GA4) Demos

## Purpose
This repo has examples of getting started with Reporting API for Universal Analytics and Data API for GA4.

## Credits

The code is taken from the following sources. Please refer to these sources while writing your own code. 

UA: 
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

https://developers.google.com/analytics/devguides/reporting/core/v4/samples#multiple-segments

https://medium.com/analytics-for-humans/submitting-your-first-google-analytics-reporting-api-request-cdda19969940 

GA4: 
https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries 

https://github.com/googleapis/python-analytics-data/tree/main/samples/snippets 

## Set up

### General set up steps

Set up steps are described here:

UA: 
https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

GA4: 
https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries

### Credential file
Make sure you put a JSON service account credential file in the ./sandbox subdirectory. Refereance that file in your code.

The service account should have Viewer access to your UA view and GA4 property. 

### Requirements

pip install -r ua/requirements.txt

pip install -r ga4/requirements.txt