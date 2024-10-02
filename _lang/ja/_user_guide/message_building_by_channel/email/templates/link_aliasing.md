---
nav_title: リンクのエイリアシング
article_title: リンクのエイリアシング
alias: /link_aliasing/
page_order: 3
description: "この記事では、リンクのエイリアシングがどのように機能し、リンクがどのように見えるかを説明する。"
channel:
  - email

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}リンクエイリアス
 
> リンクエイリアスを使用して、Brazeからの電子メールメッセージで送信されるリンクを識別するために、認識可能なユーザー生成名を作成する。これらのリンクは、セグメンテーション・リターゲティング、アクションベースのトリガー、リンク分析に利用できる。リンクエイリアスは、特定のリンクをクリックしたユーザーを再ターゲットする機能を提供し、ユーザーがエイリアスされた特定のリンクをクリックしたときにアクションベースのトリガーを作成することを可能にする。

## リンクエイリアスを作成する

リンクエイリアスは、Eメールチャンネル内のリンクにブレイズが生成したクエリーパラメーターを装飾することで機能する。リンクエイリアスを作成するには、以下の手順に従う： 

1. メール本文を開く。
2. **リンク管理**タブをクリックする。
3. Brazeは、各リンクに固有のデフォルトリンクエイリアスを自動的に生成する。
4. エイリアスに名前をつける。エイリアスは、メールキャンペーンのバリアントまたはキャンバスのコンポーネントごとに一意に命名する必要がある。 

また、レポーティングやセグメンテーションを行う際に、特定のリンクを参照するためのエイリアスを設定することもできる。 

![][2]

リンクのエイリアシングは、クエリーパラメーターを付加しても安全なHTMLアンカータグ内の`href` 属性でのみサポートされている。Brazeが簡単に`lid` 。`lid` 。この値を追加しないと、Brazeはリンクエイリアス用のURLを認識しない。

### リンクエイリアスを管理する

以下の手順に従って、トラッキングされたリンクのエイリアスをすべて表示する：

1. **ワークスペース設定]の** **\[設定]>**\[**電子メール設定]**に移動する。
2. **Link Aliasing Settings**タブをクリックする。

{% alert important %}
[古いナビゲーションを]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)使用している場合、これらの設定は「**設定の管理**」にある。
{% endalert %}

ここでは、すべてのリンクエイリアスを並べ替えたり検索したりすることもできる。

![キャンバスのステップのアクティブな部分である「test」という名前のリンクエイリアスを示す「Tracked Link Aliases」ページ。][8]

#### リンク・エイリアスの追跡を解除する

**リンクエイリアシング設定**タブでは、リンクエイリアスのトラッキングをオフにすることができる。

1. リンクエイリアスを選択する。
2. **トラッキングをオフにするを**クリックする。  

#### エイリアスとユーザー・プロフィール・データをリンクする

Brazeでは、アプリやウェブサイトにリンクエイリアスがあり、ユーザーがそれをクリックすると、そのイベントがエイリアスを持つユーザーのプロファイルに記録される。後でこのリンクエイリアスの名前を変更しても、ユーザープロファイルの以前のクリックデータは更新さ**れず**、以前のリンクエイリアスとして表示される。そのため、新しいリンクエイリアスに基づいてユーザーをターゲットにした場合、以前のリンクエイリアスのデータは含まれない。

### ワークフローをチェックする

Brazeは、メール内のリンクを評価し、リンクテンプレートを追加し、セグメンテーションとレポート作成に有効な命名規則を提供することを推奨している。これは、すべてのリンクを追跡するのに役立つ。

リンクエイリアスが有効な場合、メッセージ、コンテンツブロック、リンクテンプレートは変更されない。リンク・テンプレートやコンテンツ・ブロックを使用した既存のメッセージも同じである。しかし、メッセージを更新すると、リンクエイリアスマークアップがすべてのリンクに適用されるため、リンクを表示するにはリンクテンプレートを適用し直す必要がある。

### データを抽出する

List link alias for campaign][3] と \[List link alias for Canvas][4] ] エンドポイントを使用して、キャンペーンまたはメール固有のキャンバスコンポーネントの各メッセージバリアントで設定された`alias` を抽出する。

## コンテンツブロックのリンクエイリアス

