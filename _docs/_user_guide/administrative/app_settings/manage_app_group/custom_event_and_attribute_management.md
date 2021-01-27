---
nav_title: Custom Event and Attribute Management
page_order: 1
---

# Custom Event and Attribute Management

## Adding Custom Attributes, Custom Events, Products, and Event Properties

To add a Custom attribute, event, or product, go to the Custom Attributes, Custom Events, or Products pages, respectively, under “Manage App Groups” by clicking the “Add ..” button on the upper right hand corner of the lists of data. This will enable tracking on it.

![customattributessearch1.png][71]


You can also add event properties for custom events or products by clicking on the “Manage Properties” link in the “Event Properties” column:

![customeventsview1.png][72]
![manageproperties1.png][73]

To make these added Custom attributes, events, products, or event properties trackable, you must ask your developer to create it in the SDK using the exact name you used to add it earlier. Or, you may use Braze's APIs to import data on that attribute. After that, the Custom attribute, event, or other will be actionable and apply to your users!

{% alert note %}
All User Profile data (Custom events, Custom attribute, Custom data) is stored as long as those profiles are active. Custom event properties are stored and available for Segmentation for thirty (30) days. If you'd like to leverage event properties for Segmentation, please contact your Braze account or customer success manager. 
{% endalert %}

## Blocklisting Custom Attributes, Custom Events, and Products
If you want to stop tracking a specific Custom attribute/custom event/product (e.g., accidental creation during testing, no longer useful), search for it in the Custom Events tab, then click Blocklist.

In order to prevent collection of certain device attributes, see our [SDK guide][88].

Once a Custom event or attribute is blocklisted,
- No data will be collected regarding that event/attribute,
- Existing data will not be wiped,
- Blocklisted events/attributes will not show up in filters or graphs.

Changes to the blocklist may take a few minutes to propagate. You may re-enable any blocklist event or attribute at anytime.

{% alert note %}
Please note that you should still remove the event/attribute from your app code during your next release.
{% endalert %}

## Forcing Data Type Comparisons
Braze automatically recognizes data types for attribute data that is sent to us. However, in the event multiple data types are applied to a single attribute, you can force the data type of any attribute to let us know what it really is. Click on the drop-down in the Data Type column to choose.

*Note*: Forcing data types does not apply to event properties, or purchase properties.

![customeventsviewdatatypedropdown1.png][75]

{% alert warning %}
If you elect to force the data type for an attribute, any data that comes in that isn't the specified type will be ignored.
{% endalert %}

### Data Type Coercion

| Forced Data Type | Description |
|------------------|-------------|
| Boolean | Inputs of `1`, `true`, `t` (not case sensitive) will be stored as `true` |
| Boolean | Inputs of `0`, `false`, `f` (not case sensitive) will be stored as `false` |
| Number | Integers or Floats (i.e. `1`, `1.5`) will be stored as numbers |
| Array | Comma separated list of values, with or without square brackets (i.e.`[first, second, third]`, or `first,second,third`) will be stored as an Array |
{: .reset-td-br-1 .reset-td-br-2}

For more information on specific filter options exposed by different data type comparisons please see [Configuring Reporting article][43]. And for more information on the different available data types, please see the section on ["Custom Attribute Data Types"][44].

{% alert note %}
Please note that data sent to Braze is immutable and cannot be deleted or modified once we've received it. However, you can use any of the steps listed above to exercise control over what you're tracking in your dashboard.
{% endalert %}


[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[71]: {% image_buster /assets/img_archive/customattributessearch1.png %}
[72]: {% image_buster /assets/img_archive/customeventsview1.png %}
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/customeventsviewdatatypedropdown1.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
