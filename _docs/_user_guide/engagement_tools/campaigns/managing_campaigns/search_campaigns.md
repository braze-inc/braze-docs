---
nav_title: Searching for Campaigns
article_title: Searching for campaigns
page_order: 10
page_type: reference
description: "This article covers search terms you can use to find campaigns."
tool:
  - Campaigns

---

# Searching for campaigns

This page describes how you can use the search field of the campaigns list to refine your results.

## Keyword search

Enter the name of a campaign, or search for keywords in a campaign name, description, or message fields. For example, here we've searched for "this week", which is pulling from the title and message of this re-engagement campaign.

![Campaign search for keywords "this week" with the results from the message title and body.][1]

## Search exact text

To find exact matches to your search terms, wrap your search in square brackets `[ ]`.

For example, if you search for `[flow]`, you'll see any campaigns that have the word "flow" in it, but not "flower" or "overflow".

## Filters

Use the filters in the side menu to group results by creator, editor, send dates, or channel, or select **Only Show Mine** to limit the results of your search to campaigns you've created. You can also filter by status and [tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) to further narrow down your results.

![][2]

Expand the search dropdown to filter by last editor, target segment, messaging channel, or date.

![][3]

## Search syntax

Selecting a campaign filter will automatically add the appropriate syntax to the search field. However, you can manually enter these filters as well. When using manual search, the syntax is the filter name, followed by a semicolon, followed by your input. For example, to search for push campaigns, enter `channel:push`.

Here's a list of supported search filters:

| Search for | Filter | Input |
| --- | --- | --- |
| Campaign API identifier | `api_id` | A specific [campaign API identifier]({{site.baseurl}}/api/identifier_types#api-identifier-types) |
| Segment a campaign targets | `segment` | Segment name |
| Messaging channel a campaign targets | `channel` | One of the following: <br>-`content_cards` <br>- `email`<br>- `push`<br>- `sms` (returns both SMS and MMS)<br>- `webhook`
| Status or delivery type | `status` | One of the following: <br>- `one-time` <br>- `recurring` <br>- `triggered` <br>- `multivariate` <br>- `transactional` <br> - `drafts` <br> - `stopped` <br> - `archived` <br> - `all` |
| Tag | `tag` | - A single tag name <br>- A list of tag names separated by commas |
| Most recent editor | `edited_by` | A user's email address |
| Date campaign was created | `created` | - A single date in the format `YYYY/MM/DD`<br> - A range of dates in the format `YYYY/MM/DD-YYYY/MM/DD` |
| Date campaign was last edited | `edited` | - A single date in the format `YYYY/MM/DD`<br> - A range of dates in the format `YYYY/MM/DD-YYYY/MM/DD` |
| Date campaign was last sent | `sent` | - A single date in the format `YYYY/MM/DD`<br> - A range of dates in the format `YYYY/MM/DD-YYYY/MM/DD` |
| Campaigns you created | `created_by_me` | `true` |


[1]: {% image_buster /assets/img_archive/campaign_search.png %}
[2]: {% image_buster /assets/img_archive/campaign_search2.png %}
[3]: {% image_buster /assets/img_archive/campaign_search3.png %}