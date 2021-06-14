---
nav_title: Link Aliasing
permalink: /linkaliasing/
description: "This article describes how Link Aliasing works and some of the nuances with the feature."
hidden: true
---

# Link Aliasing
 
> Use link aliasing to create recognizable, user-generated names to identify links sent in email messages from Braze. Link aliasing gives you the ability to re-target users that have clicked specific links, allowing you to create action-based triggers when users click a specific aliased link. 

## Overview

Link aliasing works by decorating a Braze-generated query parameter on links in the email channel. For each known link that is present in the email body, Braze will append {% raw %}`lid={{placeholder}}` to the end{% endraw %}, where {% raw %}`{{placeholder}}`{% endraw %} is a unique Liquid-generated alphanumeric value. 

These query parameters are also added to Content Blocks, enabling link tracking for segmentation purposes. 

![link_aliasing_composer][2]

To create a link alias, click on the __Link Management__ tab in a Braze campaign or Canvas wizard to decorate all known links in the email body. Users can also set an alias that will be used to reference this link when dealing with reporting or segmentation. Aliases must be uniquely named per email campaign variant or Canvas step. You can also add link templates from the link management section. 

### Feature Enablement

Enabling link aliasing is simple and does not require any downtime. This enablement is not backward compatible, meaning any previously created messages or Content Blocks will not be recognized by this feature (unless modified and relaunched again). 

## Preconditions and Limitations

__Messages Modified by HTML Parser__<br>
Your messages will be modified by an HTML parser; this could lead to the parser correcting potentially incorrect HTML. (This is already the case if you use features such as pre-header input field, Liquid statements, or link templates)<br><br>
__Partially Migrated State__<br>
You may find yourself in a partially migrated state where some messages and Content Blocks will have aliasing. Editing messages or Content Blocks prior to having the feature enabled will result in Braze editing links.<br><br>
__Link Aliasing Support__<br>
Link aliasing is only supported in `href` attributes within HTML anchor tags where it is safe to append a query parameter. It is a best practice to include a questions mark "?" at the end of your link so Braze can append the `lid` value easily.<br><br>
__Updating Content Block limitations__<br>
Adding `lid` values to an existing Content Block will only support propagating link documents to the first 50 "includers". An includer is a message variant where the Content Block is used, or another Content Block is nested.

## Post Enablement

{% tabs %}
{% tab Message Variants %}
__Message Variants__

New email message variants (campaign or Canvas) will have their links modified where Braze will append a {% raw %}`lid={{placeholder}}`{% endraw %} to each link, where applicable. 

Any email message variant that was created prior to Braze enabling this feature will only have its links modified when the HTML in those variants is edited.

{% endtab %}
{% tab HTML Content Blocks%}
__HTML Content Blocks__

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
For new message variants, any existing link template can be used from the __Link Management__ tab.

For any email message variation set up before this feature was enabled, the existing link templates will still be present. However, if the message variation is edited, the link templates will need to be reapplied.

## Link Segmentation
Two new segmentation filters are now available, allowing you to create segmentation filters based on clicking a specific tracked alias. The filter only displays campaigns or Canvases that have tracked aliases present.
 
In addition to creating segment filters, you can also create action-based messages targeting any link (tracked or not tracked) across any email campaign or canvas step. 

## Tracking and Reporting

### Link Tracking

For segmentation purposes, only 100 links can be tracked per app group by default. Links within messages that are archived will automatically be untracked. If archived messages are unarchived, links will need to be tracked again.

### Link Click Reporting
Link reporting will now be indexed by the `alias` rather than top-level domains and/or full URLs. 

![link_aliasing_click_table][1]

## Things to Note

__Using HTML Content Blocks in other Channels__<br>
If the HTML Content Block is used in other channels (for example, in-app message), a `lid=` value will still be appended on each link. The value will not be populated, so your links will look something like this: `http://www.braze.com?lid="`

__Heatmap__<br>
The heatmap feature is not supported with this version of the link aliasing product. Future iterations may support showcasing the heatmap.

__API-Triggered__<br>
This feature does not support any message variant where the customer passes data related to links. 

__Extracting Data__<br>
The following endpoints are available to extract the `alias` set in each message variant in a campaign or an email Canvas step:

- [Campaign Link Alias Endpoint][3]
- [Canvas Link Alias Endpoint][4]


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/ 
[4]: {{site.baseurl}}/get_canvas_link_alias/