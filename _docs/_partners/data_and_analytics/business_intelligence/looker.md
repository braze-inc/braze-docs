---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "This reference article outlines the partnership between Braze and Looker, a business intelligence and big-data analytics platform."
page_type: partner
search_tag: Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> [Looker](https://looker.com/), a business intelligence and big-data analytics platform, enables you to explore, analyze, and share real-time business analytics seamlessly.

The Braze and Looker integration allows Braze users to leverage first-party [Looker Blocks](#looker-blocks) and [Looker Actions](#looker-actions) user flagging via the REST API. These flagged users can be added to segments to [target](#segment-users) future Braze campaigns or Canvases. To use Looker with Braze, we recommend sending your Braze data to a [data warehouse using Braze currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/), then use Braze Looker Blocks to quickly model and visualize your Braze data in Looker.

## Prerequisites

| Requirement | Description |
|---|---|
|Looker account | A [Looker account](https://looker.com/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Limitations

- This process only works with data that has not been pivoted.
- The API processes a maximum of 100,000 rows at a time.
- The final count of a user's flag may be lower due to duplicates or non-users.

## Integration

### Looker Blocks

Our Looker Blocks help Braze customers quickly access a view of granular data we offer via [Currents]({{site.baseurl}}/partners/braze_currents/about/). Our blocks provide pre-made visualizations and modeling for Currents data so Braze customers can easily implement analytic patterns like retention, evaluate message deliverability, take a more detailed look at user behavior, and more.

To implement the Looker Blocks, follow the instructions in the README files of the GitHub code.
- [Message engagement analytics block README](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [User behavior analytics block README](https://github.com/llooker/braze_retention_block/blob/master/README.md)

Both integrations assume that your [initial Braze integration]({{site.baseurl}}/user_guide/onboarding_with_braze/integration/), as well as your Braze integration with a Looker-compatible [data warehouse](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), is appropriately configured to capture and send necessary data.


{% alert important %}
Braze has built our Looker Blocks using [Snowflake](https://www.snowflake.com/) as our data warehouse. While we aim for our Blocks to work with as many data warehouses as possible, some SQL functions may differ in availability, syntax, or behavior across dialects.
{% endalert %}

{% alert warning %}
Be aware of different naming conventions! Custom names can cause incongruities in data unless you change all corresponding names. If you've customized any View/table or model names, rename each in the LookML to the name you've selected.
{% endalert %}

#### Available Blocks

| Block | Description |
|---|---|
| Message engagement analytics block | This block includes data around push, email, in-app messages, webhook, conversion, Canvas entry, and campaign control group enrollment events. <br><br>Learn more about this [Looker Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), or check out the [GitHub code](https://github.com/llooker/braze_message_engagement_block). |
| User behavior analytics block | This block includes data around custom events, purchases, sessions, location events, and uninstalls.<br><br>Learn more about this [Looker Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), or check out the [GitHub code](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Looker Actions

Looker Actions allow you to flag users within Braze via the REST API endpoint from a Looker Look. Actions require that a dimension is tagged with `braze_id`. The Action will append the flagged value to the user's `looker_export` custom attribute.

{% alert important %}
Only existing users will be flagged. You cannot use pivoted Looks when flagging data in Braze.
{% endalert %}

#### Step 1: Set up a Braze Looker action

Set up a Braze Looker Action with your Braze REST API key and REST endpoint.

![The Looker Braze configuration page. Here, you can find fields for Braze API key and Braze REST API endpoint.]({% image_buster /assets/img/braze-looker-action.png %})

#### Step 2: Set up Looker Develop

Within Looker Develop, select the appropriate views. Add `braze_id` to the dimensions tag and commit the changes.
This `braze_id` tag is use to determine which field is the unique key.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Make sure to commit the changes. Looker Action will only work with production settings.**

#### Step 3: Set user attributes in tags

Optionally, any attribute can be set using a `braze[]` tag with the attribute name in the brackets. For example, if you wanted a custom attribute `user_segment` to be sent, the tag would be `braze[user_segment]`.

Note the following limitations:
- Attributes will only be sent if it's **included as a field within the look**.
- Supported types are `Strings`, `Boolean`, `Numbers`, and `Dates`.
- Attribute names are case-sensitive.
- Standard attributes can also be set as long as they match the [standard user profile]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields) names exactly.
- The full tag should be formatted within quotes. For example, `tags: ["braze[first_name]"]`. Other tags can also be assigned but will be ignored.
- Additional information can be found on [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Step 4: Send the Looker action

1. Within a Look with a `braze_id` dimension selected, click the settings gear ( <i class="fas fa-cog"></i> ) on the upper right, and select **Send...**.
2. Select the custom Braze Action.
3. Under **Unique Key**, provide the primary user mapping key for the Braze account (`external_id` or `braze_id`).
4. Give the export a name. If none is provided, `LOOKER_EXPORT` will be used.
5. Under **Advanced Options**, select **Results in Table** or **All Results** and then **Send**.<br><br>![]({% image_buster /assets/img/send-looker-action.png %})<br><br>If the export was correctly sent, then `LOOKER_EXPORT` should appear in the user's profile as a custom attribute with the value you entered in the action.<br><br>![]({% image_buster /assets/img/custom-attributes-looker.png %})

##### Example outgoing API

The following is an example of an outgoing API call, which will be sent to the [`/users/track/` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

###### Header
```
Authorization: Bearer [API_KEY]
```

###### Body
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Segment users in Braze {#segment-users}

In Braze, to create a segment of these flagged users, navigate to **Segments** under **Engagement**, name your segment, and select **Looker_Export** as the filter. Next, use the "includes value" option and provide the custom attribute flag you assigned in Looker.

![In the Braze segment builder, the filter "looker_export" is set to "includes_value" and "Looker".]({% image_buster /assets/img/braze_segments.png %})

Once saved, you can reference this segment during Canvas or campaign creation in the targeting users step.

## Troubleshooting
If you're having issues with the Looker Action, add a test user to [internal groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/) and check that the following:

* The API key has the `users.track` permissions.
* The correct REST endpoint is entered, such as `https://rest.iad-01.braze.com`.
* A `braze_id` tag is set in the dimension view.
* Your query includes the Id dimension or attribute as a column.
* Looker results are not pivoted.
* The unique key is correctly selected. Usually the `external_id`.
* `braze_id` in the dimension is different then the `braze_id` in the api. `braze_id` in the dimension is use to indicated that it's the `id` field for the Braze API. For most purposes, upon send `external_id` is the primary key.
* The `external_id` user exist in the Braze platform.
* The `looker_export` field is set as `Automatically Detect` under `Braze Platform > Settings > Manage Settings > Custom Attributes`.
* The changes are commit to production. Looker Action works on production settings.

