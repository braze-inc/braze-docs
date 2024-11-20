---
nav_title: モバイル統合
article_title: ジオフェンスモバイル統合
page_order: 2
page_type: reference
description: "この参考記事では、ジオフェンスを使用する際に必要なモバイル統合について説明する。"
tool: Location

---

# モバイル統合

> この参考記事では、ジオフェンスを使用する際に必要なモバイル統合について説明する。

## クロスプラットフォームの要件

ジオフェンスをトリガーとするキャンペーンは、iOS と Android で利用できます。ジオフェンスをサポートするには、次が必要です。

1. 統合は、バックグラウンドプッシュ通知をサポートしている必要があります。
2. Braze のジオフェンスまたは位置情報の収集機能が有効になっている必要があります。
3. iOS バージョン 11 以降のデバイスの場合、ジオフェンスを機能させるには、ユーザーが位置情報へのアクセスを常に許可する必要があります。

{% alert important %}
Braze SDKバージョン3.6.0から、Brazeロケーションコレクションはデフォルトで無効になった。Androidでイネーブルメントが有効になっていることを確認するには、`braze.xml` で`com_braze_enable_location_collection` が`true` に設定されていることを確認する。
{% endalert %}

## ジオフェンスの設定

### 緯度と経度

ジオフェンスの地理的中心。

### 半径

地理的中心から計測されたジオフェンスの半径 (メートル単位)。すべてのジオフェンスについて、最小半径を100～150メートルに設定することを推奨する。

プラットフォームに関する詳しいガイダンスについては、以下のガイドを参照のこと：
- [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence)
- [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5)

### クールダウン

ユーザーは、個々のジオフェンスで入ったり出たりするトランジションを実行すると、ジオフェンス・トリガー通知を受け取る。トランジションが発生した後、そのユーザーがその個々のジオフェンスで同じトランジションを再び実行できないあらかじめ定義された時間がある。この時間は「クールダウン」と呼ばれ、Brazeによってあらかじめ設定されている。その主な目的は、不要なネットワーク要求を防ぐことです。

### テクノロジーパートナー

また、次のような一部のパートナーとジオフェンスを活用することもできます。 

- [Radar][12]
- [Foursquare][13]

## よくある質問

ジオフェンスに関するよくある質問への回答については、 [ジオフェンスに関するよくある質問][5]をご覧ください。

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
[12]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[13]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/

