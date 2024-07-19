---
nav_title: Link Aliasing
article_title: Link Aliasing
alias: /link_aliasing/
page_order: 3
description: "This article describes how link aliasing works and what your links will look like."
channel:
  - email

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Link aliasing
 
> Use link aliasing to create recognizable, user-generated names to identify links sent in email messages from Braze. These links are available for segmentation retargeting, action-based triggering, and link analytics. Link aliasing gives you the ability to retarget users that have clicked specific links, allowing you to create action-based triggers when users click a specific aliased link.

## Creating a link alias

Link aliasing works by decorating a Braze-generated query parameter on links in the email channel. To create a link alias, follow these steps: 

1. Open your email body.
2. Click the **Link Management** tab.
3. Braze automatically generates unique default link aliases for each of your links.
4. Give the alias a name. Aliases must be uniquely named per email campaign variant or Canvas component. 

You can also set an alias that will be used to reference a specific link when dealing with reporting or segmentation. 

![][2]

Link aliasing is only supported in `href` attributes within HTML anchor tags where it is safe to append a query parameter. It's best to include a question mark (?) at the end of your link so that Braze can easily append the `lid` value. Without appending the `lid` value, Braze will not recognize the URL for link aliasing.

### Managing link aliases

Follow these steps to view all of your tracked link aliases:

1. Go to **Settings** > **Email Preferences** under **Workspace Settings**.
2. Click the **Link Aliasing Settings** tab.

{% alert important %}
If you are using the [older navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), these settings are under **Manage Settings**.
{% endalert %}

Here, you can also sort and search through all link aliases.

![Tracked Link Aliases page that shows a link alias named "test" that is an active part of a Canvas step.][8]

#### Untracking link aliases

On the **Link Aliasing Settings** tab, you can turn off tracking for link aliases.

1. Select the link alias.
2. Click **Turn off tracking**.  

#### Link aliases and user profile data

In Braze, if you have a link alias in your app or website and a user clicks on it, the event is recorded in the user's profile with the alias. Later, if you decide to rename this link alias, the previous click data in the user profile **will not** be updated, meaning it will still show as the previous link alias. So, if you target users based on the the new link alias, it will not include the data from the previous link alias.

### Checking workflows

Braze recommends evaluating the links within the email, adding link templates, and providing a naming convention that works for segmentation and reporting purposes. This helps you keep track of all links.

When link aliasing is enabled, messages, Content Blocks, and link templates are not modified. Any existing messages using link templates or Content Blocks will be the same. However, when you update a message, link alias markup will apply to all of the links, so you'll need to reapply the link templates for the links to be visible.

### Extracting data

Use the [List link alias for campaign][3] and [List link alias for Canvas][4] endpoints to extract the `alias` set in each message variant in a campaign or an email-specific Canvas component.

## Link aliasing in Content Blocks

New Content Blocks will have their links modified where Braze will append a `lid={{placeholder}}` to each link where applicable. This placeholder value is resolved when inserted into an email message variant.

To modify the links within existing Content Blocks that were created before Braze enabled link aliasing, duplicate the existing Content Blocks, then modify the links within the duplicated Content Blocks.

When a Content Block without a `lid` value is inserted into a new message, the links from that Content Block are not tracked with an alias. When a new Content Block is inserted into an "old" message variant, the links from that message variant will be recognized by link aliasing. Links from the Content Block are also recognized. However, "old" Content Blocks cannot nest "new" Content Blocks.

{% alert tip %}
For Content Blocks, Braze recommends creating copies of existing Content Blocks to use in new messages. This can be done by bulk duplicating to prevent scenarios where you might reference a Content Block that has not been enabled for link aliasing in a new message.
{% endalert %}

## Examples

The following table provides examples of links in an email body, link aliasing results, and explanations for how the original link is updated with link aliasing.

