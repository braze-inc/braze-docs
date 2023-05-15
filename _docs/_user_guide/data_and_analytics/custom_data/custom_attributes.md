---
nav_title: Custom Attributes
article_title: Custom Attributes
page_order: 10
page_type: reference
description: "This reference article describes custom attributes, and explains the various custom attribute data types."
search_rank: 1
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Custom attributes

> Custom attributes are a collection of your users' unique traits. Custom attributes are best for storing attributes about your users, or information about low-value actions within your application. 

When stored in Braze, these characteristics can be used to build out audience segments and personalize messaging using Liquid. You should keep in mind that we don't store time-series information for custom attributes, so you won't be able to get any graphs based upon them like you can for custom events.

## Managing custom attributes

To create and manage custom attributes in the dashboard, go to **Manage Settings** > **Custom Attributes**. 

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), you can find **Custom Attributes** under **Data Settings**.
{% endalert %}

From this page, you can view, manage, or blocklist existing custom attributes, or create a new one. If you block a custom attribute, no data will be collected regarding that attribute, existing data will be unavailable unless reactivated, and blocklisted attributes will not show up in filters.

To remove custom attributes from user profiles, set the value to "null" in your API request to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

## Setting custom attributes

The following lists methods across various platforms that are used to set custom attributes.

{% details Expand for documentation by platform %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/setting_custom_attributes/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/)

{% enddetails %}

## Custom attribute storage

All data stored on the **User Profile**, including custom attribute data, is retained indefinitely as long as each profile is [active]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Custom attribute data types

Custom attributes are extraordinarily flexible tools that allow for great targeting.

The following data types may be stored as custom attributes:

- [Booleans](#booleans)
- [Numbers](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Time](#time)
- [Objects]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Arrays of objects]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)

### Booleans (true/false) {#booleans}

Boolean attributes are useful for storing simple binary data about your users, like subscription statuses. You can find users that explicitly have a variable set to a true or false value, in addition to those that don't have any record of that attribute recorded yet.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the boolean value **is** either true, false, true or not set, or false or not set | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, or **FALSE OR NOT SET** |
| Check if the boolean value **exists** on a user's profile | **IS NOT BLANK**  | **N/A** |
| Check if the boolean value **does not exist** on a user's profile | **IS BLANK**  | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Numbers {#numbers}

