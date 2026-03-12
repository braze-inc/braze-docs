---
nav_title: Data types
article_title: Data types
page_order: 1
page_type: reference
description: "Reference for supported data types for custom attributes, event properties, and catalogs in Braze."
toc_headers: h2
---

# Data types

> This page consolidates the supported data types for custom attributes, event properties, and catalogs. Each custom data type has slightly different data type support and constraints.

## Definitions {#definitions}

Use this table to see which data types you can use for user profile attributes, event data, or catalog items. Refer to the sections that follow for usage and constraints for each type.

<table role="presentation" class="definitions-table reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4 reset-td-br-5">
  <thead>
    <tr>
      <th>Data type</th>
      <th>Definition</th>
      <th>Custom attributes</th>
      <th>Event properties</th>
      <th>Catalogs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Boolean</td>
      <td>Value <code>true</code> or <code>false</code></td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
    </tr>
    <tr>
      <td>Number</td>
      <td>Whole number or decimal</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
    </tr>
    <tr>
      <td>String</td>
      <td>Text; 255 characters or fewer</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
    </tr>
    <tr>
      <td>Time</td>
      <td>Date and time in a standard format (<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>)</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>Ordered list of values</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
    </tr>
    <tr>
      <td>Object</td>
      <td>Structured data with named fields (nested key-value)</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
      <td>✅ Supported</td>
    </tr>
    <tr>
      <td>Array of objects</td>
      <td>List of objects</td>
      <td>✅ Supported</td>
      <td>❌ Not supported</td>
      <td>❌ Not supported</td>
    </tr>
  </tbody>
</table>

### Important considerations 

- **Array:** Custom attributes and event properties have size limits. Datetimes are not supported inside arrays in event properties. Catalogs support only string arrays, with a maximum of 100 elements.
- **Object:** In Braze, this appears as "nested custom attributes" for custom attributes, "nested objects" for event properties, and "JSON object" for catalogs.
- **Time:** In event properties, this type is labeled "Datetime."

## Custom attribute data types {#custom-attribute-data-types}

Custom attributes support the data types listed in the [Definitions](#definitions) table. The following describes usage and segmentation for each supported data type.

{% tabs %}
{% tab Boolean %}

For **Boolean** attributes, the following segmentation options are available.

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the boolean value **is** either true, false, true or not set, or false or not set | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, or **FALSE OR NOT SET** | If this filter specifies `coffee_drinker`, a user will match this filter in the following circumstances: <br> {::nomarkdown}<ul><li>If this filter is <code>true</code> and the user has the value <code>coffee_drinker</code></li><li>If this filter is <code>false</code> and the user doesn't have the value <code>coffee_drinker</code></li><li>If this filter is <code>true or not set</code> and the user has the value <code>coffee_drinker</code> or no value</li><li>If this filter is <code>false or not set</code> and the user doesn't have <code>coffee_drinker</code> or any value</li></ul>{:/} |
| Check if the boolean value **exists** on a user's profile and is not null | **IS NOT BLANK**  | **N/A** | If this filter specifies `coffee_drinker` and a user has a value for the attribute `coffee_drinker`, the user will match this filter. |
| Check if the boolean value **does not exist** on a user's profile or is null | **IS BLANK**  | **N/A** | If this filter specifies `coffee_drinker` and a user either doesn't have the attribute `coffee_drinker` or the value for `coffee_drinker` is null, the user will match this filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Numbers %}

{% alert tip %}
Money spent should not be recorded by this method. Rather it should be recorded via [purchase events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/).
{% endalert %}

For **Number** attributes, the following segmentation options are available.

