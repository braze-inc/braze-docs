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

1. メールの本文を開きます。
2. \[**リンク管理**] タブをクリックします。
3. Brazeは、各リンクに固有のデフォルトリンクエイリアスを自動的に生成する。
4. エイリアスに名前をつける。エイリアスは、メールキャンペーンのバリアントまたはキャンバスのコンポーネントごとに一意の名前にする必要があります。 

また、レポーティングやセグメンテーションを行う際に、特定のリンクを参照するためのエイリアスを設定することもできます。 

![][2]

リンクのエイリアシングは、クエリーパラメーターを付加しても安全なHTMLアンカータグ内の`href` 属性でのみサポートされている。Braze が `lid` の値を簡単に追加できるように、リンクの最後に疑問符 (?) を含めることをお勧めします。`lid` 。この値を追加しないと、Brazeはリンクエイリアス用のURLを認識しない。

### リンクエイリアスを管理する

以下の手順に従って、トラッキングされたリンクのエイリアスをすべて表示する：

1. \[**設定**] > \[**メール設定**] (\[**ワークスペース設定**] の下) に移動します。
2. \[**リンクエイリアスの設定**] タブをクリックします。

{% alert important %}
[古いナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)を使用している場合、これらの設定は \[**設定の管理**] にあります。
{% endalert %}

ここでは、すべてのリンクエイリアスを並べ替えたり検索したりすることもできる。

![キャンバスステップのアクティブな部分である「test」という名前のリンクエイリアスを示す「追跡されたリンクエイリアス」ページ。][8]

#### リンクエイリアスの追跡の解除

**リンクエイリアシング設定**タブでは、リンクエイリアスのトラッキングをオフにすることができる。

1. リンクエイリアスを選択する。
2. \[**追跡をオフにする**] をクリックします。  

#### エイリアスとユーザー・プロフィール・データをリンクする

Brazeでは、アプリやウェブサイトにリンクエイリアスがあり、ユーザーがそれをクリックすると、そのイベントがエイリアスを持つユーザーのプロファイルに記録される。後でこのリンクエイリアスの名前を変更しても、ユーザープロファイルの以前のクリックデータは更新さ**れず**、以前のリンクエイリアスとして表示される。そのため、新しいリンクエイリアスに基づいてユーザーをターゲットにした場合、以前のリンクエイリアスのデータは含まれない。

### ワークフローをチェックする

Brazeは、メール内のリンクを評価し、リンクテンプレートを追加し、セグメンテーションとレポート作成に有効な命名規則を提供することを推奨している。これは、すべてのリンクを追跡するのに役立つ。

リンクエイリアスが有効な場合、メッセージ、コンテンツブロック、リンクテンプレートは変更されない。リンク・テンプレートやコンテンツ・ブロックを使用した既存のメッセージも同じである。しかし、メッセージを更新すると、リンクエイリアスマークアップがすべてのリンクに適用されるため、リンクを表示するにはリンクテンプレートを適用し直す必要がある。

### データの抽出

\###\[List link alias for campaign][3] と \[List link alias for キャンバス][4] エンドポイントを使用して、キャンペーンまたはメール固有のキャンバスコンポーネントの各メッセージバリアントで設定された `alias` を抽出します。

## コンテンツブロックのリンクエイリアス

新しいコンテンツブロックのリンクが変更され、Braze は該当する各リンクに `lid={{placeholder}}` を追加します。このプレースホルダーの値は、Eメールメッセージバリアントに挿入されると解決される。

Brazeがリンクエイリアスを有効にする前に作成された既存のコンテンツブロック内のリンクを修正するには、既存のコンテンツブロックを複製し、複製したコンテンツブロック内のリンクを修正する。

`lid` 値を持たないコンテンツブロックを新しいメッセージに挿入した場合、そのコンテンツブロックからのリンクはエイリアスで追跡されない。新しいコンテンツブロックが「古い」メッセージバリアントに挿入されると、そのメッセージバリアントからのリンクはリンクエイリアスによって認識されます。コンテンツブロックからのリンクも認識される。ただし、「古い」コンテントブロックが「新しい」コンテントブロックをネストすることはできません。

{% alert tip %}
Braze では、コンテンツブロックについては、既存のコンテンツブロックのコピーを作成し、新しいメッセージで使用することをお勧めします。これは、新規メッセージ内でリンクエイリアスが有効になっていないコンテンツブロックを参照してしまう可能性を回避するために、一括複製によって行うことができます。
{% endalert %}

