---
nav_title: User Data Collection
page_order: 3
layout: user_guide
user_top_header: "User Data Collection"
user_top_text: "Before completing your Braze implementation, ensure that you have a conversation between your marketing team and your development team regarding your marketing goals. When deciding what you want to track, and how you want to track it with Braze, it's useful to consider these goals and work backwards from there."

user_featured_title: "Popular Articles"

user_featured_list:
  - name: User Archival Definitions
    link: /docs/user_guide/data_and_analytics/user_data_collection/user_archival/
    fa_icon: fas fa-users
  - name: Data Collected by Default
    link: /docs/user_guide/data_and_analytics/user_data_collection/data_collected_by_default/
    fa_icon: fas fa-chart-bar
  - name: User Profile Lifecycle
    link: /docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
    fa_icon: fas fa-sync

user_menu_title: "More Articles"

user_menu_list:
  - name: Taxi/Ride-Sharing App Use Case
    link: /docs/user_guide/data_and_analytics/user_data_collection/collection_use_case/
    fa_icon: fas fa-taxi
  - name: User Import
    link: /docs/user_guide/data_and_analytics/user_data_collection/user_import/
    fa_icon: fas fa-user
---

Please reference our case of a [Taxi/Ride-Sharing App]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/collection_use_case/#taxiride-sharing-app-use-case) at the end of this guide for an example of this process.

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
