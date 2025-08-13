---
nav_title: 利用可能なパートナー
article_title: 利用可能な Currents のパートナー
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze Currents との連携に使用できるデータパートナーとそのユースケースについて概説します。"
tool: Currents

---

# 利用可能なパートナー

> このページでは、Braze Currentsと連携できるデータパートナーの一覧と、そのユースケースの概要を説明する。 

{% alert note %}
Braze から配信するイベントの命名規則が、パートナーによって異なる場合があります。たとえば、セグメントでの Currents メール開封イベントは `Email Opened` ですが、Mixpanel では `Email Open` になります。
{% endalert %}

## データウェアハウスストレージ
[![ブレイズ・ラーニング・コース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
データウェアハウスストレージは、Currents からストリーミングされるすべての情報の収集ソースを提供します。これらのパートナーは、ウェアハウス (フラットファイルストレージ用) として機能するか、ビジネスインテリジェンスツール、機械学習アルゴリズム、マーケティングパフォーマンスに関するインサイトの取得などに活用できます。

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

弊社は Currents とデータウェアハウスの力を確信しており、[社内で活用しています]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)。

## 顧客データ

ここに示す顧客データプラットフォームは、複数のソースから情報を収集して他のさまざまな場所に転送するため、Braze のデータを可能な限り最も優れた方法で活用できます。

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents/)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents)
* [トレジャーデータ]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents/)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents/)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents/)
* [アンペア]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents)

## 行動分析

ここに示すパートナーは製品分析とビジネスインテリジェンスを専門としており、ユーザーの行動に基づいてユーザーの対話を促進できるように支援します。

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/)

* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)

* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/)



