---
nav_title: Analytics
article_title: About Analytics for the Braze SDK
page_order: 2.6
description: "Learn about the Braze SDK's analytics, so you can better understand which data Braze collects, the difference between custom events and custom attributes, and best practices for managing analytics."
platform: 
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - Unreal Engine
  - Xamarin
---

# Analytics

> Learn about the Braze SDK's analytics, so you can better understand which data Braze collects, the difference between custom events and custom attributes, and best practices for managing analytics.

{% alert tip %}
During your Braze implementation, be sure to discuss marketing goals with your team, so you can best decided the data you want to track and how you want to track it with Braze. For an example, see our [Taxi/Ride-Sharing App](#example-case) case study at the end of this guide.
{% endalert %}

## Automatically collected data

Certain user data is collected automatically by our SDK—for example, First Used App, Last Used App, Total Session Count, Device OS, etc. If you follow our integration guides to implement our SDKs, you will be able to take advantage of this [default data collection]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Checking this list can help you avoid storing the same information about users more than once. With the exception of session start and end, all other automatically tracked data does not count toward your data point usage.

See our [SDK primer]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) article to allowlist processes that block the default collection of certain data items.

## Custom events

Custom events are actions taken by your users; they're best suited for tracking high-value user interactions with your application. Logging a custom event can trigger any number of follow-up campaigns with configurable delays, and enables the following segmentation filters around the recency and frequency of that event:

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the custom event has occurred **more than X number of times** | **MORE THAN** | **NUMBER** |
| Check if the custom event has occurred **less than X number of times** | **LESS THAN** | **NUMBER** |
| Check if the custom event has occurred **exactly X number of times** | **EXACTLY** | **NUMBER** |
| Check if the custom event last occurred **after X date** | **AFTER** | **TIME** |
| Check if the custom event last occurred **before X date** | **BEFORE** | **TIME** |
| Check if the custom event last occurred **more than X days ago** | **MORE THAN** | **NUMBER OF DAYS AGO** (Positive) Number) |
| Check if the custom event last occurred **less than X days ago** | **LESS THAN** | **NUMBER OF DAYS AGO** (Positive) Number) |
| Check if the custom event occurred **more than X (Max = 50) number of times** | **MORE THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the custom event occurred **less than X (Max = 50) number of times** | **LESS THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the custom event occurred **exactly X (Max = 50) number of times** | **EXACTLY** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze notes the number of times these events have occurred as well as the last time they were performed by each user for segmentation. On the **Custom Events** analytics page, you can view in aggregate how often each custom event occurs, as well as by segment over time for more detailed analysis. This is particularly useful to view how your campaigns have affected custom event activity by looking at the gray lines Braze overlays on the time-series to indicate the last time a campaign was sent.

