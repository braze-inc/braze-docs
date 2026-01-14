---
nav_title: Custom attributes
article_title: Custom Attributes
page_order: 10
page_type: reference
description: "This page describes custom attributes and explains the various custom attribute data types."
search_rank: 1
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Custom attributes

> This page covers custom attributes, which are a collection of your users' unique traits. Custom attributes are best for storing attributes about your users, or information about low-value actions within your application. 

When stored in Braze, custom attributes can be used to build out audience segments and personalize messaging using Liquid. Keep in mind that we don't store time-series information for custom attributes, so you won't be able to get any graphs based on them like you can for custom events.

## Managing custom attributes

To create and manage custom attributes in the dashboard, go to **Data Settings** > **Custom Attributes**. 

![Four custom attributes that are booleans.]({% image_buster /assets/img/export_custom_attributes.png %})

The **Last updated** column lists the last time the custom attribute was edited, such as when it was last set to blocklist or active.

{% alert important %}
For proper message targeting, be sure that your custom attribute data type matches the actual custom attribute.
{% endalert %}

From this page, you can view, manage, create, or blocklist existing custom attributes. Select the menu next to a custom attribute for the following actions:

### Blocklisting

Custom attributes can be blocklisted individually in the actions menu, or up to 100 attributes can be selected and blocklisted in bulk. If you block a custom attribute, no data will be collected regarding that attribute, existing data will be unavailable unless reactivated, and blocklisted attributes will not show up in filters or graphs. Additionally, if the attribute is currently referenced by filters or triggers in other areas of the Braze dashboard, a warning modal will appear explaining that all instances of the filters or triggers that reference it will be removed and archived.

### Marking as personally identifiable information (PII)

Administrators can also create custom attributes and mark them as PII from this page. These attributes will only be visible to admins and dashboard users with the “View Custom Attributes Marked as PII” permission.

### Adding descriptions

You can add a description to a custom attribute after it's created if you have the `Manage Events, Attributes, Purchases` [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/). Edit the custom attribute and input whatever you like, such as a note for your team.

### Adding tags

You can add tags to a custom attribute after it's created if you have the "Manage Events, Attributes, Purchases" [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/). The tags can then be used to filter the list of attributes. 

### Removing custom attributes

There are two ways you can remove custom attributes from user profiles:

