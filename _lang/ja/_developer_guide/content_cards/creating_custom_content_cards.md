---
nav_title: カスタムコンテンツカードの作成
article_title: カスタムコンテンツカードの作成
page_order: 5
description: "この記事では、カスタムコンテンツカード UI を作成するためのコンポーネントについて説明します"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# カスタムコンテンツカードの作成

> この記事では、カスタムコンテンツカードを実装するときに使用する基本的なアプローチと、バナー画像、メッセージ受信トレイ、画像のカルーセルの3つの一般的なユースケースについて説明します。コンテンツ・カードのカスタマイズ・ガイドの他の記事をすでに読んで、デフォルトでできることと、カスタム・コードが必要なことを理解していることを前提としている。特に、カスタム・コンテンツ・カードの[アナリティクスを記録]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics)する方法を理解することである。 

Brazeには、`imageOnly`、`captionedImage`、`classic`、`classicImage`、`control`といったさまざまな[コンテンツカードタイプ]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details)が用意されています。これらは実装の出発点として使用でき、ルックアンドフィールを調整できます。 

また、Braze モデルからのデータを入力した独自のプレゼンテーション UI を作成することで、完全にカスタムな方法でコンテンツカードを表示することもできます。コンテンツカードオブジェクトを解析し、そのペイロードデータを抽出します。次に、結果のモデルデータを使用してカスタム UI を入力します。[ハイハイ、歩く、走る]({{site.baseurl}}/developer_guide/customization_guides/customization_overview)のうちの「走る」フェーズです。

{% alert note %}
デフォルトの各コンテンツカードタイプは、汎用コンテンツカードモデルクラスから異なるプロパティを継承するサブクラスです。これらの継承プロパティを理解すると、カスタマイズを行う際に役立ちます。詳細については、カードクラスのドキュメントを参照してください ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard)、[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html))。
{% endalert %}


## カスタマイズの概要

ユースケースによって、カスタムコンテンツカードの実装方法は厳密には多少異なりますが、次の基本的な方法に従います。

1. 独自の UI を構築する
2. データの更新をリッスンする
3. 分析を手動でログに記録する

### ステップ1:カスタム UI を作成する 

{% tabs %}
{% tab Android %}

まず、独自のカスタムフラグメントを作成します。デフォルトの[`ContentCardFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)は、デフォルトのコンテンツカードタイプのみに対応するよう設計されていますが、良い出発点です。

{% endtab %}
{% tab iOS %}

まず、独自のカスタムビューコントローラーコンポーネントを作成します。デフォルトの[`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller)は、デフォルトのコンテンツカードタイプのみに対応するよう設計されていますが、良い出発点です。

{% endtab %}
{% tab Web %}

まず、カードのレンダリングに使用するカスタム HTML コンポーネントを作成します。 

{% endtab %}
{% endtabs %}

### ステップ 2:カードの更新情報を購読する

次に、カードの更新時に[データ更新を購読]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates)するコールバック関数を登録します。 

### ステップ3: 分析を実装する

コンテンツカードのインプレッション数、クリック数、却下数は、カスタムビューに自動的に記録されません。すべての指標が Braze ダッシュボードの分析に適切に記録されるように、[それぞれのメソッドを実装]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events)する必要があります。

## コンテンツカードの配置

コンテンツカードはさまざまな方法で使用できます。一般的な3つの実装は、メッセージセンター、バナー広告、または画像カルーセルとして使用することです。これらの配置ごとに、[キーと値のペア]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (データモデルの`extras`プロパティ) をコンテンツカードに割り当て、その値に基づいて、ランタイム時にカードの動作、外観、または機能を動的に調整します。 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### メッセージの受信トレイ

コンテンツカードを使用してメッセージセンターをシミュレーションできます。この形式では、各メッセージはクリック時のイベントを動作させる[キーと値のペア]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs)を含む独自のカードです。これらのキーと値のペアは、ユーザーが受信トレイのメッセージをクリックしたときに、アプリケーションが行き先を決定する際に参照する重要な識別子です。キーと値のペアの値は任意です。 

