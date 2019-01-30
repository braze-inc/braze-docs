---
nav_title: Advanced Filters
page_order: 5
---

# Advanced Filters

## Encoding Filters

{% raw %}
| filter name | filter description | example input | example output |
|---|---|---|---|
`md5` | returns md5 encoded string | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | returns sha1 encoded string | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | returns sha2 encoded string | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
`base64` | encodes string into base64 | `{{'blah' | base64_encode}}` | YmxhaA== |
`hmac_sha1` | returns hmac-sha1 encoded string | `{{'hey' | hmac_sha1: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |

## URL Filters

| filter name | filter description | example input | example output |
|---|---|---|---|
| `url_escape` | identifies all characters in a string that are not allowed in URLS, and replaces the characters with their escaped variants | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | replaces all characters in a string that are not allowed in URLs with their escaped variants, including the ampersand (&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | encodes a string that is url friendly | `{{ 'google search' | url_encode }}` | google+search |

## Property Accessor Filter

| filter name | filter description |
|---|---|---|---|
| `property_accessor` | takes a hash and hash key and returns the value in that hash at that key |

Example hash : `{“a” => 42, “b” => 0}`

Example input: `{{hash | property_accessor: 'a'}}`

Example output: `42`

Additionally, the property accessor filter allows you to template a custom attribute into a hash key to access a particular hash value.

## Number formatting filters

| filter name | filter description | example input | example output |
|---|---|---|---|
| `number_with_delimiter` | Formats a number with commas | `{{ 123456 | number_with_delimiter }}` | 123,456 |

## JSON Escape / String Escape Filter

| filter name | filter description |
|---|---|---|---|
| `json_escape` | escapes any special characters in a string (i.e. double quote `""` and backslash '\'). |

This filter should always be used when personalizing a string in a JSON dictionary and is useful for webhooks in particular.
{% endraw %}


[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/
[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[5]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[6]: #conditional-messaging-logic-tags
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[12]: https://docs.shopify.com/themes/liquid-documentation/filters
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %}
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
[9]: #connected-content
[11]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_events/
[13]: {% image_buster /assets/img_archive/total_revenue_ios.png %}
[14]: {% image_buster /assets/img_archive/games_liquid.png %}
[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[16]: #manipulating-message-content-filters
[17]: #conditional-logic
[18]: #aborting-messages
[19]: https://docs.shopify.com/themes/liquid/filters/math-filters
[20]: https://docs.shopify.com/themes/liquid/filters/string-filters
[21]: https://docs.shopify.com/themes/liquid/filters/string-filters#capitalize
[22]: https://docs.shopify.com/themes/liquid/filters/array-filters
[23]: https://docs.shopify.com/themes/liquid/filters/array-filters#first
[24]: https://docs.shopify.com/themes/liquid/filters/additional-filters#date
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[27]: #adding-personalizable-attributes-objects
[29]: {% image_buster /assets/img_archive/MemberSince.png %}
[30]: #variable-tags
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[33]:{% image_buster /assets/img_archive/SupportedAttributes.png %}
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[36]:{% image_buster /assets/img_archive/value_null.png %}
[37]:#accounting-for-null-attribute-values
[38]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[39]: #most-recently-used-device-information
[40]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#optional-idfa-collection
[41]: https://dashboard-01.braze.com/app_settings/app_settings/custom_attributes
[42]: https://dashboard-01.braze.com/app_settings/app_settings/custom_events
[43]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
[46]: #targeted-device-information
