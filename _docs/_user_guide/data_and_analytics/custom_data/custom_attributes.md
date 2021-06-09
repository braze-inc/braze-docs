---
nav_title: Custom Attributes
page_order: 3

page_type: reference
description: "This reference article describes custom attributes, and explains the various custom attribute data types."
---

# Custom Attributes
Custom attributes are best for storing attributes about your users, or information about low-value actions within your application. You should keep in mind that we don't store time-series information for Custom attributes, so you won't be able to get any graphs based upon them like you can for Custom events.

We get that Custom attributes can be confusing, so read closely and check out our [LAB course on Custom events and attributes](http://lab.braze.com/custom-events-and-attributes)!

## Custom Attribute Storage
All data stored on the User Profile, including Custom Attribute data, is retained indefinitely as long as each profile is active.

## Custom Attribute Data Types
Custom Attributes are extraordinarily flexible tools that allow for great targeting.

The following data types may be stored as custom attributes:


### Booleans (True/False)
Boolean attributes are useful for storing subscription statuses, and other simple binary data about your users. The input options that we provide allow you to find users that have explicitly had a variable set to a true/false value in addition to those that don't have any record of that attribute recorded yet.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the boolean value __is__ | __IS__  | __TRUE__, __FALSE__, __TRUE OR NOT SET__, or __FALSE OR NOT SET__ |
| Check if the boolean value __exists__ on a user's profile | __EXISTS__  | __N/A__ |
| Check if the boolean value __does not exist__ on a user's profile | __DOES NOT EXIST__  | __N/A__ |
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
| Check if the numeric attribute __is more than__ a __number__| __MORE THAN__ | __NUMBER__ |
| Check if the numeric attribute __is less than__ a __number__| __LESS THAN__ | __NUMBER__ |
| Check if the numeric attribute __is exactly__ a __number__| __EXACTLY__ | __NUMBER__ |
| Check if the numeric attribute __does not equal__ a __number__| __DOES NOT EQUAL__ | __NUMBER__ |
| Check if the numeric attribute __exists__ on a user's profile | __EXISTS__ | __N/A__ |
| Check if the numeric attribute __does not exist__ on a user's profile | __DOES NOT EXIST__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Strings (Alpha-Numeric Characters)
String attributes are useful for storing user input, such as a favorite brand, a phone number, or a last search string within your application. 

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the string attribute __exactly matches__ an inputted string| __EQUALS__ | __STRING__ |
| Check if the string attribute __partially matches__ an inputted string __OR__ Regular Expression | __MATCHES REGEX__ | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the string attribute __does not partially match__ an inputted string __OR__ Regular Expression | __DOES NOT MATCH REGEX__ * | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the string attribute __does not match__ an inputted string| __DOES NOT EQUAL__ | __STRING__ |
| Check if the string attribute __exists__ on a user's profile | __IS NOT BLANK__ | __N/A__ |
| Check if the string attribute __does not exist__ on a user's profile | __BLANK__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
A date string such as "12-1-2021" or "12/1/2021" will be converted to a datetime object and treated as a [time attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
When segmenting using the __DOES NOT MATCH REGEX__ filter, you must already have a custom attribute with a value assigned in that user profile. Braze suggests using "OR" logic to check if a custom attribute is blank to ensure users are being targeted properly.<br>

More resources on RegEx:
- [RegEx with Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [RegEx Debugger and Tester](https://regex101.com/)
- [RegEx Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Arrays
Array attributes are good for storing related lists of information about your users. For example, storing the last 100 pieces of content a user watched within an array would allow specific interest segmentation.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the array attribute __includes a value which exactly matches__ an inputted value| __INCLUDES VALUE__ | __STRING__ |
| Check if the array attribute __does not include a value which exactly matches__ an inputted value| __DOESN'T INCLUDE VALUE__ | __STRING__ |
| Check if the array attribute __contains a value which partially matches__ an inputted value __OR__ Regular Expression | __MATCHES REGEX__ | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the array attribute __has any value__ | __HAS A VALUE__ | __N/A__ |
| Check if the array attribute __is empty__ | __IS EMPTY__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
For more on how to use our RegEx filter, check out this documentation on [Perl compatible regular expressions (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
More resources on RegEx:
- [RegEx with Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [RegEx Debugger and Tester](https://regex101.com/)
- [RegEx Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Time
Time attributes are useful for storing the last time a specific action was taken, so you can offer content specific re-engagement messaging to your users.

Time filters using relative dates (e.g., more than 1 day ago, less than 2 days ago) measure 1 day as 24 hours. Any campaign that you run using these filters will include all users in 24-hour increments. For example, last used app more than 1 day ago will capture all users who "last used the app more than 24 hours" from the exact time the campaign runs. The same will be true for campaigns set with longer date ranges – so five days from activation will mean the prior 120 hours.

For example, to build a segment that targets users with a time attribute between 24 and 48 hours in the future, apply the filters `in more than 1 day in the future` and `in less than 2 days in the future`.

{% alert warning %}
The last date a custom event or purchase event occurred is automatically recorded, and should not be recorded in duplicate via a custom time attribute.
{% endalert %}

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the time attribute __is before__ a __selected date__| __BEFORE__ | __CALENDAR DATE SELECTOR__ |
| Check if the time attribute __is after__ a __selected date__| __AFTER__ | __CALENDAR DATE SELECTOR__ |
| Check if the time attribute is __more than X number__ of __days ago__ | __MORE THAN__ | __NUMBER OF DAYS AGO__ |
| Check if the time attribute is __less than X number__ of __days ago__| __LESS THAN__ | __NUMBER OF DAYS AGO__ |
| Check if the time attribute is __in more than X number__ of __days in the future__ | __IN MORE THAN__ | __NUMBER OF DAYS IN FUTURE__ |
| Check if the time attribute is __less than X number__ of __days in the future__ | __IN LESS THAN__ | __NUMBER OF DAYS IN FUTURE__  |
| Check if the time attribute __exists__ on a user's profile | __EXISTS__ | __N/A__ |
| Check if the time attribute __does not exist__ on a user's profile | __DOES NOT EXIST__ | __N/A__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert update %}

As of March 10, 2020, the behavior of "Day of Recurring Event", "Less than X Days Ago", and "Less than X Days in the Future" has changed. If you use these filters in your segmentation, we recommend readjusting your segments to take these changes into account.
<br> <br>
"Day of Recurring Event"

- **Change:** Current date is now counted in this segmentation filter.
- When using the "Day of Recurring Event" filter, and are then prompted to select the "Calendar Day of Recurring Event", if you select `IS LESS THAN` or `IS MORE THAN`, the current date will be counted for that segmentation filter.
- For example, if on March 10, 2020, you selected the date of the attribute to be `LESS THAN ... March 10, 2020`, attributes will be considered for the days up to, and including March 10, 2020. 

<br> 

"Less than X Days Ago" and "Less than X Days in the Future"
- **Change:** These filters used to include future dates for past date queries, and past dates for future queries. 
- Less than X Days Ago: Includes dates between X days ago and the current date/time. We will no longer include any dates in the future.
- Less than X Days in the Future: Includes dates between the current date/time and X days in the future. We will no longer include any dates in the past.

{% endalert %}


## Purchase and Revenue Tracking {#purchase-revenue-tracking}

Using our purchase methods to record in-app purchases establishes the Lifetime Value(LTV) for each individual user profile. This data is viewable within our revenue page in time-series.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the total number of dollars spent __is greater than__ a __number__| __GREATER THAN__ | __NUMBER__ |
| Check if the total number of dollars spent __is less than__ a __number__| __LESS THAN__ | __NUMBER__ |
| Check if total number of dollars spent __is exactly__ a __number__| __EXACTLY__ | __NUMBER__ |
| Check if the purchase last occurred __after X date__ | __AFTER__ | __TIME__ |
| Check if the purchase last occurred __before X date__ | __BEFORE__ | __TIME__ |
| Check if the purchase last occurred __more than X days ago__ | __MORE THAN__ | __TIME__ |
| Check if the purchase last occurred __less than X days ago__ | __LESS THAN__ | __TIME__ |
| Check if the purchase occurred __more than X (Max = 50) number of times__ | __MORE THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __less than X (Max = 50) number of times__ | __LESS THAN__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
| Check if the purchase occurred __exactly X (Max = 50) number of times__ | __EXACTLY__ | in the past __Y Days (Y = 1,3,7,14,21,30)__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
If you would like to segment on the number of times a specific purchase has occurred, you should also record that purchase individually as an [incrementing custom attribute]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

{% alert update %}

As of March 10, 2020, the behavior of "Day of Recurring Event" has changed, now including the current date in the filter.
<br><br>
Explanation:
When using the "Day of Recurring Event" filter, and are then prompted to select the "Calendar Day of Recurring Event". If you select `IS LESS THAN` or `IS MORE THAN`, the current date will be counted for that segmentation filter.
<br> 
<br> 
For example, if on March 10, 2020, you select the date of the attribute to be `LESS THAN ... March 10, 2020`, attributes will be considered for the days up to, and including March 10, 2020. 
{% endalert %}

You can change the data type of your custom attribute, but you should be aware of [what other changes this action entails]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).
