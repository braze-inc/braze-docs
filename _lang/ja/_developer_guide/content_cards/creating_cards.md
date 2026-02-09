---
nav_title: カードの作成
article_title: コンテンツカードの作成
page_order: 0
description: "この記事では、カスタムコンテンツカードUI を作成するコンポーネントについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# コンテンツカードの作成

> この記事では、カスタムコンテンツカードを実装するときに使用する基本的なアプローチと、3 つの一般的なユースケースについて説明します。コンテンツ・カードのカスタマイズ・ガイドの他の記事をすでに読んで、デフォルトでできることと、カスタム・コードが必要なことを理解していることを前提としている。特に、カスタムコンテンツカードの[アナリティクスを記録]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)する方法を理解すると役立ちます。 

{% multi_lang_include banners/content_card_alert.md %}

## カードを作成する

### ステップ1:カスタム UI を作成する 

{% tabs local %}
{% tab web %}

まず、カードのレンダリングに使用するカスタム HTML コンポーネントを作成します。 

{% endtab %}
{% tab android %}

まず、独自のカスタムフラグメントを作成します。デフォルトの[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)は、デフォルトのコンテンツカードタイプのみに対応するよう設計されていますが、良い出発点です。

{% endtab %}
{% tab swift %}

まず、独自のカスタムビューコントローラーコンポーネントを作成します。デフォルトの[`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller)は、デフォルトのコンテンツカードタイプのみに対応するよう設計されていますが、良い出発点です。

{% endtab %}
{% endtabs %}

### ステップ 2:カードの更新情報を購読する

次に、カードの更新時に[データ更新を購読]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates)するコールバック関数を登録します。 

### ステップ3: 分析を実装する

コンテンツカードのインプレッション数、クリック数、却下数は、カスタムビューに自動的に記録されません。すべての指標が Braze ダッシュボードの分析に適切に記録されるように、[それぞれのメソッドを実装]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events)する必要があります。

### ステップ4:カードのテスト (オプション)

コンテンツカードをテストするには:

1. [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) メソッドを呼び出して、アプリケーションでアクティブなユーザーを設定します。
2. Braze で、[**キャンペーン**] に移動し、[新しいコンテンツカードキャンペーンを作成します]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create)。
3. キャンペーンで、[**テスト**] を選択し、テストユーザーの `user-id` を入力します。準備ができたら、[**テストを送信**] を選択します。すぐにデバイスでコンテンツカードを起動できます。

![Brazeのコンテンツカードキャンペーンでは、自分のユーザーIDをテスト受信者として追加し、コンテンツカードをテストすることができる。]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## コンテンツカードの配置

コンテンツカードはさまざまな方法で使用できます。3つの一般的な実装は、それらをメッセージセンター、動的画像広告、または画像カルーセルとして使用することである。これらの配置ごとに、[キーと値のペア]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (データモデルの`extras`プロパティ) をコンテンツカードに割り当て、その値に基づいて、ランタイム時にカードの動作、外観、または機能を動的に調整します。 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### メッセージの受信トレイ

コンテンツカードを使用してメッセージセンターをシミュレーションできます。この形式では、各メッセージはクリック時のイベントを動作させる[キーと値のペア]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs)を含む独自のカードです。これらのキーと値のペアは、ユーザーが受信トレイのメッセージをクリックしたときに、アプリケーションが行き先を決定する際に参照する重要な識別子です。キーと値のペアの値は任意です。 

#### 例

たとえば、ユーザーがおすすめを有効にするためのコールトゥアクションと、新しいサブスクライバセグメントに付与されるクーポンコードという 2 つのメッセージカードを作成できます。

`body`、`title`、`buttonText`などのキーは、マーケターが設定できる単純な文字列値を持つ場合があります。`terms`のようなキーは、法務部門が承認したフレーズの小さなコレクションを提供する値を持つ場合があります。`style` や`class_type` などのキーには、アプリやサイトでのカードのレンダリング方法を決定するために設定できる文字列値があります。

{% tabs local %}
{% tab Reading recommendations %}
読み取り推奨カードのキーと値のペア:

| キー         | 値                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Politer Weekly のプロファイルに興味のある内容を追加して、個人的な読書レコメンデーションを手に入れましょう。 |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab New subscriber coupon %}
新しいサブスクライバクーポンのキーと値のペア:

| キー         | 値                                                            |
|------------|------------------------------------------------------------------|
| `title`      | 無制限のゲームに登録する                                    |
| `body`       | 夏の終わりスペシャル - Politer ゲームが10%オフ              |
| `buttonText` | 今すぐ購読する                                                    |
| `style`      | プロモーション                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Additional information for Android %}

Android と FireOS SDK では、メッセージセンターのロジックは Braze のキーと値のペアが提供する`class_type`値によって駆動されます。[`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards/)メソッドを使用すると、これらのクラスタイプをフィルタリングして識別できます。

{% tabs local %}
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

フルカスタムのカルーセルフィードでコンテンツカードを設定できます。これにより、ユーザーは追加の機能付きカードをスワイプして表示できます。デフォルトでは、コンテンツカードは作成された日付(最新のもの)でソートされ、ユーザーには対象となるすべてのカードが表示されます。

コンテンツカードカローセルを実装するには:

1. [コンテンツカードの変更]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed)を監視し、コンテンツカードの到着を処理するカスタムロジックを作成します。
2. カスタムクライアント側ロジックを作成して、カルーセル内の特定の数のカードを一度に表示します。たとえば、配列から最初の5つのコンテンツカードオブジェクトを選択したり、キーと値のペアを導入して条件付きロジックを構築したりできます。

{% alert tip %}
カルーセルをセカンダリコンテンツカードフィードとして実装する場合は、[ キーと値のペア]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) を使用してカードを正しいフィードにソートします。
{% endalert %}

### 画像のみ

コンテンツカードは「カード」のように見せる必要はありません。たとえば、コンテンツカードは、ホームページまたは指定されたページの上部に永続的に表示される動的イメージとして表示できます。

これを実現するために、マーケターは**画像のみ**タイプのコンテンツカードでキャンペーンまたはキャンバスステップを作成します。次に、[コンテンツカードを補足コンテンツとして]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content)使用するのに適したキーと値のペアを設定します。
