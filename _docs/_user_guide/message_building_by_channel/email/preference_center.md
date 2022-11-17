---
nav_title: Preference Center
article_title: Preference Center
page_order: 5
description: "This article describes how to create and edit a preference center using the Preference Center Braze endpoints."
channel:
  - email
---

# Creating a preference center via API

Setting up a preference center provides a one-stop shop for your users to edit their notification preferences with your [email messaging]({{site.baseurl}}/user_guide/message_building_by_channel/email/). By using the [Preference Center Braze endpoints]({{site.baseurl}}/api/endpoints/preference_center), you can directly edit the HTML of your preference center to align with your branding and to understand your users' preferences.

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
Let's begin building a preference center using the [`/preference_center/v1` endpoint][1]. To customize your preference center, you can include HTML that aligns with your branding for the `preference_center_page_html` field and `confirmation_page_html` field.

The [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}` endpoint][2] allows you to grab the preference center URL for a specific user outside of an email that is sent through Braze.

## Step 2: Include in email campaign

Next, insert your preference center into your email campaign by pasting a combination of HTML that includes Liquid. For example, you can paste the following as the link URL in either the HTML or Drag & Drop Editor.  

```html
<a href="{{preference_center.${preference_center_name_example}}}">Edit your preferences</a>
```
{%endraw%}

{% alert important %}
The above Liquid tag will only work when launching a Campaign or Canvas. Sending a test email will not render a valid link.
{% endalert %}

## Editing a preference center

You can edit and update your preference center by using the [`/preference_center/v1/{preferenceCenterExternalId}` endpoint][3]. 

## Identifying preference centers and details

To identify your preference centers, use the [`/preference_center/v1/{preferenceCenterExternalId}` endpoint][4] to return related information such as the last updated timestamp, the preference center ID, and more.

[1]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[2]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[3]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[4]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/ 
