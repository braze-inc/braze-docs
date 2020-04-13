---
nav_title: "Trigger Properties Object"
page_order: 11

page_type: reference

platform:
  - API
tool:
  - Campaigns
  - Canvas

description: "This article explains the different components of the Trigger Properties object."
---

#  Trigger Properties Object Specification

When using one of the endpoints for sending a campaign with API Triggered Delivery, you may provide a map of keys and values to customize your message.

If you make an API request that contains an object in `"trigger_properties"`, the values in that object can then be referenced in your message template under the api_trigger_properties namespace.
{% raw %}
For example, a request with the following could add the word `"shoes"` to a message by adding `{{api_trigger_properties.${product_name}}}`.
{% endraw %}

```json
"trigger_properties" : {
  "product_name" : "shoes",
  "product_price" : 79.99
  }
```




[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays [
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/overview/#user-data-collection
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 codes"
[21]: http://docs.python-requests.org/en/latest/ "Requests"
[22]: https://rubygems.org/gems/multi_json "multiJSON"
[23]: https://rubygems.org/gems/rest-client "Rest Client"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 codes"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#braze-user-profile-fields
