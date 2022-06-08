---
nav_title: Custom Event and Attribute Management
article_title: Custom Event and Attribute Management
page_order: 1
page_type: reference
description: "This reference article covers managing custom events and attributes, as well as understanding data type comparisons."

---

# Custom event and attribute management

## Adding custom attributes, custom events, and products

You can manage custom attributes, custom events (and their properties), and products (and their properties) from the respective tabs on **Manage Settings** page:

- Custom Attributes
- Custom Events
- Products

To add a custom attribute, event, or product, go to the respective tab and click **+ Add**. Give it a name (and for custom attributes, a data type) and click **Save**. This will enable tracking on it.

### Managing properties

Once you have created a **Custom Event** or **Product**, you can click **Manage Properties** for that event or product to add new properties, blocklist existing properties, and view which campaigns or Canvases use this property in a [trigger event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-1-select-a-trigger-event).

![Custom properties for a custom event][73]{: style="max-width:70%"}

To make these added custom attributes, events, products, or event properties trackable, you must ask your developer to create it in the SDK using the exact name you used to add it earlier. Or, you can use Braze's [APIs]({{site.baseurl}}/api/basics/) to import data on that attribute. After that, the custom attribute, event, or other will be actionable and apply to your users!

{% alert note %}
All User Profile data (custom events, custom attributes, custom data) is stored as long as those profiles are active. Custom event properties are stored and available for Segmentation for 30 days. If you'd like to leverage event properties for Segmentation, contact your Braze account manager, customer success manager, or open a [support ticket]({{site.baseurl}}/braze_support/).
{% endalert %}

## Blocklisting custom attributes, custom events, and products

If you want to stop tracking a specific custom attribute, event, or product (e.g., accidental creation during testing, no longer useful), search for it in the **Custom Events** tab, then click **Blocklist**.

To prevent collecting certain device attributes, see our [SDK guide][88].

Once a custom event or attribute is blocklisted:

- No data will be collected regarding that event/attribute,
- Existing data will be unavailable, unless reactivated,
- Blocklisted events and attributes will not show up in filters or graphs.

To accomplish this, Braze sends the blocklisting information down to each device. This is important as if you’re thinking about blocklisting a huge number of events and attributes (hundreds of thousands or millions), it will be a data intensive operation.

Something to consider is that blocklisting a high number of events and attributes is possible, but not advisable. This is because each time an event is performed or an attribute is (potentially) sent up to Braze, this event or attribute has to be checked against the entire blocklist. If it appears on the list, it won’t be sent up. This operation takes time, and if the list grows big enough, your app could start to slow down. If you have no need to use the event or attribute in the future, it should be removed from your app code during your next release.

Changes to the blocklist may take a few minutes to propagate. You may re-enable any blocklist event or attribute at anytime.

## Forcing data type comparisons

Braze automatically recognizes data types for attribute data that is sent to us. However, in the event multiple data types are applied to a single attribute, you can force the data type of any attribute to let us know what it really is. Click on the drop-down in the Data Type column to choose.

{% alert note %} Forcing data types does not apply to event properties, or purchase properties. {% endalert %}

![Custom attributes data type drop-down][75]

{% alert warning %}
If you choose to force the data type for an attribute, any data that comes in that isn't the specified type will be ignored.
{% endalert %}

### Data type coercion

| Forced Data Type | Description |
|------------------|-------------|
| Boolean | Inputs of `1`, `true`, `t` (not case sensitive) will be stored as `true` |
| Boolean | Inputs of `0`, `false`, `f` (not case sensitive) will be stored as `false` |
| Number | Integers or Floats (i.e., `1`, `1.5`) will be stored as numbers |
{: .reset-td-br-1 .reset-td-br-2}

For more information on specific filter options exposed by different data type comparisons check out [Configuring reporting][43]. And for more information on the different available data types, refer to [Custom attribute data types][44].

{% alert note %}
Data sent to Braze is immutable and cannot be deleted or modified once we've received it. However, you can use any of the steps listed in the preceding sections to exercise control over what you're tracking in your dashboard.
{% endalert %}


[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
