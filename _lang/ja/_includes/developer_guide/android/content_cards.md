## 前提条件

Brazeコンテンツカードを使用する前に、アプリに[Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を統合する必要がある。ただし、追加の設定は不要だ。

## Googleの断片

Android では、コンテンツカードフィードは Braze Android UI プロジェクトで使用可能な[フラグメント](https://developer.android.com/guide/components/fragments.html)として実装されます。この[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)クラスは、コンテンツカードの内容を自動的に更新して表示し、使用状況分析をログに記録します。ユーザーの`ContentCards` カードに表示できるカードは、Braze ダッシュボードで作成されます。

アクティビティにフラグメントを追加する方法については、[Googleのフラグメントに関するドキュメントを](https://developer.android.com/guide/fragments#Adding)参照せよ。

## カードのタイプとプロパティ

コンテンツカードデータモデルはAndroid SDKで利用可能であり、以下の固有のコンテンツカードタイプを提供する。各タイプはベースモデルを共有している。これにより、独自のプロパティを持つことに加え、ベースモデルから共通のプロパティを継承できる。完全な参照ドキュメントについては、を参照せよ[`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)。

### 基本カードモデル {#base-card-for-android}

[ベースカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)モデルは、すべてのカードの基本的な動作を規定します。  

|プロパティ | 説明 |
|---|---|
|`getId()` | Brazeで設定されたカードのID を返します。|
|`getViewed()` | カードがユーザーによって既読か未読かを反映したブール値を返す。|
|`getExtras()` | このカードのキーと値の追加のマップを返します。|
|`getCreated()`  | カードの作成時刻をBrazeからunixタイムスタンプで返す。|
|`isPinned` | カードがピン留めされているかどうかを示すブール値を返す。|
|`getOpenUriInWebView()`  | このカードの Uris を開くべきかどうかを示すブール値を返す。 <br> Braze WebView で開くべきかどうか|
|`getExpiredAt()` | カードの有効期限を取得する。|
|`isRemoved()` | エンドユーザーがこのカードを退会したかどうかを示すブール値を返す。|
|`isDismissibleByUser()`  | そのカードがユーザーによって閉じられるかどうかを示すブール値を返す。|
|`isClicked()` | このカードのクリック状態を反映したブール値を返す。|
|`isDismissed` | カードが破棄されたかどうかを示すブール値を返す。カードを却下済みとしてマークするには、`true`に設定する。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。|
|`isControl()` | このカードがコントロールカードであり、描画されるべきでない場合、ブール値を返す。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 画像, 写真のみ {#banner-image-card-for-android}

[画像のみのカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)はクリック可能なフルサイズの画像です。

|プロパティ | 説明 |
|---|---|
|`getImageUrl()` | カードの画像のURLを返す。|
|`getUrl()` | カードがクリックされた後に開かれるURLを返す。HTTP (s) URL でもプロトコル URL でもかまいません。|
|`getDomain()` | プロパティ URL のリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### キャプション付き画像 {#captioned-image-card-for-android}

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
|`isDismissed` | カードが破棄されたかどうかを示すブール値を返す。カードを却下済みとしてマークするには、`true`に設定する。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## カードメソッド

すべての[`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)データモデルオブジェクトは、ユーザーイベントを Braze サーバーに記録するための次の分析方法を提供します。

|方法 | 説明 |
|---|---|
|`logImpression()` | 特定のカードのインプレッションを手動でBrazeに記録する。 |
|`logClick()` | 特定のカードのBrazeへのクリックを手動で記録する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
