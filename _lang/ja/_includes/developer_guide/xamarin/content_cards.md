## .NET MAUI コンテンツカードについて

Braze .NET MAUI (旧Xamarin) SDKには、コンテンツカードの使用を開始するためのデフォルト カード フィードが含まれています。Braze SDKに含まれるデフォルトのカードフィードは、ユーザーのコンテンツカードのすべてのアナリティクスのトラッキング、却下、レンダリングを処理する。

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## カードの種類とプロパティ

Braze .NET MAUI SDKには、基本モデルを共有する3 つの一意のコンテンツカードs カードタイプがあります。[バナー](#xamarin_banner)、[キャプションイメージ](#xamarin_captioned-image)、および[クラシック](#xamarin_classic)。各タイプはベースモデルから共通のプロパティを継承し、次の追加プロパティを持ちます。

### 基準カード型式

|プロパティ           | 説明                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | Braze によって設定されたカードの ID。                                                                                            |
|`created`          | Brazeからのカード作成時間のUNIXタイムスタンプ。                                                             |
|`expiresAt`        | カードの有効期限を示すUNIXタイムスタンプ。値が0より小さい場合は、カードの有効期限がないことを意味する。      |
|`viewed`           | カードがユーザーによって読まれているか読まれていないか。これはアナリティクスのログを記録しない。                                           |
|`clicked`          | カードがユーザーによってクリックされたかどうか。                                                                         |
|`pinned`           | カードが固定されているかどうか。                                                                                            |
|`dismissed`        | ユーザーがこのカードを退会したかどうか。すでに閉じられたカードに閉じられたマークを付けることは、ノーオペになります。 |
|`dismissible`      | ユーザーがカードを閉じられるかどうか。                                                                           |
|`urlString`        | (オプション) カードのクリックアクションに関連付けられたURL ストリング。                                                       |
|`openUrlInWebView` | このカードのURL をBraze WebView で開封するかどうか。                                                 |
|`isControlCard`    | このカードがコントロールカードかどうか。コントロールカードをユーザーに表示しないでください。                                |
|`extras`           | このカードのキー・バリュー・エキストラのマップ。                                                                             |
|`isTest`           | このカードがテストカードかどうか。                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ベースカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) および [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) のドキュメントを参照してください。

### バナー

バナーカードはクリック可能なフルサイズの画像である。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | カードの画像のURL。                                                                                      |
|`imageAspectRatio` | カード画像のアスペクト比。これは、画像の読み込みが完了する前にヒントとして利用するためです。特定の状況ではプロパティが提供されない場合があることに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

バナーカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) および [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) のドキュメント (現在は画像のみに名称変更) を参照してください。

### キャプション付き画像

キャプション付き画像カードはクリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
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
|`image`            | (オプション）カードの画像のURL。                                                                           |
|`title`            | カードのタイトルテキスト。                                                                                      |
|`cardDescription`  | カードの説明テキスト。                                                                                |
|`domain`           | (オプ シ ョ ナル） プ ロパテ ィ URL の リ ン ク テキス ト 、 た と えば`"braze.com/resources/"` 。カードの UI に表示され、カードをクリックした時の動作/方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

クラシック (テキストアナウンス) コンテンツカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) および [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) のドキュメントを参照してください。クラシック画像 (ショートニュース) カードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) および [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) のドキュメントを参照してください。

## カードメソッド

以下の追加メソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

| 方法                                   | 説明                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Braze SDKサーバーから最新のコンテンツカードを要求する。                                           |
| `getContentCards()`                      | Braze SDKからコンテンツカードを取得する。これでサーバーから最新のカードリストが返される。 |
| `logContentCardClicked(cardId)`          | 指定されたコンテンツカードIDのクリックを記録する。この方法は、分析でのみ使用されます。                    |
| `logContentCardImpression(cardId)`       | 与えられたコンテンツカードIDのインプレッションを記録する。                                                      |
| `logContentCardDismissed(cardId)`        | 指定されたコンテンツカード ID が閉じられたことを記録します。                                                        |
