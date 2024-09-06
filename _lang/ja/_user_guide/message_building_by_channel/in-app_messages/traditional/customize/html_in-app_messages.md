---
nav_title: HTMLアプリ内メッセージ
article_title: カスタムHTMLアプリ内メッセージ
page_order: 0
page_type: reference
description: "この記事では、JavaScriptメソッド、ボタントラッキング、BrazeのインタラクティブHTMLプレビューの使用など、アプリ内メッセージのカスタムコードの概要を説明する。"
channel:
  - in-app messages
---

# カスタムHTMLアプリ内メッセージ {#custom-html-messages}

> 標準のアプリ内メッセージは様々な方法でカスタマイズできるが、HTML、CSS、JavaScriptを使ってデザイン・構築されたメッセージを使えば、キャンペーンのルック＆フィールをさらに自由にコントロールできる。簡単な構成で、あらゆるニーズに合ったカスタム機能とブランディングを実現できる。 

HTMLアプリ内メッセージでは、以下のようにメッセージのルック＆フィールをより自由にコントロールできる：

- カスタムフォントとカスタムスタイル
- ビデオ
- 複数の画像
- オン・クリック行動
- インタラクティブ・コンポーネント
- カスタム・アニメーション

カスタムHTMLメッセージは、[JavaScript Bridgeの](#javascript-bridge)メソッドを使って、イベントのログを取ったり、カスタム属性を設定したり、メッセージを閉じたりすることができる！[GitHubのリポジトリには][2]、HTMLアプリ内メッセージの使い方やカスタマイズ方法、HTML5アプリ内メッセージのテンプレートなどが詳しく説明されている。

{% alert note %}
Web SDKでHTMLアプリ内メッセージを有効にするには、Brazeに`allowUserSuppliedJavascript` の初期化オプションを指定する必要がある：例えば`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})` 。HTMLのアプリ内メッセージはJavaScriptを実行することができるため、セキュリティ上の理由から、サイト管理者に有効にしてもらう必要がある。
{% endalert %}

## JavaScriptブリッジ {#javascript-bridge}

Web、Android、iOS、およびSwift SDK用のHTMLアプリ内メッセージは、Braze SDKとインターフェースするためのJavaScript「ブリッジ」をサポートしており、ユーザーがリンクのある要素をクリックしたり、コンテンツに関与したりしたときに、Brazeのカスタムアクションをトリガーすることができる。これらのメソッドは、グローバル変数`brazeBridge` または`appboyBridge` 。

{% alert important %}
Brazeでは、グローバル変数`brazeBridge` の使用を推奨している。グローバル変数`appboyBridge` は非推奨だが、既存のユーザーには機能し続ける。`appboyBridge` を使用している場合は、`brazeBridge` に移行することをお勧めする。<br><br> `appboyBridge` は以下のSDKバージョンで非推奨となった：
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
リキッドを参照して挿入することはできない <code>customAttributes</code> をJavaScript Bridgeのメソッドに置き換える。
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## リンクベースのアクション

カスタムJavaScriptに加えて、Braze SDKは、これらの便利なURLショートカットで分析データを送信することもできる。これらのクエリーパラメーターとURLスキームは、すべて大文字と小文字を区別することに注意されたい。

### ボタンのクリックトラッキング（非推奨）

{% alert warning %}
`abButtonID` の使用は、[HTML with Preview]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) メッセージタイプではサポートされていません。詳しくは、[アップグレードガイドを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes)参照のこと。
{% endalert %}

アプリ内メッセージ分析のためにボタンのクリックを記録するには、ディープリンク、リダイレクトURL、アンカー要素`<a>` のクエリパラメータとして`abButtonId` を追加する。ボタン1」のクリックを記録するには`?abButtonId=0` 、「ボタン2」のクリックを記録するには`?abButtonId=1` 。

他のURLパラメータと同様に、最初のパラメータはクエスチョンマーク`?` で始め、それ以降のパラメータはアンパサンド`&` で区切る。

#### URLの例

- `https://example.com/?abButtonId=0` - ボタン1クリック
- `https://example.com/?abButtonId=1` - ボタン2をクリックする
- `https://example.com/?utm_source=braze&abButtonId=0` - 他の既存のURLパラメータでボタン1クリック
- `myApp://deep-link?page=home&abButtonId=1` - ボタン2クリックでモバイル・ディープリンク
- `<a href="https://example.com/?abButtonId=1">` - ボタン2クリックでアンカー要素`<a>` 

{% alert note %}
アプリ内メッセージはボタン1とボタン2のクリックのみをサポートする。これら2つのボタンIDのいずれかを指定しないURLは、一般的な「ボディクリック」として記録される。
{% endalert %}

