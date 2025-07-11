---
nav_title: Tags
article_title: Tags
page_order: 12
page_type: reference
description: "This reference article covers tags in the Braze dashboard, which you can use to further organize and sort your engagement."

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
When you use bulk tagging to apply a new tag to multiple campaigns that already have different tags, each selected campaign will receive the new tag, and any tags present on a campaign will be applied to all other selected campaigns, even if those tags were not originally associated with them.
{% endalert %}

### Viewing tags

The tags set on a campaign, Canvas, or segment are visible on the details page near the engagement name. They also appear on campaign analytics.

![Tags shown on the Campaign Analytics page.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtering by tag

Tags are visible in the list of campaigns, Canvases, or segments, along with additional tags for status labels such as **Archived** and **Draft**. To filter by a tag, select the tag name from the list of tags.

![Tags on the list of campaigns.]({% image_buster /assets/img_archive/tags_grid.png %})

## Custom data tags

Tags may also be added to custom data when managing [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) and [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
This feature is currently in early access. Contact your customer success manager if you're interested in participating in this early access.
{% endalert %}

## Managing tags

You can use the same tags across campaigns, Canvases, and segments. To efficiently rename, remove, or add tags across your dashboard, go to **Settings** > **Tag Management**.

![Tags tab on the Manage Settings page.]({% image_buster /assets/img_archive/tags_view.png %})

To further organize your tags, nest your tags under a parent tag. For example, you can keep all holiday tags nested under a parent `Holidays` tag, or all tags related to a stage of your marketing funnel under a parent `Funnel` tag. 

To do so, create a new tag, select **Nest Tag Under**, and choose which existing tag to nest your new tag under. You can also nest existing tags from the **Tag Management** page. On this page, hover over a row with your tag and click **<i class="fas fa-pencil-alt"></i>Edit**. Then, follow the same steps as before.

![Create a nested tag.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Best practices {#tags-best-practices}

Tags can be a useful organizational tool for keeping track of engagement tactics. You can link segments and campaigns to business objectives, funnel stages, and the like.

The following is an example of tags an eCommerce app might find useful:

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>Funnel</th>
    <th>Business Objectives</th>
    <th>Regional</th>
    <th>Campaigns</th>
    <th>Holidays</th>
    <th>Transactions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>On-boarding<br>Re-engagement<br>Loyal<br>PowerUser<br>Churn<br>Lost</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>UnitedStates<br>Northeast<br>Midwest<br>South<br>West<br>LATAM<br>AP<br>WesternEurope<br>MiddleEast</td>
    <td>Sales<br>Coupons<br>Events</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>StPatricksDay<br>MarchMadness<br>Easter<br>Passover<br>MothersDay<br>MemorialDay<br>FathersDay<br>FourthJuly<br>LaborDay<br>VeteransDay<br>ColumbusDay<br>PresidentsDay<br>Halloween<br>RoshHashanah<br>Thanksgiving<br>Christmas<br>Hanukkah<br>NewYears</td>
    <td>Transactional<br>Notification<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

## Use cases

Looking for inspiration on how to leverage tags to manage your messaging lifecycle? Here are some common use cases:

### Throttling

Limit how often your customers receive campaigns of a certain type. For example, you could set the following filters to limit the frequency of promotional campaigns:

`Last received campaign` with tag `Promo` more than 5 days ago 
<br>`OR`<br>
`Has not received campaign` with tag `Promo`

### Reporting

Set up an Engagement Report to keep an eye on the volume of all campaigns with a certain tag. For example, if you want to monitor all of your push campaigns, you could add a tag like `Push Reporting` to those campaigns, then set up an [Engagement Report]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) to send you a report of those tagged campaigns every day.