Numeric attributes include [integers](https://en.wikipedia.org/wiki/Integer) and [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic), and have a wide variety of use-cases. Incrementing number custom attributes are useful for storing the number of times a given action or event has occurred without counting against your data cap. Standard numbers have all sorts of usages, such as recording:

- Shoe size
- Waist size
- Number of times a user has viewed a certain product feature, or category

{% alert tip %}
Money spent should not be recorded by this method. Rather it should be recorded via our [purchase methods](#purchase-revenue-tracking).
{% endalert %}

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the numeric attribute **is more than** a **number**| **MORE THAN** | **NUMBER** |
| Check if the numeric attribute **is less than** a **number**| **LESS THAN** | **NUMBER** |
| Check if the numeric attribute **is exactly** a **number**| **EXACTLY** | **NUMBER** |
| Check if the numeric attribute **does not equal** a **number**| **DOES NOT EQUAL** | **NUMBER** |
| Check if the numeric attribute **exists** on a user's profile | **EXISTS** | **N/A** |
| Check if the numeric attribute **does not exist** on a user's profile | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Number attribute details

- "Exactly 0" and "Less Than" filters include users with NULL fields
  - To exclude users without a value for custom attributes, you need to include the **is not blank** filter.

### Strings (alpha-numeric characters) {#strings}

String attributes are useful for storing user input, such as a favorite brand, a phone number, or a last search string within your application. String attributes can be up to 255 characters long.

Note that if you input any values with spaces in between, before, or after words, then Braze will also check for the same spaces.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the string attribute **exactly matches** an inputted string| **EQUALS** | **STRING**<br>Case sensitive |
| Check if the string attribute **partially matches** an inputted string **OR** Regular Expression | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION**<br>Not case sensitive. |
| Check if the string attribute **does not partially match** an inputted string **OR** Regular Expression | **DOES NOT MATCH REGEX** * | **STRING** **OR** **REGULAR EXPRESSION**<br>Not case sensitive. |
| Check if the string attribute **does not match** an inputted string| **DOES NOT EQUAL** | **STRING**<br>Not case sensitive.  |
| Check if the string attribute **exists** on a user's profile | **IS NOT BLANK** | **N/A** |
| Check if the string attribute **does not exist** on a user's profile | **BLANK** | **N/A** |
| Check if the string exactly matches **any** of the inputted strings | **IS ANY OF** | **STRING**<br>Case sensitive; multiple strings allowed |
| Check if the string attribute **does not exactly match any** of the inputted strings | **IS NONE OF** | **STRING**<br>Case sensitive; multiple strings allowed |
| Check if the string attribute **partially matches any** of the inputted strings | **CONTAINS ANY OF** | **STRING**<br>Case sensitive; multiple strings allowed |
| Check if the string attribute **does not partially match any** of the inputted strings | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Case sensitive; multiple strings allowed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
A date string such as "12-1-2021" or "12/1/2021" will be converted to a datetime object and treated as a [time attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
When segmenting using the **DOES NOT MATCH REGEX** filter, you must already have a custom attribute with a value assigned in that user profile. Braze suggests using "OR" logic to check if a custom attribute is blank to ensure users are being targeted properly.<br>

More resources on regular expressions:
- [Regular expressions with Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Regular expression debugger and tester](https://regex101.com/)
- [Regular expression tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Arrays {#arrays}

Array attributes are good for storing related lists of information about your users. For example, storing the last 100 pieces of content a user watched within an array would allow specific interest segmentation.

By default, the max length of an array for an attribute is set to 25, and can be increased to 100 for an individual array. For example, if you're sending over an attribute such as "Movies Watched" and it is set to 100, when a user watches a 101th movie, the first movie will be removed from the array and the most recent movie will be added.

If you'd like this maximum increased, reach out to your customer success manager. Your dashboard administrator can then increase the maximum length for individual arrays to over 100 from the **Custom Attributes** tab of the **Manage Settings** page.

Note that If you input any values with spaces in between, before, or after words, then Braze will also check for the same spaces.

{% alert note %}
The option to increase the max length will not be available if the attribute is set to automatically detect the data type; the data type must be set to array.
{% endalert %}

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the array attribute **includes a value which exactly matches** an inputted value| **INCLUDES VALUE** | **STRING** |
| Check if the array attribute **does not include a value which exactly matches** an inputted value| **DOESN'T INCLUDE VALUE** | **STRING** |
| Check if the array attribute **contains a value which partially matches** an inputted value **OR** Regular Expression | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION** |
| Check if the array attribute **has any value** | **HAS A VALUE** | **N/A** |
| Check if the array attribute **is empty** | **IS EMPTY** | **N/A** |
| Check if the array attribute **includes a value which exactly matches any** of the inputted values | **INCLUDES ANY OF** | **STRING**<br>Case sensitive; multiple values allowed |
| Check if the array attribute **does not include a value which exactly match any** of the inputted values | **INCLUDES NONE OF** | **STRING**<br>Case sensitive; multiple values allowed |
| Check if the array attribute **contains a value which partially matches any** of the inputted values | **VALUES CONTAIN ANY OF** | **STRING**<br>Case sensitive; multiple values allowed |
| Check if the array attribute **does not include a value which partially match any** of the inputted values | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Case sensitive; multiple values allowed |
| Check if the array attribute **includes all** of the inputted values | **IS ALL OF** | **STRING**<br>Case sensitive; multiple values allowed |
| Check if the array attribute **does not include all of** the inputted values | **ISN'T ALL OF** | **STRING**<br>Case sensitive; multiple values allowed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
For more on how to use our regular expressions filter, check out this documentation on [Perl compatible regular expressions](http://www.regextester.com/pregsyntax.html) (PCRE).
<br>
More resources on regex:
- [Regex with Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Regex Debugger and Tester](https://regex101.com/)
- [Regex Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Time {#time}

Time attributes are useful for storing the last time a specific action was taken, so you can offer content specific re-engagement messaging to your users.

Time filters using relative dates (e.g., more than 1 day ago, less than 2 days ago) measure 1 day as 24 hours. Any campaign that you run using these filters will include all users in 24-hour increments. For example, `last used app more than 1 day ago` will capture all users who "last used the app more than 24 hours" from the exact time the campaign runs. The same will be true for campaigns set with longer date ranges—so five days from activation will mean the prior 120 hours.

For example, to build a segment that targets users with a time attribute between 24 and 48 hours in the future, apply the filters `in more than 1 day in the future` and `in less than 2 days in the future`.

{% alert warning %}
The last date a custom event or purchase event occurred is automatically recorded and shouldn't be recorded again via a custom time attribute.
{% endalert %}

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the time attribute **is before** a **selected date**| **BEFORE** | **CALENDAR DATE SELECTOR** |
| Check if the time attribute **is after** a **selected date**| **AFTER** | **CALENDAR DATE SELECTOR** |
| Check if the time attribute is **more than X number** of **days ago** | **MORE THAN** | **NUMBER OF DAYS AGO** |
| Check if the time attribute is **less than X number** of **days ago**| **LESS THAN** | **NUMBER OF DAYS AGO** |
| Check if the time attribute is **in more than X number** of **days in the future** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** |
| Check if the time attribute is **less than X number** of **days in the future** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  |
| Check if the time attribute **exists** on a user's profile | **IS NOT BLANK** | **N/A** |
| Check if the time attribute **does not exist** on a user's profile | **IS BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Time attribute details

- Day of Recurring Event
  - When using the "Day of Recurring Event" filter, and are then prompted to select the "Calendar Day of Recurring Event", if you select `IS LESS THAN` or `IS MORE THAN`, the current date will be counted for that segmentation filter.
  - For example, if on March 10, 2020, you selected the date of the attribute to be `LESS THAN ... March 10, 2020`, attributes will be considered for the days up to, and including March 10, 2020. 
- Less than X Days Ago: The "Less than X Days Ago" filter includes dates between X days ago and the current date/time.
- Less than X Days in the Future: Includes dates between the current date/time and X days in the future.

### Objects

You can use nested custom attributes to send objects as a data type for custom attributes. For more information, refer to [Nested custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).

### Arrays of objects

Use an array of objects to group related attributes. For more details, refer to our article on [Array of objects]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/).

## Purchase and revenue tracking {#purchase-revenue-tracking}

Using our purchase methods to record in-app purchases establishes the Lifetime Value (LTV) for each individual user profile. This data is viewable within our revenue page in time-series.

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
If you would like to segment on the number of times a specific purchase has occurred, you should also record that purchase individually as an [incrementing custom attribute]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

You can change the data type of your custom attribute, but you should be aware of the impacts of [changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).

