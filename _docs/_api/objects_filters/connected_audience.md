---
nav_title: "Connected Audience Filter & Object"
article_title: API Connected Audience Object
page_order: 3
page_type: reference
description: "This article explains the different components of the Connected Audience Object and the Filters that create it."

---

# Connected audience object specification

A Connected Audience Object is a selector that identifies the audience to send the message to. It is composed of either a single Connected Audience Filter or several Connected Audience Filters in a logical expression using either `AND` or `OR` operators.

Multiple filter example:

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Connected audience filters

Combining multiple custom attribute filters will create a Connected Audience Filter, which will create a Connected Audience Filter when combined with `AND` and `OR` operators.

### Custom attribute filter

This filter allows you to segment based on a user's custom attribute. These filters contain up to three fields:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Allowed comparisons by data type

The custom attribute's data type determines the comparisons that are valid for a given filter.

| Custom Attribute Type | Allowed Comparisons |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `does_not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` | 
{: .reset-td-br-1 .reset-td-br-2}

#### Attribute comparison caveats

| Comparison | Additional considerations |
| --- | --- |
| `value` | The `value` is not required when using the `exists` or `does_not_exist` comparisons. `value` must be an ISO 8601 DateTime string when using the `before` and `after` comparisons.
|`matches_regex` | When using the `matches_regex` comparison, the value passed must be a string. To read more about using regular expressions with Braze, check out our documentation on [regular expressions]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) and custom attribute [data types]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2}

#### Custom attribute example

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Push subscription filter

This filter allows you to segment based on a user's push subscription status.

#### Filter body

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Allowed comparisons:** `is`, `is_not`
- **Allowed values:** `opted_in`, `subscribed`, `unsubscribed`

### Email subscription filter

This filter allows you to segment based on a user's email subscription status.

#### Filter body

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Allowed comparisons:** `is`, `is_not`
- **Allowed values:** `opted_in`, `subscribed`, `unsubscribed`

### Last used app filter

This filter allows you to segment based on when was the last time the user used the App. These filters contain two fields:

#### Filter body
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Allowed comparisons:** `after`, `before`
- **Allowed values:** DateTime (ISO 8601 string)

