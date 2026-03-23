{% multi_lang_include archive/web-v4-rename.md %}

## 前提条件

コンテンツカードを使用するには、[Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) をアプリに統合する必要があります。ただし、追加のセットアップは必要ありません。代わりに独自の UI を構築するには、[コンテンツカードカスタマイズガイド]({{site.baseurl}}/developer_guide/content_cards/)を参照してください。

## 標準フィード UI

付属のコンテンツカード UI を使用するには、Web サイト上のどこにフィードを表示するかを指定する必要があります。 

この例では、コンテンツカードフィードを配置する `<div id="feed"></div>` があります。3つのボタンを使って、フィードの非表示、表示、トグル（現在の状態に応じて非表示または表示）を切り替えます。

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

`toggleContentCards(parentNode, filterFunction)` および `showContentCards(parentNode, filterFunction)` メソッドを使用する際、引数が指定されない場合、すべてのコンテンツカードはページ右側の固定位置サイドバーに表示されます。引数が指定された場合は、フィードは指定された `parentNode` オプションに配置されます。

|パラメーター | 説明 |
|---|---|
|`parentNode` | コンテンツカードをレンダリングする HTML ノード。親ノードがすでに直系の子孫として Braze コンテンツカードビューを持っている場合、既存のコンテンツカードは置き換えられます。たとえば、`document.querySelector(".my-container")` を渡します。|
|`filterFunction` | このビューに表示されるカードのフィルターまたはソート関数。`Card` オブジェクトの配列で呼び出され、`{pinned, date}` でソートされます。このユーザーにレンダリングするソート済みの `Card` オブジェクトの配列を返す必要があります。省略した場合は、すべてのカードが表示されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

コンテンツカードの切り替えに関する詳細は、[SDK リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)を参照してください。

## Web でのコンテンツカードのテスト

ブラウザーの開発者ツールを使用して、コンテンツカードの統合をテストできます。

1. コンテンツカードキャンペーンを作成し、テストユーザーをターゲットにします。
2. Web SDK が統合されている Web サイトにログインします。
3. ブラウザーのコンソールを開きます。Chrome の場合、ページを右クリックし、**検証**を選択してから、**Console** タブを選択します。
4. コンソールで以下のコマンドを実行します。
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## カードの種類とプロパティ

コンテンツカードデータモデルは Web SDK で使用でき、次のコンテンツカードタイプを提供します。[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)、[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)、[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) です。各タイプはベースモデル [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) から共通のプロパティを継承し、以下の追加プロパティを持ちます。

{% alert tip %}
コンテンツカードデータを記録するには、[分析の記録]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)を参照してください。
{% endalert %}

### 基本カードモデル

すべてのコンテンツカードは、以下の共有プロパティを持っています。

