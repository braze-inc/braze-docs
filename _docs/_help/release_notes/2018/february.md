---
nav_title: February
page_order: 11
noindex: true
page_type: update
description: "This article contains release notes for February 2018."
---
# February 2018

## iOS push badge count

You can now [update badge count]({{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count) within the push composer from Braze.
For each push message, you can specify what badge count that notification triggers.

## Exporting users via API using email addresses

You can now [export user profile data via API]({{site.baseurl}}/developer_guide/rest_api/export/#user-export) by specifying email addresses.
This export includes all profiles associated with that email address.

## Email template APIs

You can now create and update [email templates via API]({{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates). Each template will have an **email_template_id** that can be referenced in other API calls.

## REST API keys permissions

You can now create [multiple REST API keys]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) and configure access permissions for each. Each key can be configured to grant access to certain endpoints.

You can also specify a [whitelist of IP addresses]({{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting) and subnets that are allowed to make REST API requests for a given REST API Key.

