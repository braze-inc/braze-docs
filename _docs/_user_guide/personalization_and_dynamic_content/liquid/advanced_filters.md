---
nav_title: Advanced filters
article_title: Advanced Liquid Filters
page_order: 4
description: "This reference article lists advanced filters, examples, and how they can be used in your campaign."

---

# Advanced filters

> This reference article provides an overview of advanced filters in Liquid and how they can be used.

## Encoding filters

{% raw %}
| filter name | filter description | example input | example output |
|---|---|---|---|
`md5` | Returns md5 encoded string | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | Returns sha1 encoded string | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | Returns sha2 (256-bit, also known as SHA-256) encoded string | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
`base64` | Returns base64 encoded string | `{{'blah' | base64_encode}}` | YmxhaA== |
`hmac_sha1_hex` (previously `hmac_sha1`) | Returns hmac-sha1 signature, encoded as a hex string | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | Returns hmac-sha1 signature, encoded as a base64 string | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | Returns hmac-sha256 signature, encoded as a hex string | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
`hmac_sha256_base64` | Returns hmac-sha256 signature, encoded as a base64 string | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## URL filters

| filter name | filter description | example input | example output |
|---|---|---|---|
| `url_escape` | Identifies all characters in a string that are not allowed in URLS, and replaces the characters with their escaped variants | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | Replaces all characters in a string that are not allowed in URLs with their escaped variants, including the ampersand (&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | Encodes a string that is URL friendly | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}
{% alert tip %}
The `assign` tag can be combined with HTML to save you time and effort when creating multiple hyperlinks.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Property accessor filter

| filter name | filter description |
|---|---|---|---|
| `property_accessor` | Takes a hash and hash key and returns the value in that hash at that key |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Example hash:** `{"a" => 42, "b" => 0}`
**Example input:** `{{hash | property_accessor: 'a'}}`
**Example output:** `42`

Additionally, the property accessor filter allows you to template a custom attribute into a hash key to access a particular hash value.

{% endraw %}

{% alert note %} 
There is no way to instantiate a hash as a variable (such as an expression) in Liquid within Braze. 
{% endalert %}

{% raw %}

## Number formatting filters

| filter name | filter description | example input | example output |
|---|---|---|---|
| `number_with_delimiter` | Formats a number with commas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## JSON escape / string escape filter

| filter name | filter description |
|---|---|
| `json_escape` | Escapes any special characters in a string (such as double quote `""` and backslash '\'). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

This filter should always be used when personalizing a string in a JSON dictionary and is useful for webhooks in particular.

## JSON-formatting filters

| filter name | filter description |
|---|---|
| `json_parse` | Converts a JSON string into a corresponding data structure, such as an object or array. | 
| `as_json_string` | Converts a data structure, such as an object or array, into a corresponding JSON string. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

{% details json_parse example input and output %}

### Input 

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### Output

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details as_json_string example input and output %}

### Input

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### Output

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
