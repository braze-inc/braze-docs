---
nav_title: API Settings
page_order: 0

page_type: reference
description: "This reference article covers the API Settings page, which displays API identifications for your app group."
tool: Dashboard
---

# API Settings Tab

The API Settings page displays API identifications for your app group. The first section on Services will link you to our technical documentation for whatever you’re using the API for ([User Data][3], [Messaging][4], [Email Sync][5], and [Exporting][6] your data).

### REST API Keys

This section provides your App Group REST API Key, the unique identifier that allows you access to your data for an app group. This key is required with every request to the Braze API.

### API Whitelisting

You can whitelist specific IP addresses and subnets to send requests to our API for this app group. If you don’t specify any, requests can be sent from any IP address.

### Identification

These identifiers are used to reference specific Apps in requests made to the Braze API.

### Additional API Identifiers

To integrate with our API, you can search for the identifiers related to any Segment, Campaigns or Cards that you want to access from Braze's external API. All messages should follow [UTF-8][12] encoding. Once you’ve selected any of them, the identifier will be displayed underneath the dropdown menu.

[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/
[4]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[5]: {{site.baseurl}}/developer_guide/rest_api/email_sync/
[6]: {{site.baseurl}}/developer_guide/rest_api/export/
[12]: https://en.wikipedia.org/wiki/UTF-8
