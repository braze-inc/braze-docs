---
nav_title: SQL variables
article_title: Query Builder SQL variables
page_order: 2
page_type: reference
description: "Learn how to use variables in the Query Builder, so you can reuse your queries and avoid hard-coding any data in your code."
tool: Reports
---

# Query Builder SQL variables

> Learn how to use SQL variables in the Query Builder, so you can reuse your queries and avoid hard-coding any data in your code.

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
{{variable_type.${custom_label}}}
```
{% endraw %}

Replace the following:

| Placeholder      | Description                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | The predefined variable type you'd like to use, such as `campaign` or `catalog_fields`. For the full list, see [Supported variable types](#variable-types). |
| `custom_label` | The label used to identify the variable in the **Variables** tab of your Query Builder. |
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

By default, the **Variables** tab isn't shown in the Query Builder. It only appears after adding your first variable to the query. There, you'll be able to assign it a value. The specific values you can choose will depend on that specific variable's [type](#variable-types).

In the following example, the "Summer Feature Launch" campaign is assigned as a value, along with the first and last days of June 2025.

![The "Variable" tab in the Query Builder showing the given example.]({% image_buster /assets/img/query_builder_example.png %})

## General variable types {#variable-types}

### Number

`number` can be used in combination with other non-string variables. Accepts any positive or negative number, including decimal numbers, such as `5.5`.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### String

For changing repetitive string values between report runs. Use this variable to avoid hardcoding a value multiple times in your SQL.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### List {#list}

For selecting from a list of options.

{% tabs local %}
{% tab choose one %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab choose multiple %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Radio button

For showing options as radio buttons instead of a select dropdown in the **Variables** tab. This cannot be used on its own&#8212;it must be used in combination with a [list](#list).

{% tabs %}
{% tab usage %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![An example radio button rendered in Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Multi-select

For whether the select dropdown allows a single or multi-select. This cannot be used on its own&#8212;it must be used in combination with a [list](#list).

{% tabs %}
{% tab usage %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![An example multi-select list rendered in Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Options 

For providing the list of selectable options in the form of a label and value. The label is what gets shown and the value is what the variable gets replaced with when the option is selected. This cannot be used on its own&#8212;it must be used in combination with a [list](#list).

{% tabs %}
{% tab usage %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Braze-specific variable types

### Date range

For displaying a calendar to select dates from. Replace `start_date` and `end_date` with a Unix timestamp in seconds for a specified date in UTC, such as `1696517353`. Optionally, you can set only a `start_date` or `end_date` to only display a single date in the calendar. If the labels of your `start_date` and `end_date` don't match, they'll be treated as two separate dates, rather than a date range.

{% tabs %}
{% tab usage %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

You can set the date range to any of the following options. If both `start_date` and `end_date` are used and share the same label all options will be shown. Otherwise, if only one is used, then only the specified option will be displayed.

| Option | Description | Required values |
| --- | --- | --- |
| Relative | Specifies the past X days | Requires `start_date` |
| Start date | Specifies a start date | Requires `start_date` |
| End date | Specifies an end date | Requires `end_date` |
| Date range | Specifies both a start and end date | Requires both `start_date` and `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Your Liquid will be used to display a calendar within the given date range:

![An example calendar rendered in Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campaigns

{% tabs local %}
{% tab one campaign %}
For selecting one campaign. Sharing the same label with a Canvas will result in a radio button within the **Variables** tab that for selecting either Canvas or campaign.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple campaigns %}
For multi-selecting campaigns. Sharing the same label with a Canvas will result in a radio button within the **Variables** tab for selecting either Canvas or campaign.

- **Replacement value:** Campaigns BSON IDs

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campaign variants %}
For selecting campaign variants that belong to the selected campaign. It must be used in conjunction with a campaign or campaigns variable.

