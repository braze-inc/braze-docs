---
nav_title: 統合
article_title: iOS のコンテンツカード統合
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "この記事では、コンテンツカードデータモデル、標準フィード UI オプション、その他のカードメソッドを含む Web 用コンテンツカード統合について説明します。"
search_rank: 1
---

# コンテンツカードの統合

> この記事では、コンテンツカードデータモデル、標準フィード UI オプション、その他のカードメソッドを含む Web 用コンテンツカード統合について説明します。

{% multi_lang_include archive/web-v4-rename.md %}

Braze Web SDKには、統合作業をスピードアップするためのコンテンツカードフィードUIが含まれています。代わりに独自の UI を構築したい場合は、『[コンテンツカードカスタマイズガイド』]({{site.baseurl}}/developer_guide/customization_guides/content_cards)を参照してください。

## 標準フィード UI

付属のコンテンツカード UI を使用するには、Web サイトのどこにフィードを表示するかを指定する必要があります。 

この例では、コンテンツカードフィードを配置したい場所があります。`<div id="feed"></div>`3 つのボタンを使用して、フィードの非表示、表示、切り替え (現在の状態に基づいて非表示または表示) を切り替えます。

\`\`\`html

<button id="toggle" type="button">カードフィードの切り替え</button>
<button id="hide" type="button">カードフィードを非表示</button>
<button id="show" type="button">カードフィードを表示</button>

<nav>
    <h1>カスタマイズしたフィード</h1>
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

`toggleContentCards(parentNode, filterFunction)``showContentCards(parentNode, filterFunction)`およびメソッドを使用する場合、引数が指定されていない場合、すべてのコンテンツカードがページの右側の固定位置のサイドバーに表示されます。それ以外の場合、`parentNode`フィードは指定されたオプションに配置されます。

|パラメーター | 説明 |
|---|---|
`parentNode`| | コンテンツカードをレンダリングする HTML ノード。親ノードに直系の子孫として既にBrazeコンテンツカードビューがある場合は、既存のコンテンツカードが置き換えられます。たとえば、渡す必要があります`document.querySelector(".my-container")`。|
| `filterFunction` | このビューに表示されるカードのフィルターまたはソート機能。`Card`でソートされたオブジェクトの配列で呼び出されます`{pinned, date}`。`Card`このユーザーにレンダリングするソートされたオブジェクトの配列を返すことが期待されています。省略すると、すべてのカードが表示されます。|
{: .reset-td-br-1 .reset-td-br-2}

[コンテンツカードの切り替えについて詳しくは、SDK リファレンスドキュメントを参照してください](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)。

## コンテンツカードデータモデル{#data-models}

コンテンツカードデータモデルは Web SDK で使用できます。

Braze Web SDK には次の 3 種類のコンテンツカードが用意されています。[画像のみ、キャプション付き画像](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)[[、クラシックカード。](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)各タイプはベースモデルから共通のプロパティを継承し、次の追加プロパティを持ちます。

カードデータの購読については、「[分析のロギング]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics)」を参照してください。

### 基本コンテンツカードモデルプロパティ-カード

すべてのコンテンツカードには次の共有プロパティがあります。

|プロパティ|説明|
|---|---|
|`expiresAt` | カードの有効期限の UNIX タイムスタンプ。
| `extras` |（オプション）値文字列を含む文字列オブジェクトとしてフォーマットされたキーと値のペアのデータ。|
| `id` | (オプション) カードの ID。これは、分析目的でイベントとともに Braze に報告されます。|
| `pinned` | このプロパティは、カードがダッシュボードで「固定」されるように設定されているかどうかを反映します。|
| `updated` | このカードが最後に変更されたときのUNIXタイムスタンプ。|
| `viewed` | このプロパティは、ユーザーがカードを閲覧したかどうかを反映します。|
| `isControl` | このプロパティは、カードがA/Bテスト内の「コントロール」`true` グループである場合です。| |
{: .reset-td-br-1 .reset-td-br-2}

### 画像のみコンテンツカードプロパティ-画像のみ

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) カードはクリック可能なフルサイズの画像です。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像の縦横比で、画像の読み込みが完了する前のヒントになります。特定の状況ではプロパティが提供されない場合があることに注意してください。|
| `categories` | このプロパティは、カスタム実装の整理のみを目的としています。これらのカテゴリはダッシュボードコンポーザーで設定できます。|
| `clicked` | このプロパティは、このカードがこのデバイスでこれまでにクリックされたことがあるかどうかを示します。|
| `created` | Braze からのカード作成時刻を示す UNIX タイムスタンプ。|
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示します。|
| `dismissible` | このプロパティは、ユーザーがカードを非表示にして表示されないようにできるかどうかを反映します。|
`imageUrl`| | カードの画像の URL。|
`linkText`| | URL の表示テキスト。|
`url`| | カードをクリックした後に開かれるURL。|
{: .reset-td-br-1 .reset-td-br-2}

### キャプション付き画像コンテンツカードのプロパティ-キャプション付き画像

[CaptionEdImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) カードは、説明文が付いた、クリック可能なフルサイズの画像です。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像の縦横比で、画像の読み込みが完了する前のヒントになります。特定の状況ではプロパティが提供されない場合があることに注意してください。|
| `categories` | このプロパティは、カスタム実装の整理のみを目的としています。これらのカテゴリはダッシュボードコンポーザーで設定できます。|
| `clicked` | このプロパティは、このカードがこのデバイスでこれまでにクリックされたことがあるかどうかを示します。|
| `created` | Braze からのカード作成時刻を示す UNIX タイムスタンプ。|
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示します。|
| `dismissible` | このプロパティは、ユーザーがカードを非表示にして表示されないようにできるかどうかを反映します。|
`imageUrl`| | カードの画像の URL。|
`linkText`| | URL の表示テキスト。|
| `title` | このカードのタイトルテキスト。|
`url`| | カードをクリックした後に開かれるURL。|
{: .reset-td-br-1 .reset-td-br-2}

### クラシックコンテンツカードのプロパティ-クラシックカード

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) モデルには、テキストのない画像または画像付きのテキストを含めることができます。

|プロパティ|説明|
|---|---|
| `aspectRatio` | カードの画像の縦横比で、画像の読み込みが完了する前のヒントになります。特定の状況ではプロパティが提供されない場合があることに注意してください。|
| `categories` | このプロパティは、カスタム実装の整理のみを目的としています。これらのカテゴリはダッシュボードコンポーザーで設定できます。|
| `clicked` | このプロパティは、このカードがこのデバイスでこれまでにクリックされたことがあるかどうかを示します。|
| `created` | Braze からのカード作成時刻を示す UNIX タイムスタンプ。|
| `description` | このカードの本文テキスト。|
| `dismissed` | このプロパティは、このカードが却下されたかどうかを示します。|
| `dismissible` | このプロパティは、ユーザーがカードを非表示にして表示されないようにできるかどうかを反映します。|
`imageUrl`| | カードの画像の URL。|
`linkText`| | URL の表示テキスト。|
| `title` | このカードのタイトルテキスト。|
`url`| | カードをクリックした後に開かれるURL。|
{: .reset-td-br-1 .reset-td-br-2}

## コントロールグループ  

デフォルトのコンテンツカードフィードを使用すると、インプレッションとクリックが自動的に追跡されます。

コンテンツカードにカスタムインテグレーションを使用する場合は、[コントロールカードが表示されたときのインプレッションを記録する必要があります]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/)。この取り組みの一環として、A/B テストでインプレッションを記録するときは、必ずコントロールカードを取り扱ってください。これらのカードは空白で、ユーザーには見えませんが、インプレッションを記録して、コントロールカード以外のカードとのパフォーマンスを比較する必要があります。

コンテンツカードが A/B テストのコントロールグループに含まれているかどうかを判断するには、`card.isControl`プロパティ (Web SDK v4.5.0+) を確認するか、カードがインスタンス () かどうかを確認します。`ControlCard` `card instanceof braze.ControlCard`

## カードメソッド

|メソッド | 説明 |
|---|---|
| [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| 指定されたカードリストのインプレッションイベントを記録します。これは、Braze UI ではなくカスタマイズされた UI を使用する場合に必要です。|
| [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| 指定されたカードのクリックイベントを記録します。これは、Braze UI ではなくカスタマイズされた UI を使用する場合に必要です。|
| [`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| ユーザーのコンテンツカードを表示します。|
| [`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| 現在表示されているブレイズコンテンツカードを非表示にする。|
| [`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| ユーザーのコンテンツカードを表示します。|
| [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|前回のコンテンツカード更新で現在利用可能なカードをすべて取得します。|
| [`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| コンテンツカードの更新を購読する.<br> サブスクライバーコールバックは、コンテンツカードが更新されるたびに呼び出されます。|
| [`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|プログラムでカードを消去する (v2.4.1で使用可能)|.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

詳細については、[SDK リファレンスドキュメントを参照してください](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)。

{% alert note %}
さらに進む準備はできましたか？コンテンツカードの基本を理解したら、[コンテンツカードカスタマイズガイドを参照してカスタマイズを開始してください]({{site.baseurl}}/developer_guide/customization_guides/content_cards)。
{% endalert %}
