---
nav_title: Preference Center
article_title: Preference Center
page_order: 5
description: "This article describes how to create and edit a preference center using the Preference Center Braze endpoints."
channel:
  - email
---

# Creating a preference center via API

Setting up a preference center provides a one-stop shop for your users to edit their notification preferences with your [email messaging]({{site.baseurl}}/user_guide/message_building_by_channel/email/). By using the preference center Braze endpoints, you can directly edit the HTML of your preference center to align with your branding and to understand your users' preferences.

{% alert important %}
The Braze endpoints used to create a preference center are currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

| Requirement | Description |
|---|---|
| Enabled preference center | Your Braze dashboard has permissions to use the preference center feature. |
| Valid app group with an email subscription group | A working app group with valid users and an email subscription group. |
| Valid user | A user with an email address and an external ID. |
| Generated API key with preference center permissions | In the Braze dashboard, go to **Developer Console** > **API Settings** to confirm that you have access to an API key with preference center permissions. |
{: .reset-td-br-1 .reset-td-br-2}

## Step 1: Create a preference center via API

{% raw %}
Let's begin building a preference center using the [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/) endpoint. To customize your preference center, you can include HTML that aligns with your branding for the `preference_center_page_html` field and `confirmation_page_html` field.

The [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) endpoint allows you to grab the preference center URL for a specific user outside of an email that is sent through Braze.

## Step 3: Include in email campaign

Next, include insert your preference center into your email campaign by using a combination of HTML that includes Liquid. Here's an example of what you could include at an email footer to indicate to your users that they can edit their preferences. 

```html
<a href="{{preference_center.${preference_center_name_example}}}">Edit your preferences</a>
```
{%endraw%}

## Editing a preference center

You can edit and update your preference center by using the [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) endpoint. 

## Identifying preference centers and details

To identify your preference centers, use the [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) endpoint to return related information such as the a last updated timestamp, the preference center ID, and more.

`