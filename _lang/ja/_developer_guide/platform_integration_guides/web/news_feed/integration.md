---
nav_title: 統合
article_title: ウェブ用ニュースフィードの統合
platform: Web
page_order: 0
page_type: reference
description: "この記事では、ニュースフィードカードの種類と、Braze SDKを介してニュースフィードをWebアプリケーションに統合する方法について説明する。"
channel: news feed

---

# ニュースフィード統合

> この記事では、Braze Web SDKのニュースフィードの設定方法について説明する。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

ニュースフィードは、ユーザー向けに完全にカスタマイズ可能なアプリ内コンテンツフィードである。当社のターゲティングとセグメンテーションにより、各ユーザーの興味に個別に対応したコンテンツのストリームを作成することができる。ユーザーのライフサイクルにおける位置づけやアプリの性質によって、これはオンボーディング・コンテンツ・サーバー、広告センター、アチーブメント・センター、あるいは一般的なニュース・センターとなる。

## ニュースフィードの例

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="ニュースフィードの例では、フォローリクエスト、更新通知、広告など、いくつかの通知が表示されている。" height="600" />

## 統合

ニュースフィードの表示をBraze Web SDKで切り替えるには、次のように呼び出すだけでよい：

``` javascript
braze.toggleFeed();
```

これにより、キャッシュされた最新のニュースフィードカードが表示され（これらのカードが1分以上古かったり、ニュースフィードが一度も更新されていない場合は、更新が開始される）、画面に表示されている限り、Brazeサーバーから新しいカードが受信されると自動的に表示が更新される。

デフォルトでは、フィードはウェブサイトの右側にある固定位置のサイドバーに表示される（または、レスポンシブCSSによって、モバイルデバイスではフルスクリーンのオーバーレイとして表示される）。この動作をオーバーライドし、独自の親要素内に静的に配置されたニュースフィードを表示したい場合は、`showFeed` の最初の引数として以下の要素を指定する：

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

特定のニュースフィードカードの静的なセットを表示したり、サーバーからカードをフィルタリングしたり、独自の更新セマンティクスを提供したい場合は、自動更新を無効にして独自のカードを提供することができる：

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

`showFeed` 、`destroyFeed` 、`toggleFeed` に関する完全なドキュメントは[JSDocsを][2]参照のこと。

## カードのタイプ

Braze Web SDKは、ベースモデルである[Cardを][1]共有する[ClassicCard][3]、[Banner][4]、[CaptionedImageの][5]3つのユニークなニュースフィードカードタイプをサポートしている。

### 未読カードのカウントを要求する

未読カードの数は、以下を呼び出していつでもリクエストできます。

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

これは、ニュースフィードの未読カードの数を示すバッジによく使われる。詳細は[JS Reference Docsを][17]参照のこと。Brazeは、フィードを表示するか、次の関数を呼び出すまで、新しいページのロード時にニュースフィードカードを更新しない（そのため、この関数は0を返す）ことに注意。 `braze.requestFeedRefresh();`

### キーと値のペア

オプションで、`Card` オブジェクトはキーと値のペアを `extras` として保持できます。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用します。これらの値にアクセスするには、`card.extras` 。

## カスタマイズ

BrazeのUI要素には、Brazeダッシュボード内のコンポーザーにマッチし、他のBrazeモバイルプラットフォームとの一貫性を目指したデフォルトのルック＆フィールが付属している。Brazeのデフォルトスタイルは、Braze SDK内のCSSで定義されている。アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準フィードをカスタマイズできます。

例えば、以下はニュースフィードの幅を800pxにするオーバーライドの例である：

``` css
body .ab-feed {
  width: 800px;
}
```

## カテゴリー

Braze ニュースフィードのインスタンスは、特定の「カテゴリ」からのカードのみを受信するように構成できます。これにより、1 つのアプリケーション内で複数のニュースフィードストリームを効果的に統合することができます。

ニュースフィードのカテゴリは、3番目の`allowedCategories` パラメータを`toggleFeed` に与えることで定義できる：

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

次の例のように、フィードにカテゴリーを組み合わせて入力することもできる：

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```

## 既読 / 未読インジケーター

Brazeは、ニュースフィードカードに以下の写真のように未読と既読を表示する：

![ニュースフィードのカードに、時計の画像とテキストが表示される。テキストの右上には、カードが読まれたかどうかを示す青かグレーの三角形がある。青い三角形は、カードが読まれたことを示す。][25]

### インジケーターを無効にする

この機能を無効にするには、CSSに以下のスタイルを追加する：

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

[1]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html
[2]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showfeed
[3]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html
[4]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html
[5]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html
[14]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[17]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html
[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}