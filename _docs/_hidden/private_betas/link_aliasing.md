---
nav_title: Link Aliasing
permalink: /link_aliasing/
description: "This article describes how Link Aliasing works and some of the nuances with the feature."
hidden: true
---

# Link Aliasing
 
> Use link aliasing to create recognizable, user-generated names to identify links sent in email messages from Braze. Link aliasing gives you the ability to re-target users that have clicked specific links, allowing you to create action-based triggers when users click a specific aliased link. 

## Overview

Link aliasing works by decorating a Braze-generated query parameter on links in the email channel. For each known link that is present in the email body, Braze will append {% raw %}`lid={{placeholder}}` to the end{% endraw %}, where {% raw %}`{{placeholder}}`{% endraw %} is a unique Liquid-generated alphanumeric value. 

These query parameters are also added to Content Blocks, enabling link tracking for segmentation purposes. 

![Link Aliasing Composer][2]

To create a link alias, click on the **Link Management** tab in a Braze campaign or Canvas wizard to decorate all known links in the email body. Users can also set an alias that will be used to reference this link when dealing with reporting or segmentation. Aliases must be uniquely named per email campaign variant or Canvas step. You can also add link templates from the link management section. 

### Feature Enablement

Enabling link aliasing is simple and does not require any downtime. This enablement is not backward compatible, meaning any previously created messages or Content Blocks will not be recognized by this feature (unless modified and relaunched again). 

## Preconditions and Limitations

### Messages modified by HTML parser
Your messages will be modified by an HTML parser; this could lead to the parser correcting potentially incorrect HTML. This is already the case if you use features such as pre-header input field, Liquid statements, or link templates.

### Partially migrated state
You may find yourself in a partially migrated state where some messages and Content Blocks will have aliasing. Editing messages or Content Blocks prior to having the feature enabled will result in Braze editing links.
### Link Aliasing support
Link aliasing is only supported in `href` attributes within HTML anchor tags where it is safe to append a query parameter. It is a best practice to include a questions mark "?" at the end of your link so Braze can append the `lid` value easily.

### Updating Content Block limitations
Adding `lid` values to an existing Content Block will only support propagating link documents to the first 50 "includers". An includer is a message variant where the Content Block is used, or another Content Block is nested.

## Post Enablement

{% tabs %}
{% tab Message Variants %}

New email message variants (campaign or Canvas) will have their links modified where Braze will append a {% raw %}`lid={{placeholder}}`{% endraw %} to each link, where applicable. 

Any email message variant that was created prior to Braze enabling this feature will only have its links modified when the HTML in those variants is edited.

{% endtab %}
{% tab HTML Content Blocks%}

New Content Blocks will have their links modified where Braze will append a {% raw %}`lid={{placeholder}}`{% endraw %} to each link, where applicable. The placeholder value is resolved when inserted into an email message variant.

Any existing Content Blocks that were created before Braze enabled this feature will only have their links modified when the HTML in that Content Block is edited, and the Content Block is relaunched.

When a Content Block that is not decorated with the `lid` value is inserted into...<br>
&#45; a new message, the links from that Content Block are not tracked with an alias.<br>
&#45; an old message, and that message has not been edited; the links are not tracked with any alias.

When a new Content Block is inserted into an 'old' message variant, the links from that message variant will be recognized by this feature (since the variant was edited). Links from the Content Block are also recognized.

"Old" Content Blocks (not marked up) cannot nest "new" Content Blocks.

{% alert tip%}
For Content Blocks, it is recommended to create copies of existing Content Blocks to use in new messages. This can be done by using the [bulk duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/#duplicate-multiple-templates) functionality. This prevents some edge cases where you might reference a Content Block that has not been enabled for link aliasing in a new message.
{% endalert %}

{% endtab %}
{% endtabs %}

## Link Templates
For new message variants, any existing link template can be used from the **Link Management** tab.

For any email message variation set up before this feature was enabled, the existing link templates will still be present. However, if the message variation is edited, the link templates will need to be reapplied.


## Link Segmentation

Retargeting of aliases is now available as a segmentation filter. The two new filters allow you to create segmentation filters based on your customers clicking a specific tracked alias, from either an email campaign or Canvas step. The filter only displays campaigns or Canvases that have tracked aliases present.

### Tracking a Link

When composing your email message, a new column will be present in the **Link Management** tab. Here, you can indicate to Braze which alias you would like to be "tracked" for segmentation purposes. Only aliases that you have indicated to be tracked will be present in segmentation filters. Please note that tracked aliases are only for segmentation purposes and will have no impact on your link being tracked for reporting purposes. 

### Untracking a Link
Untracking a link will not deallocate existing segments with the filter to the untracked alias. The old data will remain on the user profiles until they are evicted by newer data. The following segmentation filters will continue to exist but new segments cannot be created with that filter.

### Segment Filters

#### Clicked Alias in Campaign
Retarget users based on the specific alias that was clicked in a campaign. Only the campaigns that have aliases which were tracked will be reflected here.

#### Clicked Alias in Canvas Step
Retarget users based on the specific alias that was clicked in a Canvas step. A pipe delimited filter option displays the Canvas and Canvas step, followed by the alias within the Canvas step. Only Canvas steps with tracked aliases will be shown here.

#### Clicked Alias in Campaign or Canvas
Retarget users based on any alias that was clicked in the campaign or Canvas step. Because aliases are considered "global", any global alias will target link clicks from all campaigns and Canvas steps.

![Segmentation Filters for Link Aliasing][5]

### Action Based Filters
 
In addition to creating segment filters, you can also create action-based messages targeting any link (tracked or not tracked) across any email campaign or Canvas step.

![Action Based Filters for Link Aliasing][6]

## Tracking and Reporting

### Link Tracking

For segmentation purposes, only 100 links can be tracked per app group by default. Links within messages that are archived will automatically be untracked. If archived messages are unarchived, links will need to be tracked again.

### Link Click Reporting
Link reporting will now be indexed by the `alias` rather than top-level domains and/or full URLs. 

![Link Aliasing Click Table][1]

### Currents Event Changes

The [email clicks event][7] occurs when a user clicks an email. Multiple events may be generated for the same campaign if a user clicks multiple times or clicks different links within the email.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the url that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

## Additional information

### HTML Content Blocks in other channels 
If the HTML Content Block is used in other channels (for example, in-app message), a `lid=` value will still be appended on each link. The value will not be populated, so your links will look something like this: `http://www.braze.com?lid="`.

### Heatmap
The heatmap feature is not supported with this version of the link aliasing product. Future iterations may support showcasing the heatmap.

### API-Triggered
This feature does not support any message variant where the customer passes data related to links. 

### Extracting Data
The following endpoints are available to extract the `alias` set in each message variant in a campaign or an email Canvas step:

- [Campaign Link Alias Endpoint][3]
- [Canvas Link Alias Endpoint][4]


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/ 
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#email-clicks-events/