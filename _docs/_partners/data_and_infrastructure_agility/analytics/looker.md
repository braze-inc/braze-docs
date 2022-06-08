---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "This article outlines the partnership between Braze and Looker, a business intelligence and big-data analytics platform."
page_type: partner
search_tag: Partner

---

# Looker

> [Looker](https://looker.com/), a business intelligence and big-data analytics platform, enables you to explore, analyze, and share real-time business analytics seamlessly.

The Braze and Looker integration allows Braze users to leverage first-party [Looker Blocks](#looker-blocks) and [Looker Actions](#looker-actions) user flagging via the REST API. Once flagged, these users can be added to segments to [target](#segment-users) future Braze campaigns or Canvases. To use Looker with Braze, we recommend sending your Braze data to a [data warehouse using Braze currents][6], then use Braze's Looker Blocks to quickly model and visualize your Braze data in Looker.

## Prerequisites

| Requirement | Description |
|---|---|
|Looker account | A [Looker account](https://looker.com/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][1]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Limitations

- This process only works with data that has not been pivoted.
- Currently, the API is limited to 100,000 rows sent.
- The final count of a user's flag may be lower due to duplicates or non-users.

## Integration

### Looker Blocks

Our Looker Blocks help Braze customers quickly access a view of granular data we offer via [Currents][5]. Our blocks provide pre-made visualizations and modeling for Currents data so Braze customers can easily implement analytic patterns like retention, evaluate message deliverability, take a more detailed look at user behavior, and more.

To implement the Looker Blocks, follow the instructions in the README files of the GitHub code.
- [Message engagement analytics block README][2]
- [User behavior analytics block README][3]

Both integrations assume that your [initial Braze integration][4], as well as your Braze integration with a Looker-compatible [data warehouse][7], is appropriately configured to capture and send necessary data.


{% alert important %}
Braze has built our Looker Blocks using [Snowflake](https://www.snowflake.com/) as our data warehouse. While we aim for our Blocks to work with as many data warehouses as possible, some SQL functions may differ in availability, syntax, or behavior across dialects.
{% endalert %}

{% alert warning %}
Be aware of different naming conventions! Custom names can cause incongruences in data unless you change all corresponding names. If you've customized any View/table or model names, rename each in the LookML to the name you've selected.
{% endalert %}

#### Available Blocks

| Block | Description |
|---|---|
| Message engagement analytics block | This block includes data around push, email, in-app messages, webhook, newsfeed, conversion, Canvas entry, and campaign control group enrollment events. <br><br>Learn more about this [Looker Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), or check out the [Github code](https://github.com/llooker/braze_message_engagement_block). |
| User behavior analytics block | This block includes data around custom events, purchases, sessions, location events, and uninstalls.<br><br>Learn more about this [Looker Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), or check out the [Github code](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2}

### Looker Actions

Looker Actions allow you to flag users within Braze via the REST API endpoint from a Looker Look. Actions require that a dimension is tagged with `braze_id`. The Action will append the flagged value to the user's `looker_export` custom attribute.

{% alert important %}
Only existing users will be flagged. You cannot use pivoted Looks when flagging data in Braze.
{% endalert %}

#### Step 1: Set up a Braze Looker action

Set up a Braze Looker Action with your Braze REST API key and REST endpoint.

![The Looker Braze configuration page. Here you can find fields for Braze API key and Braze REST API endpoint.][12]

#### Step 2: Set up Looker Develop

Within Looker Develop, select the appropriate views. Add `braze_id` to the dimensions tag.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

#### Step 3: Set user attributes in tags

Optionally, any attribute can be set using a `braze[]` tag with the attribute name in the brackets. For example, if you wanted a custom attribute `user_segment` to be sent, the tag would be `braze[user_segment]`.

Note the following limitations:
- Attributes will only be sent if it's **included as a field within the look**.
- Supported types are `Strings`, `Boolean`, `Numbers`, and `Dates`.
- Attribute names are case-sensitive.
- Default attributes can also be set as long as they match the [standard user profile]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields) names exactly.
- The full tag should be formatted within quotes. For example, `tags: ["braze[first_name]"]`. Other tags can also be assigned but will be ignored.
- Additional information can be found on [Github](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Step 4: Send the Looker action

1. Within a Look with a `braze_id` dimension selected, click the settings gear ( <i class="fas fa-cog"></i> ) on the upper right, and select **Send...**.
2. Select the custom Braze Action.
3. Under **Unique Key**, provide the primary user mapping key for the Braze account (`external_id` or `braze_id`).
4. Give the export a name. If none is provided, `LOOKER_EXPORT` will be used.
5. Under **Advanced Options**, select **Results in Table** or **All Results** and then **Send**.<br><br>![][13]<br><br>If the export was correctly sent, then `LOOKER_EXPORT` should appear in the user's profile as a custom attribute with the value you entered in the action.<br><br>![][14]

##### Sample outgoing API

The following is a sample of an outgoing API call, which will be sent to the [/users/track/][10] endpoint.

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

![In the Braze segment builder, the filter "looker_export" is set to "includes_value" and "Looker".][15]

Once saved, you can reference this segment during Canvas or campaign creation in the targeting users step.

## Troubleshooting
If you're having issues with the Looker Action, add a test user to [internal groups][16] and check that the following:

* The API key has the `users.track` permissions.
* The correct REST endpoint is entered i.e., `https://rest.iad-01.braze.com`.
* A `braze_id` tag is set in the dimension view.
* Your query includes the Id attribute as a column.
* Looker results are not pivoted.
* The unique key is correctly selected. Usually the `external_id`.
* The `external_id` user exist in the Braze platform.
* The `looker_export` field is set as `Automatically Detect` under `Braze Platform > Settings > Manage Settings > Custom Attributes`.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}//user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[8]: https://dashboard.braze.com/app_settings/developer_console/
[9]: {{site.baseurl}}/api/basics/#endpoints
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {% image_buster /assets/img/user_track_api.png %}
[12]: {% image_buster /assets/img/braze-looker-action.png %}
[13]: {% image_buster /assets/img/send-looker-action.png %}
[14]: {% image_buster /assets/img/custom-attributes-looker.png %}
[15]: {% image_buster /assets/img/braze_segments.png %}
[16]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/
