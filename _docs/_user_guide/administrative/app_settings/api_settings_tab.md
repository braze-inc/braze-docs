---
nav_title: APIs and identifiers
article_title: APIs and Identifiers
page_order: 3
page_type: reference
description: "This article covers the APIs and Identifiers page, which displays API identifications for your workspace."

---

# API keys

> The **APIs and Identifiers** page is your centralized hub for managing all your REST API keys in one place. Here, you can access each workspace's set of API keys and app identifiers.

You can find the **APIs and Identifiers** page under **Settings**.

## API keys

This section provides your workspace REST API keys, the unique identifiers that allow you access to your data for a workspace. A REST API key is required with every request to the Braze API. For more information on creating and using API keys, refer to our [REST API key overview]({{site.baseurl}}/api/api_key/).

### API IP allowlisting

For additional security, you can specify a list of IP addresses and subnets allowed to make REST API requests for a given REST API Key. This is referred to as allowlisting, or whitelisting. To allow specific IP addresses or subnets, add them to the **Whitelist IPs** section when creating a new REST API Key: 

![API IP Whitelisting section of creating a new API key]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

If you don't specify any, requests can be sent from any IP address.

{% alert tip %}
Making a Braze-to-Braze webhook and using allowlisting? Check out our list of [IPs to whitelist]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### API usage alerts

Set up API usage alerts to monitor key API activity and spot issues early. These alerts help you detect unexpected traffic patterns before they impact your experience.

You can track two types of API activity:

- **REST API endpoints:** Actions like sending messages, creating campaigns, or exporting data.
- **SDK API requests:** Events from your customer experience, such as triggering in-app messages or syncing user profiles. *This feature is available if you’ve purchased Monthly Active Users (CY 24–25).*

Once you choose what to track, you can define alert conditions. For example, get notified if error responses increase by 20% within an hour. You’ll get a notification by email, webhook, or both, depending on your settings. To get started, see [API usage alerts]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_alerts/).

## App identifiers

This section includes a list of identifiers used to reference specific apps in requests made to the Braze API. To learn more about application identifiers, refer to [App identifier API key]({{site.baseurl}}/api/identifier_types/).

## Other identifiers

To integrate with our API, you can search for the identifiers related to any segments, campaigns, Content Cards, and more that you want to access from the Braze external API. All messages should follow [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding. After you've selected any of them, the identifier will be displayed underneath the dropdown menu.

For more information, refer to [API identifier types]({{site.baseurl}}/api/identifier_types/).

