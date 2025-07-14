---
nav_title: 사용 가능한 파트너
article_title: 사용 가능한 커런츠 파트너
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze 커런츠와 통합하는 데 사용할 수 있는 데이터 파트너와 그 사용 사례를 간략하게 설명합니다."
tool: Currents

---

# 사용 가능한 파트너

> 이 페이지에는 브레이즈 커런츠와 통합할 수 있는 데이터 파트너가 나열되어 있으며 사용 사례에 대한 개요가 나와 있습니다. 

{% alert note %}
Braze에서 한 파트너를 위해 흐르는 이벤트의 이름 지정 규칙이 다른 파트너와 일치하지 않을 수 있습니다. 예를 들어, Segment의 커런츠 이메일 열기 이벤트는 `Email Opened`이며, Mixpanel에서는 `Email Open`입니다.
{% endalert %}

## 데이터 웨어하우스 스토리지
[![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
데이터 웨어하우스 스토리지는 Currents에서 스트리밍되는 모든 정보에 대한 수집 소스를 제공합니다. 이러한 파트너는 플랫 파일 스토리지를 위한 창고 역할을 하거나 비즈니스 인텔리전스 도구 및 머신 러닝 알고리즘을 강화하고 마케팅 성과에 대한 인사이트를 얻는 데 사용할 수 있습니다.

* [Amazon S3][1]
* [Google Cloud Storage][2]
* [Microsoft Azure Blob Storage][3]

저희는 커런츠와 데이터 웨어하우스를 함께 [사용하는]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/) 것에 대해 확신을 가지고 있으며, 직접 사용하고 있습니다!

## 고객 데이터

이러한 고객 데이터 플랫폼은 여러 소스에서 정보를 수집하고 다양한 위치로 라우팅하여 Braze 데이터를 최상의 방법으로 활용할 수 있도록 지원합니다.

* [mParticle][6]
* [세그먼트][7]
* [Tealium][8]
* [Treasure Data][10]
* [RudderStack][9]
* [Adobe][12]
* [Amperity][13]

## 행동 분석

이러한 파트너는 제품 분석 및 비즈니스 인텔리전스를 전문으로 하며, 사용자의 행동을 기반으로 사용자와 상호 작용하는 데 도움을 줄 수 있습니다.

* [Amplitude][4]

* [Mixpanel][5]

* [Heap][11]



[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/google_cloud_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/microsoft_azure_blob_storage_for_currents/
[4]: {{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/
[5]: {{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/
[6]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/
[7]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/
[8]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents
[9]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack_for_currents/
[10]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/treasure_data/treasure_data_for_currents/
[11]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/
[12]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/adobe_for_currents/
[13]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents
