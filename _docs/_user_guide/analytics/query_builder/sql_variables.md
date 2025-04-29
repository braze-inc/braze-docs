---
nav_title: SQL Variables
article_title: Query Builder SQL variables
page_order: 2
page_type: reference
description: "Learn how to use variables in the Query Builder, so you can reuse your queries and avoid hard-coding any data in your code."
tool: Reports
---

# Query Builder variables

> Learn how to use variables in the Query Builder, so you can reuse your queries and avoid hard-coding any data in your code.

## Why use SQL variables?

The benefits of using SQL variables include:

- Save time by creating a campaign variable to select from a list when creating your report, instead of pasting in campaign IDs.
- Swap in values by adding variables that allow you to reuse the report for slightly different use cases in the future (such as a different custom event).
- Reduce user error when editing your SQL by reducing the amount of editing needed for each report. Teammates that are more comfortable with SQL can create reports that less technical teammates can then use.

## Using variables

### Step 1: Add a variable

To add a variable to your query, use the following syntax:

{% raw %}
```sql
'{{variable_type.${custom_name}}}'
```
{% endraw %}

Replace the following:

| Placeholder      | Description                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | The predefined variable type you'd like to use, such as `campaign` or `catalog_fields`. For the full list, see [Variable types](#variable-types). |
| `custom_name` | The name of your variable. This is used to identify the variable in the **Variables** tab of your Query Builder. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

In the following example, the total number of users between the first and last day of a month is queried for a campaign. Each variable will be assigned a value in the next step.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Step 2: Assign a value

By default, the **Variables** tab isn't shown in the Query Builder. It only appears after adding your first variable to the query.

