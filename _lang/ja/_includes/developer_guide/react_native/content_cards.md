## Reactネイティブコンテンツカードについて

Braze SDK には、コンテンツカードを使い始めるためのデフォルトのカードフィードが含まれています。カードフィードを表示するには、`Braze.launchContentCards()` メソッドを使用できます。Braze SDK に含まれるデフォルトのカードフィードは、ユーザーのコンテンツカードの分析トラッキング、却下、レンダリングをすべて処理します。

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## カードの方法

独自の UI を構築するには、利用可能なカードのリストを取得し、カードの更新をリッスンすることができます。

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
カードを表示する独自の UIを構築することを選択した場合、それらのカードの分析を受け取るために `logContentCardImpression` を呼び出す必要があります。これには、`control` カードも含まれる。カードはユーザーに表示されないが、追跡されなければならない。
{% endalert %}

以下の追加メソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

| 方法                                   | 説明                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | コンテンツカードUI要素を起動する。                                                                 |
| `requestContentCardsRefresh()`           | Braze SDKサーバーから最新のコンテンツカードを要求する。結果として得られるカードのリストは、以前に登録された[コンテンツカードイベントの各リスナー](#reactnative_cards-methods)に渡されます。 |
| `getContentCards()`                      | Braze SDKからコンテンツカードを取得する。これは、サーバーからのカードの最新のリストで解決されるプロミスを返します。 |
| `getCachedContentCards()`                | キャッシュから最新のコンテンツカードの配列を返す。                                            |
| `logContentCardClicked(cardId)`          | 指定されたコンテンツカードIDのクリックを記録する。この方法は、分析でのみ使用されます。クリックアクションを実行するには、さらに `processContentCardClickAction(cardId)` を呼び出します。                                                        |
| `logContentCardImpression(cardId)`       | 与えられたコンテンツカードIDのインプレッションを記録する。                                                      |
| `logContentCardDismissed(cardId)`        | 指定されたコンテンツカード ID が閉じられたことを記録します。                                                        |
| `processContentCardClickAction(cardId)`  | 特定のカードのアクションを実行する。                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## カードの種類とプロパティ

コンテンツカードのデータモデルは、対応ネイティブSDKで使用でき、次のコンテンツカード型を提供します。[Image Only](#image-only)、[キャプションイメージ](#captioned-image)、および[クラシック](#classic)。また、特殊な[コントロール](#control) カード型もあります。これは、指定されたカードのユーザーs に返されます。各タイプは、固有のプロパティに加えて、基本モデルから共通のプロパティを継承します。

{% alert tip %}
コンテンツカードのデータモデルの完全なリファレンスについては、[[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)] および [[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard)] のドキュメントを参照してください。
{% endalert %}

### 基準カード型式

ベースカードモデルは、すべてのカードの基本的な動作を規定します。

|プロパティ      | 説明                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | Braze によって設定されたカードの ID。                                                                                            |
|`created`     | Brazeからのカード作成時間のUNIXタイムスタンプ。                                                             |
|`expiresAt`   | カードの有効期限を示すUNIXタイムスタンプ。値が0より小さい場合は、カードの有効期限がないことを意味する。      |
|`viewed`      | カードがユーザーによって読まれているか読まれていないか。これはアナリティクスのログを記録しない。                                           |
|`clicked`     | カードがユーザーによってクリックされたかどうか。                                                                         |
|`pinned`      | カードが固定されているかどうか。                                                                                            |
|`dismissed`   | ユーザーがこのカードを退会したかどうか。すでに閉じられたカードに閉じられたマークを付けることは、ノーオペになります。 |
|`dismissible` | ユーザーがカードを閉じられるかどうか。                                                                           |
|`url`         | (オプション) カードのクリックアクションに関連付けられたURL ストリング。                                                       |
|`openURLInWebView` | このカードのURL をBraze WebView で開封するかどうか。                                            |
|`isControl`   | このカードがコントロールカードかどうか。コントロールカードをユーザーに表示しないでください。                                |
|`extras`      | このカードのキー・バリュー・エキストラのマップ。                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ベースカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) および [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) のドキュメントを参照してください。

### 画像のみ

画像のみのカードはクリック可能なフルサイズの画像です。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | コンテンツカードの種類、`IMAGE_ONLY`                                                                              |
|`image`            | カードの画像のURL。                                                                                      |
|`imageAspectRatio` | カード画像のアスペクト比。これは、画像の読み込みが完了する前にヒントとして利用するためです。特定の状況ではプロパティが提供されない場合があることに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

画像のみのカードの完全なリファレンスについては、[[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)] および [[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct)] のドキュメントを参照してください。

### キャプション付き画像

キャプション付き画像カードはクリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | コンテンツカードの種類、`CAPTIONED`                                                                               |
|`image`            | カードの画像のURL。                                                                                      |
|`imageAspectRatio` | カード画像のアスペクト比。これは、画像の読み込みが完了する前にヒントとして利用するためです。特定の状況ではプロパティが提供されない場合があることに注意してください。 |
|`title`            | カードのタイトルテキスト。                                                                                      |
|`cardDescription`  | カードの説明テキスト。                                                                                |
|`domain`           | (オプ シ ョ ナル） プ ロパテ ィ URL の リ ン ク テキス ト 、 た と えば`"braze.com/resources/"` 。カードの UI に表示され、カードをクリックした時の動作/方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

キャプション付き画像カードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) および [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) のドキュメントを参照してください。

### クラシック

クラシックカードには、タイトル、説明、およびオプションの画像がテキストの左側に表示されます。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | コンテンツカードの種類、`CLASSIC`                                                                                 |
|`image`            | (オプション）カードの画像のURL。                                                                           |
|`title`            | カードのタイトルテキスト。                                                                                      |
|`cardDescription`  | カードの説明テキスト。                                                                                |
|`domain`           | (オプ シ ョ ナル） プ ロパテ ィ URL の リ ン ク テキス ト 、 た と えば`"braze.com/resources/"` 。カードの UI に表示され、カードをクリックした時の動作/方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

クラシック (テキストアナウンス) コンテンツカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) および [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) のドキュメントを参照してください。従来の"画像(短報)カードについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct)ドキュメントを参照してください。

### コントロール

コントロールカードには、基本プロパティがすべて含まれていますが、いくつかの重要な違いがあります。最も重要な点:

- `isControl` プロパティは`true` であることが保証されている。
- `extras` プロパティは空であることが保証されます。

コントロールカードの完全なリファレンスについては、[[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html)] および [[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct)] のドキュメントを参照してください。
