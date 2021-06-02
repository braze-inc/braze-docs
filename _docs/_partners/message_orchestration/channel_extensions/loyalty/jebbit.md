---
nav_title: Jebbit
page_order: 4
description: "This article outlines the partnership between Braze and Jebbit, a PaaS that allows you to pass user emails and attributes from your Jebbit campaigns as user data to Braze in real-time."
alias: /partners/jebbit/

page_type: partner
---

# Jebbit

> [Jebbit](https://www.jebbit.com/) is a PaaS to which you can build engaging experiences for users to capture first-party data.

Jebbit has partnered with Braze so that you can pass user emails and attributes from your Jebbit campaigns as user data to Braze in real-time. This data can then be utilized to drive marketing initiatives like personalized email campaigns and triggers. 

## Requirements

When requesting integrating with Jebbit, please communicate if any hard deadlines need to be met.
Additionally, please make sure that you have the attributes mapped to your Jebbit experience(s) that you would like passed to Braze.
It is also important to note that the attribute ID you have set in Jebbit is how the attribute field name will be shown in Braze.

| Requirement | Origin | Access | Description |
|---|---|---|---|
|Braze App Group REST API Key | Braze platform | Developer Console > Rest API Keys | Please create an API Key with all permissions checked under “User Data”, and provide this key via [Dropbox File Request](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx) |
|Braze API Endpoint | Braze platform | Check out our [listed endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) or open a support ticket. | We currently support the [user data]({{site.baseurl}}/api/endpoints/user_data/) endpoint specifically, but a request for a different endpoint can be supported. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Out-of-the Box Integration

### Step 1: Provide API Credentials

Please provide your API credentials as required from the above table. 
For security reasons, we ask that you transfer the information from a .txt file via a Dropbox File request. Please submit your file using the following [Dropbox URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Step 2: Confirm Test Submission

A Jebbit engineer assigned to your integration will push through a test submission for Jebbit to Braze so you are able to see exactly how the data will look in your Braze environment.
This will be the final step prior to activating the integration.

### Step 3: Activate your Jebbit Data

Now that you have your Jebbit Data flowing into your Braze account, use it to drive your marketing initiatives.

## Customization

We currently support the [user data]({{site.baseurl}}/api/endpoints/user_data/) endpoints specifically, but requests for different endpoints can be supported.
Attribute field names can also be customized to your preference.

## Using This Integration

There are no further steps required for you to connect your Jebbit data to Braze.
If you want additional attributes from Jebbit in Braze, simply map the new attribute in your Jebbit account.
The new attribute will automatically show in Braze as you collect data for that attribute.
