---
nav_title: Braze Data Transformation
permalink: "/data_transformation/"
hidden: true
---

# Braze data transformation

Data transformation at Braze allows you to set up and automate a direct integration from various external platforms to Braze by using webhooks. Once these webhooks are sent to Braze, they can be transformed into relevant user data, such as attributes, events, or purchases on Braze user profiles. You can then use this user data to power your marketing use cases.

{% alert important %}
Data transformation is currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

The result of using data transformation is a low-code solution for building integrations between your desired external platform and Braze. This can help replace your team's dependency on making manual API calls, integration tools, or customer data platform tools.

## How it works

![A source platform external to Braze flows into Braze using webhooks using data transformation updates user profiles.][8]

In Braze, you will first define a transformation, which is a mapping between the expected contents of an incoming webhook and Braze attributes, events, or purchases. You can mix and match what the webhook provides with how you want it to appear in Braze. To help you with this, you can define the transformation side-by-side with a recently received webhook.

Once your transformation is defined, you can configure your external platform's webhooks to send directly to Braze. Your transformation will apply to every webhook ingested, and your direct integration is complete.

{% alert important %}
As of December 2022, the Data Transformation team will review and approve submitted transformations.
{% endalert %}

## Creating a transformation

First, identify an external platform you want to connect to Braze. Check that the platform offers webhooks or API notifications. Next, follow these steps to create a data transformation with Braze.

1. Navigate to the Braze dashboard, and select the **Transformations** page under the **Data** section in the left navigation bar. Click **Create Transformation**.![][5]<br><br>
2. Using a sample webhook payload from your external platform. We recommend sending a test webhook to Braze. On your external platform, enter the webhook URL as the destination. If prompted, choose a non-authenticated POST request. If the external platform has a "test send" capability, use it and hit **Refresh** in Braze to display what Braze just received.<br><br>
3. Find the fields that would map to the following Braze fields:
- A Braze user (`external_id`, `user_alias`, `braze_id`, or `email`)
- Custom attributes (optional)
- Custom events (optional)
- Purchase events (optional)<br><br>
For example in this sample payload, `user_id` is the match to Braze's `external_id`, and a a webhook field is set as a Braze custom attribute:<br>![][2]<br><br>
4. Back on the Braze transformation details page, write your transformation that maps the values from your platform to Braze. For example, `user_id` can be mapped to Braze's `external_id`. You can use square brackets to reference items in the webhook.<br><br>In the sample payload, a transformation like this would achieve the desired mapping from the previous step:
- `user_id` as Braze's `external_id`
- `form_response.answers[0].text` as a custom attribute<br>![][7]
<br><br>
5. Click **Submit for Approval**, and your transformation will be sent to the Braze Data Transformation team for review. After receiving approval, you can enable the webhooks from your external platform.

## Use case

Let's say there's an online form-building and survey software company. Using a combination of webhooks and data transformation, you can direct the webhooks directly to Braze every time a survey is submitted. Here are more use cases to consider.

- Sync the event of a user completing the survey as a Braze custom event. This allows you to identify and retarget users who didn't complete the survey.
- Sync the answers submitted in a survey as custom attributes. A customer's answers are valuable first-party data that can power personalized messaging experiences for future use.

## Writing your transformation

The code you write for data transformation must return a Hash object in the format accepted by the `/users/track` endpoint. 

Any feature supported in `/users/track` is supported by data transformation, including the user attributes objects, event objects, and purchase objects. Nested attributes and event properties are also supported. Transformations are given access to a "payload" variable.

{% alert note %}
Braze data transformation currently accepts code in the Ruby programming language. Any standard Ruby control flow, such as if/else logic, is supported.
{% endalert %}

Here is a default template that includes attributes, events, and purchases to get you started:

```
return {
	"attributes": [ 
	{
		"external_id": payload["user_id"],
		"_update_existing_only" : true,
		"attribute_1": payload["attribute_1"]
	}
	],
	"events": [
	{
		"external_id": payload["user_id"],
		"_update_existing_only" : true,
		"name": payload["event_1"]",
		"time": Time.now,
		"properties": {
			"property_1": payload["event_1"]["property_1"]
		}
	}  
	],
	"purchases": [
	{
		"external_id": payload["user_id"],
		"_update_existing_only" : true,
		"product_id": payload["product_id"],
		"currency": payload["currency"],
		"price": payload["price"],
		"quantity": payload["quantity"],
		"time": payload["timestamp"],
		"properties": {
			"property_1": payload["purchase_1"]["property_1"]
		}
	}
  ]
}'
```

## Additional examples

Consider this sample payload from the survey platform Typeform, which fires whenever a survey response is received.

![][3]

{% tabs local %}
{% tab Basic transformation %}

