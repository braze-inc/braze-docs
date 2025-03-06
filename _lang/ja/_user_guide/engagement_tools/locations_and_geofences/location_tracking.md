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

一般に、モバイルアプリはデバイスの GPS チップやその他のシステム (Wi-Fi スキャンなど) を使用してユーザーの位置を追跡します。ウェブアプリは WPS (Wi-Fi ポジショニングシステム) を使用してユーザーの位置を追跡します。これらすべてのプラットフォームでは、ユーザーが位置情報の追跡にオプトインする必要があります。位置情報の追跡データの精度は、ユーザーのデバイスでWi-Fiが有効になっているかどうかによって影響を受ける可能性がある。Android ユーザーはさまざまな位置情報モードを選択することもできます。「バッテリー節約」モードまたは「デバイスのみ」モードのユーザーは、データが不正確になる可能性があります。

### IPアドレスによるSDKユーザーのロケーション

2024年11月26日現在、Braze は最初の SDK セッションの開始時から IP アドレスを使用して、位置情報に基づいて特定された国からユーザーのロケーションを検出します。 

これ以前は、SDK ユーザー作成時と最初のセッションの間、Braze はデバイスロケールの国コードを使用していました。最初のセッション開始を処理してようやく、IP アドレスを使用して、より信頼性の高い国がユーザーに設定されます。つまり、ユーザーの国がより正確に設定されるのは、最初のセッション開始が処理された後、2番目のセッション以降になってからです。

これで、Braze は IP アドレスを使用して、SDK を介して作成されたユーザープロファイルに国の値を設定します。そのIPベースの国の設定は、最初のセッション中とその後に使用できます。

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

## パートナーシップによるビーコンとジオフェンスのサポート

既存のビーコンやジオフェンスのサポートを Braze のターゲティング機能やメッセージング機能と組み合わせることで、ユーザーの物理的な行動に関する詳細な情報が判明し、それに応じてユーザーにメッセージを送ることができます。一部のパートナーとのロケーショントラッキングを活用できます。 

- [Radar][6]
- [インフィリオン][10]
- [Foursquare][7]

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
[10]: {{site.baseurl}}/partners/message_personalization/location/infillion/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