以下は、2つのメッセージカードを作成するために使用できるダッシュボード構成例です。1つのメッセージは、的を絞った読書レコメンデーションをユーザーが受け取るためのプレファレンスを追加する行動喚起であり、もう1つは新規購読者のセグメントにクーポンコードを提供するものです。 

![]({% image_buster /assets/img/content_cards/content-card-message-inbox-with-kvps.png %}){: style="max-width:20%;float:right;margin-left:15px;border:0px;"}

読書レコメンデーションカードのキーと値のペアの例は次のとおりです。

- body: Politer Weekly のプロファイルに興味のある内容を追加して、個人的な読書レコメンデーションを手に入れましょう。
- style: info
- class_type: notification_center
- card_priority: 1

新規購読者のクーポンのキーと値のペアの例は次のとおりです。

- title:無制限のゲームに登録する
- body: 夏の終わりスペシャル - Politer ゲームが10%オフ
- buttonText: 今すぐ購読する
- style: promo
- class_type: notification_center
- card_priority: 2
- terms: new_subscribers_only

マーケターは、このコンテンツカードを一部の新規ユーザーにのみ提供することができます。 

それぞれの値を扱うことになります。`body`、`title`、`buttonText`などのキーは、マーケターが設定できる単純な文字列値を持つ場合があります。`terms`のようなキーは、法務部門が承認したフレーズの小さなコレクションを提供する値を持つ場合があります。アプリやサイトで`style`や`class_type`をどのようにレンダリングするかを決めることになります。 

{% details Android に関する詳細説明 %}

Android と FireOS SDK では、メッセージセンターのロジックは Braze のキーと値のペアが提供する`class_type`値によって駆動されます。[`createContentCardable`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide)メソッドを使用すると、これらのクラスタイプをフィルタリングして識別できます。

{% tabs %}
{% tab Kotlin %}
**クリック時の動作に `class_type` を使用する**<br>
コンテンツカードのデータをカスタムクラスにインフレートするときに、データの`ContentCardClass`プロパティを使用して、データの格納に使用する具象サブクラスを決定します。

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

次に、メッセージリストに対するユーザーの操作を処理するときに、メッセージのタイプを使用して、ユーザーに表示するビューを決定できます。

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**クリック時の動作に `class_type` を使用する**<br>
コンテンツカードのデータをカスタムクラスにインフレートするときに、データの`ContentCardClass`プロパティを使用して、データの格納に使用する具象サブクラスを決定します。

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

次に、メッセージリストに対するユーザーの操作を処理するときに、メッセージのタイプを使用して、ユーザーに表示するビューを決定できます。

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### カルーセル

コンテンツカードは、ユーザーが横にスワイプして追加の注目カードを表示するカルーセルフィードに設定できます。 

コンテンツカードカルーセルを作成するには、[コンテンツカードの変更]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed)を監視し、コンテンツカードの到着を処理するロジックを実装します。デフォルトでは、コンテンツカードは作成日順 (新しい順) にソートされ、対象となるすべてのカードが表示されます。クライアント側のロジックを実装して、カルーセル内の特定の数のカードをいつでも表示できます。

そうは言っても、さまざまな方法で追加の表示ロジックを注文して適用することができます。たとえば、配列から最初の5つのコンテンツカードオブジェクトを選択したり、キーと値のペアを導入して条件付きロジックを構築したりできます。

セカンダリコンテンツカードフィードとしてカルーセルを実装する場合は、[デフォルトのコンテンツカードフィードのカスタマイズ]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds)を参照して、キーと値のペアに基づいてカードを正しいフィードにソートする方法を確認してください。

### バナー

コンテンツカードは「カード」のように見せる必要はありません。たとえば、コンテンツカードは動的なバナーとして表示され、ホームページや指定ページの上部に永続的に表示されます。

これを実現するために、マーケターは**画像のみ**タイプのコンテンツカードでキャンペーンまたはキャンバスステップを作成します。次に、[コンテンツカードを補足コンテンツとして]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content)使用するのに適したキーと値のペアを設定します。


