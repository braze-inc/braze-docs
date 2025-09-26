---
nav_title: API use cases
article_title: API Use Cases
description: "Whether you’re a proficient developer or a marketer with minimal developer resources, this reference article is designed to help you understand how to leverage the power of the Braze REST API to accomplish various tasks and enhance your customer engagement strategy."
page_type: reference
page_order: 4.8
---

# API use cases

> The [Braze REST API]({{site.baseurl}}/api/basics/) provides a wide range of endpoints designed to help manage and optimize your customer engagement strategy. In this article, we’ll explore several use cases for each endpoint collection: catalogs, email lists and addresses, export, messages, preference center, SMS, subscription groups, templates, and user data.<br><br>Each section introduces a scenario with a step-by-step guide, code sample, and expected outcome. By the end of this article, you’ll better understand how to use the Braze REST API to enhance your customer engagement efforts.

## Deleting multiple items in a catalog

A new year welcomes new product launches at Kitchenerie, a retail brand specializing in kitchenware. In the Braze dashboard, Kitchenerie has a catalog set up for its dishware collection named "Dishware". This new year also means removing the following products from its dishware collection.

* Plain Bisque
* Pearl Porcelain
* Pink Shimmer

To remove these products from its catalog, Kitchener can use the [`/catalogs/{catalog_name}/items` endpoint]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/) to pass in the item IDs.

Here's the example request:

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

After sending this payload, the following response confirms that the three collections have been successfully removed from Kitchenerie's dishware catalog.

```json
{
  "message": "success"
}
```

## Removing emails from the Braze spam list

At MovieCanon, a streaming services company, the developer team is responsible for periodically auditing its email lists to identify and keep users who are subscribed to its email campaigns. As part of this audit, MovieCanon wants to remove this list of emails from its spam list:

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

To accomplish this task, the developer team will need an API key with the `email.spam.remove` permission to use the `/email/spam/remove` endpoint. This endpoint removes email addresses from the Braze spam list and the spam list maintained by MovieCanon’s email provider.

To send this request, include either a string email address or an array of up to 50 email addresses to modify. Since the list of emails to remove is under 50, MovieCanon can accomplish this task with the following request body:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

After sending this payload successfully, this response confirms the emails have been removed from MovieCanon’s spam list.

```json
{
  "message": "success"
}
```

## Auditing all Canvases

Siege Valley Health is a hospital system that includes 10 operating hospitals and research centers with thousands of patients. Its marketing team wants to compare the Canvases sent to patients to remind them to schedule an appointment for flu shots from the past 3 years of using Braze. Siege Valley Health’s marketing team also wants a quick and efficient way to see both the list of Canvases and the analytics summary.

Let’s dive into how Siege Valley Health can accomplish these two tasks using a combination of endpoints rather than filtering through the Braze dashboard.

For the first task of auditing Canvases, use the [`/canvas/list` endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) to export a list of Canvases that includes the name and tags. Here’s an example request:

{% details Here’s the response that the Siege Valley Health marketing team would receive. %}
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      },
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      },
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

Let’s move on to the next task of viewing the analytics summary for the first Canvas from Siege Valley Health’s list of Canvases. To do so, we would use the [`/canvas/data_summary` endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) with the following request parameters:

* `canvas_id`: "canvas_identifier_2"
* `ending_at`: 2023-07-10T23:59:59
* `starting_at`: 2020-07-10T23:59:59

Here's an example request:

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Checking upcoming scheduled campaigns and Canvases

The busiest time of year is quickly approaching for Flash & Thread, a retail brand that sells clothing and beauty products online and in stores. Its marketing team wants to check the upcoming campaigns and Canvases from the Braze dashboard before March 31, 2024, at 12 pm. This can be accomplished using the [`/messages/scheduled_broadcasts` endpoint]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/). 

Here's the example request:

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

This endpoint will return the list of upcoming campaigns and Canvases. From here, the marketing team can confirm its list of messages by referencing the `name` field for the campaigns and Canvases in the response.

## Viewing an older preference center

PoliterWeekly is a digital magazine whose subscribers are reachable through email. In an effort to better understand its subscribers' user journey, the marketing team wants to review the details for PoliterWeekly’s preference center to check when it was created and last updated.

Using the [`/preference_center/v1/{preferenceCenterExternalID}` endpoint]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/), the marketing team only needs to insert the preference center external ID as the path parameter, which would look like this:

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details Here’s the response the PoliterWeekly marketing team would receive. %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Your preferences have been updated successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

From this response, the marketing team can see the preference center was created 3 years before its most recent update. With this information in mind, the marketing team could create and launch a new preference center.

{% enddetails %}

## Removing invalid phone numbers

At CashBlastr, the primary goal is to streamline how people can send and receive quick payments. As a financial service company, CashBlastr wants to keep its list of phone numbers for its customers up-to-date and accurate. The developer team has been tasked to remove the following list of phone numbers marked as “invalid” so the marketing team’s SMS messages can reach the appropriate CashBlastr customers.

- 12223135467
- 12183095514
- 14235662245
- 14324567892

To send a request with the [`/sms/invalid_phone_numbers/remove` endpoint]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/), the phone numbers must be in an array of strings in [e.164 format](https://en.wikipedia.org/wiki/E.164), with up to 50 phone numbers per request. Because the list doesn’t exceed 50 phone numbers, here’s an example of the request body CashBlastr’s developer team would send:

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

After sending this payload, the following response confirms the invalid phone numbers from CashBlastr have been removed from the Braze invalid list.

```json
{
  "message": "success"
}
```

## Viewing a user's subscription group status

SandwichEmperor is a quick-service restaurant chain in the United States, and its marketing team wants to check the subscription group statuses for a randomized list of its users for SMS. Using the [`/subscription/status/get` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/), SandwichEmperor can accomplish this task for an individual user with the following example request:

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

This endpoint also lists the subscription group statuses of a user for email and can be used to see the subscription group status for multiple users.

## Checking an HTML template for email messaging

At WorkFriends, a social network that helps build connections between workers from different industries, its marketing team is responsible for sending email campaigns to its users. These campaigns often include reminders for local events, weekly newsletters, and profile activity highlights.

In this scenario, WorkFriends has historically used a singular HTML template with its legacy branding. In an effort to align its brand identity, WorkFriends wants to verify if there’s any helpful information in this HTML template to leverage before transitioning to a new template.

{% details Here’s the response that the WorkFriends team would receive. %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

After reviewing this template information, WorkFriends can also use the [`/templates/email/update` endpoint]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) to update the email template through the API. The email template in the Braze dashboard will reflect these edits.
