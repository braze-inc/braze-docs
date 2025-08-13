---
nav_title: Jebbit
article_title: Jebbit
description: "This reference article outlines the partnership between Braze and Jebbit, a PaaS that allows you to pass user emails and attributes from your Jebbit campaigns as user data to Braze in real-time."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) is a PaaS that allows you to build engaging experiences for users to capture first-party data.

_This integration is maintained by Jebbit._

## About the integration

The Braze and Jebbit integration lets you pass user emails and attributes from your Jebbit campaigns as user data to Braze in real-time. This data can then be used to drive marketing initiatives like personalized email campaigns and triggers. 

## Prerequisites

| Requirement | Description |
|---|---|
|Jebbit account | A Jebbit account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all user data permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
|Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

When requesting integrating with Jebbit, communicate if any hard deadlines need to be met. Additionally, make sure that you have the attributes mapped to your Jebbit experience(s) that you would like passed to Braze.

### Step 1: Provide API credentials

Provide your API credentials to Jebbit in a text file via a Dropbox file request.
Submit your file using the following [Dropbox URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Step 2: Confirm test submission

A Jebbit engineer assigned to your integration will push through a test submission from Jebbit to Braze, so you can see how the data will look in your Braze environment. This is the final step in activating the integration. Now that your Jebbit data is set up, use it to drive your marketing initiatives.

{% alert note %}
The attribute ID you have set in Jebbit is how the attribute field name will be shown in Braze.
{% endalert %}

## Customization

We currently support the [user data]({{site.baseurl}}/api/endpoints/user_data/) endpoints specifically, but requests for different endpoints can be supported.

Attribute field names can also be customized to your preference.

If you want additional attributes from Jebbit in Braze, map the new attribute in your Jebbit account. The attribute will automatically show in Braze as you collect data for that attribute.

