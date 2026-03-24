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

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

一般的にモバイルアプリは、デバイスのGPSチップやその他のシステム（Wi-Fiスキャンなど）を使ってユーザーの位置情報を追跡する。WebアプリはWPS（Wi-Fi測位システム）を使ってユーザーの位置情報を追跡する。これらのプラットフォームはすべて、ユーザーが位置情報の追跡に同意する必要がある。位置情報の追跡データの精度は、ユーザーのデバイスでWi-Fiが有効になっているかどうかによって影響を受ける可能性がある。Android ユーザーはさまざまな位置情報モードを選択することもできます。「バッテリー節約」モードまたは「デバイスのみ」モードのユーザーは、データが不正確になる可能性があります。

### IPアドレスによるSDKユーザーのロケーション

Brazeは、最初のSDKセッション開始時のIPアドレスを使用して、地理的に位置する国からユーザーの位置を検出する。 

以前は、BrazeはSDKユーザー作成時と最初のセッションの間、デバイスロケールの国コードを使用していた。最初のセッション開始を処理してようやく、IP アドレスを使用して、より信頼性の高い国がユーザーに設定されます。つまり、ユーザー国がより高い精度で設定されるのは、最初のセッション開始が処理された後、2回目以降のセッションからということになる。

現在、Brazeは、SDK経由で作成されたユーザープロファイルの国設定にIPアドレスを使用しており、そのIPベースの国設定は、最初のセッション中もその後も利用可能である。

## ロケーションターゲティング

ロケーショントラッキングデータとセグメントを使用して、ロケーションベースのキャンペーンと戦略を設定できます。例えば、特定の地域に住むユーザーを対象にプロモーションキャンペーンを実施したり、規制が厳しい地域のユーザーを除外したりできます。

ロケーションセグメントの作成について詳しくは、「[ロケーションターゲティング]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/)」を参照してください。

## デフォルトロケーション属性のハード設定

また、API の[`users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して[`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)標準属性を更新することもできます。例は次のとおりです。

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

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [インフィリオン]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## よくある質問

### Braze はいつ位置データを収集しますか?

Braze は、アプリケーションがフォアグラウンドで開いている場合にのみ位置情報を収集します。その結果、フィルター `Most Recent Location` は、ユーザーが最後にアプリケーションを開いた位置情報 (セッション開始とも呼ばれます) に基づいてユーザーをターゲットにします。

また、次のニュアンスにも留意する必要があります。

- 位置情報が無効の場合、`Most Recent Location` フィルターは最後に記録された位置情報を表示する。
- ユーザープロファイルに位置情報の追跡が保存されたことがある場合、その後位置情報の追跡をオプトアウトした場合でも、`Location Available` フィルターの対象となる。

### 「最新のデバイスロケール」フィルターと「最新の位置情報」フィルターの違いは？

`Most Recent Device Locale` はユーザーのデバイス設定から取得されます。例えば、iPhoneユーザーの場合、デバイスの**「設定」**>「**一般**」>「**言語」& 「地域**」に表示される。このフィルターは、日付や住所などの言語や地域の書式をキャプチャするために使用され、`Most Recent Location` フィルターとは無関係です。

`Most Recent Location` は、デバイスの最新の既知の GPS 位置です。これはセッション開始時に更新され、ユーザーのプロファイルに保存されます。

### ユーザーが位置情報の追跡をオプトアウトした場合、以前のユーザーデータはBrazeから削除されるのか？

ユーザープロファイルに位置情報の追跡が保存されたことがある場合、そのデータが自動的に削除されることはない。

## トラブルシューティング

### 利用可能なロケーションを持つユーザーはいない

Brazeは、SDKを通じてデフォルトでユーザーの最新の位置情報を取得する。これは通常、「最新の位置情報」が、ユーザーがアプリを最後に使用した場所であることを意味します。Braze のバックグラウンド位置情報データを送信する場合は、より詳細なデータを使用できる場合があります。

利用可能なロケーションを持つユーザーがいない場合、2つの簡単なチェックでデータ収集と日付転送を確認することができる。

#### データ収集

アプリが位置情報を収集していることを確認する：

- iOS の場合、これは、ユーザーがユーザージャーニーのどこかの時点でプロンプトを介して位置情報データの共有を選択することを意味します。 
- Androidについては、設置時にアプリが細かい場所または粗い場所の許可を要求していることを確認してください。

ユーザーの位置情報がBrazeに送信されているかどうかを確認するには、**Location Available**フィルターを使用する。このフィルターによって、「最新の位置情報」を持つユーザーの割合を見ることができる。

![Location Available "フィルターを使用した "Test Location "セグメンテーション。]({% image_buster /assets/img_archive/trouble7.png %})

#### データ転送

開発者が位置情報をBrazeに渡していることを確認する。通常、位置データの受け渡しは、ユーザーが権限を付与した後に SDK によって自動的に処理されますが、開発者が Braze での位置情報の追跡を無効にしている可能性があります。位置情報のトラッキングに関する詳細は、以下を参照されたい：
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)