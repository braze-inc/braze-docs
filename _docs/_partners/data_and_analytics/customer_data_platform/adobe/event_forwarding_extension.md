---
nav_title: Event Forwarding Extension
article_title: Adobe
description: "This reference article covers the Braze event forward extension that allows you to leverage data captured in the Adobe Experience Platform Edge Network and send it to Braze in the form of server-side events."
page_type: partner
page_order: 2
search_tag: Partner

---

# Track Events API event forwarding extension

> The Braze Track Events API [event forwarding](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) extension allows you to leverage data captured in the Adobe Experience Platform Edge Network and send it to Braze in the form of server-side events using the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) API.

This document covers the use cases of the extension, how to install it in your event-forwarding libraries, and how to employ its capabilities in an event-forwarding [rule](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en).

{% alert note %}
Use of Adobe Event forwarding may increase your Braze data point usage. Refer to the Braze documentation on [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points) for more information.
{% endalert %}

## Use cases

This extension should use data from the Edge Network in Braze to take advantage of its customer analytics and targeting capabilities.

For example, consider a retail organization with a multichannel presence (website and mobile) and capturing transactional or conversational input as event data from their website and mobile platforms. 

Using various [tag](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en) rules, this data is sent to the Edge Network in real-time. From here, the Braze event forwarding extension automatically sends relevant events to Braze from the server side.

## Rate limits

| API | Rate Limits |
| --- | --- |
| User Track | 50,000 requests per minute.<br><br>Refer to the [User Track API documentation]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit) for details.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Gather required configuration details

To connect the Edge Network to Braze, the following are required:

| Key type | Description |
| --- | --- |
| Braze instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints). |
| Braze REST API key | A Braze REST API key with all permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 2: Create a secret

Create a new [event forwarding secret](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) and set the value to your [Braze API key](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). This will be used to authenticate the connection to your account while keeping the value secure.

### Step 3: Install and configure the Braze extension

1. To install the extension, [create an event forwarding property](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) or choose an existing property to edit instead.
2. Next, select **Extensions** in the left navigation. In the **Catalog** tab, select **Install** on the card for the Braze extension.
3. On the next screen, input your REST instance and API key and select **Save** when finished.

### Step 4: Create a send event rule

After installing the extension, create a new event forwarding [rule](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) and configure its conditions as desired. When configuring the actions for the rule, select the **Braze** extension, then select **Send Event** for the action type.

![]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab User Identification %}

| Input | Description |
| --- | --- |
| External user ID | A long, random, and well-distributed UUID or GUID. If you choose a different method to name your user IDs, they must also be long, random, and well-distributed. Learn more about [suggested user ID naming convention]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| Braze user ID | Braze user identifier. |
| User alias | An alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID.<br><br>The user alias object consists of two parts: an `alias_name` for the identifier itself and an `alias_label` indicating the type of alias. Users can have multiple aliases with different labels but only one `alias_name` per `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
To tie the event to a user, you must fill in either the `External User ID` field, the `Braze User Identifier` field, or the `User Alias` section.
{% endalert %}

{% endtab %}
{% tab Event Data %}

| Input | Description | Required |
| --- | --- | --- |
| Event name | Name of the event. | Yes |
| Event time | Date-time as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. | Yes |
| App identifier | The app identifier or `app_id` is a parameter associating activity with a specific app in your workspace. It designates which app within the workspace you are interacting with. | No |
| Event Properties | A JSON object containing custom properties of the event. | No |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
The **Braze Send Event** action requires only an **Event Name** and **Event Time** to be specified, but you should include as much information as possible in the custom properties field. Refer to [event object]({{site.baseurl}}/api/objects_filters/event_object/) for more details.
{% endalert %}

{% endtab %}
{% tab User Attribute %}

User attributes can be a JSON object containing fields that will create or update an attribute with the supplied name and value on the specified user profile. The following properties are supported:

| User Attribute | Description |
| --- | --- |
| First Name | First name of user. |
| Last Name | Last name of user. |
| Phone | Phone number of user. |
| Email | Email address of user. |
| Gender | One of the following strings: “M”, “F”, “O” (other), “N” (not applicable), “P” (prefer not to say). |
| City | The city of the user. |
| Country | The users country as a string in [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
| Language | The users language as a string in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format. |
| Date of Birth | The users data of birth in string in format “YYYY-MM-DD” (for example, 1980-12-21). |
| Time Zone | Time zone name from [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) database (for example, ’America/New_York’ or ’Eastern Time (US & Canada)’). |
| Facebook | A hash containing any of `id` (string), `likes` (array of strings), `num_friends` (integer). |
| Twitter | Hash containing any of id (integer), `screen_name` (string, X (formerly Twitter) handle), `followers_count` (integer), `friends_count` (integer), `statuses_count`(integer). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
All attributes added within the configuration will be sent each time the event is sent to Braze, regardless of whether the attribute's value has changed. When configuring user attributes, ensure you know how this will affect your data point usage.
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 5: Create a send purchase event rule

After installing the extension, create a new event forwarding [rule](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) and configure its conditions as desired. When configuring the actions for the rule, select the **Braze** extension, then select **Send Purchase Event** for the action type.

![]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab User Identification %}

| Input | Description |
| --- | --- |
| External user ID | A long, random, and well-distributed UUID or GUID. If you choose a different method to name your user IDs, they must also be long, random, and well-distributed. Learn more about [suggested user ID naming convention]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| Braze user ID | Braze user identifier. |
| User alias | An alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID.<br><br>The user alias object consists of two parts: an `alias_name` for the identifier itself and an `alias_label` indicating the type of alias. Users can have multiple aliases with different labels but only one `alias_name` per `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
To link the event to a user, you must complete either the `External User ID` field, the `Braze User Identifier` field, or the `User Alias` section.
{% endalert %}

