---
nav_title: ロケーションターゲティング
article_title: ロケーションターゲティング
page_order: 10
page_type: tutorial
tool: 
- Segments
- Location
description: "この記事では、ロケーションターゲティングを設定して、地域別にユーザーをセグメント化する方法について説明します。"

---

# ロケーションターゲティング

> この記事では、ロケーションターゲティングを設定して、地域別にユーザーをセグメント化する方法について説明します。これは、ロケーションベースのキャンペーンや戦略を検討している場合に最適です。

## ステップ 1:セグメントを作成する

[**セグメント**] ページの[**オーディエンス**] に移動して、現在のすべてのユーザーセグメントを表示します。このページでは、新しいセグメントを作成して名前を付けることができます。開始するには、[**セグメントを作成**] を選択し、セグメントに名前を付けます。

![Segmentを作成するためのモーダル。]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## ステップ 2: 位置情報をカスタマイズする

セグメントを作成したら、[**最新の場所**] フィルターを追加して、ユーザーがアプリを最後に使用した場所でユーザーをターゲティングします。標準の円形領域またはカスタマイズ可能な多角形領域の内部または外部でユーザーをハイライトするオプションがあります。

![円内の最新の位置をフィルタリングします。]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab Circular %}

### 円形領域

円形領域の場合は、原点を移動し、セグメンテーションの位置半径を調整できます。

![ニュージャージー州とニューヨーク州の間の都市の輪郭。]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonal %}

### 多角形領域

多角形領域の場合、セグメントに含めたい領域をより具体的に指定できます。

![選択された多角形領域としてのニューヨーク州の輪郭。]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## パートナーシップによるビーコンとジオフェンスのサポート

既存のビーコンやジオフェンスのサポートを Braze のターゲティング機能やメッセージング機能と組み合わせることで、ユーザーの物理的な行動に関する詳細な情報が判明し、それに応じてユーザーにメッセージを送ることができます。一部のパートナーとのロケーショントラッキングを活用できます。 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [インフィリオン]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

