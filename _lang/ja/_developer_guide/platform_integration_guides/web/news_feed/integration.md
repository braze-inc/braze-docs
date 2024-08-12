---
nav_title: 統合
article_title: Web 向けニュースフィード統合
platform: Web
page_order: 0
page_type: reference
description: "この記事では、ニュース フィード カードの種類と、Braze SDK を介してニュース フィードを Web アプリケーションに統合する方法について説明します。"
channel: news feed

---

# ニュースフィード統合

> この記事では、Braze Web SDK のニュース フィードを設定する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

ニュース フィードは、ユーザー向けに完全にカスタマイズ可能なアプリ内コンテンツ フィードです。当社のターゲティングとセグメンテーションにより、各ユーザーの興味に合わせて個別にカスタマイズされたコンテンツのストリームを作成できます。ユーザーのライフサイクルにおける位置とアプリの性質に応じて、オンボーディング コンテンツ サーバー、広告センター、アチーブメント センター、または一般的なニュース センターになる場合があります。

## ニュースフィードの例

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="フォローリクエスト、更新通知、広告など、さまざまな通知を表示するニュースフィードの例。" height="600" />

## 統合

Braze Web SDK を通じてニュース フィードの表示を切り替えるには、以下を呼び出すだけです。

``` javascript
braze.toggleFeed();
```

これにより、最新のキャッシュされたニュース フィード カードが表示されます (これらのカードが 1 分以上古い場合、またはニュース フィードが一度も更新されていない場合は更新が開始されます)。また、画面に表示されている限り、Braze サーバーから新しいカードを受信すると、表示が自動的に更新されます。

デフォルトでは、フィードはウェブサイトの右側の固定位置のサイドバーに表示されます（または、レスポンシブ CSS を使用してモバイル デバイスで全画面オーバーレイとして表示されます）。この動作をオーバーライドして、独自の親要素内に静的に配置されたニュースフィードを表示したい場合は、次の要素を最初の引数として指定します。 `showFeed`:

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

特定の静的なニュース フィード カード セットを表示したり、サーバーからカードをフィルター処理したり、独自の更新セマンティクスを提供したりする場合は、自動更新を無効にして独自のカードを提供できます。

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

完全なドキュメントについては [JSDocsを][2] ご覧ください。 `showFeed`、 `destroyFeed`、 そして `toggleFeed`。

## カードのタイプ

Braze Web SDK は、基本モデル [Card][1]を共有する 3 つの独自のニュース フィード カード タイプ [ClassicCard][3]、[Banner][4]、[CaptionedImage][5] をサポートしています。

### 未読カード数をリクエスト

未読カードの数は、以下を呼び出していつでもリクエストできます。

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

これは、未読のニュース フィード カードの数を示すバッジを表示するためによく使用されます。詳細については、[JS リファレンス ドキュメントを][17] 参照してください。Brazeは、フィードを表示するか、を呼び出すまで、新しいページが読み込まれてもニュースフィードカードを更新しません（したがって、この関数は0を返します）。 `braze.requestFeedRefresh();`

### キーと値のペア

オプションで、`Card` オブジェクトはキーと値のペアを `extras` として保持できます。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用します。電話するだけ `card.extras` これらの値にアクセスします。

## カスタマイズ

Braze UI 要素には、Braze ダッシュボード内のコンポーザーに一致するデフォルトのルック アンド フィールが備わっており、他の Braze モバイル プラットフォームとの一貫性を目指しています。Braze のデフォルトのスタイルは、Braze SDK 内の CSS で定義されます。アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準フィードをカスタマイズできます。

たとえば、次のオーバーライドでは、ニュース フィードが 800 ピクセルの幅で表示されます。

``` css
body .ab-feed {
  width: 800px;
}
```

## カテゴリー

Braze ニュースフィードのインスタンスは、特定の「カテゴリ」からのカードのみを受信するように構成できます。これにより、1 つのアプリケーション内で複数のニュースフィードストリームを効果的に統合することができます。

ニュースフィードのカテゴリは、3番目の `allowedCategories` パラメータに `toggleFeed`:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

次の例のように、カテゴリの組み合わせでフィードを設定することもできます。

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```

## 既読 / 未読インジケーター

Braze は、下図のようにニュース フィード カードに未読と既読のインジケーターを表示します。

![時計の画像とテキストを表示するニュースフィードカード。テキストの右上隅には、カードが読み取られたかどうかを示す青または灰色の三角形があります。青い三角形はカードが読まれたことを示します。][25]

### インジケーターを無効にする

この機能を無効にするには、CSS に次のスタイルを追加します。

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