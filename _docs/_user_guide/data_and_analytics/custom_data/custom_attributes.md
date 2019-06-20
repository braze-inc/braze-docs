---
nav_title: Custom Attributes
page_order: 3
---

# Custom Attributes
Custom Attributes are best for storing attributes about your users, or information about low-value actions within your application. You should keep in mind that we don't store time-series information for Custom Attributes, so you're not going to get any graphs based upon them like the above example for Custom Events.

We get that Custom Attributes can be confusing, so read closely and check out our [LAB course on Custom Events and Attributes](http://lab.braze.com/custom-events-and-attributes)!

### Custom Attribute Storage

All User Profile data (Custom Events, Custom Attribute, Custom Data) is stored as long as those profiles are active. Custom Event Properties are stored and available for Segmentation for thirty (30) days. If you'd like to leverage Event Properties for Segmentation, please contact your Braze account or customer success manager. 

# Custom Attribute Data Types
Custom Attributes are extraordinarily flexible tools that allow for great targeting. The following data types may be stored as custom attributes:

## Strings (Alpha-Numeric Characters)
String attributes are useful for storing user input, such as a favorite brand, a phone number, or a last search string within your application.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the string attribute __exactly matches__ an inputted string| __EQUALS__ | __STRING__ |
| Check if the string attribute __partially matches__ an inputted string __OR__ Regular Expression | __MATCHES REGEX__ | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the string attribute __does not partially match__ an inputted string __OR__ Regular Expression | __DOES NOT MATCH REGEX__ | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the string attribute __does not match__ an inputted string| __DOES NOT EQUAL__ | __STRING__ |
| Check if the string attribute __exists__ on a user's profile | __BLANK__ | __N/A__ |
| Check if the string attribute __does not exist__ on a user's profile | __IS NOT BLANK__ | __N/A__ |

{% alert tip %}
For more on how to use our RegEx filter, check out this documentation on [Perl compatible regular expressions (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
More resources on RegEx:
- [RegEx Tester and Debugger](https://regex101.com/)
- [RegEx: Learn More](https://regexr.com/)
- [RegEx Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

## Arrays
Array attributes are good for storing related lists of information about your users. For example, storing the last 100 pieces of content a user watched within an array would allow specific interest segmentation.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the array attribute __includes a value which exactly matches__ an inputted value| __INCLUDES VALUE__ | __STRING__ |
| Check if the array attribute __does not include a value which exactly matches__ an inputted value| __DOESN'T INCLUDE VALUE__ | __STRING__ |
| Check if the array attribute __contains a value which partially matches__ an inputted value __OR__ Regular Expression | __MATCHES REGEX__ | __STRING__ __OR__ __REGULAR EXPRESSION__ |
| Check if the array attribute __has any value__ | __HAS A VALUE__ | __N/A__ |
| Check if the array attribute __is empty__ | __IS EMPTY__ | __N/A__ |

{% alert tip %}
For more on how to use our RegEx filter, check out this documentation on [Perl compatible regular expressions (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>

More resources on RegEx:
- [RegEx Tester and Debugger](https://regex101.com/)
- [RegEx: Learn More](https://regexr.com/)
- [RegEx Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

## Dates
Date attributes are useful for storing the last time a specific action was taken, so you can offer content specific re-engagement messaging to your users.

{% alert warning %}
The last date a custom event or purchase event occurred is automatically recorded, and should not be recorded in duplicate via a custom date attribute.
{% endalert %}

Date filters using relative dates (e.g., more than 1 day ago, less than 2 days ago) measure 1 day as 24 hours. Any campaign that you run using these filters will include all users in 24 hour increments. For example, last used app more than 1 day ago will capture all users who "last used the app more than 24 hours" from the exact time the campaign runs. The same will be true for campaigns set with longer date ranges – so five days from activation will mean the prior 120 hours.

For example, to build a segment that targets users with a date attribute between 24 and 48 hours in the future, apply the filters `in more than 1 day in the future` and `in less than 2 days in the future`.

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

## Integers (Standard and Incrementing) and Decimals (Floats/Doubles) {#integers}
Numeric attributes have a wide variety of use-cases. Incrementing integer custom attributes are useful for storing the number of times a given action or event has occurred without counting against your data cap. Standard integers and decimals have all sorts of usages, for example : (Recording shoe size, waist size, number of times a user has viewed a certain product feature, or category.

{% alert tip %}
Money spent in app should not be recorded by this method. Rather it should be recorded via our purchase methods shown two sections below.
{% endalert %}

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the numeric attribute __is more than__ an __integer or decimal value__| __MORE THAN__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __is less than__ an __integer or decimal value__| __LESS THAN__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __is exactly__ an __integer or decimal value__| __EXACTLY__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __does not equal__ an __integer or decimal value__| __DOES NOT EQUAL__ | __INTEGER__ or __DECIMAL__ |
| Check if the numeric attribute __exists__ on a user's profile | __EXISTS__ | __N/A__ |
| Check if the numeric attribute __does not exist__ on a user's profile | __DOES NOT EXIST__ | __N/A__ |

## Booleans (True/False)
Boolean attributes are useful for storing subscription statuses, and other simple binary data about your users. The input options that we provide allow you to find users that have explicitly had a variable set to a true/false value in addition to those that don't have any record of that attribute recorded yet.

| Segmentation Options | Dropdown Filter | Input Options |
| ---------------------| --------------- | ------------- |
| Check if the boolean value __is__ | __IS__  | __TRUE__, __FALSE__, __TRUE OR NOT SET__, or __FALSE OR NOT SET__ |
| Check if the boolean value __exists__ on a user's profile | __EXISTS__  | __N/A__ |
| Check if the boolean value __does not exist__ on a user's profile | __DOES NOT EXIST__  | __N/A__ |

## Purchases / Revenue Tracking

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

{% alert tip %}
If you would like to segment on the number of times a specific purchase has occurred, you should also record that purchase individually as an [incrementing custom attribute]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/#incrementingdecrementing-custom-attributes).
{% endalert %}
