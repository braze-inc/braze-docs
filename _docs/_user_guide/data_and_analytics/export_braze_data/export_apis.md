---
nav_title: Export APIs
page_order: 8

page_type: reference
description: "This reference article describes why you might programmatically export a JSON file of Dashboard data, over exporting a CSV directly from the Dashboard."
tool: Dashboard
platform: API
---

# Export APIs

Braze's export APIs allow you to programmatically export a JSON file of Dashboard data. Our [documentation page on export APIs][24] contains a list of data that you can access, as well as instructions and sample code for the export. 

There are a few reasons why you would prefer this method over exporting a CSV directly from the Dashboard:

 - Your file is very large. From our Dashboard, you can export a CSV with at most 500,000 rows. If you're exporting data on a segment with over 500,000 users, you'll need to use our export API, which places no limit on how much you can export.
 -  You wish to interact with the data programmatically.

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[24]: {{site.baseurl}}/developer_guide/rest_api/export/#export
