---
nav_title: HTML アプリ内メッセージ
article_title: カスタムHTMLアプリ内メッセージ
page_order: 0
page_type: reference
description: "この記事では、JavaScriptメソッド、ボタントラッキング、BrazeのインタラクティブHTMLプレビューの使用など、アプリ内メッセージのカスタムコードの概要を説明する。"
channel:
  - in-app messages
---

# カスタムの HTML アプリ内メッセージ {#custom-html-messages}

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
Web SDKを通じてアプリ内メッセージでHTMLをイネーブルメントするには、Brazeに初期化`allowUserSuppliedJavascript`オプションを指定する必要がある。例えば、`initialization:`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})` {\` という形式で指定する。これはセキュリティ上の理由によるもので、HTML のアプリ内メッセージは JavaScript を実行できるため、サイト管理者が有効にする必要があります。
{% endalert %}

## JavaScriptブリッジ {#javascript-bridge}

{% include javascript_bridge/reference.md %}

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

![ページをスワイプしてHTMLプレビューを操作する。]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
HTMLで使用している`brazeBridge` JavaScriptメソッドは、ダッシュボードでプレビューしている間はユーザー・プロフィールを更新しない。
{% endalert %}

### SDK 要件 {#supported-sdk-versions}

アプリ内メッセージの HTML プレビューを使用するには、以下のBraze SDK バージョン以降にアップグレードする必要があります。

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
このメッセージタイプは特定の後続SDKバージョンでのみ受信できるため、サポート対象外のSDKバージョンを使用しているユーザーはメッセージを受信しない。このメッセージタイプの採用は、ユーザーベースのかなりの部分が到達可能になってから検討するか、アプリのバージョンが要件より後のユーザーだけをターゲットにする。[「最新のアプリバージョンによるフィルター処理」]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)を参照してください。
{% endalert %}

### キャンペーンの作成{#instructions}

モバイルアプリのユーザーは**、カスタムコードの**アプリ内メッセージを受信するために、サポートされているSDKバージョンにアップグレードする必要がある。新しいBraze SDKバージョンに依存するキャンペーンを開始する前に、モバイルアプリを[アップグレードするようユーザーに促す]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/)ことを推奨する。

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

1. メディアライブラリー経由でキャンペーンに追加された資産は、ユーザーがオフライン状態やインターネット接続が不安定な場合でも、メッセージを表示できるようにする。
2. Brazeにアップロードされたアセットは、キャンペーンをまたいで再利用できる。

##### アセットファイルを追加する

キャンペーンに新規または既存のアセットを追加できる。

キャンペーンに新しいアセットを追加するには、ドラッグ＆ドロップセクションを使ってファイルをアップロードする。このセクションで追加されたアセットも、メディアライブラリに自動的に追加される。メディアライブラリにアップロード済みのアセットを追加するには、[**メディアライブラリから追加**] を選択します。

アセットが追加されると、[**このキャンペーンのアセット**] セクションに表示されます。 

アセットのファイル名がローカルHTMLアセットのファイル名と一致する場合、自動的に置き換えられる（例：`cat.png`がアップロードされ、 が存在`<img src="cat.png" />`する）。 

それ以外の場合は、リストからアセットにカーソルを合わせ、<i class="fas fa-copy"></i> **コピーを**選択して、ファイルのURLをクリップボードにコピーする。次に、コピーしたアセットのURLを、リモートアセットを参照するときに通常行うようにHTMLに貼り付ける。

### HTMLエディタ

HTMLに加えた変更は、入力と同時にプレビュー・パネルに自動的にレンダリングされる。HTMLで使用している[`brazeBridge` JavaScript](#bridge)メソッドは、ダッシュボードでプレビューしている間はユーザー・プロフィールを更新しない。

{% alert tip %}
HTMLエディタ内で**検索**<i class="fa-solid fa-magnifying-glass"></i>を選択すれば、コード内を検索できる！
{% endalert %}

### ボタンの追跡{#button-tracking-improvements}

カスタム・コードのアプリ内メッセージでパフォーマンスを追跡するには [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)JavaScriptメソッドを使う。完全な参照については、上記の[JavaScript Bridgeメソッドを](#bridge)参照せよ。

{% alert note %}
このボタン追跡方法は、以前の自動クリック追跡方法 (`?abButtonId=0` など、現在は削除済み) に代わるものです。
{% endalert %}

### 後方互換性のない変更{#backward-incompatible-changes}

1. この新しいメッセージタイプで最も注目すべき互換性のない変更は、SDK 要件です。アプリの SDK が最小[SDK バージョン要件](#supported-sdk-versions) を満たしていないユーザーには、メッセージが表示されません。
2. これまでモバイルアプリでサポートされていた`braze://close` のディープリンクは廃止され、JavaScript`brazeBridge.closeMessage()` がサポートされるようになった。ウェブはディープリンクをサポートしていないので、これによってクロスプラットフォームのHTMLメッセージが可能になる。
3. ボタンIDに`?abButtonId=0` を使用していた自動クリックトラッキングと、閉じるボタンの「ボディクリック」トラッキングは削除された。以下のコード例は、新しいクリック・トラッキングJavaScriptメソッドを使用するためにHTMLを変更する方法を示している：

   | 前 | その後 |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_25e67aeb-49da-453b-a26a-c7d58bc4f4a9/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_8d20b050-9e1c-4b96-9e9a-f1676c5bd27b/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_28394aa0-ccd0-49c5-987a-0c9a14a48612/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_cdf981ae-ad11-44ab-bf59-e736c5ba811f/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_b3329d87-f649-4280-ac55-1073d7c361f4/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

