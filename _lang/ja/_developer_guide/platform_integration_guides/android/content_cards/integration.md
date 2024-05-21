---
nav_title: 統合
article_title: Android と FireOS のコンテンツカード統合
page_order: 0
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、コンテンツカードの統合と、Android または FireOS アプリケーションで利用できるさまざまなデータモデルおよびカード固有プロパティについて説明します。"
channel:
  - content cards
search_rank: 1
---

# コンテンツカードの統合

> このリファレンス記事では、コンテンツカードの統合と、Android または FireOS アプリケーションで利用できるさまざまなデータモデルおよびカード固有プロパティについて説明します。

{% alert note %}
実装とカスタマイズを開始する準備ができたら、「[コンテンツカードのカスタマイズガイド]({{site.baseurl}}/developer_guide/customization_guides/content_cards)」を参照してください。
{% endalert %}

Android では、コンテンツカードフィードは Braze Android UI プロジェクトで使用可能な[フラグメント][2]として実装されます。アクティビティにフラグメントを追加する方法については、[Google のフラグメント][3]を参照してください。

この[`ContentCardsFragment`][4]クラスは、コンテンツカードの内容を自動的に更新して表示し、使用状況分析をログに記録します。ユーザーの`ContentCards` カードに表示できるカードは、Braze ダッシュボードで作成されます。

## コンテンツカードデータモデル{#card-types-for-android}

コンテンツカードデータモデルは、Android SDK で使用できます。コンテンツカードデータモデルの完全なリファレンスについては、[SDK リファレンスドキュメント][1]を参照してください。

Braze には、ベースモデルを共有する4つのユニークなコンテンツカードタイプがあります。これらは、[画像のみ][30]、[キャプション付き画像][31]、[クラシック (テキストアナウンス)、][32][クラシック (ショートニュース)][41]です。各型はベースモデルから共通のプロパティを継承し、以下の追加プロパティを持ちます。

カードデータの購読については、「[分析のロギング]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics)」を参照してください。

### ベースコンテンツカードモデルのプロパティ{#base-card-for-android}

[ベースカード][29]モデルは、すべてのカードの基本的な動作を規定します。  

|プロパティ | 説明 |
|---|---|
|`getId()` | Braze が設定したカードの ID を返します。|
|`getViewed()` | カードがユーザーによって読まれているか未読であるかを反映するブール値を返します。|
|`getExtras()` | このカードのキーと値のエクストラのマップを返します。|
|`getCreated()`  | Braze でのカードの作成時刻の UNIX タイムスタンプを返します。|
|`getIsPinned` | カードが固定されているかどうかを反映するブール値を返します。|
|`getOpenUriInWebView()`  | このカードの URI を Braze WebView で開くかどうかを反映する <br> ブール値を返します。|
|`getExpiredAt()` | カードの有効期限を取得します。|
|`getIsRemoved()` | エンドユーザーがこのカードを閉じたかどうかを反映するブール値を返します。|
|`getIsDismissible()`  | カードが固定されているかどうかを反映するブール値を返します。|
{: .reset-td-br-1 .reset-td-br-2}

### 画像のみの画像カードのプロパティ{#banner-image-card-for-android}

[画像のみのカード][30]はクリック可能なフルサイズの画像です。

|プロパティ | 説明 |
|---|---|
|`getImageUrl()` | カードの画像の URL を返します。|
|`getUrl()` | カードがクリックされた後に開かれる URL を返します。HTTP (S) URL でもプロトコル URL でもかまいません。|
|`getDomain()` | プロパティ URL のリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2}

### キャプション付き画像カードのプロパティ{#captioned-image-card-for-android}

[キャプション付き画像カード][31]はクリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ | 説明 |
|---|---|
|`getImageUrl()` | カードの画像の URL を返します。|
|`getTitle()` | カードのタイトルテキストを返します。|
|`getDescription()` | カードの本文テキストを返します。|
|`getUrl()` | カードがクリックされた後に開かれる URL を返します。HTTP (s) URL でもプロトコル URL でもかまいません。|
|`getDomain()` | プロパティ URL のリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2}

### クラシックカードのプロパティ{#text-Announcement-card-for-android}

画像が含まれていないクラシック カードは、[テキストアナウンス カード][32]になります。画像が含まれている場合は、[ショートニュースカード][41]を受け取ります。

|プロパティ | 説明 |
|---|---|
|`getTitle()` | カードのタイトルテキストを返します。|
|`getDescription()` | カードの本文を返します。|
|`getUrl()` | カードがクリックされた後に開かれる URL を返します。HTTP (s) URL でもプロトコル URL でもかまいません。|
|`getDomain()` | プロパティ URL のリンクテキストを返します。|
|`getImageUrl()` | カードの画像の URL を返します。クラシックショートニュースカードにのみ適用されます。|
{: .reset-td-br-1 .reset-td-br-2}

## カードメソッド

すべての[`Card`][1]データモデルオブジェクトは、ユーザーイベントを Braze サーバーに記録するための次の分析方法を提供します。

|メソッド | 説明 |
|---|---|
|`logImpression()` | 特定のカードのインプレッションを Braze に手動で記録します。|
|`logClick()` | 特定のカードのクリックを Braze に手動で記録します。|
|`setIsDismissed()` | 特定のカードの消去を手動で Braze に記録します。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。|
{: .reset-td-br-1 .reset-td-br-2}

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html
[2]: https://developer.android.com/guide/components/fragments.html
[3]: https://developer.android.com/guide/fragments#Adding "Android ドキュメント: フラグメント"
[4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[7]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html
[55]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-control.html
[57]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html#-1644350493%2FProperties%2F-1725759721
[29]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[30]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html
[31]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[32]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[41]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