### 新しいウィンドウでリンクを開く（モバイルのみ）

アプリ外のリンクを新しいウィンドウで開くには、`?abExternalOpen=true` を設定する。リンク先を開く前にメッセージが消える。

ディープリンクの場合、Brazeは`abExternalOpen` の値に関係なくURLを開く。

### ディープリンクとして開く（モバイルのみ）

BrazeにHTTPまたはHTTPSリンクをディープリンクとして扱わせるには、`?abDeepLink=true`.

このクエリ文字列パラメータがないか、`false` に設定されている場合、Brazeはホストアプリ内の内部ウェブブラウザでウェブリンクを開こうとする。

### アプリ内メッセージを閉じる

アプリ内メッセージを閉じるには、`brazeBridge.closeMessage()` javascriptメソッドを使うことができる。

例えば、`<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` 、アプリ内メッセージを閉じる。

## プレビュー付きHTMLアップロード

カスタムHTMLアプリ内メッセージを作成する際、Brazeで直接インタラクティブコンテンツをプレビューできる。 

エディターのメッセージ・プレビュー・パネルには、メッセージに含まれるJavaScriptをレンダリングするリアルなプレビューが表示される。プレビューパネルから、ページネーションをクリックしたり、フォームやアンケートを送信したり、JavaScriptアニメーションを見たりして、カスタムメッセージをプレビューし、やりとりすることができる！

![ページをスワイプしてHTMLプレビューとインタラクトする。]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
HTMLで使用している`brazeBridge` JavaScriptメソッドは、ダッシュボードでプレビューしている間はユーザー・プロフィールを更新しない。
{% endalert %}

### SDK 要件 {#supported-sdk-versions}

アプリ内メッセージのHTMLプレビューを使用するには、以下のBraze SDK最小バージョンにアップグレードする必要がある：

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
このメッセージタイプは特定のSDKバージョン以降でしか受信できないため、サポートされていないSDKバージョンのユーザーはメッセージを受信できない。このメッセージタイプの採用は、ユーザーベースのかなりの部分が到達可能になってから検討するか、アプリのバージョンが要件より後のユーザーだけをターゲットにする。[アプリの最新バージョンによるフィルタリングの]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)詳細はこちら。
{% endalert %}

### キャンペーンを作成する {#instructions}

**カスタムコードを**アプリ内メッセージで作成する場合、カスタムタイプとして**プレビュー付きHTMLアップロードを**選択する。アプリ内メッセージ（ライブまたは下書き）でカスタムコードを作成したことがない場合、このオプションは自動的に適用され、選択する必要はない。

![メッセージタイプ」がカスタムコード、「カスタムタイプ」がプレビュー付きHTMLアップロードの場合、モバイルとウェブブラウザの両方に送信するアプリ内メッセージを作成する]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

モバイルアプリのユーザーがこのメッセージを受け取るには、サポートされているSDKのバージョンにアップグレードする必要があることを覚えておいてほしい。新しいBraze SDKバージョンに依存するキャンペーンを開始する前に、モバイルアプリを[アップグレードするようユーザーに促す]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/)ことを推奨する。

#### 資産ファイル

HTMLアップロードでカスタムコードのアプリ内メッセージを作成する場合、キャンペーンアセットを[メディアライブラリに]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)アップロードし、メッセージ内で参照することができる。

アップロード可能なファイルタイプは以下の通りである：

| ファイルの種類        | ファイル拡張子                    |
| :--------------- | :-------------------------------- |
| フォントファイル       | `.ttf``.woff`,`.otf` 、 `.woff2` |
| SVG画像       | `.svg`                            |
| JavaScriptファイル | `.js`                             |
| CSSファイル        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2}

Brazeは、2つの理由からメディアライブラリにアセットをアップロードすることを推奨している：

1. メディアライブラリ経由でキャンペーンに追加したアセットにより、ユーザーがオフラインの状態やインターネット接続が悪い状態でもメッセージを表示することができる。
2. Brazeにアップロードされたアセットは、キャンペーンをまたいで再利用できる。

##### アセットファイルを追加する

キャンペーンに新規または既存のアセットを追加できる。

キャンペーンに新しいアセットを追加するには、ドラッグ＆ドロップセクションを使ってファイルをアップロードする。このセクションで追加されたアセットも、メディアライブラリに自動的に追加される。すでにメディアライブラリにアップロードしたアセットを追加するには、**メディアライブラリから追加を**選択する。

アセットが追加されると、**このキャンペーンのアセットセクションに**表示される。 

