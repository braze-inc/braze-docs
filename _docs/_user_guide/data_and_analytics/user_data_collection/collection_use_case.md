---
nav_title: Collection Use Case
article_title: Collection Use Case
page_order: 3
page_type: reference
description: "This reference article covers an example user data collection use case—how a ride-sharing app might decide what user data to collect."

---

# Collection use case

> This reference article covers an example user data collection use case—how a ride-sharing app might decide what user data to collect.

For this example case, let's consider a taxi or ride-sharing app (such as Uber or Lyft) that wants to decide what user data to collect. The following questions and brainstorming process are a great model for marketing and development teams to follow. By the end of this exercise, both teams should have a solid understanding of what custom events and attributes make sense to collect in order to help meet their goal.

## Case question #1: What is the goal?

Their goal is straightforward in that they want users to hail taxi rides via their app.

## Case question #2: What are the intermediate steps on the way to that goal from app installation?

1. They need users to begin the registration process and fill out their personal information.
2. They need users to complete and verify the registration process by inputting a code into the app they receive via SMS.
3. They need to attempt to hail a taxi.
4. In order to hail a taxi, they must be available when they search.

These actions could then be tagged as the following custom events:

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

After implementing the events, they can run campaigns including the following:

1. Message users who Began Registration, but haven't Completed Registration within a certain time frame.
2. Send congratulation messages to users who Completed Registration.
3. Send apologies and promotional credit to users who had Unsuccessful Taxi Hails, that weren't followed by a Successful Taxi Hail within a certain amount of time.
4. Send promotions to power users with lots of Successful Taxi Hails to thank them for their loyalty.

## Case question #3: What other information might we want to know about our users that will inform our messaging?

- Whether or not they have any promotional credit?
- The average rating they give to their drivers?
- Unique Promo Codes for the user?

These characteristics could then be tagged as the following custom attributes:

- Promotional Credit Balance (Decimal Type)
- Average Driver Rating (Integer Type)
- Unique Promo Code (String Type)

Adding these attributes would allow the ability to send campaigns to users such as:

1. Reminding users who haven't used the app in 7 days and have promotional credit in their account to return to the app and use the credit.
2. Using our message templates and [personalization features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging) to drag the unique promotion code attribute into messaging directed at users.


{% alert important %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events because they are usually the result of misintegration. If you find that this has happened for a legitimate user, reach out to your Braze account manager.
{% endalert %}