| Segmentation options | Dropdown filter | Input options | Examples |
| ---------------------| --------------- | ------------- | -------- |
| Check if the numeric attribute **is exactly** a **number**| **EXACTLY** | **NUMBER** | If this filter specifies `10` and a user profile has the value `10`, the user will match this filter. |
| Check if the numeric attribute **does not equal** a **number**| **DOES NOT EQUAL** | **NUMBER** | If this filter specifies `10` and a user profile doesn't have the value `10`, the user will match this filter. |
| Check if the numeric attribute **is more than** a **number**| **MORE THAN** | **NUMBER** | If this filter specifies `10` and a user profile has a value greater than `10`, the user will match this filter. |
| Check if the numeric attribute **is less than** a **number**| **LESS THAN** | **NUMBER** | If this filter specifies `10` and a user profile has a value lesser than `10`, the user will match this filter. |
| Check if the numeric attribute **exists** on a user's profile and is not null | **IS NOT BLANK** | **N/A** | If a user profile contains the specified numeric attribute, regardless of value, the user will match this filter. |
| Check if the numeric attribute **does not exist** on a user's profile or is null | **IS BLANK** | **N/A** | If a user profile doesn't contain the specified numeric attribute or the attribute's value is null, the user will match this filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Number attribute details

- "Exactly 0" and "Less Than" filters include users with NULL fields
  - To exclude users without a value for custom attributes, you need to include the **is not blank** filter.

{% endtab %}
{% tab Strings %}

String attributes can be up to 255 characters long. Note that if you input any values with spaces in between, before, or after words, Braze will also check for the same spaces.

For **String** attributes, the following segmentation options are available.

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

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
When segmenting using the **DOES NOT MATCH REGEX** filter, you must already have a custom attribute with a value assigned in that user profile. Braze suggests using "OR" logic to check if a custom attribute is blank to ensure users are being targeted properly.
{% endalert %}

{% endtab %}
{% tab Arrays %}

Arrays have a maximum size of 100&nbsp;KB. The default length for an attribute is up to 500 items (for example, if you're sending an attribute such as "Movies Watched" set to 500, when a user watches a 501st movie, the first movie is removed and the most recent is added). Note that if you input any values with spaces in between, before, or after words, Braze will also check for the same spaces.

{% alert note %}
The option to increase the maximum length will not be available if the attribute is set to automatically detect the data type; the data type must be set to array.
{% endalert %}

For **Array** attributes, the following segmentation options are available.

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

{% endtab %}
{% tab Time %}

Time filters using relative dates (for example, more than 1 day ago, less than 2 days ago) measure 1 day as 24 hours. For example, to build a segment that targets users with a time attribute between 24 and 48 hours in the future, apply the filters `in more than 1 day in the future` and `in less than 2 days in the future`.

{% alert warning %}
The last date a custom event or purchase event occurred is automatically recorded and shouldn't be recorded again via a custom time attribute.
{% endalert %}

For **Time** attributes, the following segmentation options are available.

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

{% endtab %}
{% tab Objects %}

You can use nested custom attributes to send objects as a data type for custom attributes. For more information, refer to [Nested custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/).

{% endtab %}
{% tab Arrays of objects %}

Use an array of objects to group related attributes. For more details, refer to [Array of objects]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/).

{% endtab %}
{% endtabs %}

