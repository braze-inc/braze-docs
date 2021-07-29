---
nav_title: Custom Event and Attribute Management
page_order: 1

page_type: reference
description: "This reference article covers managing custom events and attributes, as well as understanding data type comparisons."
tool: Dashboard
---

# Custom Event and Attribute Management

## Adding Custom Attributes, Custom Events, and Products

You can manage custom attributes, custom events (and their properties), and products (and their properties) from the respective tabs on **Manage Settings** page:

- Custom Attributes
- Custom Events
- Products

To add a custom attribute, event, or product, go to the respective tab and click **+ Add**. Give it a name (and for custom attributes, a data type) and click **Save**. This will enable tracking on it.

![customattributessearch1.png][71]

### Managing Properties

Once you have created a **Custom Event** or **Product**, you can click **Manage Properties** for that event or product to add new properties, blocklist existing properties, and view which campaigns or Canvases use this property in a [trigger event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-1-select-a-trigger-event).

![customeventsview1.png][72]

![manageproperties1.png][73]{: style="max-width:70%"}

To make these added custom attributes, events, products, or event properties trackable, you must ask your developer to create it in the SDK using the exact name you used to add it earlier. Or, you can use Braze's [APIs]({{site.baseurl}}/api/basics/) to import data on that attribute. After that, the custom attribute, event, or other will be actionable and apply to your users!

{% alert note %}
All User Profile data (custom events, custom attribute, custom data) is stored as long as those profiles are active. Custom event properties are stored and available for Segmentation for thirty (30) days. If you'd like to leverage event properties for Segmentation, please contact your Braze Account Manager or Customer Success Manager.
{% endalert %}

## Blocklisting Custom Attributes, Custom Events, and Products

If you want to stop tracking a specific custom attribute, event, or product (e.g., accidental creation during testing, no longer useful), search for it in the **Custom Events** tab, then click **Blocklist**.

To prevent collecting certain device attributes, see our [SDK guide][88].

Once a custom event or attribute is blocklisted:

- No data will be collected regarding that event/attribute,
- Existing data will be unavailable, unless reactivated,
- Blocklisted events and attributes will not show up in filters or graphs.

Changes to the blocklist may take a few minutes to propagate. You may re-enable any blocklist event or attribute at anytime.

{% alert note %}
Please note that you should still remove the event or attribute from your app code during your next release.
{% endalert %}

## Forcing Data Type Comparisons

Braze automatically recognizes data types for attribute data that is sent to us. However, in the event multiple data types are applied to a single attribute, you can force the data type of any attribute to let us know what it really is. Click on the drop-down in the Data Type column to choose.

{% alert note %} Forcing data types does not apply to event properties, or purchase properties. {% endalert %}

![customeventsviewdatatypedropdown1.png][75]

{% alert warning %}
If you choose to force the data type for an attribute, any data that comes in that isn't the specified type will be ignored.
{% endalert %}

### Data Type Coercion

| Forced Data Type | Description |
|------------------|-------------|
| Boolean | Inputs of `1`, `true`, `t` (not case sensitive) will be stored as `true` |
| Boolean | Inputs of `0`, `false`, `f` (not case sensitive) will be stored as `false` |
| Number | Integers or Floats (i.e. `1`, `1.5`) will be stored as numbers |
{: .reset-td-br-1 .reset-td-br-2}

For more information on specific filter options exposed by different data type comparisons check out [Configuring Reporting][43]. And for more information on the different available data types, refer to [Custom Attribute Data Types][44].

{% alert note %}
Data sent to Braze is immutable and cannot be deleted or modified once we've received it. However, you can use any of the steps listed above to exercise control over what you're tracking in your dashboard.
{% endalert %}


[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[71]: {% image_buster /assets/img_archive/customattributessearch1.jpeg %}
[72]: {% image_buster /assets/img_archive/customeventsview1.jpeg %}
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/customeventsviewdatatypedropdown1.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
