---
nav_title: User Profiles
article_title: User Profiles
page_order: 5
page_type: reference
tool: 
  - Dashboard
description: "This reference article describes how to access a user's profile in the dashboard, profile use cases, and what each profile contains."

---

# User profiles

> This reference article describes how to access user profiles in the dashboard, the different components involved in a user profile, and showcases some examples of how you can use user profiles to troubleshoot campaigns.

User profiles are a great way to find information about specific users. All persistent data associated with a user is stored in their user profile.

## Access profiles

To access a user's profile, go to the **User Search** page and search for a user by any of the following:

- External user ID
- Email
- Phone number
- Push token

If a match is found, you can view the information that you've recorded for this user with the Braze SDK.

Most searches return one user profile. However, if you search for an email that belongs to more than one user, all user profiles that match that email will be returned. If you do enter a non-unique email, click **Next** to view the other profiles that are associated with that email.

![Search results with a banner that reads "Multiple users match your search criteria" and two buttons labelled Previous and Next.][1]

## Use cases

User profiles are a great resource for troubleshooting and testing because you can easily access information about a user's engagement history, segment membership, device, and operating system.

For example, if a user reports a problem and you aren't sure what device and operating system they are using, you can use the [Overview tab](#overview-tab) to find this information (as long as you have their email or user ID). You can also view a user's language, which could be helpful if you are troubleshooting a [multi-lingual campaign][13] that didn't behave as expected.

You can use the [Engagement tab](#engagement-tab) to verify whether a certain user received a campaign. In addition, if this particular user did receive the campaign, you can see when they received it. You can also verify whether a user is in a certain segment, and whether a user is opted in to push, e-mail, or both. This information is useful for troubleshooting purposes. For example, you should check this information if a user doesn't receive a campaign that you expected them to receive or receives a campaign that you did not expect them to receive.

## Elements of user profile

There are four main sections of a user's profile.

- **Overview:** Basic information about the user, session data, custom attributes, custom events, purchases, and the most recent device that the user logged into.
- **Engagement:** Information about the user's contact settings, campaigns received, segments, communication stats, install attribution, News Feed cards clicked, and random bucket number.
- **Social:** High-level view of the user's activity on Twitter and Facebook, if connected.
- **Messaging History:** Recent messaging-related events for this user from the past 30 days.

### Overview tab {#overview-tab}

The **Overview** tab contains basic information about a user and their interactions with your app or website.

| Overview category | Contains |
| --- | --- |
| Profile | Gender, age group, location, language, locale, time zone, and birthday. |
| Sessions overview | How many sessions they had, when their first and last session was, and on which apps. |
| Custom attributes | Which custom attributes are attributed to this user and their associated value. |
| Recent devices | How many devices they logged in on, details on each device, and their associated advertising IDs (if any). |
| Custom events | Which custom events this user has performed, how many times, and when they last performed each event. |
| Purchases | Lifetime revenue attributed to this user, their last purchase, total number of purchases, and a list of each purchase. |
{: .reset-td-br-1 .reset-td-br-2}

For more information on this data, see [User Data Collection][12].

![][8]

### Engagement tab {#engagement-tab}

The **Engagement** tab contains information about a user's interactions with the messages you sent them using Braze.

| Engagement category | Contains |
| --- | --- |
| Contact settings | Subscription status for email, SMS, and push, and the subscription groups this user is associated with for these three channels. This section also includes changelog information for push tokens.
| Campaigns received | Campaigns this user has received and when. Select a campaign from the list to view it. |
| Segments | Segments this user is included in. Select a segment from the list to view it. |
| Communication stats | When this user has last received messages from you from each channel. |
| News Feed cards clicked | News Feed cards this user has clicked on. Select a card from the list to view it. |
| Install attribution | Information about how and when a user installed your app. Learn more about [understanding user installs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Miscellaneous | The user's [random bucket number]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/). |
| Canvas messages received | Canvas messages this user has received and when. Select a message from the list to view it. |
| Predictions | [Churn Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn) and [Purchase Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases) scores for this user. |
{: .reset-td-br-1 .reset-td-br-2}

![][9]

### Social tab

The **Social** tab contains a high-level view of the user's activity on Twitter and Facebook, if these platforms are connected.

| Social category | Contains |
| --- | --- |
| Twitter | Twitter username, number of followers, number of users they're following, and number of tweets. |
| Facebook | Facebook posts this user has liked. |
{: .reset-td-br-1 .reset-td-br-2}

### Messaging History tab


[1]: {% image_buster /assets/img_archive/profiles_multiple_results.png %}
[7]: {% image_buster /assets/img_archive/user_search2.png %}
[8]: {% image_buster /assets/img_archive/user_profile2.png %}
[9]: {% image_buster /assets/img_archive/User_Profile_Engagement.png %}
[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
