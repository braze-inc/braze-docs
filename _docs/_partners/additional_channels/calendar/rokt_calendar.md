---
nav_title: Rokt Calendar
alias: /partners/rokt_calendar/

description: "This article outlines the partnership between Braze and Rokt Calendar, a dynamic calendar marketing technology that enables brands to push 1:1 events and promotional communications."
page_type: partner

---

# Rokt Calendar

> Rokt Calendar is a dynamic calendar marketing technology that enables brands to push 1:1 events and promotional communications, in the form of calendar events and notifications, across a proprietary network of subscriber calendars.

The Rokt Calendar and Braze integration allows for Rokt Calendar calendar subscribers and associated subscription data to be pushed into Braze.

Customers can use the Braze Canvas to define journey targeting, a segment of your audience, while using the calendar event as a communication method, much in the same way that SMS, email and push notifications are used. Audience segmentation can be done on any of the standard Braze user attributes as well as the custom attributes generated through the calendar subscription.

Rokt Calendar provides Braze customers the ability to align their personalized marketing initiatives and extend personalized content to the end user's Calendar. Thus, making it a more seamless experience for the end user and further develops stickiness with our customers' services. 

{% alert important %}
This partnership is in early access beta. All features may not perform as exactly described. Please reach out to your Braze Account Manager for more information.
{% endalert %}

## Pre-Requisites

