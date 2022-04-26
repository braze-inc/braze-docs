---
nav_title: Link Aliasing
permalink: /link_aliasing/
description: "This article describes how link aliasing works and what your links will look like."
hidden: true
---

# Link aliasing
 
> Use link aliasing to create recognizable, user-generated names to identify links sent in email messages from Braze. Link aliasing gives you the ability to re-target users that have clicked specific links, allowing you to create action-based triggers when users click a specific aliased link. 

{% raw %}
Link aliasing creates user-generated names that are available for segmentation retargeting, action-based triggering, and link analytics. Link aliasing works by decorating a Braze-generated query parameter on links in the email channel. For each known link that is present in the email body, Braze will append `lid={{placeholder}}` to the end, where `{{placeholder}}` is a unique Liquid-generated alphanumeric value.
{% endraw %}

## Creating a link alias

To create a link alias, click on the **Link Management** tab in a Braze campaign or Canvas wizard to decorate all known links in the email body. Users can also set an alias that will be used to reference this link when dealing with reporting or segmentation. 

Aliases must be uniquely named per email campaign variant or Canvas step. You can also add link templates from the **Link Management** section.

Link aliasing is only supported in `href` attributes within HTML anchor tags where it is safe to append a query parameter. It is best to include a question mark (?) at the end of your link so Braze can easily append the `lid` value. Without appending the `lid` value, Braze will not recognize the URL for link aliasing.

### Checking workflows

Braze recommends evaluating the links within the email, adding link templates, and providing a naming convention that works for segmentation and reporting purposes. This helps you keep track of all links! 

### Extracting Data
The following endpoints are available to extract the `alias` set in each message variant in a campaign or an email Canvas step:

- [Campaign Link Alias Endpoint][3]
- [Canvas Link Alias Endpoint][4]

## Link templates
For new message variants, any existing link template can be used from the Link Management tab. For messages that were launched with a link template, they still will be applied. If an existing message is modified, the link template must be reapplied through the Link Management tab.

Link templates would previously work on all `href` URLS.  This assumed that whatever the value in the `href` would accept a question mark(to distinguish query parameters) and then append the link template.  This behavior is now been changed with link aliasing.  

Link templates are only applied to "known links" where Braze can safely know to append query parameters.  

For example, previously link templates would apply to Liquid-generated code like this: `href={{url}}`.  With link aliasing, it would only apply if the HTML looks like this: `href={{url}}?`.  The question mark (?) would indicate to Braze that it is safe to append query parameters (in this case `lid={{placeholder}}` and then any subsequent link template. 

## Link aliasing in Content Blocks
New Content Blocks will have their links modified where Braze will append a `lid={{placeholder}}` to each link where applicable. This placeholder value is resolved when inserted into an email message variant.

Any existing Content Blocks created before Braze enabled this feature will only have their links modified when the HTML in that Content Block is edited and the Content Block is relaunched.  Ideally, rather than relaunching, you should duplicate the Content Block.  Many customers have added a new naming convetion after duplicating to indicate that this new Content Block supports link aliasing where (old = Content_Block_1) (new = Content_block_1_LA)

When a Content Block that is not decorated with the `lid` value is inserted into a new message, the links from that Content Block are not tracked with an alias.
When a new Content Block is inserted into an “old” (this equates to a message created prior to Link Aliasing being enabled) message variant, the links from that message variant will be recognized by this feature (since the variant was edited). Links from the Content Block are also recognized. Note that “Old” Content Blocks (not marked up) cannot nest “new” Content Blocks.

{% alert tip %}
For Content Blocks, Braze recommends creating copies of existing Content Blocks to use in new messages. This can be achieved with bulk duplicating to prevent scenarios where you might reference a Content Block that has not been enabled for link aliasing in a new message.
{% endalert %}

## Link segmentation

Retargeting of aliases is now available as a segmentation filter. The two filters allow you to create segmentation filters based on your customers clicking a specifically tracked alias from either an email campaign or Canvas step. Note that this filter only displays campaigns or Canvases that have tracked aliases present.

### Tracking links

When composing your email message, a new column will be present in the **Link Management** tab. Here, you can indicate to Braze which alias you would like to be “tracked” for segmentation purposes. You can track an unlimited number of links.

{% alert note %}
Braze only tracks up to the last 100 clicked link aliases at the profile level. 
{% endalert %}

Only aliases you have indicated to be tracked will be present in segmentation filters. Note that tracked aliases are only for segmentation purposes and will have no impact on your link being tracked for reporting purposes.

### Untracking links

Untracking a link will not deallocate existing segments with the filter to the untracked alias. The old data will remain on the user profiles until they are evicted by newer data. The following segmentation filters will continue to exist, but new segments cannot be created with that filter.

For segmentation purposes, only 100 links can be tracked per app group by default. Links in messages that are archived will automatically be untracked. However, if archived messages are unarchived, the links will need to be tracked again.

When link aliases are tracked, link reporting is indexed by the alias instead of top-level domains or full URLs.

![][1]

### Segment filters

#### Clicked Alias in Campaign

Retarget users based on the specific alias that was clicked in a campaign. Only the campaigns that have aliases which were tracked will be reflected here.

#### Clicked Alias in Canvas Step

Retarget users based on the specific alias that was clicked in a Canvas step. A pipe delimited filter option displays the Canvas and Canvas step, followed by the alias within the Canvas step. Only Canvas steps with tracked aliases will be shown here.

#### Clicked Alias in Campaign or Canvas

Retarget users based on any alias that was clicked in the campaign or Canvas step. Because aliases are considered "global", any global alias will target link clicks from all campaigns and Canvas steps.

![][5]

### Action-based filters
 
In addition to creating segment filters, you can also create action-based messages targeting any link (tracked or not tracked) across any email campaign or Canvas step.

![][6]

### Email clicks event

The [email clicks event][7] occurs when a user clicks an email. Multiple events may be generated for the same campaign if a user clicks multiple times or clicks different links within the email. There are two additional fields for the email clicks event when link aliasing is enabled: `link_id` and `link_alias`.

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
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas and campaigns.

_Update noted in August 2019._
{% endalert %}

## Examples

The following table provides examples of links in an email body, link aliasing results, and explanations for how the original link is updated with link aliasing.

{%raw%}
| Link in Email Body | Link with Aliasing| Logic |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Braze inserts a question mark (?) and adds the first query parameter into the URL. |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze detects other query parameters and appends `lid=` to the end of the URL. |
| `<a href="{{custom_attribute.{product_url}}?">` | `<a href=”{{custom_attribute.{product_url}}?lid=ac7a548g5kl7”>` | Braze recognizes that this is a URL and already has a question mark (?) present. Then, it appends the `lid` query parameter after the question mark. |
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email | Braze expects the URL to use a standard structure where anchors (#) are present after a question mark (?).  Because Braze reads from left to right, we will append the question mark and `lid` value before the anchor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{%endraw%}



[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/ 
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/