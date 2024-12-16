---
nav_title: Managing Custom Data
article_title: Managing Custom Data
page_order: 20
page_type: reference
description: "This reference article covers how to manage custom data, such as pre-populating campaigns and segments or blocklisting and deleting data."
---

# Managing custom data

> Learn how to pre-populate custom data in your campaigns and segments, blocklist data that is no longer useful, and manage custom events and attributes and properties.

## Pre-populating custom data

There may be times when you'd like to set up campaigns and segments using custom data before your development team has integrated that custom data. Braze allows you to pre-populate custom events and attributes on the dashboard before these pieces of data start tracking so that these events and attributes are available for use in dropdowns and as part of the campaign creation process.

To pre-populate custom events and attributes, do the following:

1. Go to **Data Settings** > **Custom Events** or **Custom Attributes** or **Products**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find these pages under **Manage Settings**.
{% endalert %}

![Navigate to Custom Attributes or Custom Events or Products.][21]{: style="max-width:90%;" }

{: start="2"}
2. To add a custom attribute, event, or product, go to the respective page and select **Add Custom Attributes** or **Add Custom Events** or **Add Products**.<br><br>For custom attributes, select a [data type][20] for this attribute (for instance, boolean or string). An attribute's data type will determine the segmentation filters available for that attribute. <br><br>![Add new attribute or event][22]{: style="max-width:80%;" }
3. Select **Save**.

### Naming custom events and custom attributes

Custom events and custom attributes are case-sensitive. Keep this in mind when your development team integrates these custom events or attributes later. They must name the custom events or attributes exactly as you named them here, or Braze will generate a different custom event or attribute.

## Managing properties

After you have created a custom event or product, select **Manage Properties** for that event or product to add new properties, blocklist existing properties, and view which campaigns or Canvases use this property in a [trigger event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-1-select-a-trigger-event).

![Custom properties for a custom event.][73]{: style="max-width:80%"}

To make these added custom attributes, events, products, or event properties traceable, you must ask your development team to create them in the SDK using the exact name you used to add them earlier. Or, you can use the Braze [API]({{site.baseurl}}/api/basics/) to import data on that attribute. After that, the custom attribute, event, or other will be actionable and applied to your users.

{% alert note %}
All user profile data (custom events, custom attributes, custom data) is stored as long as those profiles are active.
{% endalert %}

## Blocklisting custom data

You may occasionally identify custom attributes, custom events, or purchase events that either consume too many data points, are no longer useful to your marketing strategy, or were recorded in error. To stop this data from being sent to Braze, you can blocklist a custom data object while your engineering team works to remove it from the backend of your app or website.

Blocklisting prevents a particular custom data object from being recorded by Braze going forward, meaning it won't show up when searching for a specific user. Blocklisted data will not be sent by the SDK, and the Braze dashboard won't process blocklisted data from other sources (for example, the API). However, blocklisting doesn't remove data from user profiles or retroactively decrease the amount of data points incurred for that custom data object.

### Blocklisting custom attributes, custom events, and products

{% alert important %}
When an event or attribute is blocklisted, any segment, campaign, or Canvas using that event or attribute will be archived.
{% endalert %}

To stop tracking a specific custom attribute, event, or product, follow these steps:

1. Search for it in the **Custom Attributes**, **Custom Events**, or **Products** pages.
2. Select the custom attribute, event, or product. For custom attributes and events, you can select up to 10 to blocklist at a time.
3. Select **Blocklist**.

