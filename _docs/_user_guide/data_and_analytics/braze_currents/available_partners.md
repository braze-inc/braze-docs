---
nav_title: Available Partners
article_title: Available Currents Partners
page_order: 2
page_type: reference
description: "This reference article outlines the data partners you can use to integrate with Braze Currents, and their use cases."
tool: Currents

---

# Available partners

> This page outlines and describes the use cases of the data partners who you can use to integrate with Braze Currents.

{% alert note %}
Naming conventions for events that flow for one partner from Braze may not match other partners. For example, the Currents email open event in Segment is "Email Opened", while in Mixpanel, it is "Email Open".
{% endalert %}

## Data warehouses
[![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
These partners can either act as warehouses (for flat file storage) or gateways to other data manipulation tools. This is best if you need your data to be flexible, but also do backflips, and maybe a cartwheel.

* [Amazon S3][1]

* [Google Cloud Storage][2]

* [Microsoft Azure Blob Storage][3]

## Customer data

These customer data platforms collect and route information from multiple sources to a variety of other locations to empower you to utilize Braze data in the best ways possible.

* [mParticle][6]

* [Segment][7]

* [Tealium][8]


## Behavioral analytics

These partners specialize in product analytics and business intelligence and can help you interact with your users based on their actions.

* [Amplitude][4]

* [Mixpanel][5]



[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/google_cloud_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/microsoft_azure_blob_storage_for_currents/
[4]: {{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/
[5]: {{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/
[6]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/
[7]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/
[8]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents
