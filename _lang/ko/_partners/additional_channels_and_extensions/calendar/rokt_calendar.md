---
nav_title: Rokt Calendar
article_title: Rokt Calendar
alias: /partners/rokt_calendar/
description: "This reference article outlines the partnership between Braze and Rokt Calendar, a dynamic calendar marketing technology that enables brands to push 1:1 events and promotional communications, in the form of calendar events and notifications."
page_type: partner
search_tag: Partner
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) is a dynamic calendar marketing technology that enables brands to push 1:1 events and promotional communications in the form of calendar events and notifications.

_This integration is maintained by Rokt Calendar._

## About the integration

The Braze and Rokt Calendar integration allows your Rokt Calendar subscribers and their data to be pushed to Braze via Braze webhook. You can then use this data in Braze Canvases for journey targeting and audience segmentation using any of the following custom [Rokt Calendar attributes](#audience-segmentation). 

## Prerequisites

| Requirement  | Description |
| ------------ | ----------- |
| Rokt Calendar account | A client-specific Rokt Calendar account is required to take advantage of this partnership. Contact [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) to speak with an account manager  |
| Rokt Calendar setup | Your Rokt Calendar account manager will work with you to set up the calendar to best suit your needs, including settings like:<br>\- Merge flag<br>\- SubscriberID fallback flag<br>\- Email capture, if needed |
| Rokt Calendar OAuth credentials | This key provided by your Rokt Calendar account manager will enable you to connect your Braze and Rokt Calendar accounts.<br><br>This can be created in the Braze dashboard under **Settings** > **Connected Content**. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. You will need to provide this key to your Rokt Calendar account manager.<br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| [Braze REST endpoint]({{site.baseurl}}/api/basics/#endpoints) | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
| External subscriber ID | This is the identifier used by the Rokt Calendar subscription process to match the calendar subscriber with the Braze user. This is something you pass to Rokt Calendar.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Audience segmentation {#audience-segmentation}

When Rokt Calendar creates a new user or matches an existing subscriber with a Braze user, Rokt Calendar will send the following custom subscription attributes you can filter within Braze:

| Custom attribute  | Definition       | Example          |
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Rokt Calendar will also trigger a `subscribe` custom event as soon as the user has subscribed to your Rokt calendar that can be used either in Braze segmentation or be used as a trigger for a campaign or Canvas component.

## Integration

### Step 1: Building an audience of calendar subscribers

To send calendar events from Canvas, you must first have a Rokt calendar setup with users already subscribed. To do this, you will need to inform your users where and how to subscribe to the calendar. Rokt Calendar recommends that you:

#### Provide subscription integration points
To build an audience of calendar subscribers, you will need to offer a destination to which a user can navigate and subscribe. Some subscription integration point examples include:
  - Add a calendar button to your website
  - Adding a calendar link in an email or SMS 
  - Add  a calendar button to your app
  - Add a calendar link on social media

#### Promote the calendar
To build an audience of subscribers, you'll need to promote the calendar to your audience so that they know how to subscribe. Some calendar promotion examples include:
  - Posts on social media
  - Email newsletters and updates
  - Blog posts
  - In-app notifications

### Step 2: Create a Rokt Calendar webhook in Braze

Within Braze, you can set up a webhook campaign or a webhook within a Canvas to either:

- Send a new personalized event: Allow new events to be added to a segment of subscribers' calendars.
- Update a personalized event: Allow for an update to be made to an existing event in subscribers' calendars.

To create a Rokt Calendar webhook template to use in future campaigns or Canvases, navigate to **Templates** > **Webhook Templates** in the Braze platform. 

If you would like to create a one-off Rokt Calendar webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

{% tabs %}
{% tab Send a new event %}
Once you have selected the Rokt Calendar webhook template, you should see the following:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Request Body**: Raw Text
{% endtab %}
{% tab Update an existing event %}
Once you have selected the Rokt Calendar webhook template, you should see the following:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Request Body**: Raw Text
{% endtab %}
{% endtabs %}

#### Request headers and method

Rokt Calendar requires an `HTTP Header` for authorization that includes your Rokt Calendar Connected Content credential name. The following will already be included within the template as key-value pairs, but in the **Settings** tab, you must replace `<Rokt-Calendar-API>` with the credential name found in `Manage Settings > Connected Content > Credential`.

{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

{% tabs local %}
{% tab Send a new event %}
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
{% endtab %}
{% tab Update an existing event %}
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
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
The following fields include information that can be customized at the event level.

| Field             | Definition       | Example          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***Required** | A unique identifier for the event to be added or updated | `Event_00001`
| `eventTitle` <br>***Required** | The title of the event as it would appear in the calendar | Summer Sale 2019
| `eventDescr` | The description of the event as it would appear in the calendar | The sale is on for three days; click this link `www.mybusiness.com/sale` to see the offers. |
| `eventLocation` | The event's location as it would appear in the calendar, note that this is often used as a second call to action, which is complementary to the eventTitle. | Open the event to get 50% off |
| `eventStart` <br>***Required**  | The start date and time of the event as it would appear in the calendar | `2019-02-21T15:00:00` |
| `eventEnd` <br>***Required**  | The start date and time of the event as it would appear in the calendar | `2019-02-21T16:00:00` |
| `eventTz` <br>***Required**  | The time zone of the event as it would appear in the calendar, note that the list of applicable time zones can be found [here](https://roktcalendar-api.readme.io/docs/timezones). | `Eastern Standard Time` |
| `notifyBefore` <br>***Required**  | The reminder time of the event as it would appear in the calendar, note that this is expressed in minutes | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

{% alert tip %}
For a list of valid time zones, see [https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones).
{% endalert %}

### Step 3: Preview your request

Preview your request in the **Preview** panel or navigate to the **Test** tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