This simple use case takes some of those answers as attributes and writes an event to indicate that the survey was completed:

```
{
  "attributes": [ 
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_rating": payload["form_response"]["answers"][1]["number"],
    }
  ],
   "events": [ 
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
```
{% endtab %}
{% tab Intermediate transformation %}

This intermediate use case builds on the simple use case by introducing an if statement on one of the answers to categorize the user.

```
if
payload["form_response"]["answers"][1]["number"] < 7
NPS_category == "Detractor"
elsif
payload["form_response"]["answers"][1]["number"] == 7 
payload["form_response"]["answers"][1]["number"] == 8
NPS_category == "Passive"
elsif
payload["form_response"]["answers"][1]["number"] > 8
NPS_category == "Promoter"
end

{
  "attributes": [ 
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_NPS_category": NPS_category
    }
  ],
  "events": [
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
```
{% endtab %}
{% tab Advanced transformation %}

This advanced use case involves the scenario where the survey response could come from a user that does not yet exist in Braze. To solve this, the `get_user_by_email` helper function is used.

If the user exists, the existing profile is updated. If the user does not, a new alias-only user is created.

```
user = get_user_by_email(payload["form_response"]["hidden"]["email_address"])
#get_user_by_email is a Braze function that takes an email_address to see if any Braze user profiles return.
#If a profile is returned, you have the entire user object to work with (see our /export/ids documentation).
#If multiple profiles with the same email exist, we will randomly return one user object for you to work with.


if user
braze_id = user["braze_id"]
{
  "attributes": [ 
    {
      "braze_id": braze_id,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_rating": payload["form_response"]["answers"][1]["number"]
    }
  ],
  "events": [
    {
      "braze_id": braze_id,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
else
{
  "attributes": [ 
    {
      "user_alias": { "alias_label": "email", "alias_name": payload["form_response"]["hidden"]["email_address"] },
      "_update_existing_only": false,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_rating": payload["form_response"]["answers"][1]["number"]
    }
  ],
  "events": [
    {
      "user_alias": { "alias_label": "email", "alias_name": payload["form_response"]["hidden"]["email_address"] },
      "_update_existing_only": false,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
End
```
{% endtab %}
{% endtabs %}

## About helper functions

`get_user_by_email(email)` is a helper function that you can call in your transformation code to turn an email address into a Braze user profile object. This can help when an external platform sends an email address as an identifier.

**Input:** `get_user_by_email(email)` works by accepting a string email address as an input within the parentheses. You can template in the incoming webhook's email field within the parentheses. For example, ```get_user_by_email(payload["email_address"])```.

If a Braze profile exists with that email address, the [entire user export object]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#sample-user-export-file-output) is returned as a Hash. Any field in the user export object is available for use. If multiple profiles exist with the same email, only one user export object is returned.

**Output:** For example, if you had ```user = get_user_by_email(payload["email_address"])``` and a profile exists for that email address, the user will contain the entire user export object. So, `user["braze_id"]` will return the `braze_id` of the matching user. If a profile does not exist with that email address, the user will be `nil`.

You can also use if/else logic in your transformation to perform one action if a user with the email address exists, where

- ```User["braze_id"].present?```
- ```!user["braze_id"].nil?``` OR
- ```user["braze_id"] != nil)```

And another action if no user exists with that email address, where
- ```user["braze_id"].nil?``` or 
- ```user["braze_id"] == nil)```

See "Advanced Transformation" under [Additional examples](#additional-examples) for an example of this.

## Frequently asked questions

#### What gets synced with data transformation?

Any data the external platform makes available in a webhook can be synced to Braze. The more an external platform sends via webhooks, the more options there are for choosing what gets synced.

#### I'm a marketer. Do I need developer resources to use data transformation?

While we would love for developers to use this feature as well, you don't need to be one to use this! We've seen marketers successfully set up transformations without developer resources.

#### Can I still use data transformation if my external platform only gives a user's email address in their webhooks without a matching user ID to Braze?

Yes. In your transformation, you can use the `get_user_by_email` function to have Braze take an email address and return a user profile for you to map to. Check out the example for advanced transformation.

#### How do I check that my data transformation is correct?

Share your transformation code draft with the Braze Data Transformation team at [data-transformation@braze.com](mailto:data-transformation@braze.com). 


[1]: {% image_buster /assets/img_archive/data_transformation1.png %}
[2]: {% image_buster /assets/img/data_transformation/data_transformation1.jpg %}
[3]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}
[5]: {% image_buster /assets/img/data_transformation/data_transformation4.png %}
[6]: {% image_buster /assets/img/data_transformation/data_transformation5.png %}
[7]: {% image_buster /assets/img/data_transformation/data_transformation6.jpg %}
[8]: {% image_buster /assets/img/data_transformation/data_transformation7.png %}
