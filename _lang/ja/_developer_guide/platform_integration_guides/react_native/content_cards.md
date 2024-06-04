---
nav_title: コンテンツカード
article_title: React Native 用コンテンツカード
platform: React Native
page_order: 3
page_type: reference
description: "この記事では、React Native アプリ用のコンテンツカードの使用を開始する方法について説明します。"
channel: content cards

---

# コンテンツカードの統合

> この記事では、React Native 用のコンテンツカードを設定する方法について説明します。

Braze SDK には、コンテンツカードを使い始めるためのデフォルトのカードフィードが含まれています。カードフィードを表示するには、`Braze.launchContentCards()` メソッドを使用できます。Braze SDK に含まれるデフォルトのカードフィードは、ユーザーのコンテンツカードの分析トラッキング、却下、レンダリングをすべて処理します。

## カスタマイズ

独自の UI を構築するには、利用可能なカードのリストを取得し、カードの更新をリッスンすることができます。

\`\`\`javascript
// 初期カードを設定する
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`、またはタイムアウト期間の後に
Braze.addListener(Braze.Events.CONTENT\_CARDS\_UPDATED, async (update) => {
setCards(update.cards);
    });

// カードの更新を手動でトリガーする
Braze.requestContentCardsRefresh();
\`\`\`

{% alert important %}
カードを表示する独自の UIを構築することを選択した場合、それらのカードの分析を受け取るために `logContentCardImpression` を呼び出す必要があります。
{% endalert %}

以下の追加メソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

| Method                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | コンテンツカード UI要素を起動します。                                                                 |
| `requestContentCardsRefresh()`           | Braze SDK サーバーに最新のコンテンツカードを要求します。                                           |
| `getContentCards()`                      | Braze SDK からコンテンツカードを取得します。サーバーからカードの最新リストを返します。|
| `getCachedContentCards()`                | キャッシュから最新のコンテンツカード配列を返します。                                            |
| `logContentCardClicked(cardId)`          | 指定されたコンテンツカード ID のクリックを記録します。この方法は、分析でのみ使用されます。クリックアクションを実行するには、さらに `processContentCardClickAction(cardId)` を呼び出します。                                                        |
| `logContentCardImpression(cardId)`       | 指定されたコンテンツカード ID のインプレッションを記録します。                                                      |
| `logContentCardDismissed(cardId)`        | 指定されたコンテンツカード ID が閉じられたことを記録します。                                                        |
| `processContentCardClickAction(cardId)`  | 特定のカードのアクションを実行します。                                                               |
{: .reset-td-br-1 .reset-td-br-2}

## コンテンツカードのサンプル表示のテスト

コンテンツカードのサンプルをテストする手順は、次のとおりです。

1. [`Braze.changeUser('your-user-id')`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. [**キャンペーン**] に移動し、[このガイド][4]に従って新しいコンテンツカードキャンペーンを作成します。
3. コンテンツカードのテストキャンペーンを作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。まもなくデバイスでコンテンツカードを起動できるようになります。

![コンテンツカードをテストするために、テスト受信者として自分のユーザー ID を追加できることを示す Braze コンテンツカードキャンペーン。][5]

その他の統合については、プラットフォームに応じて、[Android 統合手順][2]または、[iOS 統合手順][3]に従ってください。

これのサンプル実装は、[React Native SDK][1] 内のBrazeProject にあります。

## コンテンツカードデータモデル

コンテンツカードのデータモデルは、React Native SDK で利用できます。コンテンツカードのデータモデルの完全なリファレンスについては、[Android][6] および [iOS][7] のドキュメントを参照してください。

Braze React Native SDK には、**画像のみ**、**キャプション付き画像**、**クラシック**という、ベースモデルを共有する3種類のユニークなコンテンツカードのカードがあります。各型はベースモデルから共通のプロパティを継承し、以下の追加プロパティを持ちます。

### ベースコンテンツカードモデルのプロパティ

ベースカードモデルは、すべてのカードの基本的な動作を規定します。

|プロパティ      | 説明                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`| Braze によって設定されたカードの ID。|
|`created`     | Braze でのカードの作成時刻の UNIX タイムスタンプ。                                                             |
|`expiresAt` | カードの有効期限の UNIX タイムスタンプ。値が0未満の場合、カードが期限切れにならないことを意味します。|
|`viewed`| ユーザーがカードを読んだか、それとも未読か分析は記録されません。                                           |
|`clicked`| ユーザーがカードをクリックしたかどうか。                                                                         |
|`pinned`| カードがピン留めされているかどうか。|
|`dismissed`| ユーザーがこのカードを閉じたかかどうか。すでに閉じられたカードに閉じられたマークを付けることは、ノーオペになります。|
|`dismissible`| ユーザーがカードを閉じられるかどうか。|
|`url` | (オプション) カードクリックアクションに関連付けられた URL 文字列。 |
|`openURLInWebView` | このカードの URL を Braze の WebView で開くべきかどうか。|
|`isControl` | このカードがコントロールカードかどうか。コントロールカードをユーザーに表示しないでください。|
|`extras`| このカードのキーと値のエクストラのマップ。|
{: .reset-td-br-1 .reset-td-br-2}

