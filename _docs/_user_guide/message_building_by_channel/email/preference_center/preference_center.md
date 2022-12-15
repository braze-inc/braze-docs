---
nav_title: Overview
article_title: Preference Center Overview
page_order: 1
description: "This article describes how to create and edit a preference center using the Preference Center Braze endpoints."
channel:
  - email
---

# Email preference center

The email preference center is an easy way to manage which users receive certain groups of newsletters and can be found in the dashboard under **Subscription Groups**. Each subscription group you create is added to the Preference Center list. Click on the name of the Preference Center to see an interactive preview.

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation/), you can find **Email Preference Center** under **Audience** > **Subscription** > **Email Preference Center**.
{% endalert %}

To place a link to the preference center in your emails, use the following preference center Liquid tag and add it to the desired place in your email, similar to the way you insert [unsubscribe urls](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

{% alert note %}
The Preference Center has a checkbox that will allow your users to unsubscribe from all emails. Note that you will not be able to save these preferences if sent as a test message.
{% endalert %}

The preference center is intended to be used strictly within the email channel itself. The preference center links are dynamic, based on each user, and cannot be hosted externally. You may, however, create and host your own custom preference center with the [Preference Center Endpoints]({{site.baseurl}}/api/endpoints/preference_center/) and use the [Subscription Group REST APIs][25] to keep data in sync with Braze. Refer to the next section for more.

## Customize your preference center

You can create and host on your web server a fully custom HTML preference center and sync to Braze using our [APIs][28]. At this time, you can only have one preference center, which will list all of your current subscription groups.

**Option 1: Link with string query parameters**

Use query string field-value pairs in the body of the URL to pass the users ID and email category to the page so users will only need to confirm their choice to unsubscribe. This option is good for those who store a user identifier in a hashed format and do not already have a subscription center.

For this option, each email category will require its own specific unsubscribe link:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
It is also possible to hash the users `external_id` at the point of send using a Liquid filter. This will convert the `user_id` to an md5 hash value, for example:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}

My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

**Option 2: JSON web token**

Use a [JSON web token](https://auth0.com/learn/json-web-tokens/) to authenticate users to a part of your web server (e.g., account preferences) that is normally behind a layer of authentication such as username and password login. This approach does not require query string value-pairs embedded in the URL as these can be passed in the JSON web token's payload, for example:

```json
{
    “user_id”: "1234567890",
    "name": "John Doe",
    “category": offers
}
```

### Logo

You can edit the logo of your preference center. Click the gear, then click **Edit** from the menu that appears.

[25]: {{site.baseurl}}/developer_guide/rest_api/subscription_group_api/