{% endtab %}
{% tab Purchase Data %}

| Input | Description | Required |
| --- | --- | --- |
| Product ID | Identifier for the purchase. (for example, product name or product category) | Yes |
| Purchase time | Date-time as a string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. | Yes |
| Currency | Currency as a string in [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic currency code format. | Yes |
| Price | The price of the object. | Yes |
| Quantity | The quantity purchased. If not provided, the default value will be 1. The maximum value must be lower than 100. | No |
| App identifier | The app identifier or `app_id` is a parameter associating activity with a specific app in your workspace. It designates which app within the workspace you are interacting with. | No |
| Purchase properties | A JSON object containing custom properties of the purchase. | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
The **Send Purchase Event** action requires only a `Product ID`, `Purchase Time`, `Currency`, and `Price` to be specified, but you should include as much information as possible in the purchase properties field. Refer to [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/) for more details.
{% endalert %}

{% endtab %}
{% tab User Attributes %}

You can choose whether to send attributes with each event within the configuration view.

User attributes can be a JSON object containing fields that will create or update an attribute with the supplied name and value on the specified user profile. The following properties are supported:

| User Attribute | Description |
| --- | --- |
| First name | First name of user. |
| Last name | Last name of user. |
| Phone | Phone number of user. |
| Email | Email address of user. |
| Gender | One of the following strings: “M”, “F”, “O” (other), “N” (not applicable), “P” (prefer not to say). |
| City | The city of the user. |
| Country | The users country as a string in [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
| Language | The users language as a string in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format. |
| Date of birth | The users data of birth in string in format “YYYY-MM-DD” (for example, 1980-12-21). |
| Time zone | Time zone name from [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) database (for example, ’America/New_York’ or ’Eastern Time (US & Canada)’). |
| Facebook | A hash containing any of `id` (string), `likes` (array of strings), `num_friends` (integer). |
| Twitter | Hash containing any of id (integer), `screen_name` (string, X (formerly Twitter) handle), `followers_count` (integer), `friends_count` (integer), `statuses_count`(integer). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
All attributes added within the configuration will be sent each time the event is sent to Braze, regardless of whether the attribute's value has changed. When configuring user attributes, please ensure you know how this will affect your data point usage. 
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 6: Validate data within Braze

If the event collection and Adobe Experience Platform integration were successful, you will see events within the Braze console when [viewing user profiles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Specifically, the new event data sent to Braze is reflected in the **Purchases** or **Custom Events** section of a particular user’s [overview tab]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