|プロパティ|説明|
|---|---|
| `expiresAt` | カードの有効期限を示す UNIX タイムスタンプ。|
| `extras`| （オプション）値が文字列の文字列オブジェクトとしてフォーマットされたキーと値のペアデータ。 |
| `id` | （オプション）カードの ID。分析目的でイベントとともに Braze に報告されます。 |
| `pinned` | このプロパティは、カードがダッシュボードで「ピン留め」として設定されているかどうかを反映します。|
| `updated` | このカードが最後に変更された UNIX タイムスタンプ。 |
| `viewed` | このプロパティは、ユーザーがカードを閲覧したかどうかを反映します。|
| `isControl` | カードが A/B テスト内の「コントロール」グループである場合、このプロパティは `true` になります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 画像のみ

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) カードは、クリック可能なフルサイズの画像です。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比で、画像の読み込みが完了する前のヒントとして機能します。特定の状況ではこのプロパティが提供されない場合があります。 |
| `categories` | このプロパティは、カスタム実装での整理のみを目的としています。これらのカテゴリーはダッシュボードコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示します。 |
| `created` | Braze でのカード作成時間の UNIX タイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示します。 |
| `dismissible` | このプロパティは、ユーザーがカードを閉じてビューから削除できるかどうかを反映します。 |
| `imageUrl` | カードの画像の URL。|
| `linkText` | URL の表示テキスト。 |
| `url` | カードがクリックされた後に開かれる URL。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### キャプション付き画像

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) カードは、クリック可能なフルサイズの画像で、説明文が添えられています。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比で、画像の読み込みが完了する前のヒントとして機能します。特定の状況ではこのプロパティが提供されない場合があります。 |
| `categories` | このプロパティは、カスタム実装での整理のみを目的としています。これらのカテゴリーはダッシュボードコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示します。 |
| `created` | Braze でのカード作成時間の UNIX タイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示します。 |
| `dismissible` | このプロパティは、ユーザーがカードを閉じてビューから削除できるかどうかを反映します。 |
| `imageUrl` | カードの画像の URL。|
| `linkText` | URL の表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれる URL。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### クラシック

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) モデルは、テキストなしの画像、または画像付きのテキストを含むことができます。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比で、画像の読み込みが完了する前のヒントとして機能します。特定の状況ではこのプロパティが提供されない場合があります。 |
| `categories` | このプロパティは、カスタム実装での整理のみを目的としています。これらのカテゴリーはダッシュボードコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示します。 |
| `created` | Braze でのカード作成時間の UNIX タイムスタンプ。 |
| `description` | このカードの本文テキスト。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示します。 |
| `dismissible` | このプロパティは、ユーザーがカードを閉じてビューから削除できるかどうかを反映します。 |
| `imageUrl` | カードの画像の URL。|
| `linkText` | URL の表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれる URL。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## コントロールグループ

デフォルトのコンテンツカードフィードを使用すると、インプレッションとクリックが自動的に追跡されます。

コンテンツカード用のカスタム統合を使用している場合、コントロールカードが表示されるはずだったタイミングで[インプレッションを記録する]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)必要があります。この作業の一環として、A/B テストでインプレッションを記録する際には、必ずコントロールカードを処理するようにしてください。これらのカードは空白であり、ユーザーに表示されませんが、コントロールカードでないカードとのパフォーマンスを比較するために、インプレッションを記録する必要があります。

コンテンツカードが A/B テストのコントロールグループにあるかどうかを判断するには、`card.isControl` プロパティ（Web SDK v4.5.0+）を確認するか、カードが `ControlCard` インスタンス（`card instanceof braze.ControlCard`）かどうかをチェックします。

## カードメソッド

### デフォルトフィードメソッド

Braze のデフォルトフィード UI を使用してコンテンツカードを表示する場合は、以下のメソッドを使用します。

|メソッド | 説明 |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| デフォルトのコンテンツカードフィードを表示します。指定された `parentNode` HTML 要素にカードをレンダリングします。要素が指定されていない場合は、ページ右側の固定位置サイドバーとして表示されます。オプションの `filterFunction` を使用して、表示前にカードをソートまたはフィルターできます。 |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| 現在表示されているデフォルトのコンテンツカードフィードを非表示にします。 |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| デフォルトのコンテンツカードフィードが非表示の場合は表示し、表示されている場合は非表示にします。複数のコンテンツカードフィードを同時に表示する必要がある場合は、代わりに `showContentCards` と `hideContentCards` を使用してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### カスタムフィードメソッド

独自のコンテンツカード UI を構築する場合は、以下のメソッドを使用します。

