---
nav_title: Custom attributes
article_title: Custom Attributes
page_order: 1
page_type: reference
description: "This page describes custom attributes and explains the various custom attribute data types."
search_rank: 1
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Custom attributes

> This page covers custom attributes, which are a collection of your users' unique traits. Custom attributes are best for storing attributes about your users, or information about low-value actions within your application. 

When stored in Braze, custom attributes can be used to build out audience segments and personalize messaging using Liquid. Keep in mind that Braze doesn't store time-series information for custom attributes, so you can't get any graphs based on them like you can for custom events.

## Managing custom attributes

To create and manage custom attributes in the dashboard, go to **Data Settings** > **Custom Attributes**. 

![Four custom attributes that are booleans.]({% image_buster /assets/img/export_custom_attributes.png %})

The **Last updated** column lists the last time the custom attribute was edited, such as when it was last set to blocklist or active.

{% alert important %}
For proper message targeting, be sure that your custom attribute data type matches the actual custom attribute.
{% endalert %}

From this page, you can view, manage, create, or blocklist existing custom attributes. Select the menu next to a custom attribute for the following actions:

### Blocklisting

Custom attributes can be blocklisted individually in the actions menu, or up to 100 attributes can be selected and blocklisted in bulk. If you block a custom attribute, no data is collected regarding that attribute, existing data is unavailable unless reactivated, and blocklisted attributes don't show up in filters or graphs. Additionally, if the attribute is currently referenced by filters or triggers in other areas of the Braze dashboard, a warning modal appears explaining that all instances of the filters or triggers that reference it are removed and archived.

For more details on blocklisting and deleting custom data, see [Blocklist custom data]({{site.baseurl}}/user_guide/data/activation/blocklist_custom_data/).

### Marking as personally identifiable information (PII)

Administrators can also create custom attributes and mark them as PII from this page. These attributes are only visible to admins and dashboard users with the "View Custom Attributes Marked as PII" permission.

### Adding descriptions

You can add a description to a custom attribute after it's created if you have the `Manage Events, Attributes, Purchases` [user permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/). Edit the custom attribute and input whatever you like, such as a note for your team.

### Adding tags

You can add tags to a custom attribute after it's created if you have the "Manage Events, Attributes, Purchases" [user permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/). The tags can then be used to filter the list of attributes. 

### Removing custom attributes

There are two ways you can remove custom attributes from user profiles:

* Select the custom attribute name to be removed in a [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Set the `null` value in your API request to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Exporting data

To export the list of custom attributes as a CSV file, select **Export all** at the top of the page. The CSV file is generated, and a download link is emailed to you.

## Viewing usage reports

The usage report lists all the Canvases, campaigns, and segments using a specific custom attribute. This list doesn't include uses of Liquid. 

You can view up to 100 usage reports at a time by selecting the checkboxes next to the respective custom attributes and then selecting **View usage report**.

### Values tab

When viewing a usage report, select the **Values** tab to view the top values of the selected custom attributes based on a sample of approximately 250,000 users. Note that because the results are sampled from a subset of users, the sample won't include all existing values. This means the **Values** tab shouldn't be used for troubleshooting or for use cases that require incorporating data from all users.

![Usage report for selected custom attributes with an opened "Values" tab showing a pie chart of country attribute values, such as "US" and "PR".]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Setting custom attributes

The following lists methods across various platforms that are used to set custom attributes.

{% details Expand for documentation by platform %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (formerly Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Custom attribute storage

All data stored on the **User Profile**, including custom attribute data, is retained indefinitely as long as each profile is [active]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

For a full reference of all data types you can store as custom attributes—including booleans, numbers, strings, arrays, time, objects, and arrays of objects—see [Custom attribute data types]({{site.baseurl}}/user_guide/data/activation/attributes/data_types/).
