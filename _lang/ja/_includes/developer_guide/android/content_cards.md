## 前提条件

ろう付けコンテンツカードを使用する前に、[Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) をアプリに統合する必要があります。ただし、追加のセットアップは必要ありません。

## Googleフラグメント

Android では、コンテンツカードフィードは Braze Android UI プロジェクトで使用可能な[フラグメント](https://developer.android.com/guide/components/fragments.html)として実装されます。この[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)クラスは、コンテンツカードの内容を自動的に更新して表示し、使用状況分析をログに記録します。ユーザーの`ContentCards` カードに表示できるカードは、Braze ダッシュボードで作成されます。

アクティビティにフラグメントを追加する方法については、[Googleのフラグメントドキュメント](https://developer.android.com/guide/fragments#Adding "Androidドキュメント:フラグメント")を参照してください。

## カードの種類とプロパティ

コンテンツカードデータモデルはAndroid SDK で利用でき、以下のユニークなコンテンツカードタイプを提供します。各タイプは基本モデルを共有しており、基本モデルから共通のプロパティを継承するだけでなく、独自の固有のプロパティも持つことができます。完全なリファレンスドキュメントについては、[`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) を参照してください。

### ベースカードモデル {#base-card-for-android}

[ベースカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)モデルは、すべてのカードの基本的な動作を規定します。  

|プロパティ | 説明 |
|---|---|
|`getId()` | Brazeで設定されたカードのID を返します。|
|`getViewed()` | カードがユーザーによって既読か未読かを反映したブール値を返す。|
|`getExtras()` | このカードのキーと値の追加のマップを返します。|
|`getCreated()`  | カードの作成時刻をBrazeからunixタイムスタンプで返す。|
|`getIsPinned` | カードがピン留めされているかどうかを示すブール値を返す。|
|`getOpenUriInWebView()`  | このカードの Uris を開くべきかどうかを示すブール値を返す。 <br> Braze WebView で開くべきかどうか|
|`getExpiredAt()` | カードの有効期限を取得する。|
|`getIsRemoved()` | エンドユーザーがこのカードを退会したかどうかを示すブール値を返す。|
|`getIsDismissible()`  | カードがピン留めされているかどうかを示すブール値を返す。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 画像のみ {#banner-image-card-for-android}

[画像のみのカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)はクリック可能なフルサイズの画像です。

|プロパティ | 説明 |
|---|---|
|`getImageUrl()` | カードの画像のURLを返す。|
|`getUrl()` | カードがクリックされた後に開かれるURLを返す。HTTP (s) URL でもプロトコル URL でもかまいません。|
|`getDomain()` | プロパティ URL のリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### キャプション画像 {#captioned-image-card-for-android}

[キャプション付き画像カード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)はクリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ | 説明 |
|---|---|
|`getImageUrl()` | カードの画像のURLを返す。|
|`getTitle()` | カードのタイトルテキストを返します。|
|`getDescription()` | カードの本文を返します。|
|`getUrl()` | カードがクリックされた後に開かれるURLを返す。HTTP (s) URL でもプロトコル URL でもかまいません。|
|`getDomain()` | プロパティ URL のリンクテキストを返す。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### クラシック {#text-Announcement-card-for-android}

画像が含まれていないクラシック カードは、[テキストアナウンス カード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html)になります。画像が含まれている場合は、[ショートニュースカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)を受け取ります。

|プロパティ | 説明 |
|---|---|
|`getTitle()` | カードのタイトルテキストを返します。 |
|`getDescription()` | カードの本文を返します。 |
|`getUrl()` | カードがクリックされた後に開かれるURLを返す。HTTP (s) URL でもプロトコル URL でもかまいません。 | 
|`getDomain()` | プロパティ URL のリンクテキストを返す。 |
|`getImageUrl()` | カードの画像の URL を返します。クラシックショートニュースカードにのみ適用されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## カードメソッド

すべての[`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)データモデルオブジェクトは、ユーザーイベントを Braze サーバーに記録するための次の分析方法を提供します。

|方法 | 説明 |
|---|---|
|`logImpression()` | 特定のカードのインプレッションを手動でBrazeに記録する。 |
|`logClick()` | 特定のカードのBrazeへのクリックを手動で記録する。 |
|`setIsDismissed()` | 特定のカードの消去を手動で Braze に記録します。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
