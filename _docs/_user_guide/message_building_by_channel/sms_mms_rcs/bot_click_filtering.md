---
nav_title: "Bot click filtering"
article_title: "SMS and RCS Bot Click Filtering"
description: "This reference article covers SMS and RCS bot click filtering."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 11
channel:
  - SMS
  - RCS
---

# SMS and RCS bot click filtering

> SMS and RCS bot click filtering enhances campaign analytics and workflows by excluding suspected bot clicks. A “bot click” refers to automated clicks on shortened links in SMS and RCS messages, such as those from web crawlers, Android and iOS link previews, or CPaaS security software. This feature facilitates accurate reporting, segmentation, and orchestration to engage real users. <br><br> For email campaign bot click filtering, refer to [Bot filtering for emails]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/bot_filtering/).

## How it works

Braze has a proprietary detection system that uses multiple inputs to identify suspected bot clicks, also known as non-human interactions (NHI). Bot clicks can inflate click rates, skewing engagement metrics. By filtering these, Braze facilitates the capture of reliable data for decision making.

Our system analyzes user agents associated with web crawlers, Android and iOS link previews, or CPaaS security software. A few examples of filtered user agents include `GoogleBot`, `python-requests/2.32.3`, and `Barracuda Sentinel (EE)`.

## Affected metrics and workflows

The following Braze metrics and workflows are impacted by bot clicks:

- **_Total Clicks_:** Campaign analytics and Canvas analytics will exclude bot clicks, reflecting only human interactions.
- **Segmentation filters:** Segment filters referencing SMS link interactions will exclude bot clicks for more accurate retargeting in campaigns and Canvases.
- **Orchestration:** Bot clicks are filtered from action-based triggers and Canvas action paths that reference SMS link interactions, allowing for triggers to reflect human behavior.
- **Braze Intelligence:**
    - **Intelligent Selection:** Excludes bot clicks when optimizing variant selection.
    - **Intelligent channel:** Excludes bot clicks when SMS or RCS is selected for accurate channel selection.
    - **Experiment steps:** Excludes bot clicks for reliable experiment outcomes.
    - **Currents data exports:** Includes `is_suspected_bot_click` and `suspected_bot_click_reason` fields to help analyze human versus bot clicks. These fields are available in [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), and [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/).

Unsubscribes from suspected bot clicks are unaffected. Braze processes all unsubscribe requests as usual. To block these unsubscribes, [submit product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Currents fields in SMS click events

Braze includes the following Currents fields for SMS click events:

| Field | Data type | Description |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolean | Indicates if the click is a suspected bot click. Returns `null` for all users until bot click filtering is enabled for your company. When enabled, it will populate with `true` or `false` for all new clicks going forward. |
| `suspected_bot_click_reason` | String, Array | Indicates the reason for a suspected bot click (such as `user_agent`). Populates even if filtering is disabled, providing insight into potential bot activity. This field is globally available and populates with a reason for all users, even if bot click filtering is not yet enabled. This provides insight into potential bot activity before you enable bot click filtering. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Query Builder template

For help analyzing your data, you can use the pre-built mobile template **SMS click events by bots** in [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/).

## Frequently asked questions

### How does bot click filtering impact campaign performance?

Filtering doesn't affect previously sent campaigns. When enabled, it reduces click rates from that moment onward by excluding bot clicks.

### Does bot click filtering prevent bots from clicking unsubscribe links?

No. All unsubscribe requests are processed as usual.

### Are link previews included in bot click filtering?

Yes. Link previews (such as Android and iOS link previews) are flagged as bot clicks and filtered out.

### How do I enable bot click filtering?

You must contact your Braze account team to enable bot click filtering during the early access. When bot click filtering has general availability, the feature will be on by default for all SMS and RCS users.

Also make sure you have enabled advanced click tracking for [link shortening]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/). This allows you to receive the bot click analytics, as we track this data at the individual user level. 

{% alert note %}
For further assistance, [contact Support]({{site.baseurl}}/braze_support/).
{% endalert %}