| Link in Email Body | Link with Aliasing | Logic |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Braze inserts a question mark (?) and adds the first query parameter into the URL. |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze detects other query parameters and appends `lid=` to the end of the URL. |
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} | Braze recognizes that this is a URL and already has a question mark (?) present. Then, it appends the `lid` query parameter after the question mark. |
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email | Braze expects the URL to use a standard structure where anchors (#) are present after a question mark (?). Because Braze reads from left to right, we will append the question mark and `lid` value before the anchor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Link aliasing for URLs generated via Liquid

For URLs that are generated by an `assign` statement in the HTML or in a Content Block, we recommend adding a question mark (?) into the anchor tag. This will help Braze append query parameters (`lid = somevalue`) so link aliasing can work properly. Without identifying where to append query parameters, link aliasing will not recognize these URLs.

### Example

Check out this link aliasing example for the recommended formatting of the anchor tag:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

If the link has parameters within it that contain a `?`, you can replace the `?` in the anchor tag with an ampersand (`&`), such as in this example:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}

## Link templates

For new message variants, any existing [link template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/) can be used from the **Link Management** tab. For messages that were launched with a link template, they still will be applied. If an existing message is modified, the link template must be reapplied through the **Link Management** tab. 

{% alert note %}
Link templates can only be applied for links visible in the **Link Management** tab. This means that links without the `lid` URL parameter, such as "old" Content Blocks or links that cannot be marked up, will not be eligible for link templates. To fix this, we recommend copying "old" Content Blocks or including a question mark (?) or ampersand (&) in the `href` attribute for the URL.
{% endalert %}

## Link segmentation

The retargeting of aliases filters allow you to create segmentation filters based on your customers clicking a specifically tracked alias from either an email campaign or Canvas component. This filter is only available for campaigns or Canvases that have tracked aliases present.

### Tracking links

In the **Link Management** tab, select which aliases you would like to be "tracked" for segmentation purposes and to be present in segmentation filters. Note that tracked aliases are only for segmentation purposes and will have no impact on your link being tracked for reporting purposes.

{% alert tip %}
To track link engagement metrics, make sure your link precedes with either HTTP or HTTPS.
{% endalert %}

Braze allows you to select unlimited links to track, though you may only retarget users on the most recent links they have opened. User profiles include their 100 most recently clicked links. For example, if you track 500 links and a user clicks on all 500 of them, you can retarget or create segments based on the 100 most recently clicked links.

{% tabs local %}
{% tab Drag-And-Drop Editor %}

![Link Management tab of the Drag-and-Drop email editor.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTML editor %}

![Link Management tab of the HTML email editor.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze only tracks up to the last 100 clicked link aliases at the profile level. 
{% endalert %}

### Untracking links

Untracking a link will not reallocate existing segments with the filter to the untracked alias. The old data will remain on the user profiles until it's replaced by newer data. The following segmentation filters will continue to exist, but new segments cannot be created with that filter.

For segmentation purposes, only 100 links can be tracked per workspace by default. Links in archived messages are automatically untracked. However, if archived messages are unarchived, the links will need to be tracked again. When link aliases are tracked, link reporting is indexed by the alias instead of top-level domains or full URLs.

![][1]

### Segment filters

The following segment filters apply to click events that are tracked at the time the event is processed. This means untracking links won't remove existing data and tracking a link won't backfill the data.

#### Clicked Alias in Campaign

Retarget users based on the specific alias that was clicked in a campaign. Only the campaigns that have aliases which were tracked will be reflected here.

#### Clicked Alias in Canvas Step

Retarget users based on the specific alias that was clicked in a Canvas component. A pipe delimited filter option displays the Canvas and Canvas component, followed by the alias within the Canvas component. Only Canvas steps with tracked aliases will be shown here.

#### Clicked Alias in Campaign or Canvas

Retarget users based on any alias that was clicked in the campaign or Canvas component. Because aliases are considered "global", any global alias will target link clicks from all campaigns and Canvas steps.

![][5]

### Action-based filters
 
You can create action-based messages targeting any link (tracked or not tracked) or retarget users based on if they clicked an alias across any email campaign or Canvas component. 

![][6]

### Email clicks event

The [email clicks event][7] occurs when a user clicks an email. Multiple events may be generated for the same campaign if a user clicks multiple times or clicks different links within the email. There are two additional fields for the email clicks event when link aliasing is enabled: `link_id` and `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas and campaigns.

_Update noted in August 2019._
{% endalert %}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/ 
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/
[8]: {% image_buster /assets/img/tracked_aliases.png %}