アセットのファイル名がローカルのHTMLアセットと一致する場合、自動的に置き換えられる（例えば、`cat.png` がアップロードされ、`<img src="cat.png" />` が存在する場合）。 

それ以外の場合は、リストからアセットにカーソルを合わせ、<i class="fas fa-copy"></i> **コピーを**選択して、ファイルのURLをクリップボードにコピーする。次に、コピーしたアセットのURLを、リモートアセットを参照するときに通常行うようにHTMLに貼り付ける。


### HTMLエディタ

HTMLに加えた変更は、入力と同時にプレビュー・パネルに自動的にレンダリングされる。HTMLで使用している[`brazeBridge` JavaScript](#bridge)メソッドは、ダッシュボードでプレビューしている間はユーザー・プロフィールを更新しない。

**エディター設定では**、テキストの折り返しの切り替え、フォントサイズの変更、カラーテーマの選択ができる。コード・エディターには、シンタックス・ハイライトのためのさまざまなカラー・テーマが用意されており、メッセージ・コンポーザーで潜在的なコード・エラーを直接発見したり、コードをよりよく整理したりするのに役立つ（スペースとタブのどちらを使うか、あなたがどちらの立場であれ）。

![アプリ内でHTMLメッセージを作成する際、"Editor Settings "ドロップダウンにシンタックスハイライトのオプションがある。]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

{% alert tip %}
HTMLエディター内で<kbd>Ctrl</kbd>+<kbd>F</kbd>（Windows）または<kbd>Command</kbd>+<kbd>F</kbd>（Mac）を押すと、コード内を検索できる！
{% endalert %}

### ボタン・トラッキング {#button-tracking-improvements}

カスタム・コードのアプリ内メッセージでパフォーマンスを追跡するには [`brazeBridge.logClick(button_id)`][1]JavaScriptメソッドを使う。これにより、`brazeBridge.logClick("0")` 、`brazeBridge.logClick("1")` 、`brazeBridge.logClick()` を使って、「ボタン1」、「ボタン2」、「ボディクリック」をそれぞれプログラムで追跡することができる。

| クリック数     | 方法                       |
| ---------- | ---------------------------- |
| ボタン1   | `brazeBridge.logClick("0")` |
| ボタン2   | `brazeBridge.logClick("1")` |
| ボディクリック | `brazeBridge.logClick()`    |
| カスタムボタンのトラッキング |`brazeBridge.logClick("your custom name here")`|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
このボタン追跡方法は、以前の自動クリック追跡方法（`?abButtonId=0` など）に取って代わるもので、現在は削除されている。
{% endalert %}

インプレッションごとに複数のボタン・クリック・イベントをトラッキングできる。例えば、メッセージを閉じてボタン2のクリックを記録するには、以下のようにする：

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

また、新しいカスタムボタンの名前を追跡することもできる。`brazeBridge.logClick("blue button")`、`brazeBridge.logClick("viewed carousel page 3")` などがあります。

#### 制限事項

- 1つのキャンペーンにつき、最大100個のユニークなボタンIDを持つことができる。
- ボタンIDはそれぞれ255文字まで持つことができる。
- ボタンIDは、文字、数字、スペース、ダッシュ、アンダースコアのみを含むことができる。

### 後方互換性のない変更 {#backward-incompatible-changes}

1. この新しいメッセージ・タイプで最も顕著な互換性のない変更は、SDKの要件である。アプリSDKが最小[SDKバージョン要件を満たして](#supported-sdk-versions)いないユーザーには、このメッセージは表示されない。
<br>

2. これまでモバイルアプリでサポートされていた`braze://close` のディープリンクは廃止され、JavaScript`brazeBridge.closeMessage()` がサポートされるようになった。ウェブはディープリンクをサポートしていないので、これによってクロスプラットフォームのHTMLメッセージが可能になる。

3. ボタンIDに`?abButtonId=0` を使用していた自動クリックトラッキングと、閉じるボタンの「ボディクリック」トラッキングは削除された。以下のコード例は、新しいクリック・トラッキングJavaScriptメソッドを使用するためにHTMLを変更する方法を示している：

   | 前 | その後 |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_e4f5f6b6-6766-4ac4-8ee4-445acf534d00/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_0b7e9bf3-06b1-4eba-a81b-c6aa59bb91a7/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_4f5f77d0-92d8-4c8c-82c0-7acf311fa527/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_9fee233d-ab30-48f3-9804-83b49c70eae7/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_9017bac3-a67f-4677-878f-1460fff75950/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[2]: https://github.com/braze-inc/in-app-message-templates