## 例

以下の表は、Eメール本文のリンクの例、リンクのエイリアシングの結果、リンクのエイリアシングによって元のリンクがどのように更新されるかの説明である。

| メール本文にリンクを貼る | エイリアスによるリンク | ロジック |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Brazeはクエスチョンマーク(?)を挿入し、最初のクエリーパラメーターをURLに追加する。 |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze は他のクエリパラメーターを検出し、URL の末尾に `lid=` を追加します。 |
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} | BrazeはこれがURLであることを認識し、すでにクエスチョンマーク（?）そして、疑問符の後にクエリパラメーター `lid` を追加します。 |
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

新しいメッセージバリアントには、**リンク管理**タブから既存の[リンクテンプレートを]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/)使うことができる。リンクテンプレートを使って開始されたメッセージには、リンクテンプレートが適用されます。既存のメッセージが変更された場合、リンク**管理**タブからリンクテンプレートを再適用する必要がある。 

{% alert note %}
リンクテンプレートは、**リンク管理**タブに表示されているリンクにのみ適用できる。つまり、"古い "コンテンツブロックやマークアップできないリンクなど、`lid` URLパラメータを持たないリンクは、リンクテンプレートの対象外となる。これを解決するには、「古い」コンテンツブロックをコピーするか、URL の `href` 属性に疑問符 (?) またはアンパサンド （&） を含めることをお勧めします。
{% endalert %}

## リンク・セグメンテーション

エイリアスフィルターのリターゲティングを使用すると、顧客がメールキャンペーンまたはキャンバスコンポーネントのいずれかから特別に追跡されたエイリアスをクリックする行動に基づいて、セグメンテーションフィルターを作成できます。このフィルターは、追跡されたエイリアスが存在するキャンペーンまたはキャンバスにのみ使用できる。

### トラッキングリンク

\[**リンク管理**] タブで、セグメンテーションのために「追跡」する、セグメンテーションフィルターに含めるエイリアスを選択します。追跡されるエイリアスはセグメンテーションのためだけのものであり、あなたのリンクがレポート目的で追跡されることには何の影響もないことに注意されたい。

{% alert tip %}
リンクのエンゲージメントの指標を追跡するには、リンクの前にHTTPまたはHTTPSのいずれかがあることを確認する。
{% endalert %}

Brazeでは、追跡するリンクを無制限に選択することができるが、ユーザーが開いた直近のリンクに限ってリターゲティングすることができる。ユーザープロファイルには、最近クリックした 100 個のリンクが含まれています。例えば、500のリンクを追跡し、ユーザーが500のリンクをすべてクリックした場合、最近クリックされた100のリンクに基づいてリターゲティングやセグメントを作成することができる。

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

キャンバスコンポーネントでクリックした特定のエイリアスに基づき、ユーザーをリターゲティングします。パイプ区切りのフィルターオプションは、キャンバスとキャンバスコンポーネントを表示し、その後にキャンバスコンポーネント内のエイリアスを表示します。ここでは、追跡されたエイリアスを持つキャンバスのステップのみが表示される。

#### キャンペーンまたはキャンバスでエイリアスをクリックした

キャンペーンまたはキャンバスコンポーネントでクリックした任意のエイリアスに基づき、ユーザーをリターゲティングします。エイリアスは「グローバル」と見なされるため、グローバルエイリアスはすべてのキャンペーンとキャンバスのステップからのリンククリックをターゲットにする。

![][5]

### アクションベースのフィルター
 
あらゆるリンク（トラッキング済み、未トラッキング）をターゲットとしたアクションベースのメッセージを作成したり、あらゆるメールキャンペーンやキャンバスのコンポーネントのエイリアスをクリックしたユーザーに基づいたリターゲティングを行うことができる。 

![][6]

### 電子メールのクリック・イベント

\[メールクリック数イベント][7] は、ユーザーがメールをクリックしたときに発生します。ユーザーがメールを複数回クリックしたり、メール内の異なるリンクをクリックしたりすると、同じキャンペーンについて複数のイベントが生成される場合があります。リンクエイリアスが有効な場合、Eメールクリックイベントに2つの追加フィールドがある：`link_id` と`link_alias` 。

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

_更新は 2019 年 8 月に記録されました。_
{% endalert %}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/
[8]: {% image_buster /assets/img/tracked_aliases.png %}