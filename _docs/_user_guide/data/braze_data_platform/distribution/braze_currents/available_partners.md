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

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

We're so confident in the power of Currents and data warehouses together, [we use it ourselves]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!

## Customer data

These customer data platforms collect and route information from multiple sources to a variety of other locations to empower you to utilize Braze data in the best ways possible.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents/)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents/)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents/)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents/)
* [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents)

## Behavioral analytics

These partners specialize in product analytics and business intelligence and can help you interact with your users based on their actions.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/)

* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)

* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/)



