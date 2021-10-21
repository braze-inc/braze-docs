---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "This article outlines the partnership between Braze and Looker, a business intelligence and big-data analytics platform."
page_type: partner
search_tag: Partner

---

# Looker

> Looker, a business intelligence and big-data analytics platform, enables you to explore, analyze, and share real-time business analytics seamlessly.

Looker and Braze empower you to transform customer experiences with live customer-lifecycle data visualizations.

## Integration

Braze partners with Looker through [first-party Looker Blocks](#implementing-the-looker-blocks) and [flagging users within Braze via REST API](#flagging-users-within-braze). To use Looker with braze, we recommend sending your Braze data to a [data warehouse using Braze Currents][6], then use Braze's Looker Blocks to quickly model and visualize your Braze data in Looker.

Braze's Looker Blocks can reduce the burden of modeling data and enable marketers to quickly access and visualize data.

[See how Braze uses Currents.][1]

## Available Looker Blocks

Our Looker Blocks help Braze customers quickly access a view of granular data we offer via [Currents][5]. Our blocks provide pre-made visualizations and modeling for Currents data so Braze customers can easily implement analytic patterns like retention, evaluate message deliverability, take a more detailed look at user behavior, and more.

Braze currently has two Blocks available: the Message Engagement Analytics and the User Behavior Analytics Blocks.

| Block | Description | More Information | Code |
|---|---|---|---|
| __Message Engagement Analytics Block__ | This block includes data around push, email, in-app messages, webhook, newsfeed, conversion, Canvas entry, and campaign control group enrollment events. | [Learn more about this Looker Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) from Looker. | See the code on [Github](https://github.com/llooker/braze_message_engagement_block). |
| __User Behavior Analytics Block__ | This block includes data around custom events, purchases, sessions, location events, and uninstalls. | [Learn more about this Looker Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) from Looker. | See the code on [Github](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Implementing the Looker Blocks

To implement the Looker Blocks, follow the instructions in the README files of the Github code.

- [Message Engagement Analytics Block README][2]
- [User Behavior Analytics Block README][3]

{% alert important %}
  Braze has built our Looker Blocks using [Snowflake](https://www.snowflake.com/) as our data warehouse. While we aim for our Blocks to work with as many data warehouses as possible, there may be some SQL functions that differ in availability, syntax, or behavior across dialects.
{% endalert %}

Both integrations assume that your [initial Braze integration][4], as well as your Braze integration with a Looker-compatible [data warehouse][7] is appropriately configured to capture and send necessary data.

{% alert warning %}
Be aware of different naming conventions! Custom names can cause incongruences in data unless you take care to change all corresponding names. If you've customized any View/table or model names, rename each in the LookML to the name you've selected.
{% endalert %}

## Flagging users within Braze

__Looker Actions__ allows you to flag users within Braze via the REST API Endpoint from a Looker Look. __Actions__ requires that a dimension is tagged with `braze_id`. The Action will append the flagged value to the users `looker_export` custom attribute.

{% alert important %}
Only existing users will be flagged. You cannot use pivoted Looks when flagging data in Braze.
{% endalert %}

## Update user attributes

Optional, any attributes can also be set by using a tag of `braze[]` with the name of the attribute between the `[]` ie if you want a custom attribute of `User Segment` to be sent, then the tag would be `braze[User Segment]`.
- Note the following:
  - Attribute will only be sent if it's **included as a field within the look**.
  - Attribute name are case sensitive.
  - Supported types are: `Strings`, `Booleans`, `Numbers` and `Dates`.
  - Default attributes can also be set as long as they matched the [standard user profiles]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields) name exactly.
  - The full tag will be within quotes, so it should look like `tags: ["braze[first_name]"]`. Other tags can also be assigned but will be ignored.
  - Additional information can be found on [Github](https://github.com/looker/actions/tree/master/src/actions/braze)

## Setup instructions

[You can also find these instructions and sample code on Github.](https://github.com/looker/actions/tree/master/src/actions/braze)

### Step 1: Create a REST API key

Create a REST API Key with access to `user.track` from the [Braze Developer Console][8].

![User/Track API][11]

### Step 2: Set up a Braze Looker action

Setup the Braze Looker Action with the API Key, and [Braze REST Endpoint][9].

![Braze Looker Action][12]

### Step 3: Set up Looker Develop

Within Looker Develop, select the appropriate views. Add `braze_id` to the dimensions tag.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

### Step 4: Send the Looker action

1. Within a Look with a `braze_id` dimension selected, click the Settings gear ( <i class="fas fa-cog"></i> ) on the upper right, and select `Send...`.
2. Select the custom Braze Action.
3. From the drop down, select the appropriate `Unique User Key` for the Braze account (`external_id` or `braze_id`).
4. Give the export a name. If none is provided, `LOOKER_EXPORT` will be used.
5. Under __Advanced Options__, select `Results in Table` or `All Results`
6. Click `Send`.

![Send Looker Action][13]

If the export was correctly sent, then `looker_export` should appear in the user's profile as a custom attribute with the value you entered in the Action.

![Custom Attribute in Braze from Looker][14]

### Segment users by Looker export

To target the flagged users, a Braze Segments can be created that matches the flagged value.

![Braze Segment by Looker Export][15]

### Limitations

- This process only works with data that has not been pivoted.
- Currently, the API is limited to 100,000 rows sent.
- The Final count of a user's flag may be lower due to duplicates or non-users.

### Sample outgoing API

_Sample of the Outgoing API which will be sent to the [/user/track/][10] endpoint._

```json
{
   "api_key" : "[API_KEY]",
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

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}//user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[8]: https://dashboard.braze.com/app_settings/developer_console/
[9]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-track-request
[11]: {% image_buster /assets/img/user-track-api.gif %}
[12]: {% image_buster /assets/img/braze-looker-action.png %}
[13]: {% image_buster /assets/img/send-looker-action.png %}
[14]: {% image_buster /assets/img/custom-attributes-looker.png %}
[15]: {% image_buster /assets/img/braze_segments.png %}
