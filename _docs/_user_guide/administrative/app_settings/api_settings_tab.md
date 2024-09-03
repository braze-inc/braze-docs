---
nav_title: APIs and Identifiers
article_title: APIs and Identifiers
page_order: 3
page_type: reference
description: "This article covers the APIs and Identifiers page, which displays API identifications for your workspace."

---

# API keys

> The **APIs and Identifiers** page is your centralized hub for managing all your REST API keys in one place. Here, you can access each workspace's set of API keys and app identifiers.

You can find the **APIs and Identifiers** page under **Settings**.

{% alert note %}
If you're using the older navigation, this page is called **API Settings** and is located under **Settings** > **Manage Settings**.
{% endalert %}

### API keys

This section provides your workspace REST API keys, the unique identifiers that allow you access to your data for a workspace. A REST API key is required with every request to the Braze API. For more information on creating and using API keys, refer to our [REST API key overview]({{site.baseurl}}/api/api_key/).

#### API IP allowlisting

For additional security, you can specify a list of IP addresses and subnets allowed to make REST API requests for a given REST API Key. This is referred to as allowlisting, or whitelisting. To allow specific IP addresses or subnets, add them to the **Whitelist IPs** section when creating a new REST API Key: 

![API IP Whitelisting section of creating a new API key][26]

If you don't specify any, requests can be sent from any IP address.

{% alert tip %}
Making a Braze-to-Braze webhook and using allowlisting? Check out our list of [IPs to whitelist]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### App identifiers

This section includes a list of identifiers used to reference specific apps in requests made to the Braze API. To learn more about application identifiers, refer to [App identifier API key]({{site.baseurl}}/api/identifier_types/).

### Other identifiers

To integrate with our API, you can search for the identifiers related to any segments, campaigns, Content Cards, and more that you want to access from the Braze external API. All messages should follow [UTF-8][12] encoding. After you've selected any of them, the identifier will be displayed underneath the dropdown menu.

For more information, refer to [API identifier types]({{site.baseurl}}/api/identifier_types/).

[3]: {{site.baseurl}}/api/endpoints/user_data/
[4]: {{site.baseurl}}/api/endpoints/messaging/
[5]: {{site.baseurl}}/api/endpoints/email/
[6]: {{site.baseurl}}/api/endpoints/export/
[12]: https://en.wikipedia.org/wiki/UTF-8 "Wikipedia: UTF-8"
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}