新しいコンテンツブロックはリンクが変更され、Brazeは各リンクに`lid={{placeholder}}` 。このプレースホルダーの値は、Eメールメッセージバリアントに挿入されると解決される。

Brazeがリンクエイリアスを有効にする前に作成された既存のコンテンツブロック内のリンクを修正するには、既存のコンテンツブロックを複製し、複製したコンテンツブロック内のリンクを修正する。

`lid` 値を持たないコンテンツブロックを新しいメッセージに挿入した場合、そのコンテンツブロックからのリンクはエイリアスで追跡されない。新しいコンテンツブロックが「古い」メッセージバリアントに挿入されると、そのメッセージバリアントからのリンクはリンクエイリアスによって認識される。コンテンツブロックからのリンクも認識される。しかし、「古い」コンテンツ・ブロックは「新しい」コンテンツ・ブロックをネストすることはできない。

{% alert tip %}
コンテンツブロックについては、既存のコンテンツブロックのコピーを作成し、新しいメッセージで使用することを推奨する。これは、リンクエイリアスが有効になっていないコンテンツブロッ クを新しいメッセージで参照するようなシナリオを防ぐために、一括複 製によって行うことができる。
{% endalert %}

## 例

以下の表は、Eメール本文のリンクの例、リンクのエイリアシングの結果、リンクのエイリアシングによって元のリンクがどのように更新されるかの説明である。

| メール本文にリンクを貼る | エイリアシング・リンク | ロジック |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Brazeはクエスチョンマーク(?)を挿入し、最初のクエリーパラメーターをURLに追加する。 |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Brazeは他のクエリーパラメーターを検出し、URLの最後に`lid=` 。 |
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} | BrazeはこれがURLであることを認識し、すでにクエスチョンマーク（?）そして、`lid` クエリーパラメーターをクエスチョンマークの後に追加する。 |
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email | Brazeは、クエスチョンマーク(?)の後にアンカー(#)がある標準的なURL構造を期待する。Brazeは左から右に読むので、アンカーの前にクエスチョンマークと`lid` 。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Liquid経由で生成されたURLのリンクエイリアス

HTMLまたはコンテンツ・ブロック内の`assign` ステートメントによって生成されるURLについては、アンカー・タグにクエスチョンマーク（？）を追加することを推奨する。これにより、Brazeがクエリーパラメーター（`lid = somevalue` ）を追加し、リンクエイリアスが正しく機能するようになる。クエリパラメータを追加する場所を特定しなければ、リンクエイリアスはこれらのURLを認識できない。

### 例

アンカータグの推奨フォーマットについては、リンクエイリアスの例をチェックしてほしい：

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

リンク内にクエスチョンマーク（`?` ）を含むパラメータがある場合は、この例のように、アンカータグ内のクエスチョンマークをアンパサンド（`&` ）に置き換えることができる：

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}

## リンクテンプレート

新しいメッセージバリアントには、**リンク管理**タブから既存の[リンクテンプレートを]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/)使うことができる。リンク・テンプレートを使って開始されたメッセージには、リンク・テンプレートが適用される。既存のメッセージが変更された場合、リンク**管理**タブからリンクテンプレートを再適用する必要がある。 

{% alert note %}
リンクテンプレートは、**リンク管理**タブに表示されているリンクにのみ適用できる。つまり、"古い "コンテンツブロックやマークアップできないリンクなど、`lid` URLパラメータを持たないリンクは、リンクテンプレートの対象外となる。これを解決するには、"古い "コンテンツブロックをコピーするか、URLの`href` 属性にクエスチョンマーク（？）またはアンパサンド（&）を含めることをお勧めする。
{% endalert %}

## リンク・セグメンテーション

エイリアスのリターゲティングフィルタは、メールキャンペーンまたはキャンバスコンポーネントのどちらかから特別に追跡されたエイリアスをクリックした顧客に基づいてセグメンテーションフィルタを作成することができる。このフィルターは、追跡されたエイリアスが存在するキャンペーンまたはキャンバスにのみ使用できる。

### トラッキングリンク

**リンク管理]**タブで、セグメンテーションのために "追跡 "し、セグメンテーション・フィルターに存在させたいエイリアスを選択する。追跡されるエイリアスはセグメンテーションのためだけのものであり、あなたのリンクがレポート目的で追跡されることには何の影響もないことに注意されたい。