- **Replacement value:** Campaign variants API IDs, strings delimited by commas such as `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
All campaign and Canvas variables must use the same identifiers in order to sync states within a single group.
{% endalert %}

### Canvases

{% tabs local %}
{% tab one canvas %}
For selecting one Canvas. Sharing the same label with a campaign will result in a radio button within the **Variables** tab that for selecting either Canvas or campaign.

- **Replacement value:** Canvas BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvases %}
For selecting multiple Canvases. Sharing the same label with a campaign will result in a radio button within the **Variables** tab for selecting either Canvas or campaign.

- **Replacement value:** Canvases BSON IDs

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab canvas variants %}
For selecting Canvas variants that belong to a chosen Canvas. It must be used with a Canvas or Canvases variable. Set to one or more Canvas variants API IDs, as a comma-separated string, such as in `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab one canvas step %}
For selecting a Canvas step that belongs to a chosen Canvas. It must be used with a Canvas variable.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvas steps %}
For selecting Canvas steps that belong to chosen Canvases. It must be used with a Canvas or Canvases variable.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
All campaign and Canvas variables must use the same identifiers in order to sync states within a single group.
{% endalert %}

### Products

`products` is used to select one or more products from the Braze dashboard.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab example %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Custom events

Select one or more custom events or custom event properties from a list.

{% tabs local %}
{% tab event %}
`custom_events` is used to select one or more custom events from the Braze dashboard.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab example %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}}); 
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab properties %}
`custom_event_properties` is used to select one or more properties from the currently-select custom event.  Requires a set `custom_events` variable.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Workspace

`workspace` is used to select a single workspace from the Braze dashboard.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Catalogs

Select one or more catalogs or catalog fields from a list.

{% tabs local %}
{% tab catalogs %}
`catalogs` is used to select one or more catalogs from the Braze dashboard.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab catalog fields %}
`catalog_fields` is used to set one or more fields from the currently-selected catalog. Requires a set `catalogs` variable.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segments

For selecting segments that have [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) turned on. Set this to the segment analytics ID, which corresponds to the IDs stored in the `user_segment_membership_ids` column in the tables where this column is available.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Tags

For selecting tags for campaigns and Canvases. Set to Campaigns and Canvases with single-quoted comma-separated BSON IDs that are associated with the selected tags.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Variable metadata

Metadata can be attached to a variable to change its behavior by appending the metadata with a pipe ( &#124; ) character following the variable label. The ordering of the metadata doesn't matter and you can append any number of them. Additionally, all types of metadata can be used for any variable, except for special metadata that is specific to certain variables (this will be indicated in those cases). The usage of all metadata is optional and is used to change the default's variable behavior.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Boolean

For knowing whether a variable's value is filled. This is useful for optional variables where you want to short-circuit a condition if a variable's value is not filled. Can be set to `true` or `false` depending on the other variable's value.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` and `name` refer to the referenced variable. For example, to short-circuit the following optional variable: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Visible

For whether variables are visible. All variables are visible by default in the **Variables** tab, where you can input values.

There are several special variables whose value is dependent on another variable, such as whether another variable has a value. These special variables are marked as not visible so they don't show in the **Variables** tab.

{% tabs %}
{% tab usage %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Required

For whether variables are required by default. An empty value for a variable usually leads to an incorrect query.

{% tabs %}
{% tab usage %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Order

For selecting the position of the variable in the **Variables** tab.

{% tabs %}
{% tab usage %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Include quotes

{% tabs local %}
{% tab single quotes %}
For surrounding the values of a variable with single quotes.

{% subtabs %}
{% subtab usage %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab double quotes %}
For surrounding the values of a variable with double quotes.

{% subtabs %}
{% subtab usage %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Placeholder

For specifying the placeholder text shown in the variable's input field.

{% tabs %}
{% tab usage %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Description

For specifying the description text shown under the variable's input field.

{% tabs %}
{% tab usage %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Default value

For specifying the default value for the variable when no value is specified.

{% tabs %}
{% tab usage %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Hide label

For hiding the variable's label.

{% tabs %}
{% tab usage %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}
