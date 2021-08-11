---
nav_title: Rokt Calendar
alias: /partners/rokt_calendar/

description: "This article outlines the partnership between Braze and Rokt Calendar, a dynamic calendar marketing technology that enables brands to push 1:1 events and promotional communications."
page_type: partner
---

# Rokt Calendar

> Rokt Calendar is a dynamic calendar marketing technology that enables brands to push 1:1 events and promotional communications, in the form of calendar events and notifications, across a proprietary network of subscriber calendars.

The Rokt Calendar and Braze integration allow for Rokt Calendar calendar subscribers and associated subscription data to be pushed into Braze.

Customers can use the Braze Canvas to define journey targeting, a segment of your audience, while using the calendar event as a communication method, much in the same way that SMS, email, and push notifications are used. Audience segmentation can be done on any of the standard Braze user attributes as well as the custom attributes generated through the calendar subscription.

Rokt Calendar provides Braze customers the ability to align their personalized marketing initiatives and extend personalized content to the end user's Calendar. Thus, making it a more seamless experience for the end user and further develops stickiness with our customers' services. 

## Prerequisites

| Requirement | Origin | Who | Description |
| ----------- | -------| --- | ----------- |
| Rokt Calendar Account | Rokt Calendar | Rokt Calendar Account Manager | A client-specific Rokt Calendar account will be set up. |
| Calendar Setup | Rokt Calendar | Rokt Calendar Account Manager |  A Calendar will be set up to reflect the needs of the client's context and settings: <br>- Merge Flag<br>- SubscriberID fallback flag<br>- Email Capture if Needed |
| Rokt Calendar OAuth Credentials | Rokt Calendar | Rokt Calendar Account Manager | This key will enable you to connect your Braze and Rokt Calendar accounts. It’s set up for each new Braze client and added to ‘Connected Content’ in Braze. <br><br> `Manage Settings` > `Connected Content` > `+Add Credential` |
| Braze API Key and Permissions | Braze | Customer | Each app has its own set of REST API Keys. You will need to create a new API Key can be created in the `Developer Console` > `API Settings` > `+Create New API Key` with `users.track` permissions. <br>The Braze API key will need to be provided to your Rokt Account Manager.|
| External Subscriber ID | Customer | Customer | This is the identifier that will be used by the Rokt Calendar subscription process to match the calendar subscriber with the Braze user. This is something that is passed through by the client to Rokt Calendar or email is used.|
| Webhook Setup | Rokt Calendar | Rokt Calendar Account Manager |  Add the Braze webhook type to the management center using your [Braze Endpoint]({{site.baseurl}}/api/basics?redirected=true#endpoints) and REST API Key |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## API Integration

### Building an Audience of Calendar Subscribers

In order to send calendar events from Canvas using the Rokt Calendar integration, it is required that you have a Rokt Calendar setup and users have subscribed to the calendar. To do this, you'll need to inform your users where and how to subscribe to the calendar.

| Requirement | Origin | Who | Description |
| ----------- | ------ | --- | ----------- |
| Rokt Calendar Account Setup | Rokt Calendar | Rokt Calendar Account Manager | A client-specific Rokt Calendar account will be set up, please contact [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) to speak with an account manager |
| Rokt Calendar Calendar Setup | Rokt Calendar | Rokt Calendar Account Manager | A calendar will be set up to reflect the needs of the client. The account manager will work with you to set up the calendar to best suit your needs. |
| Provide Subscription Integration Points | Customer | Customer | In order to build an audience of calendar subscribers, you’ll need to offer a destination to which the user can navigate and subscribe to the calendar.<br><br>Subscription integration point examples:<br>- Add to calendar button to your website<br>- Add to calendar button to your app<br>- Add to calendar link in an email or SMS<br>- Add to calendar link on social media<br> |
| Promote the Calendar | Customer | Customer | In order to build an audience of calendar subscribers, you’ll need to promote the calendar to your audience so that they know where/how to subscribe. <br><br>Calendar promotion examples:<br>- Posts on social media<br>- Email newsletters and updates<br>- Blog posts<br>- In-app notifications |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Audience Segmentation in Braze

When Rokt either creates a new user or matches an existing subscriber with a Braze user, Rokt will send the following subscription attributes you can filter within Braze:

| Custom Attribute  | Definition       | Example          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Code of the Rokt Calendar account | `brazetest/f5733866ade2` and `brazetest/ff10919f1078` |
| `rokt:account_id` |ID of the Rokt Calendar account | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Name of the Rokt Calendar account | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Code of the Rokt Calendar calendar | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID of the Rokt Calendar calendar | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Title of the Rokt Calendar calendar | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Country code related to the created subscription | `AU/f5733866ade2` |
| `rokt:device_name` | Device type related to the created subscription | `Desktop/f5733866ade2` |
| `rokt:geo_country` | Country of origin related to the created subscription | `Australia/f5733866ade2` |
| `rokt:optIn1` | If the user has opted-in to the first of 2 opt-ins related to the created subscription | `True/f5733866ade2` |
| `rokt:optIn2` | If the user has opted-in to the second of 2 opt-ins related to the created subscription | `True/f5733866ade2` |
| `rokt:source` | The source of the created subscription | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | The email address entered by the user during the subscription process | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | The subscription ID, serving as a unique identifier, related to the created subscription | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Subscription method (webcal/Google) related to the created subscription. | `WebCal/f5733866ade2` |
| `rokt:tags` | Calendar tags used  related to the created subscription. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

In addition, Rokt will also trigger a `subscribe` custom event as soon as the user has subscribed to your Rokt calendar that can be used either in Braze segmentation or be used as a trigger for a campaign or Canvas step.

## Using Rokt Calendar in Your Braze Campaigns & Canvases

Within Braze, you can set up a webhook campaign or a webhook within a Canvas to either:

- __Send new personalized event__: This will allow new events to be added to a segment of subscribers’ calendars.
- __Update personalized event__: This will allow for an update to be made to an event that has already been added to subscribers’ calendars.

Before you get started, the fields below detail the information that can be customized at the event level.

| Field             | Definition       | Example          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>*__Required__ | A unique identifier for the event to be added or updated | `Event_00001`
| `eventTitle` <br>*__Required__ | The title of the event as it would appear in the calendar | Summer Sale 2019
| `eventDescr` | The description of the event as it would appear in the calendar | The sale is on for 3 days, click this link `www.mybusiness.com/sale` to see the offers. |
| `eventLocation` | The location of the event as it would appear in the calendar, note that this is often used as a second call to action which is complementary to the eventTitle. | Open the event to get 50% off |
| `eventStart` <br>*__Required__  | The start date and time of the event as it would appear in the calendar | `2019-02-21T15:00:00` |
| `eventEnd` <br>*__Required__  | The start date and time of the event as it would appear in the calendar | `2019-02-21T16:00:00` |
| `eventTz` <br>*__Required__  | The time zone of the event as it would appear in the calendar, note that the list of applicable time zones can be found [here](https://roktcalendar-api.readme.io/docs/timezones). | `Eastern Standard Time` |
| `notifyBefore` <br>*__Required__  | The reminder time of the event as it would appear in the calendar, note that this is expressed in minutes | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% tabs %}
{% tab Send a New Event %}
## Send a New Event

### Step 1: Create a Webhook Template in Braze

To create a new Rokt Calendar Webhook Template you can either navigate to **Templates & Media** or create a new webhook campaign via the Dashboard. 

From the list of Templates, select **Blank Template**.

### Step 2: Fill Out Your Template

The Blank Webhook template consists of two main components, the compose and settings tab. Below we will break down the components of each tab and what settings you should set.

#### Step 2a: Webhook - Settings

Navigate to the settings tab and edit the __Request Header__ and __HTTP Method__ fields with the corresponding text segments.

| Request Headers         |
| ----------------  | ---------------- |
| Authorization  | {% raw %}Bearer {% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth Rokt-Calendar-API :body grant_type=client_credentials :save token :retry %}{{token.access_token}}{% endraw %} <br><br> Note: __Rokt-Calendar-API__ should be replaced with the credential name found in `Manage Settings` > `Connected Content` > `Credential` |
| Content-Type  | application/json |
{: .reset-td-br-1 .reset-td-br-2}

| HTTP Method |
| ----------- |
| POST |
{: .reset-td-br-1 .reset-td-br-2}

#### Step 2b: Webhook - Compose

Complete the setup by navigating to the Compose tab and define the __Webhook URL__ and edit the contents of the __Request Body__ based on the attribute and field tables shown above. 

| Webhook URL | 
| ----------- |
| {% raw %}{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] &#124; split: '/' &#124; first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}} {% endraw %} |
{: .reset-td-br-1}

##### Request Body

{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}

{% alert tip %}

For a list of valid time zones see [https://roktcalendar-api.readme.io/docs/timezones](https://roktcalendar.readme.io/docs/timezones).

{% endalert %}

### Step 3: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag.

You should be able to preview your request in the left-hand panel or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

Remember to save your template before leaving the page!

{% endtab %}
{% tab Update to Existing Event %}

## Update an Existing Event

### Step 1: Create a Webhook Template in Braze

To create a new Rokt Calendar Webhook Template you can either navigate to **Templates & Media** or create a new webhook campaign via the Dashboard. 

From the list of Templates, select **Blank Template**.

### Step 2: Fill Out Your Template

The Blank Webhook template consists of two main components, the compose and settings tab. Below we will break down the components of each tab and what settings you should set.

#### Step 2a: Webhook - Settings

Navigate to the settings tab and edit the __Request Header__ and __HTTP Method__ fields with the corresponding text segments.

| Request Headers       |        |
| ----------------  | ---------------- |
| Authorization  | {% raw %}Bearer {% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth Rokt-Calendar-API :body grant_type=client_credentials :save token :retry %}{{token.access_token}}{% endraw %} <br><br> Note: __Rokt-Calendar-API__ should be replaced with the credential name found in `Manage Settings` > `Connected Content` > `Credential` |
| Content-Type  | application/json |
{: .reset-td-br-1 .reset-td-br-2}

| HTTP Method |
| ----------- |
| POST |
{: .reset-td-br-1}

#### Step 2b: Webhook - Compose

Complete the setup by navigating to the Compose tab and define the __Webhook URL__ and edit the contents of the __Request Body__ based on the attribute and field tables shown above. 

| Webhook URL |
| ----------- |
| {% raw %}{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] &#124; split: '/' &#124; first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update {% endraw %} |
{: .reset-td-br-1}

##### Request Body
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }

```
{% endraw %}

{% alert tip %}

For a list of valid time zones see [https://roktcalendar-api.readme.io/docs/timezones](https://roktcalendar-api.readme.io/docs/timezones).

{% endalert %}

### Step 3: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag.

You should be able to preview your request in the left-hand panel or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

Remember to save your template before leaving the page!

{% endtab %}
{% endtabs %}
