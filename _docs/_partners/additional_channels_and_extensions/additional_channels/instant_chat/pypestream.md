---
nav_title: Pypestream
article_title: Pypestream
description: "This reference article outlines the partnership between Braze and Pypestream, a full-stack conversational AI platform that allows you to enhance digital engagement with your brand."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) is a full-stack, conversational AI platform offering patented, all-in-one cloud messaging to transform brands into "always-on" digital entities. With Pypestream, brands can now engage in omnichannel conversations at scale with every customer while leveraging an immersive user experience, advanced NLU capabilities, and real-time integrations to backend systems.

_This integration is maintained by Pypestream._

## About the integration

The Braze and Pypestream integration allows you to seamlessly orchestrate the end-to-end customer lifecycle from initial outreach, routed into a conversational experience, and through to omnichannel follow-up(s) via intelligent retargeting. 

## Prerequisites

| Requirement | Description |
|---|---|
| Pypestream account | A [Pypestream account](https://www.pypestream.com/contact-us/) is required to take advantage of this partnership.<br><br>Once subscribed, the Pypestream team will help you set up your dedicated environment to begin building your conversational AI solution to integrate with Braze. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

The Braze and Pypestream partnership can be used in your Canvases to achieve common use cases like:
* **Intelligent retargeting**: Retarget users with Braze Canvas after their conversational engagement with your brand by leveraging all the rich data points collected through Pypestream.
* **Dynamic targeting**: Reach out to existing and prospective customers based on their specific cohorts and segments, serving them with tailored conversational experiences through Pypestream.
* **Contextual customer insights**: After an end-user (existing or prospective customer) engages on your website, combine webpage tags ingested from the Pypestream Event Listener with customer data stored within Braze to provide a fully-personalized and contextual conversational interaction.

## Integration

Pypestream leverages a server-less integration layer to perform custom integrations into various platforms. This layer is used to interface with services or systems to support the data requirements of the conversational flow that is being built. These integrations, referred to as Action Node Integrations, are typically written in Python and deployed using the Pypestream platform. After an action node is instantiated, it provides the flexibility of integrating into any Braze API endpoint and allows the results to be evaluated in many ways. 

{% alert note %}
Visit this [Pypestream article](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) for an overview and configuration steps for Pypestream action nodes. You must be a Pypestream customer to access this documentation.
{% endalert %}

### Step 1: Set endpoint configurations

The primary configuration values, such as the Braze REST endpoint URL and the Braze API keys, should be set in the `app.py` file of the solution: 

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

### Step 2: Develop action node template

Action nodes leverage the environment that the solution is deployed to interact with, with the respective Braze endpoints(s) set in the previous step. This step develops an action node to integrate specific Braze endpoints. Use the following template as a guide in developing the integrations: 

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
    "Authorization": "{YOUR-REST-API-KEY}"
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
Creates and/or Updates User Details within Braze dashboard

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
### Step 3: Update the solution designs

The final step of integrating with the Braze REST API involves configuring the flows within Pypestream's [Design Studio](https://platform.pypestream.com/design-studio/) to use the action node that was developed in the previous step. 

{% alert note %}
Visit this [Pypestream article](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) for an overview on how to configure modes within Design Studio. You must be a Pypestream customer to access this documentation.
{% endalert %}

## Integration use case

After the prerequisites are met, and an action node structure has been created, the developer has a blank Canvas to work from when interacting with the Braze API endpoints. This example shows the steps required to integrate an action node into the Braze [`/user/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)-specifically to create a user profile to track a specific user entering a Pypestream conversational flow.

### Step 1: Collect data from the user in conversation

When a user enters into a Pypestream session, the specifics of the data collected are entirely dependent on the use case at hand. To be able to create a user profile within Braze, the conversation must collect necessary fields 
required by the desired endpoint.

For example, if the solution collected the following information from the user during the conversation for the Braze `/user/track` endpoint: 

* First name
* Last name
* Email address
* Date of birth
* City of residence
* Operating system

This data can now be sent to the Braze platform to track this user's engagement with the ability to potentially retarget them in the future. Check out the [use case list](#use-cases) to view common applications.

### Step 2: Populate data in the action node structure

Leveraging the same structure for developing action nodes, the data collected from the user can be populated in the action node to be sent to Braze via our `/user/track` endpoint.

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
Creates and/or Updates User Details within Braze dashboard

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

### Step 3: Update solution flows to redirect upon success/failure of action node

Lastly, in each solution's design, you can route users to nodes based on if the action node API call was successful. If the action node receives an error message, the end-user should be handled with care. 