![A custom event analytics graph showing stats on users who added a credit card and made a search across a period of a thirty days.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
[Incrementing custom attributes]({{site.baseurl}}/api/endpoints/messaging/) can be used to keep a counter on a user action similar to a custom event. However, you will not be able to view custom attribute data in a time-series. User actions that do not need to be analyzed in time-series should be recorded via this method.
{% endalert %}

### Custom event storage

All user profile data (custom events, custom attribute, custom data) is stored as long as those profiles are active.

### Custom event properties

With custom event properties, Braze allows you to set properties on custom events and purchases. These properties can then be used for further qualifying trigger conditions, increasing personalization in messaging, and generating more sophisticated analytics through raw data export. Property values can be string, number, boolean, or time objects. However, property values cannot be array objects.

For example, if an eCommerce application wanted to send a message to a user when they abandon their cart, it could additionally improve its target audience and allow for increased campaign personalization by adding a custom event property of the `cart_value` of users' carts.

![A custom event example that will send a campaign to a user who has abandoned their cart and left the cart value at more than 100 and less than 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Custom event properties can also be used for personalization within the messaging template. Any campaign using [Action-Based Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) with a trigger event can use custom event properties from that event for messaging personalization. If a gaming application wanted to send a message to users who had completed a level, it could further personalize the message with a property for the time it took users to complete that level. In this example, the message is personalized for three different segments using [conditional logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). The custom event property called ``time_spent``, can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players fromm around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Custom event properties are designed to help you personalize your messaging or build granular action-based delivery campaigns. If you would like to create segments based on event property recency and frequency, reach out to your customer success manager or our Support team.

## Custom attributes

Custom attributes are extraordinarily flexible tools that allow you to target users with greater specificity than you would with standard attributes. Custom attributes are great for storing brand-specific information about your users. You should keep in mind that we don't store time-series information for custom attributes, so you're not going to get any graphs based on them like the preceding example for custom events.

### Custom attribute storage

All user profile data (custom events, custom attribute, custom data) is stored as long as those profiles are active.

### Custom attribute data types

The following data types may be stored as custom attributes:

#### Strings (alphanumeric characters)

String attributes are useful for storing user input, such as a favorite brand, a phone number, or a last search string within your application. String attributes can be up to 255 characters long.

The following table describes available segmentation options for string attributes.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the string attribute **exactly matches** an inputted string| **EQUALS** | **STRING** |
| Check if the string attribute **partially matches** an inputted string **OR** regular expression | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION** |
| Check if the string attribute **does not partially match** an inputted string **OR** regular expression | **DOES NOT MATCH REGEX** | **STRING** **OR** **REGULAR EXPRESSION** |
| Check if the string attribute **does not match** an inputted string| **DOES NOT EQUAL** | **STRING** |
| Check if the string attribute **exists** on a user's profile | **IS BLANK** | **N/A** |
| Check if the string attribute **does not exist** on a user's profile | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
When segmenting using the **DOES NOT MATCH REGEX** filter, it is required that there already exists a custom attribute with a value assigned in that user profile. Braze suggests using "OR" logic to check if a custom attribute is blank in order to properly target users.
{% endalert %}

{% alert tip %}
For more on how to use our regular expressions filter, check out this documentation on [Perl compatible regular expressions (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
More resources on regex:
- [Regex with Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Regex Debugger and Tester](https://regex101.com/)
- [Regex Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Arrays

Array attributes are good for storing related lists of information about your users. For example, storing the last 100 pieces of content a user watched within an array would allow specific interest segmentation.

Custom attribute arrays are one-dimensional sets; multi-dimensional arrays are not supported. **Adding an element to a custom attribute array appends the element to the end of the array, unless it's already present, in which case it gets moved from its current position to the end of the array.** For example, if an array `['hotdog','hotdog','hotdog','pizza']` were imported, it will show in the array attribute as `['hotdog', 'pizza']` because only unique values are supported.

If the array contains its maximum number of elements, the first element will be discarded and the new element added to the end. The following lists some example code showing the array behavior in the web SDK:

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

The maximum number of elements in custom attribute arrays defaults to 25. The maximum for individual arrays can be increased to up to 100 in the Braze dashboard, under **Data Settings** > **Custom Attributes**. If you would like this maximum increased, reach out to your customer service manager. Arrays exceeding the maximum number of elements will be truncated to contain the maximum number of elements.

The following table describes available segmentation options for array attributes.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the array attribute **includes a value which exactly matches** an inputted value| **INCLUDES VALUE** | **STRING** |
| Check if the array attribute **does not include a value which exactly matches** an inputted value| **DOESN'T INCLUDE VALUE** | **STRING** |
| Check if the array attribute **contains a value which partially matches** an inputted value **OR** regular expression | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION** |
| Check if the array attribute **has any value** | **HAS A VALUE** | **N/A** |
| Check if the array attribute **is empty** | **IS EMPTY** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
We use [Perl compatible regular expressions (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Dates

Time attributes are useful for storing the last time a specific action was taken, so you can offer content specific re-engagement messaging to your users.

{% alert note %}
The last date a custom event or purchase event occurred is automatically recorded, and should not be recorded in duplicate via a custom time attribute.
{% endalert %}

Date filters using relative dates (for example, more than 1 day ago, less than 2 days ago) measure 1 day as 24 hours. Any campaign that you run using these filters will include all users in 24 hour increments. For example, last used app more than 1 day ago will capture all users who "last used the app more than 24 hours" from the exact time the campaign runs. The same will be true for campaigns set with longer date ranges – so five days from activation will mean the prior 120 hours.

The following table describes available segmentation options for time attributes.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the time attribute **is before** a **selected date**| **BEFORE** | **CALENDAR DATE SELECTOR** |
| Check if the time attribute **is after** a **selected date**| **AFTER** | **CALENDAR DATE SELECTOR** |
| Check if the time attribute is **more than X number** of **days ago** | **MORE THAN** | **NUMBER OF DAYS AGO** |
| Check if the time attribute is **less than X number** of **days ago**| **LESS THAN** | **NUMBER OF DAYS AGO** |
| Check if the time attribute is **in more than X number** of **days in the future** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** |
| Check if the time attribute is **less than X number** of **days in the future** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  |
| Check if the time attribute **exists** on a user's profile | **BLANK** | **N/A** |
| Check if the time attribute **does not exist** on a user's profile | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Numbers {#integers}

Numeric attributes have a wide variety of use cases. Incrementing number custom attributes are useful for storing the number of times a given action or event has occurred. Standard numbers have all sorts of usages, such as recording shoe size, waist size, or the number of times a user has viewed a certain product feature or category.

{% alert note %}
Money spent should not be recorded by this method. Rather it should be recorded via our [purchase methods]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking).
{% endalert %}

The following table describes available segmentation options for numeric attributes.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the numeric attribute **is more than** a **number**| **MORE THAN** | **NUMBER** |
| Check if the numeric attribute **is less than** a **number**| **LESS THAN** | **NUMBER** |
| Check if the numeric attribute **is exactly** a **number**| **EXACTLY** | **NUMBER** |
| Check if the numeric attribute **does not equal** a **number**| **DOES NOT EQUAL** | **NUMBER** |
| Check if the numeric attribute **exists** on a user's profile | **EXISTS** | **N/A** |
| Check if the numeric attribute **does not exist** on a user's profile | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Booleans (true/false)

Boolean attributes are useful for storing subscription statuses and other simple binary data about your users. The input options that we provide allow you to find users that have explicitly had a variable set to a boolean in addition to those that don't have any record of that attribute recorded yet.

The following table describes available segmentation options for boolean attributes.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the boolean value **is** | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, or **FALSE OR NOT SET** |
| Check if the boolean value **exists** on a user's profile | **EXISTS**  | **N/A** |
| Check if the boolean value **does not exist** on a user's profile | **DOES NOT EXIST**  | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Purchase events / revenue tracking

Using our purchase methods to record in-app purchases establishes the Life-time Value (LTV) for each individual user profile. This data is viewable within our revenue page in time-series graphs.

The following table describes available segmentation options for purchase events.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the total number of dollars spent **is greater than** a **number**| **GREATER THAN** | **NUMBER** |
| Check if the total number of dollars spent **is less than** a **number**| **LESS THAN** | **NUMBER** |
| Check if total number of dollars spent **is exactly** a **number**| **EXACTLY** | **NUMBER** |
| Check if the purchase last occurred **after X date** | **AFTER** | **TIME** |
| Check if the purchase last occurred **before X date** | **BEFORE** | **TIME** |
| Check if the purchase last occurred **more than X days ago** | **MORE THAN** | **TIME** |
| Check if the purchase last occurred **less than X days ago** | **LESS THAN** | **TIME** |
| Check if the purchase occurred **more than X (Max = 50) number of times** | **MORE THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the purchase occurred **less than X (Max = 50) number of times** | **LESS THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
| Check if the purchase occurred **exactly X (Max = 50) number of times** | **EXACTLY** | in the past **Y Days (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
If you would like to segment on the number of times a specific purchase has occurred, you should also record that purchase individually as an [incrementing custom attribute](#integers).
{% endalert %}

## Taxi/ride-sharing app use case {#example-case}

For this example, let's consider a ride-sharing app that wants to decide what user data to collect. The following questions and brainstorming process are a great model for marketing and development teams to follow. By the end of this exercise, both teams should have a solid understanding of what custom events and attributes make sense to collect in order to help meet their goal.

**Case Question #1: What is the goal?**

Their goal is straightforward in that they want users to hail taxi rides via their app.

**Case Question #2: What are the intermediate steps on the way to that goal from app installation?**

1. They need users to begin the registration process and fill out their personal information.
2. They need users to complete and verify the registration process by inputting a code into the app they receive via SMS.
3. They need to attempt to hail a taxi.
4. In order to hail a taxi, they must be available when they search.

These actions could then be tagged as the following custom events:

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

After implementing the events, you can now run the following campaigns:

1. Message users who Began Registration, but didn't trigger the Completed Registration event in a certain time frame.
2. Send congratulation messages to users who complete registration.
3. Send apologies and promotional credit to users who had unsuccessful taxi hails that weren't followed by a successful taxi hail within a certain amount of time.
4. Send promotions to power users with lots of Successful Taxi Hails to thank them for their loyalty.

And many more!

**Case Question #3: What other information might we want to know about our users that will inform our messaging?**

- Whether or not they have any promotional credits?
- The average rating they give to their drivers?
- Unique promo codes for the user?

These characteristics could then be tagged as the following custom attributes:

- Promotional Credit Balance (Decimal Type)
- Average Driver Rating (Number Type)
- Unique Promo Code (String Type)

Adding these attributes would afford you the ability to send campaigns to users, such as:

1. Remind users who haven't logged on in seven days but who have a promotional credit that their credit exists and they should come back to the app to use it!
2. Message users who give low driver ratings to get direct customer feedback to see why they didn't enjoy their rides.
3. Use our [message templating and personalization features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) to drag the unique promotion code attribute into messaging directed at users.

## Best practices

### General best practices

#### Use event properties

- Name a custom event something that describes an action that a user takes.
- Make generous use of custom event properties to represent important data about an event.
- For example, rather than capturing a separate custom event for watching each of 50 different movies, it would be more effective to capture simply watching a movie as an event and have an event property that includes the name of the movie.

### Development best practices

#### Set user IDs for every user

User IDs should be set for each of your users. These should be unchanging and accessible when a user opens the app. We **strongly recommend** providing this identifier as it will allow you to:

- Track your users across devices and platforms, improving the quality of your behavioral and demographic data.
- Import data about your users using our [user data API]({{site.baseurl}}/api/endpoints/user_data/).
- Target specific users with our [messaging API]({{site.baseurl}}/api/endpoints/messaging/) for both general and transactional messages.

User IDs must be less than 512 characters long and should be private and not easily obtained (for example, not a plain email address or username). If such an identifier is not available, Braze will assign a unique identifier to your users, but you will lack the capabilities listed for user IDs. You should avoid setting user IDs for users for whom you lack a unique identifier that is tied to them as an individual. Passing a device identifier offers no benefit versus the automatic anonymous user tracking Braze offers by default. The following are some examples of suitable and unsuitable user IDs.

Good options for user IDs:

- Hashed email address or unique username
- Unique database identifier

These should not be used as user IDs:

- Device ID
- Random number or session ID
- Any non-unique ID
- Email address
- Another 3rd party vendor's user ID

{% multi_lang_include alerts/important_alerts.md alert='SDK auth' %}

#### Give custom events and attributes readable names

Imagine you're a marketer who begins using Braze a year or two after implementation, reading a dropdown list full of names like "usr_no_acct" without further context may be intimidating. Giving your event and attributes identifiable and readable names will make things easier for all users of your platform. Consider the following best-practices:

- Do not begin a custom event with a numeric character. The dropdown list is sorted alphabetically and beginning with a numerical character makes it more difficult to segment by your filter of choice
- Try not to use obscure abbreviations or technical jargon where possible
  - Example: `usr_ctry` may be fine as a variable name for a user's country within a piece of code, but the custom attribute should be sent to Braze as something like `user_country` to lend some clarity to a marketer using the dashboard down the line.

#### Only log attributes when they change

We count every attribute passed to Braze as a data point, even if the passed attribute contains the same value as saved previously. Only logging data when it changes helps avoid redundant data point use and supports a smoother experience by avoiding unnecessary API calls.

#### Avoid programmatically generating event names

If you are constantly creating new event names it is going to be impossible to meaningfully segment your users. You should generally capture generic events ("Watched a Video" or "Read an Article") instead of highly specific events such as ("Watched Gangnam Style" or "Read Article: Best 10 Lunch Spots in Midtown Manhattan"). The specific data about the event should be included as an event property, not as part of the event name.

### Technical limitations and constraints

Be mindful of the following limitations and constraints when implementing custom events:

#### Length constraints

All custom events, custom attribute names (keys), and custom event string values of 255 characters or longer will be truncated. Ideally, these should be as short as possible to improve network and battery performance for your app. If possible limit them to 50 characters.

#### Content constraints
The following content will be trimmed programmatically from your attributes and events. Take care not to use the following:

- Leading and trailing whitespace
- Newlines
- All non-digits within phone numbers
  - Example: "(732) 178-1038" will be condensed to "7321781038"
- Non-whitespace characters must be converted into spaces
- $ should not be used as a prefix for any custom events
- Any invalid UTF-8 encoding values
  -  "My \x80 Field" would be condensed to "My Field"

#### Reserved keys

The following keys are reserved and cannot be used as custom event properties:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Value definitions

- Integer values are 64 bit
- Decimals have 15 decimal digits by default

### Parsing a generic name field

If only a single generic name field exists for a user (for example, 'JohnDoe'), you can assign this entire title to your user's First Name attribute. Additionally, you can attempt to parse out both the first and last name of the user using spaces, but this latter method carries the potential risk of misnaming some of your users.