![Multiple selected custom attributes that are blocklisted on the Custom Attributes page.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

You can blocklist up to 300 custom attributes and 300 custom events. To prevent collecting certain device attributes, see our [SDK guide][88].

When a custom event or attribute is blocklisted, the following applies:

- No data sent to Braze will be processed, and blocklisted events and attributes will no longer count as data points
- Existing data will be unavailable unless reactivated
- Blocklisted events and attributes will not show up in filters or graphs
- References to blocklisted data within drafts of active Canvases will load as invalid values, which may cause errors
- Anything using the blocklisted event or attribute will be archived

To accomplish this, Braze sends the blocklisting information down to each device. This is important when thinking about blocklisting a huge number of events and attributes (hundreds of thousands or millions) as it would be a data-intensive operation.

### Considerations for blocklisting

Something to consider is that blocklisting a high number of events and attributes is possible, but not advisable. This is because each time an event is performed or an attribute is (potentially) sent up to Braze, this event or attribute has to be checked against the entire blocklist. If it appears on the list, it won't be sent up. This operation takes time, and if the list grows big enough, your app could start to slow down. If you have no need to use the event or attribute in the future, it should be removed from your app code during your next release.

Changes to the blocklist may take a few minutes to propagate. You can re-enable any blocklist event or attribute at anytime.

## Deleting custom data

As you build targeted campaigns and segments, you may find that you no longer need a custom event or custom attribute. For example, if you used a specific custom attribute as part of a one-time campaign, you can delete this data after [blocklisting it](#blocklisting-custom-attributes-custom-events-and-products) and remove its references from your app. You can delete any data types (such as strings, numbers, and nested custom attributes).

To delete a custom event or custom attribute, do the following:

1. Go to **Data Settings** > **Custom Attributes** or **Custom Events**, depending on which data type you want to delete.
2. Go to the custom data and select <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Blocklist**.
3. After your custom data has been blocklisted for 7 days, select <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Delete**.

### How deletion works

When you delete custom data, the following occurs: 

- **For custom attributes:** Permanently removes the attribute data from every user's profile.
- **For custom events:** Permanently removes the event metadata from every user's profile.

When an attribute or event is selected for deletion, its status is changed to **Trashed**. For the next seven days, it's possible to restore the attribute or event. If you don't restore after 7 days, the data will be permanently deleted. If you restore the attribute or event, it will be set back to the blocklisted state.

{% alert important %}
Custom data deletion is currently in early access. Contact your Braze account manager if you're interested in participating in the early access. For more help with deleting custom data, contact your customer success manager or the Support team.<br><br>Deleting doesn't prevent additional recording of the custom data objects on user profiles, so make sure the custom data is no longer being recorded before deleting the event or attribute.
{% endalert %}

### Things to know

When deleting custom data, keep in mind the following details:

* **Deletion is permanent**. Data cannot be recovered.
* Data is removed from the Braze platform and from user profiles.
* You can "reuse" the custom attribute name or custom event name after deletion. This means if you notice that custom data "reappears" in Braze after deletion, this may be caused by an integration that hasn’t been stopped and is sending data with the same custom data name.
* You may need to blocklist an item again if your deletion results in custom data reappearing. Blocklisting status isn’t preserved because the custom data is deleted.

## Forcing data type comparisons

Braze automatically recognizes data types for attribute data that is sent to us. However, in the event multiple data types are applied to a single attribute, you can force the data type of any attribute to let us know what it is. Select from the dropdown in the **Data Type** column.

{% alert note %}
Forcing data types does not apply to event properties or purchase properties.
{% endalert %}

![Custom attributes data type dropdown][75]

{% alert warning %}
If you choose to force the data type for an attribute, any data that comes in that isn't the specified type will be ignored.
{% endalert %}

### Data type coercion

| Forced Data Type | Description |
|------------------|-------------|
| Boolean | Inputs of `1`, `true`, `t` (not case sensitive) will be stored as `true` |
| Boolean | Inputs of `0`, `false`, `f` (not case sensitive) will be stored as `false` |
| Number | Integers or Floats (such as `1`, `1.5`) will be stored as numbers |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more information on specific filter options exposed by different data type comparisons, check out [Configuring reporting][43]. And for more information on the different available data types, refer to [Custom attribute data types][44].

{% alert note %}
Data sent to Braze is immutable and cannot be deleted or modified after we've received it. However, you can use any of the steps listed in the preceding sections to exercise control over what you're tracking in your dashboard.
{% endalert %}


[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %}
[22]: {% image_buster /assets/img_archive/prepopulate_add.png %}
[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
