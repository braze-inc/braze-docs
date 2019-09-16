---
nav_title: Overview
page_order: 1
---
# User Data Collection

Before completing your Braze implementation, ensure that you have a conversation between your marketing team and your development team regarding your marketing goals. When deciding what you want to track, and how you want to track it with Braze, it's useful to consider these goals and work backwards from there. Please reference our case of a [Taxi/Ride-Sharing App]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/collection_use_case/#taxiride-sharing-app-use-case) at the end of this guide for an example of this process.

This best practice guide will help you to understand exactly what Braze considers to be a "Custom Event" vs. a "Custom Attribute".

# General Best Practices

## Don’t Over-Segment Your Tracking

- Being more generic will help you target more users and draw more useful divisions between user segments
- For example, rather than capturing a separate event for watching each of 50 different movies, it would be more effective to capture simply watching a movie as an event
- If you over segment your user data, your findings will lose statistical significance and won’t guide the development of your app and marketing initiatives as effectively
    - You will “miss the forest for the trees” when evaluating user-trend data
    - Events should be tied directly to your marketing and conversion goals

{% alert tip %}
Multiple user actions within an app can be labeled with the same custom event or attribute designation. This is useful when you want to track something generically such as "played a song" rather than recording each individual song within a music app as a separate and distinct event.
{% endalert %}

{% alert tip %}
__Only update your deltas (changing data)!__

To prevent using up your allocated data points, we recommend setting up a program that will prevent sending the same, unchanging data from your app to Braze over and over.
{% endalert %}

{% alert important %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events, because they are usually the result of misintegration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager.
{% endalert %}
