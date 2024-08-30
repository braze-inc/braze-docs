---
nav_title: 統合
article_title: コンテンツ・カードのウェブへの統合
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "この記事では、Content Cardデータモデル、標準フィードUIオプション、追加のカードメソッドなど、Web用のContent Card統合について説明する。"
search_rank: 1
---

# コンテンツカードの統合

> この記事では、Content Cardデータモデル、標準フィードUIオプション、追加のカードメソッドなど、Web用のContent Card統合について説明する。

{% multi_lang_include archive/web-v4-rename.md %}

Braze Web SDKには、Content CardsフィードUIが含まれており、統合作業をスピードアップできる。代わりに独自のUIを構築したい場合は、[コンテンツ・カードのカスタマイズ・ガイドを]({{site.baseurl}}/developer_guide/customization_guides/content_cards)参照のこと。

## 標準フィードUI

付属のContent Cards UIを使用するには、ウェブサイト上のどこにフィードを表示するかを指定する必要がある。 

この例では、Content Cardsのフィードを置きたい`<div id="feed"></div>` 。3つのボタンを使って、フィードの非表示、表示、トグル（現在の状態に応じて非表示、表示）を切り替える。

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
|`parentNode` | コンテンツカードをレンダリングするHTMLノード。親ノードがすでに直系の子孫としてBraze Content Cardsビューを持っている場合、既存のContent Cardsは置き換えられる。例えば、`document.querySelector(".my-container")` 。|
|`filterFunction` | このビューに表示されるカードのフィルターまたはソート機能。`{pinned, date}` でソートされた`Card` オブジェクトの配列で呼び出される。このユーザーにレンダリングするために、ソートされた`Card` オブジェクトの配列を返すことが期待される。省略した場合は、すべてのカードが表示される。 |
{: .reset-td-br-1 .reset-td-br-2}

コンテンツカードの切り替えに関する詳細は、[SDKリファレンスドキュメントを参照のこと](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)。

## コンテンツカードデータモデル{#data-models}

コンテンツ・カードのデータ・モデルは、Web SDKで利用できる。

Braze Web SDKには、3種類のコンテンツカードがある：[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)、[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)、[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)である。各タイプは、[ベースモデルカードから](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)共通のプロパティを継承し、以下の追加プロパティを持つ。

カードデータの購読については、「[分析のロギング]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics)」を参照してください。

### ベース・コンテンツ・カード・モデルのプロパティ - カード

すべてのコンテンツ・カードは、これらの共有プロパティを持っている：

|プロパティ|説明|
|---|---|
| `expiresAt` | カードの有効期限を示すUNIXタイムスタンプ。|
| `extras`| (オプション）値文字列を持つ文字列オブジェクトとしてフォーマットされたキーと値のペアデータ。 |
| `id` | (オプション）カードのID。これは、分析目的でイベントとともにBrazeに報告される。 |
| `pinned` | このプロパティは、カードがダッシュボードで「ピン留め」されているかどうかを反映する。|
| `updated` | このカードが最後に更新されたUNIXタイムスタンプ。 |
| `viewed` | このプロパティは、ユーザがカードを閲覧したかどうかを反映する。|
| `isControl` | このプロパティは、カードがA/Bテスト内の「コントロール」グループである場合、`true` 。|
{: .reset-td-br-1 .reset-td-br-2}

### 画像のみのコンテンツカード・プロパティ - ImageOnly

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)カードは、クリック可能なフルサイズの画像である。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比。画像の読み込みが完了する前のヒントとなる。なお、状況によっては提供できない場合もある。 |
| `categories` | このプロパティは、純粋にカスタム実装で整理するためのもので、これらのカテゴリーはダッシュボード・コンポーザーで設定できる。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示す。 |
| `created` | Brazeからのカード作成時間のUNIXタイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示す。 |
| `dismissible` | このプロパティは、ユーザがカードを削除できるかどうかを反映する。 |
| `imageUrl` | カードの画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2}

### キャプション付き画像 コンテンツカードのプロパティ - CaptionedImage

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)カードは、クリック可能なフルサイズの画像で、説明文が添えられている。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比。画像の読み込みが完了する前のヒントとなる。なお、状況によっては提供できない場合もある。 |
| `categories` | このプロパティは、純粋にカスタム実装で整理するためのもので、これらのカテゴリーはダッシュボード・コンポーザーで設定できる。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示す。 |
| `created` | Brazeからのカード作成時間のUNIXタイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示す。 |
| `dismissible` | このプロパティは、ユーザがカードを削除できるかどうかを反映する。 |
| `imageUrl` | カードの画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2}

### クラシック・コンテンツ・カードのプロパティ - ClassicCard

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)モデルは、テキストなしの画像、または画像付きのテキストを含むことができる。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像のアスペクト比。画像の読み込みが完了する前のヒントとなる。なお、状況によっては提供できない場合もある。 |
| `categories` | このプロパティは、純粋にカスタム実装で整理するためのもので、これらのカテゴリーはダッシュボード・コンポーザーで設定できる。 |
| `clicked` | このプロパティは、このカードがこのデバイスでクリックされたことがあるかどうかを示す。 |
| `created` | Brazeからのカード作成時間のUNIXタイムスタンプ。 |
| `description` | このカードの本文。 |
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示す。 |
| `dismissible` | このプロパティは、ユーザがカードを削除できるかどうかを反映する。 |
| `imageUrl` | カードの画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2}

## 対照群 

デフォルトのContent Cardsフィードを使用すると、インプレッションとクリックが自動的に追跡される。

コンテンツカード用のカスタム統合を使用している場合、コントロールカードが表示されたときの[インプレッションを記録する]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/)必要がある。この取り組みの一環として、A/Bテストでインプレッションを記録する際には、必ずコントロールカードを扱うようにする。これらのカードは空白であり、ユーザーに見られることはないが、コントロールカードでないカードとのパフォーマンスを比較するために、インプレッションを記録する必要がある。

コンテンツカードがA/Bテストのコントロールグループにあるかどうかを判断するには、`card.isControl` プロパティ（Web SDK v4.5.0+）をチェックするか、カードが`ControlCard` インスタンス（`card instanceof braze.ControlCard` ）かどうかをチェックする。

## カードメソッド

|方法 | 説明 |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| 与えられたカードのリストに対して印象イベントを記録する。これは、Braze UIではなく、カスタマイズされたUIを使用する場合に必要である。|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| 指定されたカードのクリックイベントをログに記録する。これは、Braze UIではなく、カスタマイズされたUIを使用する場合に必要である。| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| ユーザーのコンテンツカードを表示する。 |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| 現在表示されているBrazeコンテンツカードを非表示にする。 | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| ユーザーのコンテンツカードを表示する。 | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|前回のコンテンツカードの更新から、現在利用可能なすべてのカードを取得する。|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| コンテンツカードのアップデートを購読する。<br> サブスクライバーのコールバックは、コンテンツカードが更新されるたびに呼び出される。 | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|プログラムでカードを解除する（v2.4.1で利用可能）。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

詳細については、[SDKリファレンス・ドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)参照のこと。

{% alert note %}
さらに上を目指す準備はできているか？コンテンツカードの基本を理解したら、[コンテンツカードカスタマイズガイドを]({{site.baseurl}}/developer_guide/customization_guides/content_cards)参照してカスタマイズを始めよう。
{% endalert %}
