---
nav_title: 統合
article_title: Web 向けコンテンツカードの統合
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "この記事では、コンテンツカードデータモデル、標準フィード UI オプション、追加のカードメソッドなど、Web 用のコンテンツカード統合について説明します。"
search_rank: 1
---

# コンテンツカードの統合

> この記事では、コンテンツカードデータモデル、標準フィード UI オプション、追加のカードメソッドなど、Web 用のコンテンツカード統合について説明します。

{% multi_lang_include archive/web-v4-rename.md %}

Braze Web SDK には、統合作業をスピードアップするコンテンツカードフィード UI が含まれています。代わりに独自のUIを構築したい場合は、[コンテンツ・カードのカスタマイズ・ガイドを]({{site.baseurl}}/developer_guide/customization_guides/content_cards)参照のこと。

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

## コンテンツカードデータモデル{#data-models}

コンテンツカードのデータモデルは、Web SDK で利用できます。

Braze Web SDK には、3種類のコンテンツカードがあります。[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)、[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)、[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)である。各タイプは、[ベースモデルカードから](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)共通のプロパティを継承し、以下の追加プロパティを持つ。

カードデータの購読については、「[分析のロギング]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics)」を参照してください。

### ベース・コンテンツ・カード・モデルのプロパティ - カード

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

### 画像のみのコンテンツカード・プロパティ - ImageOnly

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

### キャプション付き画像 コンテンツカードのプロパティ - CaptionedImage

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

### クラシックコンテンツカードのプロパティ - ClassicCard

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

コンテンツカード用のカスタム統合を使用している場合、コントロールカードが表示されたときの[インプレッションを記録する]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/)必要があります。この作業の一環として、AB テストでインプレッションを記録する際には、必ずコントロールカードを処理するようにしてください。これらのカードは空白であり、ユーザーに表示されませんが、コントロールカードでないカードとのパフォーマンスを比較するために、インプレッションを記録する必要がある。

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

{% alert note %}
さらに上を目指す準備はできているか？コンテンツカードの基本を理解したら、[コンテンツカードカスタマイズガイドを]({{site.baseurl}}/developer_guide/customization_guides/content_cards)参照してカスタマイズを始めよう。
{% endalert %}
