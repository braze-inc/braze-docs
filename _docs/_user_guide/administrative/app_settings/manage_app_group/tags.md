---
nav_title: Tags
article_title: Tags
page_order: 2
page_type: reference
description: "This reference article covers tags in the Braze dashboard, which you can use to further organize and sort your engagement."

---
# Tags

Braze tracks author, editor, date, and status information about segments, campaigns, Canvases, and News Feed cards, and gives you the ability to create tags to further organize and sort your engagement.

## Campaign, segment, and News Feed card tags

You can add tags when creating or editing a campaign, Canvas, segment, or News Feed card. Click <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** below the engagement name and select an existing tag, or start typing to add a new tag.

![Campaign Creation][2]

You can also add tags to multiple campaigns, Canvases, segments, or News Feed cards by selecting multiple engagements and clicking <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**.

![Tagging multiple][5]

The tags set on a campaign, Canvas, segment, or News Feed card are visible on the detail page below the engagement name.

![Campaign Details][3]

They are also visible in the list of campaigns, Canvases, segments, and News Feed cards as bubbles above the engagement name, along with status labels such as **Archived** and **Draft**.

![Campaigns][4]{: style ="max-width:70%;" }

To filter by a tag, select the tag name in the left-hand toolbar or search for the tag in the search pane using the `tag:` selector. For example, to search for the `Onboarding` tag, enter "tag:Onboarding".

![Tag Search for Campaigns and Segments][6]

## Best practices {#tags-best-practices}

Tags can be a useful organizational tool for keeping track of engagement tactics. You can link segments, campaigns, and News Feed cards to business objectives, funnel stages, and the like.

Below is an example of tags an eCommerce app might find useful:

![Potential Tags][7]

You can use the same tags across segments, campaigns, and News Feed cards. To efficiently rename, remove, or add tags across your dashboard, go to the **Manage Settings** page and select the **Tags** tab.

![tags view][8]

To further organize your tags, nest your tags under a parent tag. For example, you can keep all holiday tags nested under a parent `Holidays` tag, or all tags related to a stage of your marketing funnel under a parent `Funnel` tag. 

To do so, create a new tag, select **Nest Tag Under**, and choose which existing tag to nest your new tag under. You can also nest existing tags from **Manage Settings** > **Tags**. On this page, hover over a row with your tag and click **<i class="fas fa-pencil-alt"></i>Edit**. Then, follow the same steps as before.

![Create a nested tag][1]{: style ="max-width:70%;" }

## Use cases

Looking for inspiration on how to leverage tags to manage your messaging lifecycle? Here are some common use cases:

### Throttling

Limit how often your customers receive campaigns of a certain type. For example, you could set the following filters to limit the frequency of promotional campaigns:

`Last received campaign` with tag `Promo` more than 5 days ago 
<br>`OR`<br>
`Has not received campaign` with tag `Promo`

### Reporting

Set up an Engagement Report to keep an eye on the volume of all campaigns with a certain tag. For example, if you want to monitor all of your push campaigns, you could add a tag like `Push Reporting` to those campaigns, then set up an [Engagement Report]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#automatically-select-campaigns-or-canvases) to send you a report of those tagged campaigns every day.



[1]: {% image_buster /assets/img_archive/tag_nested.png %}
[2]: {% image_buster /assets/img_archive/tags_add_tag.png %}
[3]: {% image_buster /assets/img_archive/tag_details_page.png %}
[4]: {% image_buster /assets/img_archive/tags_grid.png %}
[5]: {% image_buster /assets/img_archive/tags_apply_multiple.png %}
[6]: {% image_buster /assets/img_archive/tags_filtering.png %}
[7]: {% image_buster /assets/img_archive/Tags-Potential_Tags.png %}
[8]: {% image_buster /assets/img_archive/tags_view.png %}
