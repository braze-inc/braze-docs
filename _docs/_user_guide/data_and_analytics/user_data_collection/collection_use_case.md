---
nav_title: Collection Use Case
page_order: 3

page_type: reference
description: "This reference article covers an example user data collection use case—how a ride-sharing app might decide what user data to collect."
tool: Dashboard
---

> This reference article covers an example user data collection use case—how a ride-sharing app might decide what user data to collect.

# Taxi/Ride-Sharing App Use Case

For this example case, let's consider a Taxi/Ride-Sharing app (such as Hailo, Uber, Lyft, etc.) wants to decide what user data to collect. The questions and brainstorming process below are a great model for marketing and development teams to follow. By the end of this exercise, both teams should have a solid understanding of what custom events and attributes make sense to collect in order to help meet their goal.

## Case Question #1: What is the goal?

Their goal is straightforward in that they want users to hail taxi rides via their app.

## Case Question #2: What are the intermediate steps on the way to that goal from app installation?

1. They need users to begin the registration process and fill out their personal information.
2. They need users to complete & verify the registration process by inputting a code into the app they receive via SMS.
3. They need to attempt to hail a taxi.
4. In order to hail a taxi, they must be available when they search.

The above actions could then be tagged as the following custom events:

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

After implementing the events, you can now run the following campaigns:

1. Message users who Began Registration, but didn't Complete Registration within a certain time frame.
2. Send congratulation messages to users who complete registration.
3. Send apologies and promotional credit to users who had unsuccessful taxi hails, that weren't followed by a successful taxi hail within a certain amount of time.
4. Send promotions to power users with lots of Successful Taxi Hails to thank them for their loyalty.
5. Many, Many More.

## Case Question #3: What other information might we want to know about our users that will inform our messaging?

- Whether or not they have any promotional credit?
- The average rating they give to their drivers?
- Unique Promo Codes for the user?

The above characteristics could then be tagged as the following custom attributes:

- Promotional Credit Balance (Decimal Type)
- Average Driver Rating (Integer Type)
- Unique Promo Code (String Type)

Adding these attributes would afford you the ability to send campaigns to users like:

1. Reminding users who haven't used the app in 7 days who have promotional credit remaining on their account that it is there and that they should come back to the app and use it!
2. Use our [message templating and personalization features][13] to drag the unique promo code attribute into messaging directed at users.


{% alert important %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events because they are usually the result of misintegration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager.
{% endalert %}

[13]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging
