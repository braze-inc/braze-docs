---
nav_title: Advanced Filters
page_order: 4
description: "This reference article lists advanced filters and how they can be used in your campaign."
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## URL Filters

| filter name | filter description | example input | example output |
|---|---|---|---|
| `url_escape` | identifies all characters in a string that are not allowed in URLS, and replaces the characters with their escaped variants | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | replaces all characters in a string that are not allowed in URLs with their escaped variants, including the ampersand (&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | encodes a string that is url friendly | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Property Accessor Filter

| filter name | filter description |
|---|---|---|---|
| `property_accessor` | takes a hash and hash key and returns the value in that hash at that key |
{: .reset-td-br-1 .reset-td-br-2}

Example hash : `{“a” => 42, “b” => 0}`

Example input: `{{hash | property_accessor: 'a'}}`

Example output: `42`

Additionally, the property accessor filter allows you to template a custom attribute into a hash key to access a particular hash value.

## Number formatting filters

| filter name | filter description | example input | example output |
|---|---|---|---|
| `number_with_delimiter` | Formats a number with commas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## JSON Escape / String Escape Filter

| filter name | filter description |
|---|---|---|---|
| `json_escape` | escapes any special characters in a string (i.e. double quote `""` and backslash '\'). |
{: .reset-td-br-1 .reset-td-br-2}

This filter should always be used when personalizing a string in a JSON dictionary and is useful for webhooks in particular.
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
