---
nav_title: API Settings
page_order: 0
---

# API Settings Tab

The API Settings page displays API identifications for your app group. The first section on Services will link you to our technical documentation for whatever you’re using the API for ([User Data][3], [Messaging][4], [Email Sync][5], and [Exporting][6] your data).

### Rest API Keys

This section provides your App Group REST API Key, the unique identifier that allows you access to your data for an app group. This key is required with every request to the Braze API.

### API Whitelisting

You can whitelist specific IP addresses and subnets to send requests to our API for this app group. If you don’t specify any, requests can be sent from any IP address.

### Identification

These identifiers are used to reference specific Apps in requests made to the Braze API.

### Additional API Identifiers

To integrate with our API, you can search for the identifiers related to any Segment, Campaigns or Cards that you want to access from Braze's external API. Once you’ve selected any of them, the identifier will be displayed underneath the dropdown menu.

[1]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages
[2]: {% image_buster /assets/img_archive/msgactlog1.png %}
[3]: {{ site.baseurl }}/developer_guide/rest_api/user_data/
[4]: {{ site.baseurl }}/developer_guide/rest_api/messaging/
[5]: {{ site.baseurl }}/developer_guide/rest_api/email_sync/
[6]: {{ site.baseurl }}/developer_guide/rest_api/export/
[7]: {% image_buster /assets/img_archive/internal_group.png %}
[8]: {% image_buster /assets/img_archive/UserLogs1.png %}
[9]: {% image_buster /assets/img_archive/content_test_preview.png %}
[10]: {% image_buster /assets/img_archive/rawlogs.png %}
[11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
