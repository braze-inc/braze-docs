---
nav_title: ビーコンとジオフェンスのサポート
article_title: ビーコンとジオフェンスのサポート
page_order: 7
page_type: reference
tool: 
  - Segments
  - Location
description: "この記事では、ビーコンとジオフェンスのサポートと、位置情報パートナーアカウントを使用して位置情報の追跡を開始する方法について簡単に説明します。"

---

# ビーコンとジオフェンスのサポート

> この記事では、ビーコンとジオフェンスのサポートと、位置情報パートナーアカウントを使用して位置情報の追跡を開始する方法について簡単に説明します。

既存のビーコンやジオフェンスのサポートをターゲティングやメッセージング機能と組み合わせることで、ユーザーの物理的な行動についてより深く理解し、それに応じてメッセージを送ることができます。

## Radar のサポート

Radar は、無制限のカスタムジオフェンス、事前に構築されたPOIジオフェンス、ビーコン検出、地域検出、トリップ追跡などを完全にサポートしています。Radar と Braze の統合を有効にすると、Radar はリアルタイムの位置情報イベントとユーザー属性を転送し、リアルタイムキャンペーンのトリガー、ラストマイルの集配業務の強化、フリート追跡と配送ロジスティクスの最適化、ロケーションパターンに基づくユーザーセグメントの構築に使用できます。さらに、Radar Geo API を活用して、コネクテッドコンテンツを介してマーケティングキャンペーンを強化・パーソナライズできます。詳細については、 [Radar の統合]({{site.baseurl}}/partners/message_personalization/location/radar/#radar)をご覧ください。

## Gimbal の場所のサポート

Gimbal アカウントを Braze に接続すると、定義した場所へのユーザーの出入りを追跡し、これらの出入りからイベントをトリガーできます。さらに、地名や滞在時間などの追加情報をイベントプロパティとして追跡することで、メッセージングをさらにパーソナライズできます。[iOS][1] と [Android][2] の統合については、Gimbal のドキュメントを参照してください。 

{% alert note %}
これは、Gimbal のビーコンとジオフェンスのソリューションで同じように機能することに注意してください。
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#beacon-integration
