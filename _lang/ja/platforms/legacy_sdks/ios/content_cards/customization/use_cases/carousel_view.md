---
nav_title: カルーセルビュー
article_title: iOS 向けコンテンツカードカルーセルビュー
platform: iOS
page_order: 5
description: "この記事では、iOS アプリケーションを対象にコンテンツカードカルーセルビューのユースケースを実装する方法について説明します。"
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ユースケース:カルーセルビュー

![記事内のコンテンツカードのカルーセルを表示するニュースアプリの例。]({% image_buster/assets/img_archive/cc_politer_carousel.png %})({: style="max-width:35%;float:right;margin-left:15px;border:none;"})

このセクションでは、マルチカードカルーセルフィードの実装方法を説明します。マルチカードカルーセルフィードでは、水平方向にスワイプして追加の注目カードを表示できます。カルーセルビューを統合するには、完全にカスタマイズされたコンテンツカードの実装を使用する必要があります (「[ハイハイ - 歩く - 走る]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches)」アプローチの「走る」フェーズ)。

このアプローチでは、Braze ビューとデフォルトロジックを使用せず、代わりに、Braze モデルからのデータが取り込まれた独自のビューを使用して、完全にカスタマイズされた方法でコンテンツカードを表示します。

開発労力のレベルという点では、基本的な実装とカルーセル実装の主な違いは次のとおりです。

- 独自のビューを構築する
- コンテンツカードの分析を記録する
- カルーセルにどのカードを何枚表示するかを指示する追加のクライアント側ロジックを導入する

## 実装

### ステップ1:カスタムビューコントローラーを作成する

コンテンツカードのカルーセルを作成するには、独自のカスタムビューコントローラー (`UICollectionViewController` など) を作成して、[データ更新を配信登録]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#getting-the-data)します。デフォルトの `ABKContentCardTableViewController` はデフォルトのコンテンツカードタイプしか扱えないため、拡張したりサブクラス化したりすることはできません。

### ステップ 2:分析を実装する

完全にカスタマイズされたビューコントローラーを作成する場合、コンテンツカードのインプレッション数、クリック数、却下数は自動的に記録されません。インプレッション数、却下イベント、クリック数が Braze ダッシュボード分析に適切に記録されるようにするには、それぞれの分析メソッドを実装する必要があります。

分析メソッドについては、[カードメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#card-methods)を参照してください。 

{% alert note %}
同じページには、汎用コンテンツカードモデルクラスから継承されたさまざまなプロパティの詳細も記載されています。この情報は、ビューの実装時に役立つ可能性があります。
{% endalert %}

### ステップ3: コンテンツカードオブザーバーを作成する

コンテンツカードの到着を処理する[コンテンツカードオブザーバー]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener)を作成し、一度に特定の数のカードをカルーセルに表示する条件付きロジックを実装します。デフォルトでは、コンテンツカードは作成日順 (新しい順) にソートされ、対象となるすべてのカードが表示されます。

ただし、追加の表示ロジックを適用して、さまざまな方法でソートすることもできます。たとえば、配列から最初の 5 つのコンテンツカードオブジェクトを選択したり、キーと値のペア (データモデルの `extras` プロパティ) を導入して条件付きロジックを構築したりできます。

セカンダリコンテンツカードフィードとしてカルーセルを実装する場合は、[複数のコンテンツカードフィードを使用する]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds/)を参照して、キーと値のペアに基づいてカードが正しいフィードにソートされるようにします。

{% alert important %}
マーケターが Braze ダッシュボードに入力するキーと値のペアは、開発者がアプリのロジックに組み込むキーと値のペアと正確に一致しなければならないため、マーケティングチームと開発チームが、どのキーと値のペアを使用するか (たとえば、`feed_type = brand_homepage`) について確実に調整することが重要です。
{% endalert %}

コンテンツカードクラス、メソッド、属性に関する iOS 固有の開発者向けドキュメントについては、iOS [`ABKContentCard` クラスリファレンス](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)を参照してください。

## 考慮事項

- 完全にカスタマイズされたビューを使用すると、`ABKContentCardsController` で使用されるメソッドの拡張やサブクラス化ができなくなります。その代わりに、データモデルのメソッドとプロパティを自分で統合する必要があります。
- カルーセルビューのロジックと実装は、Braze のコンテンツカードのデフォルトタイプではないため、ユースケースを実現するためのロジックは開発チームが提供し、サポートする必要があります。
- カルーセルに一度に特定の数のカードを表示するには、クライアント側ロジックを実装する必要があります。

