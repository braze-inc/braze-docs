---
nav_title: Pypestream
page_order: 5
description: "Enhance digital engagement with your brand by combining immersive conversational AI from Pypestream with dynamic omnichannel marketing from Braze."
alias: /partners/pypestream/
page_type: partner
---

# Pypestream

> [Pypestream](https://www.pypestream.com) is a full-stack, conversational AI platform offering patented, all-in-one cloud messaging to transform brands into “always-on” digital entities. With Pypestream, brands can now engage in omnichannel conversations at scale with every customer, while leveraging an immersive user experience, advanced NLU capabilities, and real-time integrations to backend systems.

With the Braze-Pypestream partnership, brands can seamlessly orchestrate the end-to-end customer lifecycle from initial outreach, routed into a conversational experience, and through to omnichannel follow-up(s) via intelligent retargeting. Through the course of their conversation with a brand (facilitated via Pypestream), customers are segmented based on their engagement path, preferences, and responses, all of which are sent back to Braze to subsequently retarget those customers appropriately with Canvas. Brands can finally have an all-in-one 360° view of their conversations with their customers across all channels.

## Prerequisites

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Pypestream Subscription | Pypestream | If not already a Pypestream customer, please reach out via Pypestream's [Contact Page](https://www.pypestream.com/contact-us/) | Once subscribed, the Pypestream team will help you set up your dedicated environment to begin building your conversational AI solution to integrate with Braze. |
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | The Braze API Key will be used in the API calls to the Braze REST Endpoint URLs to authenticate the service. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List]({{site.baseurl}}/api/basics/?redirected=true) | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Overview

There are multiple ways to leverage the [Braze API Endpoints]({{site.baseurl}}/api/basics/?redirected=true) when designing a conversational solution using Pypestream. The document outlines what is required to set up the initial integration into the Braze Endpoint using Pypestream’s action node structure. The benefit of action nodes is the flexibility it provides when integrating into a service. Once an action node is instantiated, it provides the flexibility of integrating into any Braze API Endpoint and allows the results to be evaluated in a multitude of ways. 

## Action Node Integration

Pypestream leverages a server-less integration layer to perform custom integrations into various platforms. This layer is used to interface with services or systems to support the data requirements of the conversational flow that is being built. These integrations, which are referred to as Action Node Integrations, are typically written in Python and deployed using the Pypestream platform. The steps below highlight how to utilize an action node to integrate a Pypestream conversational flow into the Braze REST APIs. 

*Note: For an overview and configuration steps for Pypestream action nodes, refer to the [Pypestream documentation](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070). To access the documentation, you must be a Pypestream customer.*

### Step 1: Set Endpoint Configurations

The primary configuration values, such as the **Braze REST Endpoint URL** and the **Braze API Keys**, should be set in the *app.py* file of the solution: 

```
import os

NAME = '{ CUSTOMER NAME }'
BOTS = []
CSV_BOTS = ['{ SOLUTION NAME }']
PATH = os.path.dirname(__file__)

PARAMS = {
    'sandbox': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'

    },
    'prod': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'

    },
}
```

### Step 2: Develop Action Node Template for Integration

Action nodes leverage the environment that the solution is deployed to interact with, with the respective Braze endpoints(s) set in the previous step. This step develops an action node to perform the integration into the specific Braze endpoints. The following template can be used as a guide in developing the integrations: 

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR_REST_API_KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ]
}

Returns
-------
Creates and/or Updates User Details within Braze Dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```
### Step 3: Update the Solution Designs to Leverage Action Node Integration

The final step of integrating with the Braze REST API involves configuring the flows within Pypestream’s [Design Studio](https://platform.pypestream.com/design-studio/) to leverage the action node that was developed in Step 2. 

*Note: For additional information on how to configure nodes within Design Studio, please refer to the [Pypestream documentation](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070). To access the documentation, you must be a Pypestream customer.*

## Example Integration - Track Users for Targeting (User/Track) 

Once the prerequisites are met and an action node structure has been created, the developer has a blank canvas to work from when interacting with the Braze API Endpoints. Listed below are the steps required to integrate an action node into the Braze [User Track Endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) - specifically to create a user profile to track a specific user entering a Pypestream conversational flow:

### Step 1: Collect Data from User in Conversation

When a user enters into a Pypestream session, the specifics of the data collected are entirely dependent on the use case at hand. To be able to create a user profile within Braze, the conversation must collect data to send to Braze via the [User Track Endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). 

For example, if the solution collected the following information from the user during the conversation: 

* First Name
* Last Name
* Email Address
* Date of Birth
* City of Residence
* Operating System

This data can now be sent to the Braze platform to track this user’s engagement with the ability to potentially retarget them in the future. Please check out the use case list to view some common applications.

### Step 2: Populate Data in Action Node Structure

Leveraging the same structure for developing action nodes as outlined above, the data collected from the user can be populated in the action node to be sent to Braze via the [User Track Endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/):

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ],
        "partner" : 'pypestream'
}

Returns
-------
Creates and/or Updates User Details within Braze Dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "first_name": "{ FIRST_NAME }",
                    "last_name": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #custom attributes can be added here as well
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [{
                    "external_id": "{ USER_ID }",
                    "name": "{ NAME_OF_EVENT }",
                    "time": "{ EVENT_TIME }"
                }],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```

### Step 3: Update Solution Flows to Redirect Upon Success/Failure of Action Node

In each solution’s design, the solution designer can route users to nodes based on if the action node API call was successful. If the action node received an error message, the end-user should be handled with care. 

## Use Cases

When it comes to the Braze-Pypestream partnership, the possibilities are nearly endless! We’ve highlighted a few common applications below to summarize the most common ways that brands have leveraged the combined capabilities:
* **Intelligent Retargeting**: Retarget users with Braze Canvas after their conversational engagement with your brand by leveraging all the rich data points collected via Pypestream.<br><br>
* **Dynamic Targeting**: Reach out to existing and prospective customers based on their specific cohorts and segments (as defined with Braze), serving them with tailored conversational experiences via Pypestream.<br><br>
* **Contextual Customer Insights**: Once an end-user (existing or prospective customer) is engaging on your website, combine webpage tags ingested from the Pypestream Event Listener with customer data stored within Braze to provide a fully-personalized and contextual conversational interaction.
