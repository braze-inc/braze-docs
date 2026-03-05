---
nav_title: Tags
article_title: Tags
page_order: 4
page_type: reference
description: "This reference article covers tags for campaigns, Canvases, segments, and custom data in the Braze dashboard."
---

# Tags

> Braze tracks author, editor, date, and status information about segments, campaigns, and Canvases, and gives you the ability to create tags to further organize and sort your engagement.

## Campaign, Canvas, and segment tags

You can add tags when creating or editing a campaign, Canvas, or segment. Click <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** under the engagement name and select an existing tag, or start typing to add a new tag.

![Adding tags during campaign creation.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
You can add up to 175 tags to a campaign, Canvas, or segment.
{% endalert %}

### Bulk tagging

You can also add tags to multiple campaigns, Canvases, or segments by selecting multiple engagements and selecting <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**.

![Adding tags to multiple campaigns at the same time.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
When you use bulk tagging to apply a new tag to multiple campaigns that already have different tags, each selected campaign receives the new tag, and any tags present on a campaign are applied to all other selected campaigns, even if those tags were not originally associated with them.
{% endalert %}

### Viewing tags

The tags set on a campaign, Canvas, or segment are visible on the details page near the engagement name. They also appear on campaign analytics.

![Tags shown on the Campaign Analytics page.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtering by tag

Tags are visible in the list of campaigns, Canvases, or segments, along with additional tags for status labels such as **Archived** and **Draft**. To filter by a tag, select the tag name from the list of tags.

![Tags on the list of campaigns.]({% image_buster /assets/img_archive/tags_grid.png %})

## Custom data tags

Tags may also be added to custom data when managing [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes) and [custom events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#adding-tags).

{% alert important %}
This feature is currently in early access. Contact your customer success manager if you're interested in participating in this early access.
{% endalert %}

For information on renaming, removing, or nesting tags across your dashboard, see [Managing tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/#managing-tags).
