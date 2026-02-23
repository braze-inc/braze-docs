---
nav_title: Manage custom data
article_title: Manage Custom Data
page_order: 5
page_type: reference
description: "This reference article covers how to manage custom events and attributes—pre-populating, adding descriptions and tags, managing event properties, forcing data types, and marking attributes as PII."
---

# Manage custom data

> This page covers how to pre-populate custom data in your campaigns and segments, manage custom events and attributes and their properties, and configure data types. For blocklisting and deleting custom data, see [Blocklist custom data]({{site.baseurl}}/user_guide/data/activation/blocklist_custom_data/).

To learn how to manage custom attributes in particular (including adding descriptions, adding tags, and marking attributes as PII), refer to [Managing custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes).

## Pre-populating custom data

There may be times when you'd like to set up campaigns and segments using custom data before your development team has integrated that custom data. Braze allows you to pre-populate custom events and attributes on the dashboard before these pieces of data start tracking so that these events and attributes are available for use in dropdowns and as part of the campaign creation process.

To pre-populate custom events and attributes, do the following:

1. Go to **Data Settings** > **Custom Events** or **Custom Attributes** or **Products**.

![Navigate to Custom Attributes or Custom Events or Products.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. To add a custom attribute, event, or product, go to the respective page and select **Add Custom Attributes** or **Add Custom Events** or **Add Products**.<br><br>For custom attributes, select a [data type]({{site.baseurl}}/user_guide/data/activation/attributes/data_types/) for this attribute (for instance, boolean or string). An attribute's data type will determine the segmentation filters available for that attribute. <br><br>![Add new attribute or event]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. Select **Save**.

### Naming custom events and custom attributes

Custom events and custom attributes are case-sensitive. Keep this in mind when your development team integrates these custom events or attributes later. They must name the custom events or attributes exactly as you named them here, or Braze will generate a different custom event or attribute.

## Managing properties

After you have created a custom event or product, select **Manage Properties** for that event or product to add new properties, blocklist existing properties, and view which campaigns or Canvases use this property in a [trigger event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

![Custom properties for a custom event.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

To blocklist event or product properties, use the actions menu on the properties page. For blocklisting custom attributes, events, or products entirely, see [Blocklist custom data]({{site.baseurl}}/user_guide/data/activation/blocklist_custom_data/).

To make these added custom attributes, events, products, or event properties traceable, you must ask your development team to create them in the SDK using the exact name you used to add them earlier. Or, you can use the Braze [API]({{site.baseurl}}/api/basics/) to import data on that attribute. After that, the custom attribute, event, or other will be actionable and applied to your users.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

## Forcing data type comparisons

Braze automatically recognizes data types for attribute data that is sent to us. However, in the event multiple data types are applied to a single attribute, you can force the data type of any attribute to let us know what it is. Select from the dropdown in the **Data Type** column.

{% alert note %}
Forcing data types does not apply to event properties or purchase properties.
{% endalert %}

![Custom attributes data type dropdown]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
If you choose to force the data type for an attribute, any data that comes in that isn't the specified type will be coerced into that type. If such coercion is impossible (for example, a string containing letters being coerced into a number), the data will be ignored. Any data ingested before the type change will continue to be stored as the old type (and therefore may not be segmentable), and a warning will appear next to the attribute on the affected users' profiles.
{% endalert %}

### Data type coercion

| Forced Data Type | Description |
|------------------|-------------|
| Boolean | Inputs of `1`, `true`, `t` (not case sensitive) will be stored as `true` |
| Boolean | Inputs of `0`, `false`, `f` (not case sensitive) will be stored as `false` |
| Number | Integers or Floats (such as `1`, `1.5`) will be stored as numbers |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more information on specific filter options exposed by different data type comparisons, check out [Configuring reporting]({{site.baseurl}}/user_guide/analytics/reporting/configuring_reporting/). For more information on the different available data types, refer to [Custom attribute data types]({{site.baseurl}}/user_guide/data/activation/attributes/data_types/).

{% alert note %}
Data sent to Braze is immutable and cannot be deleted or modified after we've received it. However, you can use any of the steps listed in the preceding sections to exercise control over what you're tracking in your dashboard. To blocklist or delete custom data, see [Blocklist custom data]({{site.baseurl}}/user_guide/data/activation/blocklist_custom_data/).
{% endalert %}
