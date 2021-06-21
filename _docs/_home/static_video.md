---
page_order: 0.5
nav_title: Video Test Page
layout: featured_video
video_id: XY5uXoKIvFY
video_source: youtube
hidden: true
---

# User Data Collection

Before completing your Braze implementation, ensure that you have a conversation between your marketing team and your development team regarding your marketing goals. When deciding what you want to track, and how you want to track it with Braze, it's useful to consider these goals and work backwards from there. Please reference our case of a [Taxi/Ride-Sharing App][16] at the end of this guide for an example of this process.

This best practice guide will help you to understand exactly what Braze considers to be a "Custom Event" vs. a "Custom Attribute".

## Automatically Collected Data

The following events and attributes are captured and updated automatically by the Braze SDK as part of the Session Start and Session End data points, or by the Braze backend. You don't need to record them separately as Custom Events or Custom Attributes.

#### Usage Information
- First Used App (Date)
- Last Used App (Date)
- Total Session Count (Integer)
- Number of Feedback Items (Integer)
- Number of Sessions in the Last Y Days (Integer and Date)
- Email Available (Boolean)
- News Feed View Count (Integer)

#### Campaign Retargeting
- Last Received Any Message (Date)
- Last Received Email Campaign (Date)
- Last Received Push Campaign (Date)
- Last Viewed News Feed (Date)
- Clicked Card (Integer)
- Received Message from Campaign
  - This filter allows you to target users based on their having (not) received a previous campaign.
- Received Message from Campaign with Tag
  - This filter allows you to target users based on their having (not) received a campaign that currently has a tag.
- Retarget Campaign
  - This filter allows you to target users based on whether or not they have opened, or clicked on a specific email, push, or slideup in the past

#### Device Information
- Location Available (Boolean)
- Most Recent Location (if location permission is granted to your app)
- Push Enabled (Boolean)
- Device Locale
- Language (taken from Device Locale)
- Country (first taken from IP Address. If this is not available, taken from Device Locale)
- Most Recent App Version
- Device Model
- Device OS Version
- Device Resolution
- Device Wireless Carrier
- Device Time Zone
- Device Identifier
- Uninstalled (Date and Boolean)

## Custom Events

Custom Events are actions taken by your users; they're best suited for tracking high-value user interactions with your application. Logging a custom event can trigger any number of follow-up campaigns with configurable delays, and enables the following segmentation filters around the recency and frequency of that event:

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the custom event has occurred __more than X number of times__ | __MORE THAN__ | __INTEGER__ |
| Check if the custom event has occurred __less than X number of times__ | __LESS THAN__ | __INTEGER__ |
| Check if the custom event has occurred __exactly X number of times__ | __EXACTLY__ | __INTEGER__ |
| Check if the custom event last occurred __after X date__ | __AFTER__ | __DATE__ |
| Check if the custom event last occurred __before X date__ | __BEFORE__ | __DATE__ |
| Check if the custom event last occurred __more than X days ago__ | __MORE THAN__ | __NUMBER OF DAYS AGO__ (Positive) Integer) |
| Check if the custom event last occurred __less than X days ago__ | __LESS THAN__ | __NUMBER OF DAYS AGO__ (Positive) Integer) |
| Check if the custom event occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the custom event occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. On the custom events analytics page you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time-series to indicate the last time a campaign was sent.

![custom_event_analytics_example.png][8]

>  [Incrementing Custom Attributes][10] can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time-series. User actions which do not need to be analyzed in time-series should be recorded via this method.

### Custom Event Storage

All User Profile data (Custom Events, Custom Attribute, Custom Data) is stored as long as those profiles are active. Event Properties are stored for sixty (60) days for segmentation.

### Custom Event Properties

With Custom Event Properties, Braze allows you to set properties on custom events and purchases. These properties can than be used for further qualifying trigger conditions, increasing personalization in messaging, and generating more sophisticated analytics through raw data export. Property values can be string, numeric, boolean, or Date objects. However, property values cannot be array objects.

