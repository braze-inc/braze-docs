---
nav_title: HTML アプリ内メッセージ
article_title: カスタム HTML アプリ内メッセージ
page_order: 0
page_type: reference
description: "この記事では、JavaScriptメソッド、ボタントラッキング、BrazeでのインタラクティブHTMLプレビューの使用など、カスタムコードのアプリ内メッセージの概要について説明します。"
channel:
  - in-app messages
---

# カスタム HTML アプリ内メッセージ {#custom-html-messages}

> 標準のアプリ内メッセージはさまざまな方法でカスタマイズできますが、HTML、CSS、JavaScriptを使用して設計および構築されたメッセージを使用すると、キャンペーンのルックアンドフィールをさらに細かく制御できます。シンプルな構成だけで、ニーズに合わせてカスタマイズした機能やブランディングが可能になります。 

HTML アプリ内メッセージを使用すると、次のようなメッセージの外観をより細かく制御できます。

- カスタムフォントとスタイル
- 動画
- 複数の画像
- クリック時動作
- インタラクティブコンポーネント
- カスタムアニメーション

カスタム HTML メッセージでは、[JavaScript Bridge](#javascript-bridge) メソッドを使用してイベントを記録したり、カスタム属性を設定したり、メッセージを閉じたりすることができます。[GitHub リポジトリには][2]、HTML アプリ内メッセージの使用方法やニーズに合わせてカスタマイズする方法の詳細が記載されています。また、使い始める際に役立つ一連の HTML5 アプリ内メッセージテンプレートも用意されています。

{% alert note %}
Web SDK を使用して HTML アプリ内メッセージを有効にするには、たとえば Braze: `allowUserSuppliedJavascript` に初期化オプションを指定する必要があります。`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`HTMLアプリ内メッセージはJavaScriptを実行できるため、これはセキュリティ上の理由によるものです。そのため、サイト管理者に有効にしてもらう必要があります。
{% endalert %}

## JavaScript ブリッジ {#javascript-bridge}

Web、Android、iOS、Swift SDK用のHTMLアプリ内メッセージは、Braze SDKとのインターフェースとなるJavaScriptの「ブリッジ」をサポートしています。これにより、ユーザーがリンクのある要素をクリックしたり、コンテンツにアクセスしたりしたときに、カスタムBrazeアクションをトリガーできます。これらのメソッドは、`brazeBridge``appboyBridge`グローバルまたは変数で使用できます。

{% alert important %}
Braze `brazeBridge` ではグローバル変数を使用することを推奨しています。`appboyBridge`グローバル変数は廃止されましたが、既存のユーザーには引き続き機能します。を使用している場合は`appboyBridge`、への移行をお勧めします`brazeBridge`。<br><br> `appboyBridge` は、次の SDK バージョンで廃止されました。
\- Web:[3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
\- Android:[14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
\- iOS:[4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

たとえば、カスタム属性とカスタムイベントをログに記録してメッセージを閉じるには、HTML アプリ内メッセージ内で次の JavaScript を使用できます。

\`\`\`html
<button id="button">お気に入りの色を設定</button>
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

### JavaScript ブリッジメソッド {#bridge}

Braze HTML アプリ内メッセージでは、以下の JavaScript メソッドがサポートされています。

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
Liquid を参照して JavaScript Bridge <code>メソッドにカスタムアトリビュートを挿入することはできません</code>。
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## リンクベースのアクション

カスタム JavaScript に加えて、Braze SDK はこれらの便利な URL ショートカットを使用してアナリティクスデータを送信することもできます。これらのクエリパラメータと URL スキームはすべて大文字と小文字が区別されることに注意してください。

### ボタンクリックトラッキング

{% alert warning %}
[プレビューメッセージタイプの HTML では、`abButtonID`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/)の使用はサポートされていません。詳細については、[アップグレードガイドをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes)。
{% endalert %}

アプリ内メッセージ分析のボタンクリックを記録するには、任意のディープリンク、リダイレクトURL、`abButtonId`またはアンカー要素にクエリパラメータとして追加できます。`<a>`「ボタン1」のクリックを記録する場合と`?abButtonId=1`、「ボタン2」のクリックを記録する場合に使用します`?abButtonId=0`。

他の URL パラメーターと同様に、最初のパラメーターは疑問符で始まり`?`、`&`それ以降のパラメーターはアンパサンドで区切る必要があります。

#### 例

- `https://example.com/?abButtonId=0` -ボタン 1 クリック
- `https://example.com/?abButtonId=1` -ボタン 2 クリック
- `https://example.com/?utm_source=braze&abButtonId=0` -他の既存の URL パラメータでボタンを 1 回クリック
- `myApp://deep-link?page=home&abButtonId=1` -ボタン2クリックでのモバイルディープリンク
- `<a href="https://example.com/?abButtonId=1">` -`<a>` ボタンを2回クリックしたときのアンカーエレメント

{% alert note %}
アプリ内メッセージは、ボタン 1 とボタン 2 のクリックのみをサポートします。これら 2 つのボタン ID のいずれかを指定しない URL は、一般的な「ボディクリック」として記録されます。
{% endalert %}

### リンクを新しいウィンドウで開く (モバイルのみ)

アプリ外のリンクを新しいウィンドウで開くには、を設定します`?abExternalOpen=true`。メッセージはリンクを開く前に閉じられます。

ディープリンクの場合、Brazeはの値に関係なくURLを開きます。`abExternalOpen`

### ディープリンクとして開く (モバイルのみ)

Braze に HTTP または HTTPS リンクをディープリンクとして処理させるには、`?abDeepLink=true`を設定してください。

このクエリ文字列パラメータがないか`false`、に設定されている場合、Brazeはホストアプリ内の内部WebブラウザでWebリンクを開こうとします。

### ニュースフィード (モバイルのみ)

{% alert note %}
ニュースフィードは非推奨になります。Brazeは、ニュースフィードツールを使用するお客様に、コンテンツカードメッセージングチャネルに移行することを推奨しています。コンテンツカードメッセージングチャネルは、より柔軟でカスタマイズ可能で信頼性が高くなります。詳細については、[移行ガイドをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)。
{% endalert %}

モバイルアプリの場合、リンクの URL をに設定してニュースフィードを開くことができます`braze://feed`。

たとえば、`<a href="braze://feed">View Feed</a>`。

### アプリ内メッセージを閉じる

アプリ内メッセージを閉じるには、`brazeBridge.closeMessage()` javascriptメソッドを使用できます。

たとえば、`<a onclick="brazeBridge.closeMessage()" href="#">Close</a>`アプリ内メッセージを閉じます。

## HTML アップロードとプレビュー

カスタム HTML アプリ内メッセージを作成する場合、インタラクティブコンテンツを Braze で直接プレビューできます。 

エディターのメッセージプレビューパネルには、メッセージに含まれている JavaScript をレンダリングするリアルなプレビューが表示されます。ページネーションをクリックしたり、フォームやアンケートを送信したり、JavaScriptアニメーションを見たりすることで、プレビューパネルからカスタムメッセージをプレビューして操作できます。

![Interacting with the HTML preview by swiping through pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
HTML で使用している `brazeBridge` JavaScript メソッドは、ダッシュボードでプレビューしている間はユーザープロファイルを更新しません。
{% endalert %}

### SDK の要件 {#supported-sdk-versions}

アプリ内メッセージの HTML プレビューを使用するには、以下の最小バージョンの Braze SDK にアップグレードする必要があります。

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
このメッセージタイプは特定の新しいバージョンの SDK でのみ受信できるため、サポートされていない SDK バージョンを使用しているユーザーはメッセージを受信できません。このメッセージタイプは、ユーザーベースのかなりの部分にアクセスできるようになった後に採用するか、アプリのバージョンが要件よりも新しいユーザーのみを対象とすることを検討してください。[最新のアプリバージョンによるフィルタリングの詳細をご覧ください]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)。
{% endalert %}

### キャンペーンの作成 {#instructions}

**カスタムコードのアプリ内メッセージを作成する場合**、カスタムタイプとして「**プレビュー付きの HTML アップロード**」を選択します。以前にカスタムコードのアプリ内メッセージ（ライブまたはドラフト）を作成したことがない場合は、このオプションが自動的に適用されるため、選択する必要はありません。

![Creating an in-app message that sends to both Mobile and Web browsers where "Message Type" is Custom Code and "Custom Type" is HTML Upload with Preview.]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

モバイルアプリのユーザーがこのメッセージを受け取るには、サポートされている SDK バージョンにアップグレードする必要があることに注意してください。新しいBraze [SDKバージョンに依存するキャンペーンを開始する前に、モバイルアプリをアップグレードするようユーザーに促すことをお勧めします]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/)。

#### アセットファイル

HTMLアップロードを使用してカスタムコードのアプリ内メッセージを作成する場合、[キャンペーンアセットをメディアライブラリにアップロードしてメッセージで参照できます]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)。

アップロードには以下のファイルタイプがサポートされています。

| ファイルの種類 | ファイル拡張子 |
| :--------------- | :-------------------------------- |
| フォントファイル | `.ttf`、`.woff`、`.otf`、`.woff2` |
| SVG イメージ `.svg` |
| ジャバスクリプトファイル | `.js` |
| CSS ファイル `.css` |
{: .reset-td-br-1 .reset-td-br-2}

Braze がメディアライブラリにアセットをアップロードすることを推奨する理由は 2 つあります。

1. メディアライブラリを介してキャンペーンにアセットを追加すると、ユーザーがオフラインのときやインターネット接続が不十分なときでもメッセージを表示できます。
2. Braze にアップロードされたアセットは、キャンペーン全体で再利用できます。

##### アセットファイルの追加

新規または既存のアセットをキャンペーンに追加できます。

キャンペーンに新しいアセットを追加するには、ドラッグアンドドロップセクションを使用してファイルをアップロードします。このセクションで追加されたアセットは、自動的にメディアライブラリにも追加されます。メディアライブラリにアップロード済みのアセットを追加するには、「**メディアライブラリから追加**」を選択します。

アセットを追加すると、「**このキャンペーンのアセット**」セクションに表示されます。 

アセットのファイル名がローカルの HTML アセットのファイル名と一致する場合、自動的に置き換えられます (たとえば、`cat.png``<img src="cat.png" />`がアップロードされて存在する場合)。 

それ以外の場合は、リストのアセットにカーソルを合わせ、[<i class="fas fa-copy"></i>**コピー**] を選択してファイルの URL をクリップボードにコピーします。次に、リモートアセットを参照するときと同じように、コピーしたアセット URL を HTML に貼り付けます。


### HTML エディター

HTML に加えた変更は、入力時にプレビューパネルに自動的にレンダリングされます。HTML で使用している [`brazeBridge`JavaScript](#bridge) メソッドは、ダッシュボードでプレビューしている間はユーザープロファイルを更新しません。

**エディター設定を構成して**、折り返しテキストの切り替え、フォントサイズの変更、カラーテーマの選択を行うことができます。コードエディターにはシンタックスハイライト用のさまざまなカラーテーマが用意されているため、メッセージコンポーザーで潜在的なコードエラーを直接特定し、コードをより適切に整理できます (引数のどちら側を選択しても、スペースまたはタブを使用)。

![Syntax highlighting options in the "Editor Settings" dropdown when composing an HTML in-app message.]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

{% alert tip %}
HTML エディターで <kbd><kbd>Ctrl+F</kbd></kbd> (Windows) または <kbd>Command</kbd> + <kbd>F</kbd> (Mac) を押すと、コード内を検索できます。
{% endalert %}

### ボタントラッキング {#button-tracking-improvements}

[`brazeBridge.logClick(button_id)`][1]JavaScriptメソッドを使用して、カスタムコードのアプリ内メッセージ内のパフォーマンスを追跡できます。これにより、「ボタン 1」、「ボタン 2」、「ボディクリック」をそれぞれ、、またはを使用して`brazeBridge.logClick("0")``brazeBridge.logClick("1")`、プログラムで追跡できます。`brazeBridge.logClick()`

| クリック数 | メソッド |
| ---------- | ---------------------------- |
| Button 1   | `brazeBridge.logClick("0")` |
| ボタン 2 | `brazeBridge.logClick("1")` |
| ボディクリック | `brazeBridge.logClick()` |
| カスタムボタントラッキング | `brazeBridge.logClick("your custom name here")` |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
このボタントラッキング方法は、廃止された以前の自動クリックトラッキング方法（など`?abButtonId=0`）に代わるものです。
{% endalert %}

インプレッションごとに複数のボタンクリックイベントを追跡できます。たとえば、メッセージを閉じてボタン 2 のクリックを記録するには、以下を使用できます。

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

また、新しいカスタムボタン名をトラッキングすることもできます。キャンペーンごとに最大 100 個のユニークな名前を指定できます。たとえば、`brazeBridge.logClick("blue button")`または`brazeBridge.logClick("viewed carousel page 3")`。

#### 制限事項

- 1 つのキャンペーンにつき、最大 100 個のユニークなボタン ID を設定できます。
- ボタン ID には、それぞれ最大 255 文字を使用できます。
- ボタン ID には、文字、数字、スペース、ダッシュ、およびアンダースコアのみを使用できます。

### 下位互換性のない変更 {#backward-incompatible-changes}

1. この新しいメッセージタイプで互換性のない変更として最も顕著なのは、SDK の要件です。アプリ SDK が SDK [の最小バージョン要件を満たしていないユーザーには](#supported-sdk-versions)、メッセージは表示されません。
<br>

2. `braze://close`以前はモバイルアプリでサポートされていたディープリンクが削除され、JavaScriptが採用されました。`brazeBridge.closeMessage()`ウェブはディープリンクをサポートしていないため、これによりクロスプラットフォームの HTML メッセージが可能になります。

3. ボタン ID `?abButtonId=0` に使用されていた自動クリックトラッキングと、閉じるボタンの「ボディクリック」トラッキングは削除されました。次のコード例は、新しいクリックトラッキング JavaScript メソッドを使用するように HTML を変更する方法を示しています。

   | 変更前 | 処理後 |
   |:-------- |:------------|
   <code><a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">| <code><a href= "ブレイズ:</code>| 閉じるボタン | //close">Close Button</a></a></code>
   <code><a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">| <code><a href= "ブレイズ:</code>| 閉じるボタン | //close?abButtonId=0">Close Button</a></a></code>
   <code>| <code><a href= "アプリ:| <a href=" アプリ://deeplink?abButtonId=0">Track button 1</a></code>| //deeplink" onclick="brazeBridge.logClick('0')">Track button 1</a></code>
   | <code> <script><br>location.href =「ブレイズ://クローズ?AbButtonID=1"<br></script></code>| <code> <script><br>window.addEventListener("ab.BridgeReady", function(){<br>  Brazebridge.logClick (「1");<br>  ブレイズブリッジ. クローズメッセージ ();<br>});<br></script></code>|

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[2]: https://github.com/braze-inc/in-app-message-templates
