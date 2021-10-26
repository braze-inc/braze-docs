---
nav_title: Pre-Populating Custom Data
article_title: Pre-Populating Custom Data
page_order: 0.2
page_type: reference
description: "This reference article describes the process to pre-populate your campaigns and segments with custom data."
tool:
  - Segments
  - Campaigns
  
---

# Pre-populating custom data

There may be times where you'd like to start setting up campaigns and segments using custom data before that custom data has been integrated by your development team. Braze allows you to pre-populate custom events and attributes on the dashboard before these pieces of data start tracking, so that these events and attributes are available for use in dropdowns, and as part of the campaign creation process.

To pre-populate custom events and attributes, navigate to the **Manage Settings** page and select the **Custom Attributes** or **Custom Events** tab. Then add a new custom attribute or custom event.

![Navigate to Custom Attributes or Custom Events][21]

For custom attributes, select a [data type][20] for this attribute (for instance, boolean or string). An attribute's data type will determine what types of segmentation filters are available for that attribute.

![Add new attribute or event][22]{: style="max-width:60%;" }

Custom events and custom attributes are case sensitive. Keep this in mind when your development team integrates these custom events or attributes later, they must name them exactly as you have named them here—including the use of uppercase or lowercase letters—or else Braze will generate a different custom event or attribute.

[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %}
[22]: {% image_buster /assets/img_archive/prepopulate_add.png %}
