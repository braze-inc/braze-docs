---
nav_title: HTML アプリ内メッセージs
article_title: カスタムHTMLアプリ内メッセージ
page_order: 0
page_type: reference
description: "この記事では、JavaScriptメソッド、ボタントラッキング、BrazeのインタラクティブHTMLプレビューの使用など、アプリ内メッセージのカスタムコードの概要を説明する。"
channel:
  - in-app messages
---

# カスタムの HTML アプリ内メッセージ{#custom-html-messages}

> 標準のアプリ内メッセージは様々な方法でカスタマイズできるが、HTML、CSS、JavaScriptを使ってデザイン・構築されたメッセージを使えば、キャンペーンのルック＆フィールをさらに自由にコントロールできる。簡単な構成で、あらゆるニーズに合ったカスタム機能とブランディングを実現できる。 

HTMLアプリ内メッセージでは、以下のようにメッセージのルック＆フィールをより自由にコントロールできる：

- カスタムフォントとカスタムスタイル
- ビデオ
- 複数の画像
- オン・クリック行動
- インタラクティブコンポーネント
- カスタム・アニメーション

カスタムHTMLメッセージは、[JavaScript Bridgeの](#javascript-bridge)メソッドを使って、イベントのログを取ったり、カスタム属性を設定したり、メッセージを閉じたりすることができる！HTML アプリ内メッセージの使用方法と、必要に応じてカスタマイズする方法の詳細手順、および開始に役立つ HTML5 アプリ内メッセージのテンプレートのセットについては、当社の [GitHub リポジトリ](https://github.com/braze-inc/in-app-message-templates) を参照してください。

{% alert note %}
Web SDK を介して HTML アプリ内メッセージを有効にするには、初期化オプション `allowUserSuppliedJavascript` を Braze に指定する必要があります。例: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由によるもので、HTML のアプリ内メッセージは JavaScript を実行できるため、サイト管理者が有効にする必要があります。
{% endalert %}

## JavaScriptブリッジ {#javascript-bridge}

Web、Android、iOS、およびSwift SDK用のHTMLアプリ内メッセージは、Braze SDKとインターフェースするためのJavaScript「ブリッジ」をサポートしており、ユーザーがリンクのある要素をクリックしたり、コンテンツに関与したりしたときに、Brazeのカスタムアクションをトリガーすることができる。これらの方法は、グローバル変数 `brazeBridge` または`appboyBridge` とともに存在します。

{% alert important %}
Brazeでは、グローバル変数`brazeBridge` の使用を推奨している。グローバル変数 `appboyBridge` は非推奨ですが、既存のユーザー向けに引き続き機能しています。`appboyBridge` を使用している場合は、`brazeBridge` に移行することをお勧めします。<br><br> `appboyBridge` は以下のSDKバージョンで非推奨となった：
- Web:[3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android :[14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS:[4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

例えば、カスタム属性とカスタムイベントを記録し、メッセージを閉じるには、HTMLアプリ内メッセージ内で以下のJavaScriptを使うことができる：

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close this in-app message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### JavaScriptブリッジ・メソッド {#bridge}

BrazeのHTMLアプリ内メッセージでは、以下のJavaScriptメソッドがサポートされている：

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Liquid を参照して<code>customAttributes</code> をJavaScript Bridge メソッドに挿入することはできません。
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## リンクベースのアクション

カスタムJavaScriptに加えて、Braze SDKは、これらの便利なURLショートカットで分析データを送信することもできる。これらのクエリーパラメーターとURLスキームは、すべて大文字と小文字を区別することに注意されたい。

### ボタンのクリックトラッキング（非推奨）

{% alert warning %}
`abButtonID` の使用は、[HTML with Preview]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) メッセージタイプではサポートされていません。詳細については、当社の[アップグレードガイド]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes)を参照してください。
{% endalert %}

アプリ内メッセージの分析用にボタンのクリックを記録するために、任意のディープリンク、リダイレクト URL、アンカー要素 `<a>` にクエリパラメータとして `abButtonId` を追加できます。「ボタン 1」のクリックを記録するには `?abButtonId=0`、「ボタン 2」のクリックを記録するには `?abButtonId=1` を使用します。

他のURLパラメータと同様に、最初のパラメータはクエスチョンマーク`?` で始め、それ以降のパラメータはアンパサンド`&` で区切る。

#### URLの例

- `https://example.com/?abButtonId=0` - ボタン 1 のクリック
- `https://example.com/?abButtonId=1` - ボタン 2 のクリック
- `https://example.com/?utm_source=braze&abButtonId=0` - 他の既存のURLパラメータでボタン1クリック
- `myApp://deep-link?page=home&abButtonId=1` - ボタン2クリックでモバイル・ディープリンク
- `<a href="https://example.com/?abButtonId=1">` - ボタン 2 のクリックが指定されたアンカー要素`<a>`

{% alert note %}
アプリ内メッセージはボタン1とボタン2のクリックのみをサポートする。これら2つのボタンIDのいずれかを指定しないURLは、一般的な「ボディクリック」として記録される。
{% endalert %}

### 新しいウィンドウでリンクを開く（モバイルのみ）

新しいウィンドウでアプリ外のリンクを開くには、`?abExternalOpen=true` を設定します。リンク先を開く前にメッセージが消える。

ディープリンクの場合、Brazeは`abExternalOpen` の値に関係なくURLを開く。

### ディープリンクとして開く（モバイルのみ）

HTTP または HTTPS のリンクをディープリンクとして Braze で処理するには、`?abDeepLink=true` を設定します。

このクエリ文字列パラメーターが存在しないか、`false` に設定されている場合、Braze はホストアプリ内の内部 Web ブラウザーで Web リンクを開こうとします。

### アプリ内メッセージを閉じる

アプリ内メッセージを閉じるには、`brazeBridge.closeMessage()` javascriptメソッドを使うことができる。

例えば、`<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` はアプリ内メッセージを閉じます。

## プレビュー付きHTMLアップロード

カスタムHTMLアプリ内メッセージを作成する際、Brazeで直接インタラクティブコンテンツをプレビューできる。 

エディターのメッセージ・プレビュー・パネルには、メッセージに含まれるJavaScriptをレンダリングするリアルなプレビューが表示される。プレビューパネルから、ページネーションをクリックしたり、フォームやアンケートを送信したり、JavaScriptアニメーションを見たりして、カスタムメッセージをプレビューし、やりとりすることができる！

![画面をスワイプしてHTML プレビューを操作する。]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
HTMLで使用している`brazeBridge` JavaScriptメソッドは、ダッシュボードでプレビューしている間はユーザー・プロフィールを更新しない。
{% endalert %}

### SDK 要件 {#supported-sdk-versions}

アプリ内メッセージの HTML プレビューを使用するには、以下のBraze SDK バージョン以降にアップグレードする必要があります。

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
このメッセージタイプは特定の SDK バージョン以降でしか受信できないため、サポートされていない SDK バージョンを使用しているユーザーはメッセージを受信しません。このメッセージタイプの採用は、ユーザーベースのかなりの部分が到達可能になってから検討するか、アプリのバージョンが要件より後のユーザーだけをターゲットにする。[「最新のアプリバージョンによるフィルター処理」]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)を参照してください。
{% endalert %}

### キャンペーンの作成{#instructions}

携帯アプリ ユーザーは、**カスタムコード**アプリ内メッセージを受信するために、サポートされているSDKにアップグレードする必要があります。新しいBraze SDKバージョンに依存するキャンペーンを開始する前に、モバイルアプリを[アップグレードするようユーザーに促す]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/)ことを推奨する。

