---
nav_title: Overview
article_title: Preference Center Overview
page_order: 1
description: "This article describes the email preference center and how to customize it."
channel:
  - email
---

# Preference center overview

> The email preference center is an easy way to manage which users receive certain groups of newsletters and can be found in the Braze dashboard under **Subscription Groups**. 

Each subscription group you create is added to the preference center list. Click on the name of the preference center to see an interactive preview.

To place a link to the preference center in your emails, use the following Liquid tag and add it to the desired place in your email, similar to the way you insert [unsubscribe URLs](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

This will show the basic preference center layout that lists all of the email subscription groups automatically.

{% alert note %}
The preference center has a checkbox that will allow your users to unsubscribe from all emails. Note that you will not be able to save these preferences if sent as a test message.
{% endalert %}

The preference center is intended to be used within the email channel. The preference center links are dynamic based on each user and cannot be hosted externally.

## Customize your preference center

Built using the Braze [Preference Center endpoints]({{site.baseurl}}/api/endpoints/preference_center/), a preference center is a Braze-hosted website that can display your user's subscription state and subscription group statuses. 

Using HTML and CSS, your developer team can build the preference center using HTML and CSS so that the styling of the page matches your brand guidelines.

You can create multiple preference centers. Using Liquid enables you to retrieve the names of your subscription groups, and each user's status. This way, Braze stores and retrieves this data when the page is loaded.

As an alternative, you can also create and host your own preference center using the [subscription groups APIs]({{site.baseurl}}/developer_guide/rest_api/subscription_group_api/) with the following options.

**Option 1: Link with string query parameters**

Use query string field-value pairs in the body of the URL to pass the users ID and email category to the page so users will only need to confirm their choice to unsubscribe. This option is good for those who store a user identifier in a hashed format and do not already have a subscription center.

For this option, each email category will require its own specific unsubscribe link:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
It is also possible to hash the users `external_id` at the point of send using a Liquid filter. This will convert the `user_id` to an MD5 hash value, for example:
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
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

### Logo

To edit the logo in your email preference center, select the <i class="fas fa-cog"></i> gear icon and click **Edit**.
