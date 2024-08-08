---
nav_title: ロケーションターゲティング
article_title: ロケーションターゲティング
page_order: 6.5
page_type: tutorial
tool: 
- Segments
- Location
description: "この記事では、ロケーションターゲティングを設定して、地域別にユーザーをセグメント化する方法について説明します。"

---

# ロケーションターゲティング

> この記事では、ロケーションターゲティングを設定して、地域別にユーザーをセグメント化する方法について説明します。これは、ロケーションベースのキャンペーンや戦略を検討している場合に最適です。

## ステップ 1:セグメントを作成する

[**セグメント**] ページの[**オーディエンス**] に移動して、現在のすべてのユーザーセグメントを表示します。このページでは、新しいセグメントを作成して名前を付けることができます。開始するには、[**セグメントを作成**] をクリックし、セグメントに名前を付けます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**セグメント**] は [**エンゲージメント**] の下にあります。
{% endalert %}

![][1]{: style="max-width:70%;"}

## ステップ 2: 位置情報をカスタマイズする

セグメントを作成したら、[**最新の場所**] フィルターを追加して、ユーザーがアプリを最後に使用した場所でユーザーをターゲティングします。標準の円形領域またはカスタマイズ可能な多角形領域でユーザーをハイライトするオプションがあります。

![][2]

### 円形領域

円形領域の場合は、原点を移動し、セグメンテーションの位置半径を調整できます。

![ニュージャージーとニューヨークの間の都市の円形のアウトライン][3]{: style="max-width:70%;"}

### 多角形領域

多角形領域の場合、セグメントに含めたい領域をより具体的に指定できます。

![選択された多角形領域としてのニューヨーク州のアウトライン][4]{: style="max-width:70%;"}

{% alert tip %}
Braze パートナーによる支援を受けながら、ロケーションターゲティングを活用することに興味がありますか?Braze の利用可能な[状況に即したロケーションパートナー]({{site.baseurl}}/partners/message_personalization/location/)をご覧ください。
{% endalert %}

[1]: {% image_buster /assets/img_archive/createsegment2.png %}
[2]: {% image_buster /assets/img_archive/filter_recent_location.png %}
[3]: {% image_buster /assets/img_archive/location_circle.png %}
[4]: {% image_buster /assets/img_archive/create_polygon.png %}