| Requirement | Origin  | Description |
| ----------- | ------- | ----------- |
| Rokt Calendar Setup | Rokt Calendar account manager | A client specific Rokt Calendar account will be setup. |
| Rokt Calendar OAuth Credentials | Rokt Calendar account manager | This key will enable you to connect your Braze and Rokt Calendar accounts. It’s setup for each new Braze client and added to ‘Connected content’ in Braze <br> `Manage App Group` > `Connected Content` > `+Add Credential` |
| [Braze REST Endpoint]({{ site.baseurl }}/api/basics?redirected=true#endpoints) | Braze | Your REST Endpoint URL will need to be provided to your Rokt account manager to pass subscriber data into Braze.|
| [Braze REST Endpoint]({{ site.baseurl }}/api/basics?redirected=true#endpoints) | Braze | Your REST Endpoint URL will need to be provided to your Rokt account manager to pass subscriber data into Braze.|
| Braze API Key | Braze | You will need to create a new API Key can be created in the `Developer Console` > `API Settings` > `+Create New API Key` with `users.track` permissions. The Braze API key will need to be provided to your Rokt account manager.|
| External Subscriber ID | Customer | This is the identifier that will be used by the Rokt Calendar subscription process to match the calendar subscriber with the Braze user. This is something that is passed through by the client to Rokt Calendar or email is used.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## API Integration

### Generating/Onboarding Calendar Subscribers

In order to use the calendar as a communication channel within Braze, you must have an existing calendar subscriber audience. A Braze campaign can be used to generate the calendar subscribers from your existing audience through a link in an email, SMS, push, or other channel.  

Your Rokt account manager will provide you with a link to your new calendar which you can incorporate into your Braze campaign or Canvas to generate subscribers to the calendar. One of the three situations may happen:

| Integration State | Subscriber vs. User | Requirements   |
| ----------------  | ---------------- | ---------------- |
| You are an existing Rokt Calendar and Braze customer. <br> _Specifically, your calendar has subscribers and your Braze account has users that pre-date the use of the Braze integration._ | - Calendar subscribers exist. <br> - Braze users exist.| - Matching an identifier at the subscription level to Braze user identifier (for example, by email). <br> - A pre go-live data transfer of subscription data from Rokt Calendar to Braze user profile.|
| You are an existing Braze customer. <br> _Specifically, you do not have a calendar set up with any  subscribers and your Braze account has users that pre-date the use of the Braze integration._ | - No calendar subscribers. <br> - Braze users exist. | As the subscribers will be new, an agreed identifier, common to Braze users will be used.|
| You are neither a Rokt Calendar nor Braze client. <br> _Specifically, the calendar has no subscribers and the Braze account has no users that pre-date the use of the Braze integration._ | - No calendar subscribers. <br> - No Braze users. | As both subscribers and Braze users will be new, an agreed identifier will be assigned to the calendar subscription and Braze user. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
If a subscriber is not a Braze user, Rokt will create a new user. When the user logs into your app, a new Braze profile will also be created. In order to merge these user profiles, you will have to migrate the Rokt created user to the new app-created user through the [`changeUser`]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#assigning-a-user-id) through the SDKs. (Optional) Your team can also choose to delete the orphaned profile (email only profile created by Rokt).
{% endalert %}

### Audience Segmentation in Braze

When Rokt either creates a new user or matches an existing subscriber with a Braze user, Rokt will send the following subscription attributes you can filter within Braze:

| Custom Attribute  | Definition       | Example          |
| ----------------  | ---------------- | ---------------- |
| `calreply:account_code` | Code of the Rokt Calendar account. | `brazetest/f5733866ade2` and `brazetest/ff10919f1078` |
| `calreply:account_id` |Id of the Rokt Calendar account. | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `calreply:account_name` | Name of the Rokt Calendar account. | `Braze Test/f5733866ade2` |
| `calreply:calendar_code` | Code of the Rokt Calendar calendar. | `test-calendar-1/f5733866ade2` |
| `calreply:calendar_id` | Id of the Rokt Calendar calendar. | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `calreply:calendar_title` |Title of the Rokt Calendar calendar. | `Test Calendar 1/f5733866ade2` |
| `calreply:country_code` | Country code related to the created subscription. | `AU/f5733866ade2` |
| `calreply:device_name` | Device type related to the created subscription. | `Desktop/f5733866ade2` |
| `calreply:geo_country` | Country of origin related to the created subscription. | `Australia/f5733866ade2` |
| `calreply:optIn1` | If the user has opted-in to the first of 2 opt-ins related to the created subscription. | `True/f5733866ade2` |
| `calreply:optIn2` | If the user has opted-in to the second of 2 opt-ins related to the created subscription. | `True/f5733866ade2` |
| `calreply:source` | The source of the created subscription. | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `calreply:subscriber_email` | The email address entered by the user during the subscription process. | `test@email.com/f5733866ade2` |
| `calreply:subscription_id` | The subscription Id, serving as a unique identifier, related to the created subscription. | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `calreply:subscription_method` | Subscription method (webcal/Google) related to the created subscription. | `WebCal/f5733866ade2` |
| `calreply:tags` | Calendar tags used  related to the created subscription. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

In addition, Rokt will also trigger a `subscribe` custom event as soon as the user has subscribed to your Rokt calendar that can be used either in Braze segmentation or be used as a trigger for a campaign or Canvas step.

## Using Rokt Calendar in Your Braze Campaigns & Canvases

Within Braze, you can setup a Webhook Campaign or a webhook within a Canvas to either:

- [__Send new personalized event__](#send-a-new-event): This will allow new events to be added to a segment of subscribers’ calendars.
- [__Update personalized event__](#update-an-existing-event): This will allow for an update to be made to an event that has already been added to subscribers’ calendars.

Before you get started, the fields below detail the information that can be customized at the event level.

| Field             | Definition       | Example          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br> _Required._ | A unique identifier for the event to be added or updated | `Event_00001`
| `eventTitle` <br> _Required._ | The title of the event as it would appear in the calendar | Summer Sale 2019
| `eventDescr` | The description of the event as it would appear in the calendar | The sale is on for 3 days, click this link `www.mybusiness.com/sale` to see the offers. |
| `eventLocation` | The location of the event as it would appear in the calendar, note that this is often used as a second call to action which is complementary to the eventTitle. | Braze |
| `eventStart` <br> _Required._  | The start date and time of the event as it would appear in the calendar | `2019-02-21T15:00:00` |
| `eventEnd` <br> _Required._  | The start date and time of the event as it would appear in the calendar | `2019-02-21T16:00:00` |
| `eventTz` <br> _Required._  | The time zone of the event as it would appear in the calendar, note that the list of applicable time zones can be found here. | `Eastern Standard Time.` |
| `notifyBefore` <br> _Required._  | The reminder time of the event as it would appear in the calendar, note that this is expressed in minutes | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Send a New Event

#### Step 1: Create a Webhook Template in Braze

You can create this from the `Templates & Media` section, or create a new Webhook Campaign or Canvas in Braze.

Once you have selected the `Rokt Calendar - New Event` webhook template, you should see the following in the composer:

{% raw %}

| Composer Parameter | Input This Value: |
|---|---|
| `Webhook URL` | `{% assign accountCode = {{custom_attribute.${calreply:account_code}}}[0] | split: '/' | first %}https://api.calreply.net/v1/subscriptionevent/{{accountCode}}`. |
| `Request Body` | Select `Raw Text`. |
| `HTTP Method` | Select `POST`. |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

#### Step 2: Fill Out Your Template

To setup the webhook, fill out the details of the new event within the Request Body.

{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventName %}Event Name{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}10{% endcapture %}
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
  "subscriptionIds": ["{{custom_attribute.${calreply:subscription_id}| join: '","'  }}"]
}
```

{% endraw %}


{% alert tip %}

For a list of valid timezones see [https://roktcalendar-api.readme.io/docs/timezones](https://roktcalendar.readme.io/docs/timezones).

{% endalert %}

#### Step 3: Fill Out Your Request Headers & Select HTTP Method

{% raw %}

| HTTP Header       | Definition       |
| ----------------  | ---------------- |
| Authorization  | Bearer `{% connected_content https://api.calreply.net/oauth2/token :method post :basic_auth {insert credential} :body grant_type=[YOUR_CREDENTIALS] :save token :retry %}{{token.access_token}}` <br> _Note: This is the credential name in the `Manage App Group` > `Connected Content` > `Credential`_ |
| Content-Type  | `application/json` |
{: .reset-td-br-1 .reset-td-br-2}

Ensure that your `HTTP Method` is set to **Post**.

{% endraw %}

#### Step 4: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag.

You should be able to preview your request in the left-hand panel, or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}

Remember to save your template before leaving the page!

{% endalert %}

### Update an Existing Event

#### Step 1: Create a Webhook Template in Braze

You can create this from the `Templates & Media` section, or create a new Webhook Campaign or Canvas in Braze.

Once you have selected the `Rokt Calendar - Update Event` webhook template, input or select the following in the composer:

{% raw %}

| Composer Parameter | Input This Value: |
|---|---|
| `Webhook URL` | `{% assign accountCode = {{custom_attribute.${calreply:account_code}}}[0] | split: '/' | first %}https://api.calreply.net/v1/subscriptionevent/{{accountCode}}/update`. |
| `Request Body` | Select `Raw Text`. |
| `HTTP Method` | Select `POST`. |
{: .reset-td-br-1 .reset-td-br-2}

#### Step 2: Fill Out Your Template

To setup the webhook, fill out the details of the new event within the Request Body:

```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventName %}Event Name{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}10{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
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

For a list of valid timezones see [https://roktcalendar-api.readme.io/docs/timezones](https://roktcalendar.readme.io/docs/timezones).

{% endalert %}


#### Step 3: Fill Out Your Request Headers & Select HTTP Method

{% raw %}

| HTTP Header       | Definition       |
| ----------------  | ---------------- |
| Authorization  | `Bearer {% connected_content https://api.calreply.net/oauth2/token :method post :basic_auth {insert credential} :body grant_type=[YOUR_CREDENTIALS] :save token :retry %}{{token.access_token}}` <br> _Note: This is the credential name in the `Manage App Group` > `Connected Content` > `Credential_` |
| Content-Type  | `application/json` |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

Ensure that your `HTTP Method` is set to **Post**.

#### Step 4: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag.

You should be able to preview your request in the left-hand panel, or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page!
{% endalert %}