For example, if an eCommerce application wanted to send a message to a user when they abandon their cart, it could additionally improve its target audience and allow for increased campaign personalization by adding a Custom Event Property of the 'cart value' of users' carts.

![customEventProperties.png][18]

Custom Event Properties can also be used for personalization within the messaging template. Any campaign using [Action-Based Delivery][19] with a trigger event can use custom event properties from that event for messaging personalization. If a gaming application wanted to send a message to users who had completed a level, it could further personalize the message with a property for the time it took users to complete that level. In this example the message is personalized for three different segments using [conditional logic][18].  The Custom Event Property called ``time_spent``, can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

![custom_event_properties_gaming.png][19]

Custom Event Properties are designed to help you personalize your messaging or build granular Action-Based Delivery Campaigns. If you would like to create segments based on event property recency and frequency, please reach out to your Customer Success Manager, as this may incur additional data costs.

## Custom Attributes
Custom Attributes are best for storing attributes about your users, or information about low-value actions within your application. You should keep in mind that we don't store time-series information for Custom Attributes, so you're not going to get any graphs based upon them like the above example for Custom Events.

### Custom Attribute Storage

All User Profile data (Custom Events, Custom Attribute, Custom Data) is stored as long as those profiles are active. Event Properties are stored for sixty (60) days for segmentation.

### Custom Attribute Data Types
Custom Attributes are extraordinarily flexible tools that allow for great targeting. The following data types may be stored as custom attributes:

#### Strings (Alpha-Numeric Characters)
String attributes are useful for storing user input, such as a favorite brand, a phone number, or a last search string within your application. Strings attributes can be up to 256 characters long.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the string attribute __exactly matches__ an inputted string| __EQUALS__ | __STRING__ |
| Check if the string attribute __partially matches__ an inputted string __OR__ Regular Expression | __MATCHES REGEX__ | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the string attribute __does not partially match__ an inputted string __OR__ Regular Expression | __DOES NOT MATCH REGEX__* | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the string attribute __does not match__ an inputted string| __DOES NOT EQUAL__ | __STRING__ |
| Check if the string attribute __exists__ on a user's profile | __IS NOT BLANK__ | __N/A__ |
| Check if the string attribute __does not exist__ on a user's profile | __IS BLANK__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
&#42; When segmenting using the __DOES NOT MATCH REGEX__ filter, it is required that there already exists a custom attribute with a value assigned in that user profile. Braze suggests using "OR" logic to check if a custom attribute is blank in order to ensure users are being targetted properly.
{% endalert %}

