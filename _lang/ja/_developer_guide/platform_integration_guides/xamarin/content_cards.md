---
nav_title: コンテンツカードによって促進された
article_title: Xamarin用コンテンツカード
platform: 
  - Xamarin
  - iOS
  - Android
channel: content cards
page_order: 3
description: "このリファレンスでは、Xamarinプラットフォームにおけるコンテンツ・カードの実装ガイドラインについて説明する。"

---

# コンテンツカードの統合

> XamarinプラットフォームにiOS、Android、FireOSコンテンツカードをセットアップする方法を学ぶ。

Braze SDK には、コンテンツカードを使い始めるためのデフォルトのカードフィードが含まれています。Braze SDKに含まれるデフォルトのカードフィードは、ユーザーのコンテンツカードのすべてのアナリティクスのトラッキング、却下、レンダリングを処理する。

コンテンツカードをXamarinアプリに統合する方法については、[Android統合ガイドと][1] [iOS統合ガイドを][2]参照のこと。

## 前提条件

この機能を使用するには、[Xamarinプラットフォーム用のBraze SDKを統合する]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)必要がある。

## コンテンツ・カードのメソッド

以下の追加メソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

| 方法                                   | 説明                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Braze SDKサーバーから最新のコンテンツカードを要求する。                                           |
| `getContentCards()`                      | Braze SDKからコンテンツカードを取得する。これでサーバーから最新のカードリストが返される。 |
| `logContentCardClicked(cardId)`          | 指定されたコンテンツカードIDのクリックを記録する。この方法は、分析でのみ使用されます。                    |
| `logContentCardImpression(cardId)`       | 与えられたコンテンツカードIDのインプレッションを記録する。                                                      |
| `logContentCardDismissed(cardId)`        | 指定されたコンテンツカードIDの退会ログを記録する。                                                        |

## コンテンツカードデータモデル

Braze Xamarin SDKには、ベースモデルを共有する3つのユニークなコンテンツカードカードタイプがある：**バナー**、**キャプション付き画像**、**クラシック**。各タイプはベースモデルから共通のプロパティを継承し、次の追加プロパティを持ちます。

### ベースコンテンツカードモデルのプロパティ

|プロパティ           | 説明                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | ブレイズが設定したカードのID。                                                                                            |
|`created`          | Brazeからのカード作成時間のUNIXタイムスタンプ。                                                             |
|`expiresAt`        | カードの有効期限を示すUNIXタイムスタンプ。値が0より小さい場合は、カードの有効期限がないことを意味する。      |
|`viewed`           | カードがユーザーによって読まれているか読まれていないか。これはアナリティクスのログを記録しない。                                           |
|`clicked`          | カードがユーザーによってクリックされたかどうか。                                                                         |
|`pinned`           | カードが固定されているかどうか。                                                                                            |
|`dismissed`        | ユーザーがこのカードを退会したかどうか。すでに退場させられたカードに退場マークを付けることはできない。 |
|`dismissible`      | カードが使用者によって破棄可能かどうか。                                                                           |
|`urlString`        | (オプション) カードクリックアクションに関連付けられたurl文字列。                                                       |
|`openUrlInWebView` | このカードのURLをBrazeのWebViewで開くかどうか。                                                 |
|`isControlCard`    | このカードがコントロールカードであるかどうか。コントロールカードはユーザーに表示すべきではない。                                |
|`extras`           | このカードのキー・バリュー・エキストラのマップ。                                                                             |
|`isTest`           | このカードがテストカードかどうか。                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

ベースカードの完全なリファレンスは、[Androidと][3] [iOSの][4]ドキュメントを参照のこと。

### バナー・コンテンツ・カード・モデルのプロパティ

バナーカードはクリック可能なフルサイズの画像である。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | カードの画像のURL。                                                                                      |
|`imageAspectRatio` | カード画像のアスペクト比。これは、画像の読み込みが完了する前にヒントとして利用するためです。なお、状況によっては提供できない場合もある。 |
{: .reset-td-br-1 .reset-td-br-2}

バナーカードの完全なリファレンスは、[Androidと][5] [iOSの][6]ドキュメント（現在は画像のみに名称変更）を参照のこと。

### キャプション付き画像コンテンツカードモデルのプロパティ

キャプション付き画像カードはクリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | カードの画像のURL。                                                                                      |
|`imageAspectRatio` | カード画像のアスペクト比。これは、画像の読み込みが完了する前にヒントとして利用するためです。なお、状況によっては提供できない場合もある。 |
|`title`            | カードのタイトルテキスト。                                                                                      |
|`cardDescription`  | カードの説明テキスト。                                                                                |
|`domain`           | (オプ シ ョ ナル） プ ロパテ ィ URL の リ ン ク テキス ト 、 た と えば`"braze.com/resources/"` 。カードのUIに表示することで、カードをクリックしたときのアクション/方向を示すことができる。 |
{: .reset-td-br-1 .reset-td-br-2}

キャプション付き画像カードの完全なリファレンスについては、[Androidと][7] [iOSの][8]ドキュメントを参照のこと。

### クラシックコンテンツカードモデルのプロパティ

クラシックカードには、タイトル、説明、およびオプションの画像がテキストの左側に表示されます。

|プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (オプション）カードの画像のURL。                                                                           |
|`title`            | カードのタイトルテキスト。                                                                                      |
|`cardDescription`  | カードの説明テキスト。                                                                                |
|`domain`           | (オプ シ ョ ナル） プ ロパテ ィ URL の リ ン ク テキス ト 、 た と えば`"braze.com/resources/"` 。カードのUIに表示することで、カードをクリックしたときのアクション/方向を示すことができる。 |
{: .reset-td-br-1 .reset-td-br-2}

クラシックな（テキストアナウンスの）コンテンツカードの完全なリファレンスは、[Androidと][9] [iOSの][10]ドキュメントを参照のこと。クラシックな画像（短いニュース）カードの完全なリファレンスについては、[Androidと][11] [iOSの][12]ドキュメントを参照のこと。

## GIFサポート

{% multi_lang_include wrappers/gif_support/content_cards.md %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct
[5]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct
[7]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[8]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct
[9]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[10]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct
[11]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
[12]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct