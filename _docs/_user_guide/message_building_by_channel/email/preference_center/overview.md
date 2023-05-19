---
nav_title: Overview
article_title: Preference Center Overview
page_order: 1
description: "This article describes the email preference center and how to customize it."
channel:
  - email
---

# Preference center overview

> Setting up a preference center provides a one-stop shop for your users to edit and manage their notification preferences for your [email messaging]({{site.baseurl}}/user_guide/message_building_by_channel/email/).

In the Braze dashboard, navigate to **Subscription Groups > Email Preference Center** tab. 

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), you can find **Email Preference Center** under **Audience** > **Subscriptions**, then select the **Email Preference Center** tab.
{% endalert %}

This is where you can manage and view each subscription group. Each subscription group you create is added to this preference center list. You can create multiple preference centers.

{% alert important %}
The preference center is intended to be used within the Braze email channel. The preference center links are dynamic based on each user and cannot be hosted externally.
{% endalert %}

## Create a preference center via API

By using the [Preference Center Braze endpoints]({{site.baseurl}}/api/endpoints/preference_center), you can create a preference center, a website hosted by Braze, that can display your user's subscription state and subscription group statuses. Using HTML and CSS, your developer team can build the preference center using HTML and CSS so that the styling of the page matches your brand guidelines.

Using Liquid enables you to retrieve the names of your subscription groups, and each user's status. This way, Braze stores and retrieves this data when the page is loaded.

### Prerequisites

| Requirement | Description |
|---|---|
| Enabled preference center | Your Braze dashboard has permissions to use the preference center feature. |
| Valid workspace with an email, SMS, or WhatsApp subscription group | A working workspace with valid users and an email, SMS, or WhatsApp subscription group. |
| Valid user | A user with an email address and an external ID. |
| Generated API key with preference center permissions | In the Braze dashboard, go to **Developer Console** > **API Settings** to confirm that you have access to an API key with preference center permissions. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), **API Settings** is now **API Keys** and can be found at **Settings** > **Setup and Testing** > **API Keys**.
{% endalert %}

### Step 1: Create a preference center via API

Let's begin building a preference center using the [Create preference center endpoint]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). To customize your preference center, you can include HTML that aligns with your branding in the `preference_center_page_html` field and `confirmation_page_html` field.

The [Generate preference center URL endpoint]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) allows you to grab the preference center URL for a specific user outside of an email that is sent through Braze.

### Step 2: Include in email campaign

To place a link to the preference center in your emails, use the following Liquid tag in the desired place in your email, similar to the way you would insert unsubscribe URLs.

{% raw %}
```liquid
{{${preference_center.${preference_center_name_example}}}
```
{%endraw%}

You can also use a combination of HTML that includes Liquid. For example, you can paste the following as the URL in either the HTML editor or Drag & Drop Editor. This will show the basic preference center layout that lists all of the email subscription groups automatically. 

{% raw %}
```html
<a href="{{preference_center.${preference_center_name_example}}}">Edit your preferences</a>
```
{%endraw%}

The preference center has a checkbox that will allow your users to unsubscribe from all emails. Note that you will not be able to save these preferences if sent as a test message.

{% alert important %}
The above Liquid tag will only work when launching a Campaign or Canvas. Sending a test email will not generate a valid link.
{% endalert %}

#### Editing a preference center

You can edit and update your preference center by using the [Update preference center endpoint]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/). 

#### Identifying preference centers and details

To identify your preference centers, use the [View details for preference center endpoint]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) to return related information such as the last updated timestamp, the preference center ID, and more.

## Customization

Braze manages the subscription state updates from the preference center, which keeps the preference center in sync. However, you can also create and host your own preference center using the [subscription groups APIs]({{site.baseurl}}/developer_guide/rest_api/subscription_group_api/) with the following options.

### Option 1: Link with string query parameters

Use query string field-value pairs in the body of the URL to pass the users ID and email category to the page so users will only need to confirm their choice to unsubscribe. This option is good for those who store a user identifier in a hashed format and do not already have a subscription center.

For this option, each email category will require its own specific unsubscribe link:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
It is also possible to hash the user's external ID at the point of send using a Liquid filter. This will convert the `user_id` to an MD5 hash value, for example:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Option 2: Authenticate with JSON web token

Use a [JSON web token](https://auth0.com/learn/json-web-tokens/) to authenticate users to a part of your web server (e.g., account preferences) that is normally behind a layer of authentication such as username and password login. 

This approach does not require query string value-pairs embedded in the URL as these can be passed in the JSON web token's payload, for example:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```