|メソッド | 説明 |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| 現在のユーザーのコンテンツカードが更新されるたびに（セッション開始時など）呼び出されるコールバック関数を登録します。カスタムフィード用のカードデータを受信する主要な方法として使用してください。初回セッションの更新を受信するには、`openSession()` の前に呼び出す必要があります。 |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| 最新のコンテンツカード更新から、現在利用可能なすべてのカードを返します。新しいサーバーリクエストを待たずにページ読み込み時にカードを即座に表示する場合に使用します（例：アクティブなセッション中にユーザーがページに戻った場合）。 |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| Braze サーバーからコンテンツカードの即時更新をリクエストします。デフォルトでは、カードはセッション開始時およびデフォルトフィードが再度開かれたときに更新されます。特定のユーザーアクション後など、他のタイミングで強制的に更新する場合に使用します。[レート制限]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/#rate-limit)に注意してください。 |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| カードの配列に対してインプレッションイベントを記録します。カードがレンダリングされ、ユーザーに表示されたときに呼び出します。カスタム UI を使用する場合、デフォルトフィード以外ではインプレッションが自動的に追跡されないため、正確なキャンペーンレポートに必要です。 |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| 単一のカードに対してクリックイベントを記録します。カスタム UI でユーザーがカードを操作したときに呼び出します。デフォルトフィード以外ではクリックが自動的に追跡されないため、正確なキャンペーンレポートに必要です。 |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| カードの URL を処理し、設定されたクリック時アクション（Braze アクション（`brazeActions://` URL）や標準 URL ナビゲーションなど）を実行します。Braze ダッシュボードで設定されたクリック時の動作が実行されるように、カードのクリックハンドラーで呼び出してください。 |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| プログラムでカードを却下し、ユーザーのフィードから削除します。カスタム UI でユーザーがカードを却下できるようにする場合に使用します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

