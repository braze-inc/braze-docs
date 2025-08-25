---
nav_title: Users and Segments
article_title: Getting Started&#58; Users and Segments
page_order: 2
page_type: reference
description: "This article provides an overview of users and segments, outlining their significance and how they can be leveraged to engage your audience."

---

# Getting Started: Users and segments

Understanding your users and effectively targeting them is crucial for sending personalized and targeted marketing campaigns. This article provides an overview of users and segments, outlining their significance and how they can be leveraged to engage your audience.

## Users

In Braze, information about your audience is stored in user profiles. A [user profile]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) is a comprehensive collection of information and attributes that describe an individual consumer. It serves as a central repository for storing and managing data related to their behavior, preferences, and demographic details.

### Parts of a user profile

By understanding user profiles, you can gain insights into your audience and engage with them on a personalized and targeted level. A user's profile contains a lot of information, but here are some of the key parts:

- **User Identifier:** Each user profile is uniquely identified by a user ID, called an `external_id`. This identifier allows Braze to track and associate user data across different channels and devices, providing a unified view of each user's interactions with your brand. [Anonymous user profiles]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) (users who visit your website or application without logging in) don't have an `external_id`, but can be assigned [user aliases]({{site.baseurl}}/user_guide/data/user_data_collection/anonymous_users/#assigning-user-aliases) as an alternative identifier.
- [Attributes](#attributes)**:** These are specific pieces of information about the user, such as their name, age, location, or any other demographic information. You can use these attributes to segment your audience and personalize your messaging.
- [Events](#events)**:** These are actions that the user takes, like making a purchase, clicking on a link, or opening an app. Braze tracks these events to help you understand the user’s behavior and engagement. Similar to attributes, you can also use events to segment and personalize.
- **Purchases:** This section records the user's purchase history. It's crucial for understanding the user's buying habits and preferences.
- **Devices:** This section lists the devices that the user has used to interact with your brand. It can include mobile devices, web browsers, and connected devices (such as wearables and smart TVs).
- **Engagement:** This section contains information about the user's interactions with the messages you send them, what segments they belong to, subscription status, and more.
- **Message History:** This is a record of all the messages that have been sent to the user from the respective messaging channel (such as email or push).

{% alert tip %}
The Braze platform's SDKs automatically collect 27 different attributes and events. Using these standard events and attributes, you can build segments as soon as you integrate the SDK.
{% endalert %}

### Attributes

Attributes are specific characteristics or properties associated with a user. These attributes help you segment and target users based on their unique traits and interests. There are two types of attributes in Braze: standard attributes and custom attributes.

#### Standard attributes

Standard attributes are predefined attributes you can track with Braze after integrating the SDK into your app. They are common pieces of user information that most apps would find useful, such as demographics and device data. Examples include:

- First Name
- Last Name
- Email
- Gender
- Date of Birth
- Country
- City
- Last Used App
- Language
- Time Zone

#### Custom attributes

[Custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) are attributes that you define based on your specific business needs. They allow you to track information that is unique to your app or business. 

For example, a music streaming app might track custom attributes like:

- Favorite Genre
- Number of Songs Played
- Premium Subscriber (Yes/No)
- Favorite Artist

A retail app, on the other hand, might track custom attributes like:

- Preferred Clothing Size
- Favorite Brand
- Number of Purchases
- Loyalty Program Member (Yes/No)

Custom attributes give you the flexibility to collect and analyze data that's most relevant to your business. However, they require additional setup.

Both standard and custom attributes can be used to segment your audience and personalize your marketing messages. For example, you could send a special offer to users in a certain city (standard attribute) who have made more than 10 purchases (custom attribute).

### Events

Events represent specific actions or behaviors performed by users within your app or website. Examples of events can include app launches, purchases, content views, or any other action. By tracking and analyzing these events, you can gain insights into user behavior and engagement patterns.

#### Standard events

[Standard events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events#standard-events) are predefined events that Braze automatically tracks after the SDK is integrated into your app or site. Some examples of standard events include:

- **Session Start:** This event is triggered when a user opens the app.
- **Session End:** This event is triggered when a user closes the app.
- **Purchase:** This event is triggered when a user makes a purchase within the app.
- **Push Notification Click:** This event is triggered when a user clicks on a push notification.

#### Custom events

[Custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) are events that you define based on the specific actions you want to track within your app or site. For example, a music streaming app might track custom events like:

- Song Played
- Playlist Created
- Ad Skipped

A fitness app, on the other hand, might track custom events like:

- Workout Started
- Workout Completed
- Personal Record Set

Custom events give you the flexibility to track the actions that are most relevant to your app and business. However, like custom attributes, they require additional setup.

### Data points

Braze uses data points to help you define the most impactful information for your business. Data points are a crucial part of how Braze operates and are used for billing, pricing, and, most importantly, personalizing and optimizing your marketing campaigns.

Data points are logged when a user's profile data is updated or when they perform specific actions. These actions can include starting a session, ending a session, recording a custom event, or making a purchase. It's important to note that not all data collected by Braze counts as data points. For instance, data and events collected by default by the Braze Services, such as push tokens, device information, and all campaign engagement tracking events, like email opens and push notification clicks, are not counted as data points.

By thoughtfully considering what information to track as data points, you're targeting the highest-impact data for your users' experience. Your Braze account manager will help recommend data best practices to fit your needs.

Visit our dedicated article to learn more about [data points]({{site.baseurl}}/user_guide/data/data_points/).

## Segments

[Segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments) allows you to target users based on their demographic, behavioral, social, or technical characteristics and actions (that is, attributes and events). Creative and intelligent use of segmentation and messaging automation enables you to seamlessly move your users through their customer lifecycle journey.

Tips for working with segments:

- Segments in Braze are dynamic: users are always flowing in and out of segments, as they won't always fit the criteria. Users that fit the criteria of a segment at the moment of sending will be the recipients of that campaign or Canvas.
    - If you want your segment to be static, you can use Segment Extensions. Segment Extensions (with [regeneration turned off]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#extension-regeneration)) represent your audience as a single snapshot in time.
- You’re not limited to using one filter at a time. Create finely tuned, granular segments by layering multiple filters on top of each other.
- You can use the actions or inactions of your users to understand how to reach your users where they want to engage with you. These actions might be custom events, engagement with an existing campaign or Canvas, or even a specific message within a Canvas.

### Use case

Suppose you run an online clothing store, and you've set up a messaging flow to send a series of emails to users who have added an item to their cart but have not completed the purchase. This abandoned cart flow might include an initial reminder email, a follow-up email offering a discount, and a final reminder email.

![]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

You could create a segment of users who have triggered the custom event "Added Item to Cart" but have not triggered the custom event "Completed Purchase". Then, within this segment, you could further identify users who have opened the initial reminder email (engagement with a specific message) but have not made a purchase.

![]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

This segment could be targeted with a more aggressive campaign to try and convert these users into buyers. For example, you might send them a special offer or a personalized recommendation based on the items in their cart.

This is just one example of how you can use user actions and inactions, custom events, and engagement data to create segments and tailor your marketing strategies in Braze.