You can change the data type of your custom attribute, but you should be aware of the impacts. Refer to [Changing custom attribute or event data type](#changing-custom-attribute-or-event-data-type) for more.

### Consolidated operators {#consolidated-operators}

We've consolidated the list of operators available to use in attribute filters, custom attribute filters, and nested custom attribute filters. If you have existing filters using these operators, they will be automatically updated to use the new operators.

| Data type | Old operator | New operator | Value |
| --- | --- | --- | --- |
| String | equals | is any of | At least 1 value |
| String | does not equal | is none of | At least 1 value |
| Array | includes value | includes any of | At least 1 value |
| Array | doesn't include value | includes none of | At least 1 value |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Event property data types {#event-property-data-types}

When you log an event, you can attach extra information (for example, product name or price) as event properties. Each property has a name and a value. Event property values support the data types in the [Definitions](#definitions) table (Time is labeled "Datetime" in event properties).

### Expected format {#expected-format}

Property values are sent as an object: keys are the property names, and values are the property values. Property names must be non-empty strings, 255 characters or fewer, with no leading dollar signs (`$`).

Event-property-specific rules:

- **Time (Datetime):** Use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) or `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. Not supported within arrays.
- **Array:** Datetimes are not supported within arrays.
- **Nested object:** See [Nested objects]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/).
- **Payload:** Event property objects that contain array or object values can be up to 100&nbsp;KB.

You can change the data type of your custom event property, but be aware of the impacts of [changing data types](#changing-custom-attribute-or-event-data-type) after data has been collected.

For full event property behavior, reserved keys, and usage in triggers and personalization, see [Custom event properties]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).

## Purchase events and revenue {#purchase-events-and-revenue}

Purchase and revenue data is recorded through [purchase events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/) or recommended eCommerce events.

{% alert note %}
Recommended events have pre-defined schemas with set data types. For details, refer to [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/).
{% endalert %}

Logging purchase events establishes the Lifetime Value (LTV) for each user profile, and this data is viewable on the revenue page in time-series. You can segment on money spent, last purchase date, number of purchases in a time window, and more.

### Purchase event property data types {#purchase-event-property-data-types}

Purchase event property values (the `properties` object on a purchase) support the data types in the [Definitions](#definitions) table, with the same structure and naming rules as [event properties](#expected-format).

{% include data_activation/purchase_event_property_data_types.md %}

For the full purchase object schema and examples, see [Purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/). For logging purchase events, segmentation filters, and full details, refer to [Purchase events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/).

## Changing custom attribute or event data type {#changing-custom-attribute-or-event-data-type}

To change the data type of a custom attribute or event:

1. Go to **Data Settings** and select either **Custom Attributes** or **Custom Events**.
3. Find your attribute or event from the list, and select <i class="fa fa-ellipsis-v" aria-hidden="true"></i> **More actions**.
4. Select a new **Data type** from the dropdown.
5. Select **Save**.

If you change the data type of a custom attribute or event (for example, changing `time` to `string`), consider the following:

- **Filters are not automatically updated.** Segments, campaigns, Canvases, or other locations that use the changed attribute or event are not updated. Before you change the data type, stop any campaigns or Canvases that use the attribute in segments or filters, and remove the attribute from filters that reference it.
- **Existing user data is not retroactively updated.** If the changed attribute was on a user profile before the change, that value remains the old data type. Users can fall out of segments that contain the changed attribute because the filter looks for the new data type. Update those user profiles (for example, with the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)) so they match the new type and re-enter the segment if needed.
- **New data must match the new type.** API calls that send the previous data type for the changed attribute are not accepted. Send the new data type.

{% alert important %}
The ability to prevent automatic detection from updating the custom attribute data type is currently in early access. Contact your customer success manager if you're interested in participating.
{% endalert %}

## Catalog data types {#catalog-data-types}

Catalogs support the types listed in the [Definitions](#definitions) table. The following table lists each type, how it can be created or updated, and format and examples.

| Data type | Description | Available via CSV upload | Available via API and CDI |
| --- | --- | --- | --- |
| String | A sequence of characters (for example, names, descriptions, IDs). | ✅ Yes | ✅ Yes |
| Number | A numeric value, either integer or float (for example, prices, quantities, ratings). | ✅ Yes | ✅ Yes |
| Boolean | A `true` or `false` value. | ✅ Yes | ✅ Yes |
| Time | Date and time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format or Unix timestamp in seconds. | ✅ Yes | ✅ Yes |
| JSON object (Object) | Nested object with key-value pairs. Displayed in the platform but can only be created or updated through the API or CDI. | ❌ No | ✅ Yes |
| String array (Array) | A list of strings. Displayed in the platform but can only be created or updated through the API or CDI. Maximum of 100 elements. | ❌ No | ✅ Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Format and examples

| Data type | Format | Example |
| --- | --- | --- |
| String | Text | <code>"Hello World"</code> |
| Time | ISO 8601 or Unix timestamp (seconds) | <code>"2024-03-15T14:30:00Z"</code> |
| Boolean | <code>true</code> or <code>false</code> | <code>true</code> |
| Number | Integer or decimal | <code>42</code> or <code>19.99</code> |
| Object | JSON object | <code>{"key": "value", "price": 10}</code> |
| Array | Array of strings | <code>["red", "blue", "green"]</code> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For creating and updating catalogs, see [Create a catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create/).
