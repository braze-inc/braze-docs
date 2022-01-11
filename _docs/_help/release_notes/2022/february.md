---
nav_title: February
page_order: 11
noindex: true
page_type: update
description: "This article contains release notes for February 2022."
---
# February 2022

## Handling invalid phone numbers
You've encountered a scenario where a user has entered an invalid phone number. Here's your solution! Braze marks these invalid phone numbers and will not attempt to send any further communications to those numbers. Read more on how Braze [handles invalid phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers/).

### New SMS endpoints
You can now manage invalid phone numbers using the new [Braze SMS Endpoints]({{site.baseurl}}/api/endpoints/sms/)! This update features:
- [GET: Query or list invalid phone numbers endpoint]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) returns a list of phone numbers that are considered "invalid" by Braze.
- [POST: Remove invalid phone numbers endpoint]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) allows you to remove the "invalid" phone numbers from Braze's invalid list.

## Rate limits
API rate limits have been included for all [Braze Endpoint articles]({{site.baseurl}}/api/basics/#nav_top_endpoints). You can now easily view the rate limits by request type. For more information on rate limits, check out our article on [API rate limits]({{site.baseurl}}/api/api_limits/).

## New REST endpoint
Braze has added a [new EU-02 REST Endpoint]({{site.baseurl}}/api/basics/#api-definitions).

## About email
Email messages are a great way to connect with your customers. For a quick introduction on how you can customize and leverage email messages, check out our new article on [About email]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/). 

## About in-app messages
In-app messages deliver rich content to your users who are active within your app. You can easily engage with your active customers by creating in-app messges for personalized greetings or feature adoption. To learn about the advantages and message types, check out our new article on [About in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/).