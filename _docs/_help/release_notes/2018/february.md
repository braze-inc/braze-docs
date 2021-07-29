---
nav_title: February
page_order: 11
no_index: true
page_type: update
description: "This article contains release notes for February 2018."
---
# February 2018

## iOS Push Badge Count

You can now [update badge count][89] within the push composer from Braze.
For each push message, you can specify what badge count that notification triggers.

## Exporting Users via API Using Email Addresses

You can now [export user profile data via API][88] by specifying email addresses.
This export includes all profiles associated with that email address.

## Email Template APIs

You can now create and update [email templates via API][87]. Each template will have an **email_template_id** that can be referenced in other API calls.

## REST API Keys Permissions

You can now create [multiple REST API keys][86] and configure access permissions for each. Each key can be configured to grant access to certain endpoints.

You can also specify a [whitelist of IP addresses][85] and subnets that are allowed to make REST API requests for a given REST API Key.

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