* Select the custom attribute name to be removed in a [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Set the `null` value in your API request to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Exporting data

To export the list of custom attributes as a CSV file, select **Export all** at the top of the page. The CSV file will be generated, and a download link will be emailed to you.

## Viewing usage reports

The usage report lists all the Canvases, campaigns, and segments using a specific custom attribute. This list doesn't include uses of Liquid. 

You can view up to 100 usage reports at a time by selecting the checkboxes next to the respective custom attributes and then selecting **View usage report**.

### Values tab

When viewing a usage report, select the **Values** tab to view the top values of the selected custom attributes based on a sample of approximately 250,000 users. Note that because the results are sampled from a subset of users, the sample won't include all existing values. This means the **Values** tab shouldn't be used for troubleshooting or for use cases that require incorporating data from all users.

![Usage report for selected custom attributes with an opened "Values" tab showing a pie chart of country attribute values, such as "US" and "PR".]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Setting custom attributes

The following lists methods across various platforms that are used to set custom attributes.

{% details Expand for documentation by platform %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (formerly Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

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
- [Objects]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Arrays of objects]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booleans (true/false) {#booleans}

Boolean attributes are useful for storing simple binary data about your users, like subscription statuses. You can find users that explicitly have a variable set to a true or false value, in addition to those that don't have any record of that attribute recorded yet.

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the boolean value **is** either true, false, true or not set, or false or not set | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, or **FALSE OR NOT SET** | If this filter specifies `coffee_drinker`, a user will match this filter in the following circumstances: <br> {::nomarkdown}<ul><li>If this filter is <code>true</code> and the user has the value <code>coffee_drinker</code></li><li>If this filter is <code>false</code> and the user doesn't have the value <code>coffee_drinker</code></li><li>If this filter is <code>true or not set</code> and the user has the value <code>coffee_drinker</code> or no value</li><li>If this filter is <code>false or not set</code> and the user doesn't have <code>coffee_drinker</code> or any value</li></ul>{:/} |
| Check if the boolean value **exists** on a user's profile and is not null | **IS NOT BLANK**  | **N/A** | If this filter specifies `coffee_drinker` and a user has a value for the attribute `coffee_drinker`, the user will match this filter. | 
| Check if the boolean value **does not exist** on a user's profile or is null | **IS BLANK**  | **N/A** | If this filter specifies `coffee_drinker`and a user either doesn’t have the attribute `coffee_drinker` or the value for `coffee_drinker` is null, the user will match this filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Numbers {#numbers}

Numeric attributes include [integers](https://en.wikipedia.org/wiki/Integer) and [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic), and have a wide variety of use-cases. Incrementing number custom attributes are useful for storing the number of times a given action or event has occurred without counting against your data cap. Standard numbers have all sorts of usages, such as recording:

- Shoe size
- Waist size
- Number of times a user has viewed a certain product feature, or category

{% alert tip %}
Money spent should not be recorded by this method. Rather it should be recorded via our [purchase methods](#purchase-revenue-tracking).
{% endalert %}

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the numeric attribute **is exactly** a **number**| **EXACTLY** | **NUMBER** | If this filter specifies `10` and a user profile has the value `10`, the user will match this filter. |
| Check if the numeric attribute **does not equal** a **number**| **DOES NOT EQUAL** | **NUMBER** | If this filter specifies `10` and a user profile doesn't have the value `10`, the user will match this filter. |
| Check if the numeric attribute **is more than** a **number**| **MORE THAN** | **NUMBER** | If this filter specifies `10` and a user profile has a value greater than `10`, the user will match this filter. |
| Check if the numeric attribute **is less than** a **number**| **LESS THAN** | **NUMBER** | If this filter specifies `10` and a user profile has a value lesser than `10`, the user will match this filter. |
| Check if the numeric attribute **exists** on a user's profile and is not null | **IS NOT BLANK** | **N/A** | If a user profile contains the specified numeric attribute, regardless of value, the user will match this filter. |
| Check if the numeric attribute **does not exist** on a user's profile or is null | **IS BLANK** | **N/A** | If a user profile doesn't contain the specified numeric attribute or the attribute’s value is null, the user will match this filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Number attribute details

- "Exactly 0" and "Less Than" filters include users with NULL fields
  - To exclude users without a value for custom attributes, you need to include the **is not blank** filter.

### Strings (alphanumeric characters) {#strings}

String attributes are useful for storing user input, such as a favorite brand, a phone number, or a last search string within your application. String attributes can be up to 255 characters long.

Note that if you input any values with spaces in between, before, or after words, then Braze will also check for the same spaces.

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the string attribute **exactly matches** an inputted string| **EQUALS** | **STRING**<br>Case sensitive | If this filter specifies `book` and a user profile has a string attribute for `last_item_purchased` that contains `book`, the user will match this filter. |
| Check if the string attribute **partially matches** an inputted string **OR** Regular Expression | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION** <br>Not case sensitive; maximum of 32,764 characters | 
| Check if the string attribute **does not partially match** an inputted string **OR** Regular Expression | **DOES NOT MATCH REGEX** * | **STRING** **OR** **REGULAR EXPRESSION**<br>Not case sensitive; maximum of 32,764 characters |
| Check if the string attribute **does not match** an inputted string| **DOES NOT EQUAL** | **STRING**<br>Not case sensitive  | If this filter specifies `book` and a user profile has a string attribute for `last_item_purchased` that doesn't contain `book`, the user will match this filter.|
| Check if the string attribute **exists** on a user's profile and is not an empty string | **IS NOT BLANK** | **N/A** | If this filter specifies `favorite_genre` and a user profile has the attribute `favorite_genre`, the user will match this filter regardless of their attribute value. For example, the user can have `sci-fi`, `romance`, or another value.|
| Check if the string attribute **does not exist** on a user's profile | **BLANK** | **N/A** | If this filter specifies `favorite_genre` and a user profile doesn't have the attribute `favorite_genre`, the user will match this filter.|
| Check if the string exactly matches **any** of the inputted strings | **IS ANY OF** | **STRING**<br>Case sensitive; multiple strings allowed (256 maximum) | If this filter specifies `book`, `bookmark`, and `reading light`, and a user profile has at least one of those strings, the user will match this filter. |
| Check if the string attribute **does not exactly match any** of the inputted strings | **IS NONE OF** |**STRING**<br>Case sensitive; multiple strings allowed (256 maximum) | If this filter specifies `book`, `bookmark`, and `reading light`, and a user profile doesn't contain any of those strings, the user will match the filter.|
| Check if the string attribute **partially matches any** of the inputted strings | **CONTAINS ANY OF** | **STRING**<br>Case sensitive; multiple strings allowed (256 maximum) | If this filter specifies `gold` and a user profile contains `gold` in any string, such as `gold_tier` or `former_gold_tier`, the user will match the filter. |
| Check if the string attribute **does not partially match any** of the inputted strings | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Case sensitive; multiple strings allowed (256 maximum) | If this filter specifies `gold` and a user profile doesn't contain `gold` in any string, the user will match this filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
A date string such as "12-1-2021" or "12/1/2021" will be converted to a datetime object and treated as a [time attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
When segmenting using the **DOES NOT MATCH REGEX** filter, you must already have a custom attribute with a value assigned in that user profile. Braze suggests using "OR" logic to check if a custom attribute is blank to ensure users are being targeted properly.
{% endalert %}

### Arrays {#arrays}

Array attributes are good for storing related lists of information about your users. For example, storing the last 100 pieces of content a user watched within an array would allow specific interest segmentation.

By default, the length of an array for an attribute is up to 500 items. For example, if you're sending over an attribute such as "Movies Watched" and it is set to 500, when a user watches a 501st movie, the first movie will be removed from the array, and the most recent movie will be added.

Note that if you input any values with spaces in between, before, or after words, Braze will also check for the same spaces.

{% alert note %}
The option to increase the maximum length will not be available if the attribute is set to automatically detect the data type; the data type must be set to array.
{% endalert %}

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the array attribute **includes a value which exactly matches** an inputted value| **INCLUDES VALUE** | **STRING** | If this filter specifies `sci-fi` and a user profile has the value `sci-fi`, the user will match this filter.|
| Check if the array attribute **does not include a value which exactly matches** an inputted value| **DOESN'T INCLUDE VALUE** | **STRING** | If this filter specifies `sci-fi` and a user profile doesn't have the value `sci-fi`, the user will match this filter.|
| Check if the array attribute **contains a value which partially matches** an inputted value **OR** Regular Expression | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION**<br>Maximum of 32,764 characters | |
| Check if the array attribute **has any value** or is not empty | **HAS A VALUE** | **N/A** | If this filter specifies `favorite_genres` and a user profile contains `favorite_genres` with any value, the user will match this filter. |
| Check if the array attribute **is empty** or does not exist | **IS EMPTY** | **N/A** | If this filter specifies `favorite_genres` and a user profile doesn't contain `favorite_genres` or contains `favorite_genres` but has no values, the user will match this filter.|
| Check if the array attribute **includes a value which exactly matches any** of the inputted values | **INCLUDES ANY OF** | **STRING**<br>Case sensitive; multiple values allowed (256 maximum) | If this filter specifies `sci-fi, fantasy, romance` and a user profile has any combination of `sci-fi`, `fantasy`, or `romance`, including only one of them (such as only `sci-fi`). A user can have `horror` or another value in their string if they also have any of `sci-fi`, `fantasy`, and `romance`.|
| Check if the array attribute **does not include a value which exactly match any** of the inputted values | **INCLUDES NONE OF** | **STRING**<br>Case sensitive; multiple values allowed (256 maximum) | If this filter specifies `sci-fi, fantasy, romance` and a user profile doesn't have any combination of `sci-fi`, `fantasy`, or `romance`, the user will match this filter. The user can have `horror` or another value if they don't have any of `sci-fi`, `fantasy`, or `romance`.|
| Check if the array attribute **contains a value which partially matches any** of the inputted values | **VALUES CONTAIN ANY OF** | **STRING**<br>Case sensitive; multiple values allowed (256 maximum) | If this filter specifies `gold` and a user profile array contains `gold` in at least one string, the user will match this filter. This includes string values like `gold_tier`, `former_gold_tier`, and others.|
| Check if the array attribute **does not include a value which partially match any** of the inputted values | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Case sensitive; multiple values allowed (256 maximum) | If this filter specifies `gold` and a user profile array doesn't contain `gold` in any strings, the user will match this filter. This means users with string values like `gold_tier` and `former_gold_tier` won't match this filter.|
| Check if the array attribute **includes all** of the inputted values | **IS ALL OF** | **STRING**<br>Case sensitive; multiple values allowed (256 maximum) | If this filter specifies `sci-fi, fantasy, romance` and a user profile has all of those values, the user will match this filter. The user can also have `horror` or other values and match this filter.|
| Check if the array attribute **does not include all of** the inputted values | **ISN'T ALL OF** | **STRING**<br>Case sensitive; multiple values allowed (256 maximum)|  If this filter specifies `sci-fi, fantasy, romance` and a user profile doesn't have all of those values, the user will match this filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
For more on how to use regular expressions (regex), check out these resources:
- [Perl compatible regular expressions (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex with Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Regex debugger and tester](https://www.regex101.com/)
- [Regex tutorial](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Time {#time}

Time attributes are useful for storing the last time a specific action was taken, so you can offer content specific re-engagement messaging to your users.

Time filters using relative dates (for example, more than 1 day ago, less than 2 days ago) measure 1 day as 24 hours. Any campaign that you run using these filters will include all users in 24-hour increments. For example, `last used app more than 1 day ago` will capture all users who "last used the app more than 24 hours" from the exact time the campaign runs. The same will be true for campaigns set with longer date ranges—so five days from activation will mean the prior 120 hours.

For example, to build a segment that targets users with a time attribute between 24 and 48 hours in the future, apply the filters `in more than 1 day in the future` and `in less than 2 days in the future`.

{% alert warning %}
The last date a custom event or purchase event occurred is automatically recorded and shouldn't be recorded again via a custom time attribute.
{% endalert %}

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the time attribute **is before** a **selected date**| **BEFORE** | **CALENDAR DATE SELECTOR** | If this filter specifies `2024-01-31` and a user profile has a date before `2024-1-31`, the user will match this filter. |
| Check if the time attribute **is after** a **selected date**| **AFTER** | **CALENDAR DATE SELECTOR** | If this filter specifies `2024-01-31` and a user profile has a date after `2024-1-31`, the user will match this filter. |
| Check if the time attribute is **more than X number** of **days ago** | **MORE THAN** | **NUMBER OF DAYS AGO** | If this filter specifies `7` and a user profile has a date that is more than seven days ago, the user will match this filter. |
| Check if the time attribute is **less than X number** of **days ago**| **LESS THAN** | **NUMBER OF DAYS AGO** | If this filter specifies `7` and a user profile has a date that is less than seven days ago, the user will match this filter.|
| Check if the time attribute is **in more than X number** of **days in the future** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | If this filter specifies `7` and a user profile has a date that is more than seven days in the future, the user will match this filter.|
| Check if the time attribute is **less than X number** of **days in the future** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | If this filter specifies `7` and a user profile has a date that is less than seven days in the future, the user will match this filter.|
| Check if the time attribute **exists** on a user's profile and is not null | **IS NOT BLANK** | **N/A** | If this filter specifies a time attribute that is on a user profile, the user will match this filter.|
| Check if the time attribute **does not exist** on a user's profile or is null | **IS BLANK** | **N/A** | If this filter specifies a time attribute that isn't on a user profile, the user will match this filter. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Time attribute details

- Day of Recurring Event
  - When using the "Day of Recurring Event" filter, and are then prompted to select the "Calendar Day of Recurring Event", if you select `IS LESS THAN` or `IS MORE THAN`, the current date will be counted for that segmentation filter.
  - For example, if on March 10, 2020, you selected the date of the attribute to be `LESS THAN ... March 10, 2020`, attributes will be considered for the days up to, and including March 10, 2020. 
- Less than X Days Ago: The "Less than X Days Ago" filter includes dates between X days ago and the current date/time.
- Less than X Days in the Future: Includes dates between the current date/time and X days in the future.

### Objects

You can use nested custom attributes to send objects as a data type for custom attributes. For more information, refer to [Nested custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Arrays of objects

Use an array of objects to group related attributes. For more details, refer to our article on [Array of objects]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Consolidated operators

We've consolidated the list of operators available to use in attribute filters, custom attribute filters, and nested custom attribute filters. If you have existing filters using these operators, they will be automatically updated to use the new operators.

| Data type | Old operator | New operator | Value |
| --- | --- | --- | --- |
| String | equals | is any of | At least 1 value |
| String | does not equal | is none of | At least 1 value |
| Array | includes value | includes any of | At least 1 value |
| Array | doesn't include value | includes none of | At least 1 value |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Purchase and revenue tracking {#purchase-revenue-tracking}

Using our purchase methods to record in-app purchases establishes the Lifetime Value (LTV) for each individual user profile. This data is viewable within our revenue page in time-series.

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the total number of dollars spent **is greater than** a **number**| **GREATER THAN** | **NUMBER** | If this filter specifies `500` and a user profile has a value greater than `500`, the user will match this filter. |
| Check if the total number of dollars spent **is less than** a **number**| **LESS THAN** | **NUMBER** | If this filter specifies `500` and a user profile has a value less than `500`, the user will match this filter.|
| Check if total number of dollars spent **is exactly** a **number**| **EXACTLY** | **NUMBER** | If this filter specifies `500` and a user profile has the value `500`, the user will match this filter. |
| Check if the purchase last occurred **after X date** | **AFTER** | **TIME** | If this filter specifies `2024/31/1` and a user's last purchase was after `2024/31/1`, the user will match this filter.|
| Check if the purchase last occurred **before X date** | **BEFORE** | **TIME** | If this filter specifies `2024/31/1` and a user's last purchase was before `2024/31/1`, the user will match this filter.|
| Check if the purchase last occurred **more than X days ago** | **MORE THAN** | **TIME** | If this filter specifies `7` and a user's last purchase was more than seven days ago from today, the user will match this filter.|
| Check if the purchase last occurred **less than X days ago** | **LESS THAN** | **TIME** |  If this filter specifies `7` and a user's last purchase was less than seven days ago from today, the user will match this filter.|
| Check if the purchase occurred **more than X (Max = 50) number of times** | **MORE THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** |  If this filter specifies `7` times and `21` days, and a user made more than seven purchases in the past 21 days, the user will match this filter.|
| Check if the purchase occurred **less than X (Max = 50) number of times** | **LESS THAN** | in the past **Y Days (Y = 1,3,7,14,21,30)** | If this filter specifies `7` times and `21` days, and a user made less than seven purchases in the past 21 days, the user will match this filter.|
| Check if the purchase occurred **exactly X (Max = 50) number of times** | **EXACTLY** | in the past **Y Days (Y = 1,3,7,14,21,30)** | If this filter specifies `7` times and `21` days, and a user made seven purchases in the past 21 days, the user will match this filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
If you would like to segment on the number of times a specific purchase has occurred, you should also record that purchase individually as an [incrementing custom attribute]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

You can change the data type of your custom attribute, but you should be aware of the impacts of [changing data types]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).