Each variable you add is automatically added to this tab and it's where you can assign their values. The specific values you can choose will depend on that specific variable's [type](#variable-types).

In the following example, the "Summer Feature Launch" campaign is assigned as a value, along with the first and last days of June 2025.

![The "Variable" tab in the Query Builder showing the given example.]()

## Variable types {#variable-types}

### Number

- **Replacement value:** The provided value, such as `5.5`
- **Usage example:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

### Date range

![]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

If using both `start_date` and `end_date`, they must have the same name so you can use them as a date range.

#### Example values

The date range type can be relative, start date, end date, or date range.

All four types are shown if both `start_date` and `end_date` are used with the same name. If only one is used, then only the relevant types will show.

| Date range type | Description | Required values |
| --- | --- | --- |
| Relative | Specifies the past X days | Requires `start_date` |
| Start date | Specifies a start date | Requires `start_date` |
| End date | Specifies an end date | Requires `end_date` |
| Date range | Specifies both a start and end date | Requires both `start_date` and `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Replacement value:** Replaces `start_date` and `end_date` with a Unix timestamp in seconds for a specified date in UTC, such as `1696517353`.
- **Usage example:** For all of relative, start date, end date, and date range variables:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - You can use either `start_date` or `end_date` if you don’t want a date range.

### Messaging

All messaging variables must share the same identifier when you want to tie together their state in one group.

![]({% image_buster /assets/img_archive/sql_variables_canvases.png %}){: style="max-width:50%;"}

#### Canvas

For selecting one Canvas. Sharing the same name with a campaign will result in a radio button within the **Variables** tab that for selecting either Canvas or campaign.

- **Replacement value:** Canvas BSON ID
- **Usage example:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

#### Canvases

For selecting multiple Canvases. Sharing the same name with a campaign will result in a radio button within the **Variables** tab for selecting either Canvas or campaign.

- **Replacement value:** Canvases BSON IDs
- **Usage example:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

#### Campaign

For selecting one campaign. Sharing the same name with a Canvas will result in a radio button within the **Variables** tab that for selecting either Canvas or campaign.

- **Replacement value:** Campaign BSON ID
- **Usage example:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

#### Campaigns

For multi-selecting campaigns. Sharing the same name with a Canvas will result in a radio button within the **Variables** tab for selecting either Canvas or campaign.

- **Replacement value:** Campaigns BSON IDs
- **Usage example:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

#### Campaign variants

For selecting campaign variants that belong to the selected campaign. It must be used in conjunction with a campaign or campaigns variable.

- **Replacement value:** Campaign variants API IDs, strings delimited by commas such as `api-id1, api-id2`.
- **Usage example:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

#### Canvas variants

For selecting Canvas variants that belong to a chosen Canvas. It must be used with a Canvas or Canvases variable.

- **Replacement value:** Canvas variants API IDs, strings delimited by commas such as in `api-id1, api-id2`.
- **Usage example:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

#### Canvas Step

For selecting a Canvas step that belongs to a chosen Canvas. It must be used with a Canvas variable.

- **Replacement value:** Canvas step API ID
- **Usage example:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

#### Canvas Steps

For selecting Canvas steps that belong to chosen Canvases. It must be used with a Canvas or Canvases variable.

- **Replacement value:** Canvas steps API IDs
- **Usage example:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}

### Products

For selecting a list of product names.

- **Replacement value:** Product names are surrounded by single quotes and separated by commas, such as in `product1, product2`
- **Usage example:** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

### Custom events

For selecting a list of custom events.

- **Replacement value:** Custom event property names are separated by commas such as in `event1, event2`
- **Usage example:** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

### Custom event properties

For selecting a list of custom event property names. It must be used with the custom events variable.

- **Replacement value:** Custom event property names are separated by commas such as in `property1, property2`
- **Usage example:** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

### Workspace

For selecting a workspace.

- **Replacement value:** Workspace BSON ID
- **Usage example:** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

### Catalogs

For selecting catalogs.

- **Replacement value:** Catalog BSON IDs
- **Usage example:** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

### Catalog Fields

For selecting catalog fields. It must be used with the catalogs variable.

- **Replacement value:** Catalog field names
- **Usage example:** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

### Options {#options}

For selecting from a list of options.

- **Replacement value:** The value of the selected options
- **Usage example:**
    - For select dropdown: {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - `is_multi_select` allows specifying whether the end user can select more than one option
    - For radio button: {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

### Segments

For selecting segments that have [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) turned on.

- **Replacement value:** The segment analytics ID, which corresponds to the IDs stored in the `user_segment_membership_ids` column in the tables where this column is available.
- **Usage example:** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

### String

For changing repetitive string values between report runs. Use this variable to avoid hardcoding a value multiple times in your SQL.

- **Replacement value:** The string as is without any surrounding quotes
- **Usage example:** {% raw %}`{{string.${some name}}}`{% endraw %}

### Tags

For selecting tags for campaigns and Canvases.

- **Replacement value:** Campaigns and Canvases with single-quoted comma-separated BSON IDs that are associated with the selected tags
- **Usage example:** {% raw %}`{{tags.${some tags}}}`{% endraw %}

## Variable metadata

Metadata can be attached to a variable to change its behavior by appending the metadata with a pipe ( &#124; ) character following the variable name. The ordering of the metadata doesn’t matter and you can append any number of them. Additionally, all types of metadata can be used for any variable, except for special metadata that is specific to certain variables (this will be indicated in those cases). The usage of all metadata is optional and is used to change the default’s variable behavior.

**Usage example:** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

### Visible

For whether variables are visible. All variables are visible by default in the **Variables** tab, where you can input values.

There are several special variables whose value is dependent on another variable, such as whether another variable has a value. These special variables are marked as not visible so they don't show in the **Variables** tab.

**Usage example:** `visible: ‘false’`

### Required

For whether variables are required by default. An empty value for a variable usually leads to an incorrect query.

**Usage example:** `required: ‘false’`

### Order

For selecting the position of the variable in the **Variables** tab.

**Usage example:** `order: ‘1’`

### Include single quotes

For surrounding the values of a variable with single quotes.

**Usage example:** `include_quotes: ‘true’`

### Include double quotes

For surrounding the values of a variable with double quotes.

**Usage example:** `include_double_quotes: ‘true’`

### Multi-select

For whether the select dropdown allows a single or multi-select. For now, you can include this metadata only if you use the [Options](#options) variable.

**Usage example:** `is_multi_select: ‘true’`

![]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

### Radio button

For showing options as radio buttons instead of a select dropdown in the **Variables** tab. You can include this metadata only if you use the [Options](#options) variable.

**Usage example:** `is_radio_button: ‘true’`

![]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

### Options 

For providing the list of selectable options in the form of a label and value. The label is what gets shown and the value is what the variable gets replaced with when the option is selected. You can include this metadata only if you use the [Options](#options) variable.

**Usage example:** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

### Placeholder

For specifying the placeholder text shown in the variable’s input field.

**Usage example:** `placeholder: ‘enter some value’`

### Description

For specifying the description text shown under the variable’s input field.

**Usage example:** `description: ‘some description’`

### Default value

For specifying the default value for the variable when no value is specified.

**Usage example:** `default_value: ‘5’`

### Hide label

For hiding the variable's name label. The variable's name is used as a default label.

**Usage example:** `hide_label: ‘true’`

## Special variables

The following variables can be used with other variables:

### Presence or absence of another variable’s value

For knowing whether a variable’s value is filled. This is useful for optional variables where you want to short-circuit a condition if a variable’s value is not filled.

- **Replacement value:** `true` or `false` depending on the other variable’s value
- **Usage example:** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` and `name` refer to the referenced variable. For example, to short-circuit the following optional variable: {% raw %}`{{campaigns.${messaging}}`, you can use the following:
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}
