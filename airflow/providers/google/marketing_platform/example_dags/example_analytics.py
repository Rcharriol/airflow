# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example Airflow DAG that shows how to use Google Analytics 360.
"""
import os

from airflow import models
from airflow.providers.google.marketing_platform.operators.analytics import (
    GoogleAnalyticsListAccountsOperator, GoogleAnalyticsRetrieveAdsLinksListOperator,
)
from airflow.utils import dates

default_args = {"start_date": dates.days_ago(1)}

ACCOUNT_ID = os.environ.get("GA_ACCOUNT_ID", "123456789")
WEB_PROPERTY = os.environ.get("GA_WEB_PROPERTY", "UA-12345678-1")

with models.DAG(
    "example_google_analytics",
    default_args=default_args,
    schedule_interval=None,  # Override to match your needs
) as dag:
    # [START howto_marketing_platform_list_accounts_operator]
    list_account = GoogleAnalyticsListAccountsOperator(task_id="list_account")
    # [END howto_marketing_platform_list_accounts_operator]

    # [START howto_marketing_platform_retrieve_ads_links_list_operator]
    list_ad_link = GoogleAnalyticsRetrieveAdsLinksListOperator(task_id="list_ad_link",
                                                               account_id=ACCOUNT_ID,
                                                               web_property_id=WEB_PROPERTY)
    # [END howto_marketing_platform_retrieve_ads_links_list_operator]