詳細については、[SDK リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

## ベストプラクティス

### メソッドを正しい順序で呼び出す

カスタムフィードの場合、`subscribeToContentCardsUpdates()` が `openSession()` の前に呼び出された場合にのみ、セッション開始時にコンテンツカードが更新されます。Braze メソッドは以下の順序で呼び出してください。

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### キャッシュされたカードを使用してページ読み込み間でコンテンツを保持する

`subscribeToContentCardsUpdates()` は新しい更新がある場合（セッション開始時など）にのみコールバックを呼び出すため、ユーザーがセッション中にページを更新すると、カスタムフィードからカードが消えることがあります。これを防ぐには、`getCachedContentCards()` を使用してローカルキャッシュからカードを即座にレンダリングし、新しい更新のサブスクリプションと併用してください。

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### カスタムフィードの分析を記録する

カスタム UI を使用する場合、インプレッション、クリック、却下は自動的に追跡されません。各イベントを手動で記録する必要があります。

- **インプレッション:** カードがユーザーに表示されたときに、カードオブジェクトの配列を指定して `logContentCardImpressions([card1, card2, ...])` を呼び出します。
- **クリック:** ユーザーがカードを操作したときに `logContentCardClick(card)` を呼び出します。
- **クリック時の動作:** カードに設定されたクリック時アクション（URL へのナビゲーションやカスタムイベントの記録など）を実行するために `handleBrazeAction(card.url)` を呼び出します。

{% alert warning %}
`logContentCardClick()` に渡す引数は、オリジナルの Braze `Card` オブジェクトである必要があります。カードデータを変換または再構築した場合（例：シリアライズとデシリアライズ）、クリックは記録されず、「card must be a Card object.」というエラーが表示されます。
{% endalert %}

## Google Tag Manager の使用

Google Tag Manager は、[Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn)（当社 Web SDK のバージョン）を Web サイトコードに直接注入することで機能します。これは、コンテンツカードを実装する場合を除き、Google Tag Manager なしで SDK を統合した場合と同様に、すべての SDK メソッドを利用できることを意味します。

### コンテンツカードの設定

{% tabs local %}
{% tab google tag manager %}
コンテンツカードフィードを標準的に統合するには、Google Tag Manager で**カスタム HTML** タグを使用できます。以下をカスタム HTML タグに追加すると、標準のコンテンツカードフィードが有効になります。

```html
<script>
   window.braze.showContentCards();
</script>
```

![コンテンツカードフィードを表示するカスタム HTML タグの Google Tag Manager でのタグ設定。]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
コンテンツカードとそのフィードの外観をより自由にカスタマイズするために、コンテンツカードをネイティブ Web サイトに直接統合できます。これには、標準フィード UI を使用する方法と、カスタムフィード UI を作成する方法の2つのアプローチがあります。

{% subtabs local %}
{% subtab standard feed %}
[標準フィード UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui) を実装する場合、Braze メソッドの先頭に `window.` を追加する必要があります。たとえば、`braze.showContentCards` の代わりに `window.braze.showContentCards` を使用します。
{% endsubtab %}

{% subtab custom feed %}
[カスタムフィード]({{site.baseurl}}/developer_guide/content_cards/creating_cards/)のスタイリングについては、GTM なしで SDK を統合した場合と同じステップです。たとえば、コンテンツカードフィードの幅をカスタマイズする場合は、以下を CSS ファイルに貼り付けます。

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

1. **タグテンプレートを更新する**<br>ワークスペース内の **Templates** ページに移動します。更新が利用可能であることを示すアイコンが表示されます。<br><br>![更新が利用可能であることを示すテンプレートページ]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>そのアイコンをクリックし、変更を確認した後、**Accept Update** をクリックします。<br><br>![新旧のタグテンプレートを比較した画面と「Accept Update」ボタン]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **バージョン番号を更新する**<br>タグテンプレートが更新されたら、Braze 初期化タグを編集し、SDK バージョンを最新の `major.minor` バージョンに更新します。たとえば、最新バージョンが `4.1.2` の場合、`4.1` と入力します。SDK のバージョン一覧は[変更ログ](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)で確認できます。<br><br>![SDK バージョンを変更するための入力フィールドを持つ Braze 初期化テンプレート]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA および公開**<br>Google Tag Manager の[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)を使用して、新しい SDK バージョンが動作していることを確認してから、タグコンテナーに更新を公開します。

### トラブルシューティング {#troubleshooting}

#### タグデバッグを有効にする {#debugging}

それぞれの Braze タグテンプレートにはオプションの **GTM Tag Debugging** チェックボックスがあり、Web ページの JavaScript コンソールにデバッグメッセージを記録するために使用できます。

![Google Tag Manager のデバッグツール]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### デバッグモードに入る

Google Tag Manager の統合をデバッグするもう1つの方法は、Google の[プレビューモード](https://support.google.com/tagmanager/answer/6107056)機能を使用することです。

これにより、Web ページのデータレイヤーからトリガーされた各 Braze タグに送信されている値を特定できるほか、トリガーされたタグとトリガーされなかったタグについても確認できます。

![Braze 初期化タグの概要ページには、どのタグがトリガーされたかを含むタグの概要が表示されます。]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### カスタムイベントのタグシーケンスを確認する {#tag-sequencing}

カスタムイベントやその他のアクションが Braze に記録されない場合、よくある原因は競合です。アクションタグ（**Custom Event** や **Purchase** など）が **Braze Initialization** タグの完了前に発火してしまうことがあります。これを修正するには、GTM で[タグシーケンス](https://support.google.com/tagmanager/answer/6238868)を設定します。

1. 正しく記録されていないアクションタグを開きます。
2. **Advanced Settings** > **Tag Sequencing** で、**A tag that fires before \[this tag\]** を選択します。
3. セットアップタグとして **Braze Initialization** タグを選択します。

これにより、アクションタグが Braze にデータを送信する前に、SDK が完全に初期化されることが保証されます。

#### 詳細ログの有効化

トラブルシューティング用の詳細なログをキャプチャするには、Google Tag Manager 統合で詳細ログを有効にできます。これらのログは、ブラウザーの[開発者ツール](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)の **Console** タブに表示されます。

Google Tag Manager 統合で、Braze 初期化タグに移動し、**Enable Web SDK Logging** を選択します。

![Braze 初期化タグの概要ページで、Web SDK ログを有効にするオプションがオンになっています。]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md