---
nav_title: 統合
article_title: Android と FireOS のニュースフィード統合
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、さまざまなニュースフィードカードの種類、利用可能なカード固有のプロパティ、Android または FireOS アプリケーションのカスタム統合例について説明します。"
channel:
  - news feed
  
---

# ニュースフィード統合

> このリファレンス記事では、さまざまなニュースフィードカードの種類、利用可能なカード固有のプロパティ、Android または FireOS アプリケーションのカスタム統合例について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを利用しているお客様に、コンテンツカードのメッセージングチャネルへの移行をお勧めしています。移行により、柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

Android では、ニュースフィードは Braze Android UI プロジェクトで使用可能な[フラグメント][2]として実装されます。アクティビティにフラグメントを追加する方法については、[フラグメントに関する Google のドキュメント][2]を参照してください。

`BrazeFeedFragment` クラスは、ニュースフィードの内容を自動的に更新して表示し、使用状況分析をログに記録します。ユーザーのニュースフィードカードに表示できるカードは、Braze ダッシュボードで設定されます。

## カードのタイプ

Braze には、バナー画像、キャプション付き画像、テキストアナウンス、ショートニュースの 5 種類のユニークなカードタイプがあります。各タイプはベースモデルから共通のプロパティを継承し、次の追加プロパティを持ちます。

### ベースカードモデルのプロパティ

[ベースカード][29]モデルは、すべてのカードの基本的な動作を規定します。  

|プロパティ|説明|
|---|---|
| `getId()` | Braze が設定したカードの ID を返します。 |
| `getViewed()` | カードがユーザーによって読まれているか未読であるかを反映するブール値を返します。 |
| `getExtras()` | このカードのキーと値のエクストラのマップを返します。 |
| `setViewed(boolean)` ｜カードの閲覧済みフィールドを設定します。|
| `getCreated()` | Braze ダッシュボードでのカードの作成時刻の UNIX タイムスタンプを返します。 |
| `getUpdated()` | Braze ダッシュボードでのカードの最終更新時刻の UNIX タイムスタンプを返します。 |
| `getCategories()` | カードに割り当てられているカテゴリのリストを返します。カテゴリのないカードには `ABKCardCategoryNoCategory` が割り当てられます。 |
| `isInCategorySet(EnumSet)` | 指定されたカテゴリセットにカードが属している場合は true を返します。 |
{: .reset-td-br-1 .reset-td-br-2}

### バナー画像カードのプロパティ

[バナー画像カード][30]は、クリック可能なフルサイズの画像です。

|プロパティ|説明|
|---|---|
|`getImageUrl()` | カードの画像のURLを返します。|
|`getUrl()` | カードがクリックされた後に開かれる URL を返します。HTTP または HTTPS URL、あるいはプロトコル URL の場合もあります。|
| `getDomain()` | プロパティ URL のリンクテキストを返します。 |
{: .reset-td-br-1 .reset-td-br-2}

### キャプション付き画像カードのプロパティ

[キャプション付き画像カード][31]はクリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ|説明|
|---|---|
|`getImageUrl()` | カードの画像のURLを返します。|
|`getTitle()` | カードのタイトルテキストを返します。|
|`getDescription()` | カードの本文を返します。|
|`getUrl()` | カードがクリックされた後に開かれる URL を返します。 HTTP または HTTPS URL、あるいはプロトコル URL の場合もあります。|
|`getDomain()` ｜プロパティ URL のリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2}

### テキスト通知カード (画像なしのキャプション付き画像) のプロパティ

[テキスト通知カード][32]は、説明的なテキストを含んだクリック可能なカードです。

|プロパティ|説明|
|---|---|
|`getTitle()` | カードのタイトルテキストを返します。|
|`getDescription()` | カードの本文を返します。|
|`getUrl()` | カードがクリックされた後に開かれる URL を返します。HTTP または HTTPS URL、あるいはプロトコル URL の場合もあります。|
|`getDomain()` ｜プロパティ URL のリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2}

### ショートニュースカードのプロパティ

[ショートニュースカードは][33]、画像とそれに付随する説明文を含むクリック可能なカードです。

|プロパティ|説明|
|---|---|
|`getImageUrl()` | カードの画像のURLを返します。|
|`getTitle()` | カードのタイトルテキストを返します。|
|`getDescription()` | カードの本文を返します。|
|`getUrl()` | カードがクリックされた後に開かれる URL を返します。HTTP または HTTPS URL、あるいはプロトコル URL の場合もあります。|
|`getDomain()` ｜プロパティ URL のリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2}

## セッション分析

Android UI フラグメントでは、セッション分析は自動的に追跡されません。セッションが[正しく追跡][4]されるようにするには、アプリが開かれたときに `IBraze.openSession()` を呼び出します。

## リンク

アプリ内メッセージからニュースフィードへのリンクは、`AndroidManifest.xml` 内で`BrazeFeedActivity` を登録することで有効にする必要がある。

## カスタムフィードの統合

完全にカスタムの方法でフィードを表示するには、モデルからのデータが入力された独自のビューを使用ます。ニュースフィードモデルを取得するには、ニュースフィードの更新を配信登録し、結果のモデルデータを使用してビューを設定する必要があります。また、ユーザーがビューを操作する際に、モデルオブジェクトの分析をログに記録する必要もあります。

### パート 1:フィードの更新の配信登録

まず、カスタムフィードクラスでサブスクライバーを保持するプライベート変数を宣言します。

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

次に、通常はカスタムフィードアクティビティの `Activity.onCreate()` 内で、以下のコードを追加して、Braze のフィードドの更新を購読します。

\`\`\`java
// まず古いサブスクリプションを削除
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // FeedUpdatedEvent に含まれる Card オブジェクトのこのリストは、ニュースフィードビューにデータを挿入するために使用する必要があります。
    List<Card> cards = event.getFeedCards();
    // ここにロジックを挿入
  }
};
Braze.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// フィードデータの更新をリクエスト
Braze.getInstance(context).requestFeedRefresh();
\`\`\`

また、カスタムフィードアクティビティが表示されなくなったら、配信を停止することをお勧めします。アクティビティの `onDestroy()` ライフサイクルメソッドに次のコードを追加します。

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### パート 2:分析のログ記録

カスタムビューを使用する場合、分析は Braze ビューを使用する場合にのみ自動的に処理されるため、分析を手動でログに記録する必要があります。

フィードの表示をログに記録するには、[`Braze.logFeedDisplayed()`][6] を呼び出します。

インプレッションやカードのクリックをログに記録するには、それぞれ [`Card.logClick()`][7] または [`Card.logImpression()`][8] を呼び出します。

[2]: http://developer.android.com/guide/components/fragments.html
[3]: https://developer.android.com/guide/fragments#Adding "Android ドキュメント: フラグメント"
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html
[7]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/card_types/#card-types
[29]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[30]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html
[31]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[32]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[33]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
