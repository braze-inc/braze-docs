---
nav_title: Export APIs
article_title: Export APIs
page_order: 8
page_type: reference
description: "This reference article describes why you might programmatically export a JSON file of dashboard data, over exporting a CSV directly from the dashboard."
platform: API

---

# Export APIs

> This page covers Braze Export APIs, which allow you to programmatically export a JSON file of dashboard data. Refer to [Export endpoints]({{site.baseurl}}/api/endpoints/export/) for a list of data that you can access, including instructions and sample code for the export.

## When to use export APIs instead of CSV downloads

There are a few reasons why you would prefer this method over exporting a CSV directly from the dashboard:

 - Your file is very large. From our dashboard, you can export a CSV with at most 500,000 rows. If you're exporting data on a segment with over 500,000 users, you'll need to use our export API, which has no limit on how much you can export.
 -  You want to interact with the data programmatically.

{% alert tip %}
For help with CSV and API exports, refer to [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

