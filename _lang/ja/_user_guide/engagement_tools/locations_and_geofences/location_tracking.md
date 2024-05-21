---
nav_title: 位置情報の追跡
article_title: 位置情報の追跡
page_order: 0
page_type: reference
description: "この参考記事では、アプリでロケーショントラッキングとターゲットターゲットを使用する方法と、ロケーショントラッキングをサポートしているパートナーについて説明します。"
tool: Location
search_rank: 2
---

# 位置情報の追跡

> 位置情報収集は、GPS 位置データを使用してアプリを開いたときのユーザーの最新の位置情報をキャプチャします。この情報を使用して、定義した場所にいたユーザーに基づいてデータをセグメント化できます。 

## 位置追跡を有効にする

アプリで位置情報収集を有効にするには、使用しているプラットフォームの開発者ガイドを参照してください。

- [iOS][2]
- [Android][3]
- [Web][4]

一般に、モバイルアプリはデバイスの GPS チップやその他のシステム (Wi-Fi スキャンなど) を使用してユーザーの位置を追跡します。ウェブアプリは WPS (Wi-Fi ポジショニングシステム) を使用してユーザーの位置を追跡します。これらすべてのプラットフォームでは、ユーザーが位置情報の追跡にオプトインする必要があります。

位置追跡データの正確性は、ユーザーが端末で Wi-Fi を有効にしているかどうかによって影響を受ける可能性があることに注意してください。Android ユーザーはさまざまな位置情報モードを選択することもできます。「バッテリー節約」モードまたは「デバイスのみ」モードのユーザーは、データが不正確になる可能性があります。 

## ロケーションターゲティング

ロケーショントラッキングデータとセグメントを使用して、ロケーションベースのキャンペーンと戦略を設定できます。例えば、特定の地域に住むユーザーを対象にプロモーションキャンペーンを実施したり、規制が厳しい地域のユーザーを除外したりできます。

ロケーションセグメントの作成について詳しくは、「[ロケーションターゲティング][1]」を参照してください。

## デフォルトロケーション属性のハード設定

また、API の[`users/track`エンドポイント][8]を使用して[`current_location`][9]標準属性を更新することもできます。例は次のとおりです。
```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## テクノロジーパートナー

また、一部のパートナーで位置追跡を利用することもできます。 

- [Radar][6]
- [Foursquare][7]
- [Gimbal][10]

## よくある質問

ロケーションに関するよくある質問への回答については、[ロケーションに関するよくある質問][11]をご覧ください。

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/data_augmentation/contextual_location/gimbal/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
