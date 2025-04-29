---
nav_title: Available Partners
article_title: Available Currents Partners
page_order: 2
page_type: reference
description: "This reference article outlines the data partners you can use to integrate with Braze Currents, and their use cases."
tool: Currents

---

# Available partners

> This page lists the data partners you can integrate with Braze Currents, and outlines their use cases. 

{% alert note %}
Naming conventions for events that flow for one partner from Braze may not match other partners. For example, the Currents email open event in Segment is `Email Opened`, while in Mixpanel, it is `Email Open`.
{% endalert %}

## Data warehouse storage
[![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
Data warehouse storage offers a collection source for all the information streamed from Currents. These partners can either act as warehouses (for flat file storage) or be used to power business intelligence tools and machine learning algorithms, get insights on marketing performance, and more.

* [Amazon S3][1]
* [Google Cloud Storage][2]
* [Microsoft Azure Blob Storage][3]

We're so confident in the power of Currents and data warehouses together, [we use it ourselves]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!

## Customer data

These customer data platforms collect and route information from multiple sources to a variety of other locations to empower you to utilize Braze data in the best ways possible.

* [mParticle][6]
* [Segment][7]
* [Tealium][8]
* [Treasure Data][10]
* [RudderStack][9]
* [Adobe][12]
* [Amperity][13]

## Behavioral analytics

These partners specialize in product analytics and business intelligence and can help you interact with your users based on their actions.

* [Amplitude][4]

* [Mixpanel][5]

* [Heap][11]



[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/google_cloud_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/microsoft_azure_blob_storage_for_currents/
[4]: {{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/
[5]: {{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/
[6]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mparticle/mparticle_for_currents/
[7]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/
[8]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents
[9]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack_for_currents/
[10]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/treasure_data/treasure_data_for_currents/
[11]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/
[12]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/adobe_for_currents/
[13]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents
