{% multi_lang_include archive/web-v4-rename.md %}

## 前提条件

コンテンツカードを使用する前に、[Braze Web SDKを]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)アプリに[統合する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)必要がある。しかし、追加の設定は必要ない。代わりに独自のUIを構築するには、[コンテンツカードカスタマイズガイドを]({{site.baseurl}}/developer_guide/content_cards/)参照のこと。

## 標準フィードUI

付属のコンテンツカード UI を使用するには、Web サイト上のどこにフィードを表示するかを指定する必要があります。 

この例では、コンテンツカードフィードを配置する `<div id="feed"></div>` があります。3つのボタンを使って、フィードの非表示、表示、トグル（現在の状態に応じて非表示、表示）を切り替える。

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

`toggleContentCards(parentNode, filterFunction)` 、`showContentCards(parentNode, filterFunction)` メソッドを使用する際、引数が与えられない場合、すべてのコンテンツカードはページ右側の固定位置のサイドバーに表示される。そうでなければ、フィードは指定された`parentNode` オプションに置かれる。

|パラメーター | 説明 |
|---|---|
|`parentNode` | コンテンツカードをレンダリングするHTMLノード。親ノードがすでに直系の子孫として Braze コンテンツカードビューを持っている場合、既存のコンテンツカードは置き換えられます。たとえば、`document.querySelector(".my-container")` を渡す必要があります。|
|`filterFunction` | このビューに表示されるカードのフィルターまたはソート機能。`Card` オブジェクトの配列で呼び出され、`{pinned, date}` でソートされます。このユーザーにレンダリングするために、ソートされた `Card` オブジェクトの配列を返す必要があります。省略した場合は、すべてのカードが表示される。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

コンテンツカードの切り替えに関する詳細は、[SDK リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)を参照してください。

## カードの種類とプロパティ

コンテンツ・カード・データ・モデルはWeb SDKで利用可能で、以下のコンテンツ・カード・タイプを提供する：[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)、[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)、[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)である。各タイプは、[ベースモデルカードから](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)共通のプロパティを継承し、以下の追加プロパティを持つ。

{% alert tip %}
コンテンツカードのデータを記録するには、[分析を記録するを]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)参照のこと。
{% endalert %}

### ベースカードモデル

すべてのコンテンツカードは、以下の共有プロパティを持っています。

|プロパティ|説明|
|---|---|
| `expiresAt` | カードの有効期限を示すUNIXタイムスタンプ。|
| `extras`| (オプション）値文字列を持つ文字列オブジェクトとしてフォーマットされたキーと値のペアデータ。 |
| `id` | (オプション）カードのID。これは、分析目的でイベントとともに Braze に報告されます。 |
| `pinned` | このプロパティは、カードがダッシュボードで「ピン留め」されているかどうかを反映する。|
| `updated` | このカードが最後に更新されたUNIXタイムスタンプ。 |
| `viewed` | このプロパティは、ユーザがカードを閲覧したかどうかを反映する。|
| `isControl` | カードが AB テスト内の「コントロール」グループである場合、このプロパティは `true` です。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 画像のみ

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)カードは、クリック可能なフルサイズの画像である。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比。画像の読み込みが完了する前のヒントとなる。特定の状況ではプロパティが提供されない場合があることに注意してください。| |
| `categories` | このプロパティは、純粋にカスタム実装で整理するためのもので、これらのカテゴリーはダッシュボードコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示す。 |
| `created` | Brazeからのカード作成時間のUNIXタイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示す。 |
| `dismissible` | このプロパティは、ユーザーがカードを閉じてビューから削除できるかどうかを反映します。 |
| `imageUrl` | カードの画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### キャプション付き画像

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)カードは、クリック可能なフルサイズの画像で、説明文が添えられている。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比。画像の読み込みが完了する前のヒントとなる。特定の状況ではプロパティが提供されない場合があることに注意してください。| |
| `categories` | このプロパティは、純粋にカスタム実装で整理するためのもので、これらのカテゴリーはダッシュボードコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示す。 |
| `created` | Brazeからのカード作成時間のUNIXタイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示す。 |
| `dismissible` | このプロパティは、ユーザーがカードを閉じてビューから削除できるかどうかを反映します。 |
| `imageUrl` | カードの画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### クラシック

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)モデルは、テキストなしの画像、または画像付きのテキストを含むことができる。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比。画像の読み込みが完了する前のヒントとなる。特定の状況ではプロパティが提供されない場合があることに注意してください。| |
| `categories` | このプロパティは、純粋にカスタム実装で整理するためのもので、これらのカテゴリーはダッシュボードコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示す。 |
| `created` | Brazeからのカード作成時間のUNIXタイムスタンプ。 |
| `description` | このカードの本文。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示す。 |
| `dismissible` | このプロパティは、ユーザーがカードを閉じてビューから削除できるかどうかを反映します。 |
| `imageUrl` | カードの画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 対照群

デフォルトのコンテンツカードフィードを使用すると、インプレッションとクリックが自動的に追跡されます。

コンテンツカード用のカスタム統合を使用している場合、コントロールカードが表示されたときの[インプレッションを記録する]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)必要があります。この作業の一環として、AB テストでインプレッションを記録する際には、必ずコントロールカードを処理するようにしてください。これらのカードは空白であり、ユーザーに表示されませんが、コントロールカードでないカードとのパフォーマンスを比較するために、インプレッションを記録する必要がある。

コンテンツカードが AB テストのコントロールグループにあるかどうかを判断するには、`card.isControl` プロパティ(Web SDK v4.5.0+) を確認するか、カードが `ControlCard` インスタンス (`card instanceof braze.ControlCard`) かどうかをチェックします。

## カードメソッド

|方法 | 説明 |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| 指定されたカードの一覧のインプレッションイベントを記録します。これは、Braze UI ではなく、カスタマイズされた UI を使用する場合に必要です。|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| 指定されたカードのクリックイベントをログに記録する。これは、Braze UI ではなく、カスタマイズされた UI を使用する場合に必要です。| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| ユーザーのコンテンツカードを表示する。 |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| 現在表示されているBrazeコンテンツカードを非表示にする。 | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| ユーザーのコンテンツカードを表示する。 | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|前回のコンテンツカードの更新から、現在利用可能なすべてのカードを取得する。|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| コンテンツカードの更新を購読する。<br> サブスクライバーのコールバックは、コンテンツカードが更新されるたびに呼び出されます。 | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|プログラムでカードを解除する（v2.4.1で利用可能）。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

詳細については、[SDK リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

## Googleタグマネージャーを使う

Google Tag Manager は、[ Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (当社Web SDKのバージョン) をWeb サイト コードに直接注入することで機能します。これは、コンテンツカードを実装する場合を除き、Google Tag Manager なしでSDKを統合した場合と同様に、すべてのSDK方法を利用できることを意味します。

### コンテンツカードの設定

{% tabs local %}
{% tab Google Tag Manager %}
コンテンツカードフィードを標準的に統合するには、Google タグマネージャで**カスタムHTML**タグを使用できます。以下をカスタムHTML タグに追加すると、標準のコンテンツカードフィードが有効になります。

```html
<script>
   window.braze.showContentCards();
</script>
```

![コンテンツカードのフィードを表示するカスタムHTMLタグのGoogleタグマネージャーでのタグ設定]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab マニュアル %}
コンテンツカードとそのフィードの外観をより自由にカスタマイズするために、コンテンツカードをネイティブ Web サイトに直接統合できます。これには、標準フィード UI を使用する方法と、カスタムフィード UI を作成する方法の2つの方法があります。

{% subtabs local %}
{% subtab standard feed %}
[スタンダードフィード UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui)を実装する場合、Brazeメソッドはメソッドの先頭に`window.`を追加する必要があります。たとえば、`braze.showContentCards` の代わりに `window.braze.showContentCards` にする必要があります。
{% endsubtab %}

{% subtab custom feed %}
[カスタムフィード]({{site.baseurl}}/developer_guide/content_cards/creating_cards/)スタイルの場合、ステップsは、GTMなしでSDKを統合した場合と同じです。たとえば、コンテンツカードフィードの幅をカスタマイズする場合は、以下をCSSに貼り付けることができます。

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### テンプレートのアップグレード {#upgrading}

Braze Web SDK の最新バージョンにアップグレードするには、Google Tag Manager ダッシュボードで次の3つのステップを実行します。

1. **タグテンプレートを更新する**<br>ワークスペース内の**Templates** ページに移動します。更新が利用可能であることを示すアイコンが表示されます。<br><br>![更新があることを示すテンプレートページ]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>そのアイコンをクリックし、変更を確認した後、**Accept Update**をクリックします。<br><br>![新旧タグテンプレートの比較画面と「更新を受け入れる」ボタン]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **バージョン番号を更新する**<br>タグテンプレートが更新されたら、Braze 初期化タグを編集し、SDK バージョンを最新の `major.minor` バージョンに更新します。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。SDKのバージョン一覧は[変更履歴で](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)見ることができる。<br><br>![SDKバージョンを変更するための入力フィールドを持つBraze初期化テンプレート]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA および公開**<br>Google Tag Manager の [[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)] を使用して、新しい SDK バージョンが動作していることを確認してから、タグコンテナーに更新を公開します。

### トラブルシューティング {#troubleshooting}

#### タグデバッグを有効にする {#debugging}

それぞれのBraze タグ テンプレートにはオプションの**GTM タグ デバッグ** チェックボックスがあり、ウェブページのJavaScript コンソールへのデバッグメッセージのログ記録に使用できます。

![Google Tag Managerのデバッグツール]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### デバッグモードに入る

Google Tag Manager の統合をデバッグするもう1つの方法は、Google の [[プレビューモード](https://support.google.com/tagmanager/answer/6107056)] 機能を使用することです。

これにより、Web ページのデータレイヤーから、トリガーされた Braze 各タグに送信されている値を特定できるほか、トリガーされたタグとトリガーされなかったタグについても確認できます。

![Braze 初期化タグの概要ページには、トリガーされたタグに関する情報など、タグの概要が表示されます。]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### 詳細ログの有効化

Braze テクニカルサポートがテスト中にログにアクセスできるようにするには、Google Tag Manager 統合で詳細ログを有効にします。これらのログは、ブラウザーの[開発者ツール](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)の [**コンソール**] タブに表示されます。

Google Tag Manager 統合で、Braze 初期化タグに移動し、[**Web SDK ログを有効にする**] を選択します。

![Web SDK ログを有効にするオプションがオンになっている Braze 初期化タグの概要ページ。]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
