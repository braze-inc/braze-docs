---
nav_title: Managing Custom Data
article_title: Managing Custom Data
page_order: 20
page_type: reference
description: "This reference article covers how to manage custom data, such as pre-populating campaigns and segments or blocklisting and deleting data."
---

# Managing custom data

> Learn how to pre-populate custom data in your campaigns and segments, or blocklist data that is no longer useful.

## Pre-populating custom data

There may be times when you'd like to set up campaigns and segments using custom data before your development team has integrated that custom data. Braze allows you to pre-populate custom events and attributes on the dashboard before these pieces of data start tracking so that these events and attributes are available for use in dropdowns and as part of the campaign creation process.

To pre-populate custom events and attributes, do the following:

1. Go to **Data Settings** > **Custom Events** or **Custom Attributes**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find these pages under **Manage Settings**.
{% endalert %}

![Navigate to Custom Attributes or Custom Events][21]{: style="max-width:90%;" }

{: start="2"}
2. Add a new custom attribute or custom event.<br><br> For custom attributes, select a [data type][20] for this attribute (for instance, boolean or string). An attribute's data type will determine the segmentation filters available for that attribute. <br><br>![Add new attribute or event][22]{: style="max-width:70%;" }

### Naming custom events and custom attributes

Custom events and custom attributes are case-sensitive. Keep this in mind when your development team integrates these custom events or attributes later. They must name the custom events or attributes exactly as you named them here, or Braze will generate a different custom event or attribute.

## Blocklisting custom data

You may occasionally identify custom attributes, custom events, or purchase events that either consume too many data points, are no longer useful to your marketing strategy, or were recorded in error. To stop this data from being sent to Braze, you can blocklist a custom data object while your engineering team works to remove it from the backend of your app or website.

Blocklisting prevents a particular custom data object from being recorded by Braze going forward. Blocklisting does not remove data from user profiles or retroactively decrease the amount of data points incurred for that custom data object. 

For instructions and details about blocklisting custom data, refer to [Custom event and attribute management]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/#blocklisting-custom-attributes-custom-events-and-products).

### Deleting custom data

The custom data can be deleted after you blocklist the custom data object and remove references from your app or website. For help deleting custom data, contact your customer success manager or the Support team.

Deleting custom data does the following:

- Removes the custom attribute, custom event, or purchase event from segment filter selections and analytics pages.
- Removes the custom attribute, custom event, or purchase event from the respective page under **Data Settings**.

{% alert important %}
Deleting does not remove data already recorded on user profiles, or prevent additional recording of the custom data objects on user profiles. Make sure the custom data is no longer being recorded before having the event or attribute deleted.
{% endalert %}


[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %}
[22]: {% image_buster /assets/img_archive/prepopulate_add.png %}