#### 資産ファイル

HTMLアップロードでカスタムコードのアプリ内メッセージを作成する場合、キャンペーンアセットを[メディアライブラリに]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)アップロードし、メッセージ内で参照することができる。

アップロード可能なファイルタイプは以下の通りである：

| ファイルの種類        | ファイル拡張子                    |
| :--------------- | :-------------------------------- |
| フォントファイル       | `.ttf``.woff`,`.otf` 、 `.woff2` |
| SVG画像       | `.svg`                            |
| JavaScriptファイル | `.js`                             |
| CSSファイル        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Brazeは、2つの理由からメディアライブラリにアセットをアップロードすることを推奨している：

1. メディアライブラリ経由でキャンペーンに追加したアセットにより、ユーザーがオフラインの状態やインターネット接続が悪い状態でもメッセージを表示することができる。
2. Brazeにアップロードされたアセットは、キャンペーンをまたいで再利用できる。

##### アセットファイルを追加する

キャンペーンに新規または既存のアセットを追加できる。

キャンペーンに新しいアセットを追加するには、ドラッグ＆ドロップセクションを使ってファイルをアップロードする。このセクションで追加されたアセットも、メディアライブラリに自動的に追加される。メディアライブラリにアップロード済みのアセットを追加するには、[**メディアライブラリから追加**] を選択します。

アセットが追加されると、[**このキャンペーンのアセット**] セクションに表示されます。 

アセットのファイル名がローカルのHTMLアセットと一致する場合、自動的に置き換えられる（例えば、`cat.png` がアップロードされ、`<img src="cat.png" />` が存在する場合）。 

それ以外の場合は、リストからアセットにカーソルを合わせ、<i class="fas fa-copy"></i> **コピーを**選択して、ファイルのURLをクリップボードにコピーする。次に、コピーしたアセットのURLを、リモートアセットを参照するときに通常行うようにHTMLに貼り付ける。


### HTMLエディタ

HTMLに加えた変更は、入力と同時にプレビュー・パネルに自動的にレンダリングされる。HTMLで使用している[`brazeBridge` JavaScript](#bridge)メソッドは、ダッシュボードでプレビューしている間はユーザー・プロフィールを更新しない。

{% alert tip %}
HTMLエディタで<i class="fa-solid fa-magnifying-glass"></i>**検索**を選択してコード内で検索できます!
{% endalert %}

### ボタンの追跡{#button-tracking-improvements}

カスタム・コードのアプリ内メッセージでパフォーマンスを追跡するには [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)JavaScriptメソッドを使う。これにより、`brazeBridge.logClick('0')` 、`brazeBridge.logClick('1')` 、`brazeBridge.logClick()` を使用して、「ボタン 1」、「ボタン 2」、「本文クリック」をそれぞれプログラムで追跡できます。

| クリック数     | 方法                       |
| ---------- | ---------------------------- |
| ボタン1   | `brazeBridge.logClick('0')` |
| ボタン2   | `brazeBridge.logClick('1')` |
| 本文クリック | `brazeBridge.logClick()`    |
| カスタムボタンのトラッキング |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
このボタン追跡方法は、以前の自動クリック追跡方法 (`?abButtonId=0` など、現在は削除済み) に代わるものです。
{% endalert %}

インプレッションごとに複数のボタンクリックイベントを追跡できます。例えば、メッセージを閉じてボタン2のクリックを記録するには、以下のようにする：

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

また、新しいカスタムボタンの名前 (キャンペーンあたり一意の名前を最大 100 個) も追跡できます。`brazeBridge.logClick('blue button')`、`brazeBridge.logClick('viewed carousel page 3')` などがあります。

{% alert tip %}
`onclick` 属性内でJavaScript メソッドを使用する場合は、二重引用符で囲まれたHTML 属性との競合を避けるために、文字列値を一重引用符で囲みます。
{% endalert %}

#### 制限事項

- キャンペーンあたり最大 100 個の一意のボタン ID を設定できます。
- ボタン ID はそれぞれ最大 255文字です。
- ボタン ID には、英字、数字、スペース、ダッシュ、およびアンダースコアのみを使用できます。

### 後方互換性のない変更{#backward-incompatible-changes}

1. この新しいメッセージタイプで最も注目すべき互換性のない変更は、SDK 要件です。アプリの SDK が最小[SDK バージョン要件](#supported-sdk-versions) を満たしていないユーザーには、メッセージが表示されません。
<br>

2. これまでモバイルアプリでサポートされていた`braze://close` のディープリンクは廃止され、JavaScript`brazeBridge.closeMessage()` がサポートされるようになった。ウェブはディープリンクをサポートしていないので、これによってクロスプラットフォームのHTMLメッセージが可能になる。

3. ボタンIDに`?abButtonId=0` を使用していた自動クリックトラッキングと、閉じるボタンの「ボディクリック」トラッキングは削除された。以下のコード例は、新しいクリック・トラッキングJavaScriptメソッドを使用するためにHTMLを変更する方法を示している：

   | 前 | その後 |
   |:-------- |:------------|
   |<code>hra;lt"braze://close">閉じるボタン</a></code>|<code><a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">閉じるボタン</a></code>|
   |<code>hra;lt"braze://close?abButtonId=0">閉じるボタン</a></code>|<code><a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">閉じるボタン</a></code>|
   |<code>hra;lt"app://deeplink?abButtonId=0">トラックボタン1</a></code>|<code>hra="app://deeplink" onclick="brazeBridge.logClick('0')">トラックボタン1</a></code>|
   |<code><script><br>location.href = "braze://close?abButtonId=1"<br></script></code>|<code><script><br>window.addEventListener("ab.BridgeReady", function(){<br>  brazeBridge.logClick("1");<br>  brazeBridge.closeMessage();<br>});<br></script></code>|

