---
nav_title: 사용 가능한 파트너
article_title: 사용 가능한 커런츠 파트너
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze 커런츠와 통합하는 데 사용할 수 있는 데이터 파트너와 그 사용 사례에 대해 간략하게 설명합니다."
tool: Currents

---

# 사용 가능한 파트너

> 이 페이지에는 Braze 커런츠와 통합할 수 있는 데이터 파트너 목록과 사용 사례가 간략하게 설명되어 있습니다. 

{% alert note %}
Braze에서 한 파트너를 위해 흐르는 이벤트의 이름 지정 규칙이 다른 파트너와 일치하지 않을 수 있습니다. 예를 들어, 세그먼트의 커런츠 이메일 오픈 이벤트는 `Email Opened` 이며, Mixpanel에서는 `Email Open` 입니다.
{% endalert %}

## 데이터 웨어하우스 스토리지
데이터 웨어하우스 스토리지는 커런츠에서 스트리밍되는 모든 정보에 대한 수집 소스를 제공합니다. 이러한 파트너는 플랫 파일 스토리지를 위한 웨어하우스 역할을 하거나 비즈니스 인텔리전스 도구와 머신 러닝 알고리즘을 강화하고 마케팅 성과에 대한 인사이트를 얻는 데 사용할 수 있습니다.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
* [Microsoft Azure Blob 스토리지]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

저희는 커런츠와 데이터 웨어하우스를 함께 [사용하는]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/) 것에 대해 확신을 가지고 있으며, [직접 사용하고]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/) 있습니다!

## 고객 데이터

이러한 고객 데이터 플랫폼은 여러 데이터 소스로부터 정보를 수집하고 다양한 위치로 라우팅하여 사용자가 가능한 최선의 방법으로 Braze 데이터를 활용할 수 있도록 지원합니다.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents/)
* [세그먼트]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents/)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents/)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents/)
* [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents)

## 행동 분석

이러한 파트너는 제품 분석 및 비즈니스 인텔리전스를 전문으로 하며 사용자의 행동을 기반으로 사용자와 상호 작용하는 데 도움을 줄 수 있습니다.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/)

* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)

* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/)