{% alert tip %}
リンクのエンゲージメントの指標を追跡するには、リンクの前にHTTPまたはHTTPSのいずれかがあることを確認する。
{% endalert %}

Brazeでは、追跡するリンクを無制限に選択することができるが、ユーザーが開いた直近のリンクに限ってリターゲティングすることができる。ユーザーのプロフィールには、最近クリックされた100のリンクが含まれている。例えば、500のリンクを追跡し、ユーザーが500のリンクをすべてクリックした場合、最近クリックされた100のリンクに基づいてリターゲティングやセグメントを作成することができる。

{% tabs local %}
{% tab ドラッグ・アンド・ドロップ・エディター %}

![ドラッグ＆ドロップ・メール・エディタのリンク管理タブ]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTMLエディタ %}

![HTMLメールエディターのリンク管理タブ]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Brazeは、プロフィールレベルで、過去100回クリックされたリンクエイリアスのみを追跡する。
{% endalert %}

### リンクの追跡を解除する

リンクのトラッキングを解除しても、そのフィルタを持つ既存のセグメントは、トラッキングされていないエイリアスに再割り当てされない。古いデータは、新しいデータに置き換わるまでユーザー・プロファイルに残る。以下のセグメンテーション・フィルターは存在し続けるが、そのフィルターを使って新しいセグメントを作成することはできない。

セグメンテーションのため、デフォルトでは1ワークスペースにつき100リンクしか追跡できない。アーカイブされたメッセージのリンクは自動的に追跡解除される。しかし、アーカイブされたメッセージがアーカイブされない場合、リンクを再度追跡する必要がある。リンクエイリアスが追跡される場合、リンクレポートはトップレベルドメインや完全なURLではなく、エイリアスによってインデックスされる。

![][1]

### セグメントフィルター

以下のセグメントフィルターは、イベント処理時に追跡されるクリックイベントに適用される。つまり、リンクの追跡を解除しても既存のデータは削除されず、リンクを追跡してもデータは埋め戻されない。

#### キャンペーンでエイリアスをクリックした

キャンペーンでクリックされた特定のエイリアスに基づき、ユーザーをリターゲティングする。追跡されたエイリアスを持つキャンペーンのみがここに反映される。

#### キャンバスステップでエイリアスをクリック

キャンバスコンポーネントでクリックされた特定のエイリアスに基づき、ユーザーを再ターゲットする。パイプで区切られたフィルターオプションは、CanvasとCanvasコンポーネントを表示し、その後にCanvasコンポーネント内のエイリアスを表示する。ここでは、追跡されたエイリアスを持つキャンバスのステップのみが表示される。

#### キャンペーンまたはキャンバスでエイリアスをクリックした

キャンペーンまたはキャンバスコンポーネントでクリックされたエイリアスに基づき、ユーザーをリターゲティングする。エイリアスは「グローバル」と見なされるため、グローバルエイリアスはすべてのキャンペーンとキャンバスのステップからのリンククリックをターゲットにする。

![][5]

### アクションベースのフィルター
 
あらゆるリンク（トラッキング済み、未トラッキング）をターゲットとしたアクションベースのメッセージを作成したり、あらゆるメールキャンペーンやキャンバスのコンポーネントのエイリアスをクリックしたユーザーに基づいたリターゲティングを行うことができる。 

![][6]

### 電子メールのクリック・イベント

email clicks イベント][7] は、ユーザーがEメールをクリックしたときに発生する。ユーザーがメールを複数回クリックしたり、メール内の異なるリンクをクリックしたりすると、同じキャンペーンについて複数のイベントが生成される場合があります。リンクエイリアスが有効な場合、Eメールクリックイベントに2つの追加フィールドがある：`link_id` と`link_alias` 。

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
Brazeはキャンバスのステップ（スケジュール可能なエントリーステップを除く）を、たとえ「スケジュール」されていても、トリガーされたイベントとして扱うため、`dispatch_id` の動作はキャンバスとキャンペーンで異なる。Canvasとキャンペーンにおける[`dispatch_id` 行動について]({{site.baseurl}}/help/help_articles/data/dispatch_id/)詳しく知る。

_更新は2019年8月に行われる。_
{% endalert %}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/
[8]: {% image_buster /assets/img/tracked_aliases.png %}