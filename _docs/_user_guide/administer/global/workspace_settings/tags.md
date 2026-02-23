---
nav_title: Managing tags
article_title: Managing tags
page_order: 6
page_type: reference
description: "This reference article covers how to manage tags in the Braze dashboard—renaming, nesting, and organizing tags across campaigns, Canvases, and segments."
---

# Managing tags

> Use the same tags across campaigns, Canvases, and segments. To efficiently rename, remove, or add tags across your dashboard, go to **Settings** > **Tag Management**.

For information on adding and using tags on campaigns, Canvases, segments, and custom data, see [Tags]({{site.baseurl}}/user_guide/data/activation/tags/).

## Managing tags

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

Looking for inspiration on how to leverage tags to manage your messaging lifecycle? Here are some common use cases.

{% tabs %}
{% tab Throttling %}

### Throttling

Limit how often your customers receive campaigns of a certain type. For example, you could set the following filters to limit the frequency of promotional campaigns:

`Last received campaign` with tag `Promo` more than 5 days ago 
<br>`OR`<br>
`Has not received campaign` with tag `Promo`

{% endtab %}
{% tab Reporting %}

### Reporting

Set up an Engagement Report to keep an eye on the volume of all campaigns with a certain tag. For example, if you want to monitor all of your push campaigns, you could add a tag like `Push Reporting` to those campaigns, then set up an [Engagement Report]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) to send you a report of those tagged campaigns every day.

{% endtab %}
{% endtabs %}
