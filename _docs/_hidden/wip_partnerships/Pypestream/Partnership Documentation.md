---
nav_title: Pypestream
page_order: 1

description: "Enhance digital engagement with your brand by combining immersive conversational AI from Pypestream with dynamic omnichannel marketing from Braze."
alias: /partners/pypestream/

page_type: partner
hidden: true
---

# Pypestream

> Pypestream is a full-stack, conversational AI platform offering patented, all-in-one cloud messaging to transform brands into “always-on” digital entities. With Pypestream, brands can now engage in omnichannel conversations at scale with every customer, while leveraging an immersive user experience, advanced NLU capabilities, and real-time integrations to backend systems. Please visit www.pypestream.com for more information.

With the Braze-Pypestream partnership, brands are able to seamlessly orchestrate the end-to-end customer lifecycle from initial outreach, routed into a conversational experience, and through to omnichannel follow-up(s) via intelligent retargeting. In addition to higher click rates with Braze’s hyper-personalized cross-channel personalization, engagement and conversion rates improve markedly for engagements within Pypestream’s conversational interface, when compared to traditional websites and online forms. Through the course of their conversation with a brand (facilitated via Pypestream), customers are segmented based on their engagement path, preferences and responses, all of which are sent back to Braze as the system of record to subsequently retarget those customers appropriately with Canvas. Brands can finally have an all-in-one 360° view of their conversations with their customers across all channels.

## Requirements or Pre-Requisites

In order to integrate Pypestream with Braze, you'll first need a subscription to the Pypestream platform. If you are not already already a Pypestream customer, please contact the team directly via https://www.pypestream.com/contact-us/ and mention your desire to leverage the Braze integration in order to take advantage of the partnership in place between both companies. Once you have subscribed to Pypestream, the team will help to set you up with your own dedicated enviroment to being building your Pypestream conversational AI solution to integrate with Braze.

Included below are the additional details specific to both Braze and Pypestream that will be needed to integrate both platforms.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | The Braze API Key will be used in the API calls to the Braze REST Endpoint URLs to authenticate the service. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List](https://www.braze.com/docs/api/basics/?redirected=true) | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |

## Action Node Integration

Pypestream leverages a server-less integration layer to perform custom integrations into various platforms. This layer is used to interface with various services and/or systems to support the data requirements of the conversational flow that is being built. These integrations, which are referred to as Action Node Integrations, are typically written in Python and deployed using the Pypestream platform. The steps below highlight how to utilize an action node to integrate a Pypestream conversational flow into the Braze REST APIs. 

*Note: For an overview and configuration steps for Pypestream action nodes, refer to the [Pypestream documentation](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070). In order to access the documentation, you must be a Pypestream customer*

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

Action nodes will leverage the environment that the solution is deployed to interact with the respective Braze endpoint(s) set in Step 1. The next step is to develop an action node to perform the integration into the specific Braze endpoints. The following template can be used as a guide to developing the integrations: 

```

# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
action node script
for braze integration

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

Creates and/or updates user details within Braze dashboard

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

The final step of integrating with the Braze REST API Endpoints involves configuring the flows within Pypestream’s [Design Studio](https://platform.pypestream.com/design-studio/) to leverage the action node that was developed in Step 2. 

For additional information on how to configure action nodes within Design Studio, please refer to the [Pypestream documentation](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070). Note: In order to access the documentation, you must be a Pypestream customer*

## Customization

There are multiple ways to leverage the [Braze API Endpoints](https://www.braze.com/docs/api/basics/?redirected=true) when designing a conversational solution using Pypestream. This documentation outlines the steps required to set up the initial integration into the Braze Endpoint using Pypestream’s action node structure. The benefit of action nodes is the flexibility it provides when integrating into a service. Once the action node is instantiated, one has the flexibility of integrating into any Braze API Endpoint and evaluating the results in a multitude of ways. 

In the next section, we’ll discuss in more depth how to leverage an action node to integrate into the Braze [User Track Endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) to track and retarget users entering a Pypestream conversational flow.

## Example Integration - Track Users for Targeting with User Track API Endpoint

Once the prerequisites are met and an action node structure has been created, the developer has a blank canvas to work from when interacting with the Braze API Endpoints. The following outlines in detail the steps required to integrate an action node into the Braze Braze [User Track Endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) - specifically to create a user profile to track a specific user entering a Pypestream conversational flow:

### Step 1: Collect Data from User in Conversation

When a user enters into a Pypestream session, the specifics of the data collected are entirely dependent on the use case at-hand. To be able to create a user profile within Braze, the conversation must collect data to send to Braze via the User Track Endpoint. 

For example, if the solution collected the following information from the user during the conversation: 

* First Name
* Last Name
* Email Address
* Date of Birth
* City of Residence
* Operating System

This data can now be sent to the Braze platform to track this user’s engagement, with the ability to potentially retarget them in the future (for additional use case information, please see the Use Cases section below).

### Step 2: Populate Data in Action Node Structure

Leveraging the same structure for developing action nodes as outlined above, the data collected from the user can be populated in the action node to be sent to Braze via the User Track Endpoint:

```

# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
action node script
for braze integration

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

Creates and/or updates user details within Braze dashboard

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

In each solution’s design, the solution designer has the ability to route users to nodes based on if the action node API call was successful or not. If the action node received an error message, the end-user should be handled with care. 

## Use Cases

When it comes to the Braze-Pypestream partnership, the possibilities are nearly endless! That said, we’ve highlighted a few common applications below to summarize the most common ways that brands have leveraged the combined capabilities:
* **Intelligent Retargeting**: Retarget users with Braze Canvas after their conversational engagement with your brand by leveraging all the rich data points collected via Pypestream.
* **Dynamic Targeting**: Reach out to existing and prospective customers based on their specific cohorts and segments (as defined with Braze), serving them with tailored conversational experiences via Pypestream.
* **Contextual Customer Insights**: Once an end-user (existing or prospective customer) is engaging on your website, combine webpage tags ingested from the Pypestream Event Listener with customer data stored within Braze to provide a fully-personalized and contextual conversational interaction.



[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