{% alert tip %}
For more on how to use our RegEx filter, check out this documentation on [Perl compatible regular expressions (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
More resources on RegEx:
- [RegEx with Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [RegEx Debugger and Tester](https://regex101.com/)
- [RegEx Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Arrays
Array attributes are good for storing related lists of information about your users. For example, storing the last 100 pieces of content a user watched within an array would allow specific interest segmentation.

Custom attribute arrays are one-dimensional sets; multi-dimensional arrays are not supported. __Adding an element to a custom attribute array appends the element to the end of the array, unless it's already present, in which case it gets moved from its current position to the end of the array.__ For example, if an array ['hotdog','hotdog','hotdog','pizza'] were imported, it will show in the array attribute as ['hotdog', 'pizza'], because we only support unique values.

If the array contains its maximum number of elements, the first element will be discarded and the new element added to the end. Below is some example code showing the array behavior in the web SDK:

```
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']

```

The maximum number of elements in Custom Attribute Arrays defaults to 25. The maximum for individual arrays can be increased to up to 100. If you would like this maximum increased, please reach out to your Customer Service Manager. Arrays exceeding the maximum number of elements will be truncated to contain the maximum number of elements.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the array attribute __includes a value which exactly matches__ an inputted value| __INCLUDES VALUE__ | __STRING__ |
| Check if the array attribute __does not include a value which exactly matches__ an inputted value| __DOESN'T INCLUDE VALUE__ | __STRING__ |
| Check if the array attribute __contains a value which partially matches__ an inputted value __OR__ Regular Expression | __MATCHES REGEX__ | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the array attribute __has any value__ | __HAS A VALUE__ | __N/A__ |
| Check if the array attribute __is empty__ | __IS EMPTY__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

>  We use [Perl compatible regular expressions (PCRE)][11].

#### Dates
Date attributes are useful for storing the last time a specific action was taken, so you can offer content specific re-engagement messaging to your users.

>  The last date a custom event or purchase event occurred is automatically recorded, and should not be recorded in duplicate via a custom date attribute.

Date filters using relative dates (e.g., more than 1 day ago, less than 2 days ago) measure 1 day as 24 hours. Any campaign that you run using these filters will include all users in 24 hour increments. For example, last used app more than 1 day ago will capture all users who "last used the app more than 24 hours" from the exact time the campaign runs. The same will be true for campaigns set with longer date ranges – so five days from activation will mean the prior 120 hours.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the date attribute __is before__ a __selected date__| __BEFORE__ | __CALENDAR DATE SELECTOR__ |
| Check if the date attribute __is after__ a __selected date__| __AFTER__ | __CALENDAR DATE SELECTOR__ |
| Check if the date attribute is __more than X number__ of __days ago__ | __MORE THAN__ | __NUMBER OF DAYS AGO__ |
| Check if the date attribute is __less than X number__ of __days ago__| __LESS THAN__ | __NUMBER OF DAYS AGO__ |
| Check if the date attribute is __in more than X number__ of __days in the future__ | __IN MORE THAN__ | __NUMBER OF DAYS IN FUTURE__ |
| Check if the date attribute is __less than X number__ of __days in the future__ | __IN LESS THAN__ | __NUMBER OF DAYS IN FUTURE__  |
| Check if the date attribute __exists__ on a user's profile | __EXISTS__ | __N/A__ |
| Check if the date attribute __does not exist__ on a user's profile | __DOES NOT EXIST__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Integers (Standard and Incrementing) and Decimals (Floats/Doubles) {#integers}
Numeric attributes have a wide variety of use-cases. Incrementing integer custom attributes are useful for storing the number of times a given action or event has occurred. Standard integers and decimals have all sorts of usages, for example : (Recording shoe size, waist size, number of times a user has viewed a certain product feature, or category).
>  Money spent in app should not be recorded by this method. Rather it should be recorded via our [purchase methods][4].

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the numeric attribute __is more than__ an __integer or decimal value__| __MORE THAN__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __is less than__ an __integer or decimal value__| __LESS THAN__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __is exactly__ an __integer or decimal value__| __EXACTLY__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __does not equal__ an __integer or decimal value__| __DOES NOT EQUAL__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __exists__ on a user's profile | __EXISTS__ | __N/A__ |
| Check if the numeric attribute __does not exist__ on a user's profile | __DOES NOT EXIST__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Booleans (True/False)
Boolean attributes are useful for storing subscription statuses, and other simple binary data about your users. The input options that we provide allow you to find users that have explicitly had a variable set to a true/false value in addition to those that don't have any record of that attribute recorded yet.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the boolean value __is__ | __IS__  | __TRUE__, __FALSE__, __TRUE OR NOT SET__, or __FALSE OR NOT SET__ |
| Check if the boolean value __exists__ on a user's profile | __EXISTS__  | __N/A__ |
| Check if the boolean value __does not exist__ on a user's profile | __DOES NOT EXIST__  | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Purchase Events / Revenue Tracking

Using our purchase methods to record in-app purchases establishes the Life-time Value(LTV) for each individual user profile. This data is viewable within our revenue page in time-series.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the total number of dollars spent __is greater than__ an __integer or decimal value__| __GREATER THAN__ | __INTEGER__ or __DECIMAL__ |
| Check if the total number of dollars spent __is less than__ an __integer or decimal value__| __LESS THAN__ | __INTEGER__ or __DECIMAL__ |
| Check if total number of dollars spent __is exactly__ an __integer or decimal value__| __EXACTLY__ | __INTEGER__ or __DECIMAL__ |
| Check if the purchase last occurred __after X date__ | __AFTER__ | __DATE__ |
| Check if the purchase last occurred __before X date__ | __BEFORE__ | __DATE__ |
| Check if the purchase last occurred __more than X days ago__ | __MORE THAN__ | __DATE__ |
| Check if the purchase last occurred __less than X days ago__ | __LESS THAN__ | __DATE__ |
| Check if the purchase occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

>  If you would like to segment on the number of times a specific purchase has occurred, you should also record that purchase individually as an [incrementing custom attribute][12].

## Taxi/Ride-Sharing App Use Case {#example-case}
For this example case, let's consider a Taxi/Ride-Sharing app (such as Hailo, Lyft, etc.) that wants to decide what user data to collect. The questions and brainstorming process below are a great model for marketing and development teams to follow. By the end of this exercise, both teams should have a solid understanding of what custom events and attributes make sense to collect in order to help meet their goal.

__Case Question #1: What is the goal?__

Their goal is straightforward in that they want users to hail taxi rides via their app.

__Case Question #2: What are the intermediate steps on the way to that goal from app installation?__

1. They need users to begin the registration process and fill out their personal information.
2. They need users to complete & verify the registration process by inputting a code into the app they receive via SMS.
3. They need to attempt to hail a taxi.
4. In order to hail a taxi, they must be available when they search.

The above actions could then be tagged as the following Custom Events:

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

After implementing the events, you can now run the following campaigns:

1. Message users who Began Registration, but didn't Completed Registration within a certain time frame.
2. Send congratulation messages to users who complete registration.
3. Send apologies and promotional credit to users who had unsuccessful taxi hails, that weren't followed by a successful taxi hail within a certain amount of time.
4. Send promotions to power users with lots of Successful Taxi Hails to thank them for their loyalty.
5. Many, Many More.

__Case Question #3: What other information might we want to know about our users that will inform our messaging?__

- Whether or not they have any promotional credit?
- The average rating they give to their drivers?
- Unique Promo Codes for the user?

The above characteristics could then be tagged as the following Custom Attributes:

- Promotional Credit Balance (Decimal Type)
- Average Driver Rating (Integer Type)
- Unique Promo Code (String Type)

Adding these attributes would afford you the ability to send campaigns to users like:

1. Reminding users who haven't used the app in 7 days who have promotional credit remaining on their account that it is there and that they should come back to the app and use it!
2. Messaging users who give low driver ratings to get direct customer feedback to see why they didn't enjoy their rides.
3. Use our [message templating and personalization features][17] to drag the unique promo code attribute into messaging directed at users.

## Best Practices

### General Best Practices

#### Don’t Over-Segment Your Tracking

- Being more generic will help you target more users and draw more useful divisions between user segments
- For example, rather than capturing a separate event for watching each of 50 different movies, it would be more effective to capture simply watching a movie as an event
- If you over segment your user data, your findings will lose statistical significance and won’t guide the development of your app and marketing initiatives as effectively
    - You will “miss the forest for the trees” when evaluating user-trend data
    - Events should be tied directly to your marketing and conversion goals

>  Multiple user actions within an app can be labeled with the same custom event or attribute designation. This is useful when you want to track something generically such as "played a song" rather than recording each individual song within a music app as a separate and distinct event.

### Development Best Practices

#### Set User IDs for Every User

User IDs should be set for each of your users. These should be unchanging and accessible when a user opens the app. We __strongly recommend__ providing this identifier as it will allow you to:

- Track your users across devices and platforms, improving the quality of your behavioral and demographic data.
- Import data about your users using our [User Data API][9].
- Target specific users with our [Messaging API][10] for both general and transactional messages.

User IDs must be less than 512 characters long and should be private and not easily obtained (e.g. not a plain email address or username). If such an identifier is not available, Braze will assign a unique identifier to your users, but you will lack the capabilities above. You should avoid setting User IDs for users for whom you lack a unique identifier that is tied to them as an individual. Passing a device identifier offers no benefit versus the automatic anonymous user tracking Braze offers by default. Below are some examples of suitable and unsuitable user IDs.

Good options for User IDs:

- Hashed email address or unique username
- Unique database identifier
- Facebook ID

These should not be used as user IDs:

- Device ID
- Random number or session ID
- Any non-unique ID

#### Give Custom Events and Attributes Readable Names
Imagine you're a marketer who begins using Braze a year or two after implementation, reading a dropdown list full of names like "usr_no_acct" without further context may be intimidating. Giving your event and attributes identifiable and readable names will make things easier for all users of your platform. Consider the following best-practices:

- Do not begin a custom event with a numeric character. The drop-down list is sorted alphabetically and beginning with a numerical character makes it more difficult to segment by your filter of choice
- Try not to use obscure abbreviations or technical jargon where possible
  - Example: `usr_ctry` may be fine as a variable name for a user's country within a piece of code, but the custom attribute ought be sent to Braze as `user_country` at very least to lend some clarity to a marketer using the dashboard down the line.

#### Only Log Attributes When They Change
We count every attribute passed to Braze as a data point, even if the passed attribute contains the same value as saved previously. Only logging data when it changes helps avoid redundant data point use and ensures a smoother experience by avoiding unnecessary API calls.

#### Avoid Programmatically Generating Events
If you are constantly creating new event names it is going to be impossible to meaningfully segment your users. You are going to run into the same over-segmentation problems described above. Additionally, programmatic custom events run a risk of containing more than 255 characters which is a constraint placed upon events and attributes (see below). You should generally capture generic events (“Watched a Video” or “Read an Article”) instead of highly specific events such as (“Watched Gangnam Style” or “Read Article: Best 10 Lunch Spots in Midtown Manhattan”).

### Technical Limitations & Constraints
Please be mindful of the following limitations and constraints when implementing custom events:

#### Length Constraints
All custom events, custom attribute names (keys), and custom event string values of 255 characters or longer will be truncated. Ideally, these should be as short as possible to improve network and battery performance for your app. If possible limit them to 50 characters.

#### Content Constraints
The following content will be trimmed programmatically from your attributes and events. Please take care not to use the following:

- Leading and trailing whitespace
- Newlines
- All non-digits within phone numbers
  - Example: "(732) 178-1038" will be condensed to "7321781038"
- Non-whitespace characters must be converted into spaces
- $ should not be used as a prefix for any custom events
- Any invalid UTF-8 encoding values
  -  "My \x80 Field" would be condensed to "My Field"

#### Reserved Keys
Prior to iOS SDK version 3.0 and Android SDK version 2.0, the following keys are __RESERVED__ and __CANNOT__ be used as Custom Attributes:

- `email`
- `facebook`
- `twitter`
- `first_name`
- `last_name`
- `dob`
- `external_id`
- `country`
- `home_city`
- `bio`
- `gender`
- `phone`
- `email_subscribe`
- `push_subscribe`

Additionally, the following keys are reserved and cannot be used as Custom Event Properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Value Definitions

- Integer values are 64 bit
- Decimals have 15 decimal digits by default

### Parsing a Generic Name Field

If only a single generic name field exists for a user (e.g. 'JohnDoe'), you can assign this entire title to your user's First Name attribute. Additionally, you can attempt to parse out both the first and last name of the user using spaces, but this latter method carries the potential risk of misnaming some of your users.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[10]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[11]: http://www.regextester.com/pregsyntax.html
[12]: #integers
[16]: #example-case
[17]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[18]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[19]: {% image_buster /assets/img_archive/custom_event_properties_gaming.png %} "custom_event_properties_gaming.png"