ベースカードの完全なリファレンスについては、[Android][8] および [iOS][9] のドキュメントを参照してください。

### 画像のみコンテンツカードモデルのプロパティ

画像のみのカードはクリック可能なフルサイズの画像です。

|プロパティ| 説明|
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`| コンテンツカードの種類、`IMAGE_ONLY`。|
|`image`| カードの画像の URL。|
|`imageAspectRatio`| カードの画像のアスペクト比。これは、画像の読み込みが完了する前にヒントとして利用するためです。特定の状況ではプロパティが提供されない場合があることに注意してください。|
{: .reset-td-br-1 .reset-td-br-2}

画像のみのカードの完全なリファレンスについては、[Android][10] および [iOS][11] のドキュメントを参照してください。

### キャプション付き画像コンテンツカードモデルのプロパティ

キャプション付き画像カードはクリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ| 説明|
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`|コンテンツカードの種類、`CAPTIONED`。|
|`image`| カードの画像の URL。|
|`imageAspectRatio`| カードの画像のアスペクト比。これは、画像の読み込みが完了する前にヒントとして利用するためです。特定の状況ではプロパティが提供されない場合があることに注意してください。|
|`title`|カードのタイトルテキスト。|
|`cardDescription`|カードの説明テキスト。|
|`domain` | (オプション) プロパティ URL のリンクテキスト (例：`"braze.com/resources/"`)。カードの UI に表示され、カードをクリックした時の動作/方向を示すことができます。|
{: .reset-td-br-1 .reset-td-br-2}

キャプション付き画像カードの完全なリファレンスについては、[Android][12] および [iOS][13] のドキュメントを参照してください。

### クラシックコンテンツカードモデルのプロパティ

クラシックカードには、タイトル、説明、およびオプションの画像がテキストの左側に表示されます。

|プロパティ| 説明|
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`|コンテンツカードの種類、`CLASSIC`。|
|`image` | (オプション) カードの画像のURL。 |
|`title`|カードのタイトルテキスト。|
|`cardDescription`|カードの説明テキスト。|
|`domain` | (オプション) プロパティ URL のリンクテキスト (例：`"braze.com/resources/"`)。カードの UI に表示され、カードをクリックした時の動作/方向を示すことができます。|
{: .reset-td-br-1 .reset-td-br-2}

クラシック (テキストアナウンス) コンテンツカードの完全なリファレンスについては、[Android][14] および [iOS][15] のドキュメントを参照してください。クラシック画像 (ショートニュース) カードの完全なリファレンスについては、[Android][16] および [iOS][17] のドキュメントを参照してください。

[1]: https://github.com/braze-inc/braze-react-native-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[3]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[5]: {% image_buster /assets/img/react-native/content-card-test.png %} 「コンテンツカードキャンペーンテスト」
[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html
[7]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[9]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct
[10]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html
[11]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct
[12]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[13]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct
[14]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[15]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct
[16]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
[17]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct
