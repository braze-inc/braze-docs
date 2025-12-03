---
nav_title: Link aliasing
article_title: Link Aliasing
alias: /link_aliasing/
page_order: 3
description: "This article describes how link aliasing works and provides examples for what your links will look like."
channel:
  - email

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Link aliasing
 
> Use link aliasing to create recognizable, user-generated names to identify links sent in email messages from Braze. These links are available for segmentation retargeting, action-based triggering, and link analytics.

## About link aliasing

With link aliasing, you can create user-generated names to identify and track links sent in emails. This way, you can efficiently use these recognizable link aliases in your emails to track engagement and analyze campaign performance, without needing to reference the full link.

With link aliasing, you can:

- **Retarget users who have clicked specific links:** Identify and target users who have clicked a link.
- **Create action-based triggers:** Send an email when a user clicks a link.
- **Analyze metrics:** Compare how many users have clicked Link A versus Link B.

### How it works

Braze uniquely identifies links within emails by appending an extra parameter called the `lid` (also known as the link identifier) to every link URL. This `lid` value allows Braze to track, monitor, and aggregate user interactions with the link even if the rest of the URL parameters may differ. This helps to provide insights into how users engage with the content in your email campaigns.

Link identifiers will also be updated if an email campaign, Canvas with an email message, or Content Block is duplicated.

## Creating a link alias

To create a link alias, follow these steps: 

1. In your campaign or Canvas component, go to your email body.
2. Select the **Link Management** tab.
3. Braze automatically generates unique default link aliases for each of your links.
4. Give the alias a name. Aliases must be uniquely named per email campaign variant or Canvas component. 

You can also set an alias that will be used to reference a specific link when dealing with reporting or segmentation. 

![Link Management page with four link aliases.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
Link aliasing is only supported in `href` attributes within HTML anchor tags where it is safe to append a query parameter. It's best practice to include a question mark (?) at the end of your link so that Braze can easily append the `lid` value. Without appending the `lid` value, Braze will not recognize the URL for link aliasing.
{% endalert %}

## Managing link aliases

To view all of your tracked link aliases, do the following:

1. Go to **Settings** > **Email Preferences** under **Workspace Settings**.
2. Select the **Link Aliasing Settings** tab.

{% alert important %}
If you are using the [older navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), these settings are under **Manage Settings**.
{% endalert %}

Here, you can sort, search, and turn off tracking for link aliases.

![Tracked Link Aliases page that shows active and inactive link aliases associated with various campaigns.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Use the [List link alias for campaign]({{site.baseurl}}/get_campaign_link_alias/) and [List link alias for Canvas]({{site.baseurl}}/get_canvas_link_alias/) endpoints to extract the `alias` set in each message variant in a campaign or an email-specific Canvas component.
{% endalert %}

Braze recommends evaluating the links within the email, adding link templates, and providing a naming convention that works for segmentation and reporting purposes. This helps you keep track of all links.

When link aliasing is turned on, messages, Content Blocks, and link templates are not modified. Any existing messages using link templates or Content Blocks will be the same. However, when you update a message, link alias markup will apply to all of the links, so you'll need to reapply the link templates for the links to be visible.

## How links are updated with link aliasing

The following tables provide examples of links in an email body, link aliasing results, and explanations for how the original link is updated with link aliasing.

### Permalink

**Logic:** Braze inserts a question mark (?) and adds the first query parameter into the URL.

| Link in Email Body    | Link with Aliasing                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link with more query parameters

**Logic:** Braze detects other query parameters and appends `lid=` to the end of the URL.

| Link in Email Body                                            | Link with Aliasing                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML link

**Logic:** Braze recognizes a link is a URL and already has a question mark (?) present, so the `lid` query parameter is appended after the question mark.

| Link in Email Body                                                | Link with Aliasing                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link with anchor

**Logic:** Braze expects the URL to use a standard structure where anchors (#) are present after a question mark (?). Because Braze reads from left to right, the question mark and `lid` value are appended before the anchor.

| Link in Email Body                               | Link with Aliasing                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link with anchor and capture tag

**Logic:** When using link aliasing with URLs that contain anchors (#), Braze expects the anchor to be placed after the query parameters. This means that the `lid` value must be appended before the anchor for proper tracking, and since Braze reads the URL from left to right, the question mark (?) and `lid` should come before the anchor.

| Link in Email Body                                                                        | Link with Aliasing                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tracking link aliases

In the **Link Management** tab, select which aliases you would like to be "tracked" for segmentation purposes and to be present in segmentation filters. Note that tracked aliases are only for segmentation purposes and will have no impact on your link being tracked for reporting purposes.

{% alert tip %}
To track link engagement metrics, make sure your link precedes with either HTTP or HTTPS. To turn off click tracking for specific links, refer to [Universal links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

Braze allows you to select unlimited links to track, though you may only retarget users on the most recent links they have opened. User profiles include their 100 most recently clicked links. For example, if you track 500 links and a user clicks on all 500 of them, you can retarget or create segments based on the 100 most recently clicked links.

![The Link Management tab with two selected links.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze only tracks up to the last 100 clicked link aliases at the profile level. 
{% endalert %}

### Action-based filters
 
You can create action-based messages targeting any link (tracked or not tracked) or retarget users based on whether they clicked an alias across any email campaign or Canvas component.

![Action-Based Options to target users who have clicked an alias in a Canvas component or interacted with a campaign.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Segmentation filters

In Braze, if you have a link alias in your email and a user clicks on it, the event is recorded in the user's profile with the alias.

If you use the "Clicked Alias in Any Campaign or Canvas Step" segmentation filter and later decide to rename this link alias, the previous click data in the user profile **will not** be updated, meaning it will still show as the previous link alias. So, if you target users based on the new link alias, it will not include the data from the previous link alias.

If you use the "Clicked Alias in Campaign" or "Clicked Alias in Canvas" segmentation filter, this will filter your users by whether they clicked a specific alias in a specific campaign or Canvas. If multiple users share the same email address and the link alias is clicked, all other users who share the email address will have their user profiles updated. 

The following segmentation filters apply to click events that are tracked at the time the event is processed. This means untracked links won't remove existing data and tracking a link won't backfill the data. For more details, see [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Untracking links

Untracking a link won't reallocate existing segments with the filter to the untracked alias. The old data will remain on the user profiles until it’s replaced by newer data. 

Links in archived messages are automatically untracked. However, if archived messages are unarchived, the links will need to be tracked again. When link aliases are tracked, link reporting is indexed by the alias instead of top-level domains or full URLs.

To view all of the links in your email campaign and their respective total clicks, go to **Message Analytics** > **Email Performance** > **Preview & Heatmap**, and select the **Show Heatmap** toggle.

![Link Table by Total Clicks panel with link aliases and their total clicks.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### Email clicks event

If you export your engagement data with Currents, an email click event will be slightly different if you have link aliasing enabled. It will have two additional fields for the [email clicks event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) when link aliasing is turned on: `link_id` and `link_alias`.

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

## Link aliasing in Content Blocks

New Content Blocks will have their links modified where Braze will append a `lid={{placeholder}}` to each link where applicable. This placeholder value is resolved when inserted into an email message variant.

To modify the links within existing Content Blocks that were created before Braze enabled link aliasing, duplicate the existing Content Blocks, then modify the links within the duplicated Content Blocks.

When a Content Block without a `lid` value is inserted into a new message, the links from that Content Block are not tracked with an alias. When a new Content Block is inserted into an "old" message variant, the links from that message variant will be recognized by link aliasing. Links from the Content Block are also recognized. However, "old" Content Blocks cannot nest "new" Content Blocks.

{% alert tip %}
For Content Blocks, Braze recommends creating copies of existing Content Blocks to use in new messages. This can be done by bulk duplicating to prevent scenarios where you might reference a Content Block that has not been enabled for link aliasing in a new message.
{% endalert %}

## Link aliasing for URLs generated by Liquid

For URLs that are generated by Liquid, such as `assign` statements in the HTML or from a Content Block, you must add a question mark (`?`) to the Liquid tag. This allows Braze to append query parameters (`lid = somevalue`) so that link aliasing can work properly. Without identifying where to append query parameters, link aliasing will not recognize these URLs and link templates won't apply.

### Example

Check out this link aliasing example for the recommended formatting of the link:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

If the link has parameters within it that contain a question mark (`?`), you can replace it in the anchor tag with an ampersand (`&`), such as in this example:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}


