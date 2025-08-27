---
nav_title: リンクのエイリアシング
article_title: リンクのエイリアシング
alias: /link_aliasing/
page_order: 3
description: "この記事では、リンクエイリアスがどのように機能するかを説明し、リンクがどのように見えるかの例を示す。"
channel:
  - email

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}リンクエイリアス
 
> リンクエイリアスを使用して、Brazeからの電子メールメッセージで送信されるリンクを識別するために、認識可能なユーザー生成名を作成する。これらのリンクは、セグメンテーション・リターゲティング、アクションベースのトリガー、リンク分析に利用できる。

## リンクエイリアスについて

リンクエイリアスを使用すると、ユーザー生成名を作成して、メールで送信されたリンクを識別子し、追跡することができる。こうすることで、エンゲージメントを追跡し、キャンペーンのパフォーマンスを分析するために、完全なリンクを参照することなく、メール内でこれらの認識可能なリンクエイリアスを効率的に使用することができる。

リンクエイリアスを使用すると、以下のことができます。

- **特定のリンクをクリックしたユーザーをリターゲティングする：**リンクをクリックしたユーザーを識別子し、ターゲットを絞る。
- **アクションベースのトリガーを作成する：**ユーザーがリンクをクリックしたときにメールを送信する。
- **指標を分析する。**何人のユーザーがリンクAとリンクBをクリックしたかを比較する。

### 仕組み

Brazeは、`lid` （リンク識別子とも呼ばれる）と呼ばれる追加パラメータをすべてのリンクURLに付加することで、メール内のリンクを一意に識別する。この`lid` の値により、Brazeは、URLパラメータの残りの部分が異なっていても、リンクに対するユーザーインタラクションを追跡、監視、集計することができる。これにより、ユーザーがメールキャンペーンのコンテンツに対するユーザーのエンゲージメントに関するインサイトを提供できるようになります。

## リンクエイリアスを作成する

リンクエイリアスを作成するには、以下の手順に従う： 

1. キャンペーンまたはキャンバスコンポーネントで、メール本文に移動します。
2. [**リンク管理**] タブを選択します。
3. Brazeは、各リンクに固有のデフォルトリンクエイリアスを自動的に生成する。
4. エイリアスに名前をつける。エイリアスは、メールキャンペーンのバリアントまたはキャンバスのコンポーネントごとに一意の名前にする必要があります。 

また、レポーティングやセグメンテーションを行う際に、特定のリンクを参照するためのエイリアスを設定することもできます。 

![4つのリンクエイリアスを持つリンクマネージメントページ]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
リンクのエイリアシングは、クエリーパラメーターを付加しても安全なHTMLアンカータグ内の`href` 属性でのみサポートされている。Brazeが簡単に`lid` の値を追加できるように、リンクの最後にクエスチョンマーク(?)を付けるのがベストプラクティスだ。`lid` 。この値を追加しないと、Brazeはリンクエイリアス用のURLを認識しない。
{% endalert %}

## リンクエイリアスを管理する

トラッキングしたリンクエイリアスをすべて表示するには、以下のようにする：

1. [**設定**] > [**メール設定**] ([**ワークスペース設定**] の下) に移動します。
2. **リンクエイリアス設定**タブを選択する。

{% alert important %}
[古いナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)を使用している場合、これらの設定は [**設定の管理**] にあります。
{% endalert %}

ここでは、並べ替え、検索、リンクエイリアスのトラッキング追跡をオフにすることができる。

![Eメール_アンケート "という名前のキャンペーンに関連付けられている "TechPartners "と "Help "という名前の2つのリンクエイリアスを示すトラッキング追跡リンクエイリアスページ。]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
[List link alias for campaign]({{site.baseurl}}/get_campaign_link_alias/)および[List link alias for Canvas]({{site.baseurl}}/get_canvas_link_alias/)エンドポイントを使用して、キャンペーンまたはメール固有のキャンバスコンポーネントの各メッセージバリアントに設定された`alias` を抽出する。
{% endalert %}

Brazeは、メール内のリンクを評価し、リンクテンプレートを追加し、セグメンテーションとレポート作成に有効な命名規則を提供することを推奨している。これは、すべてのリンクを追跡するのに役立つ。

リンクエイリアスがオンの場合、メッセージ、コンテンツブロック、リンクテンプレートは変更されない。リンク・テンプレートやコンテンツ・ブロックを使用した既存のメッセージも同じである。しかし、メッセージを更新すると、リンクエイリアスマークアップがすべてのリンクに適用されるため、リンクを表示するにはリンクテンプレートを適用し直す必要がある。

## リンクエイリアスによるリンクの更新方法

以下の表は、メール本文のリンクの例、リンクエイリアスの結果、リンクエイリアスによって元のリンクがどのように更新されるかの説明である。

### パーマリンク

**ロジック:**Brazeはクエスチョンマーク(?)を挿入し、最初のクエリーパラメーターをURLに追加する。

| メール本文にリンクを貼る    | エイリアスによるリンク                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### より多くのクエリーパラメーターを持つリンク

**ロジック:**Braze は他のクエリパラメーターを検出し、URL の末尾に `lid=` を追加します。

| メール本文にリンクを貼る                                            | エイリアスによるリンク                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTMLリンク

**ロジック:**Brazeは、リンクがURLであり、すでにクエスチョンマーク(?)があると認識するため、クエスチョンマークの後に`lid` クエリーパラメータが追加される。

| メール本文にリンクを貼る                                                | エイリアスによるリンク                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### アンカー付きリンク

**ロジック:**Brazeは、クエスチョンマーク(?)の後にアンカー(#)がある標準的なURL構造を期待する。Brazeは左から右に読むので、クエスチョンマークと`lid` の値はアンカーの前に付加される。

| メール本文にリンクを貼る                               | エイリアスによるリンク                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### アンカーとキャプチャタグによるリンク

**ロジック:**アンカー(#)を含むURLでリンクエイリアスを使用する場合、Brazeはアンカーがクエリーパラメーターの後に置かれることを期待する。つまり、適切なトラッキングのためにアンカーの前に `lid` 値を付加する必要があります。Braze は URL を左から右の順で読み取るので、疑問符 (?) と `lid`はアンカーの前に配置されている必要があります。

| メール本文にリンクを貼る                                                                        | エイリアスによるリンク                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## トラッキングリンク エイリアス

[**リンク管理**] タブで、セグメンテーションのために「追跡」する、セグメンテーションフィルターに含めるエイリアスを選択します。追跡されるエイリアスはセグメンテーションのためだけのものであり、あなたのリンクがレポート目的で追跡されることには何の影響もないことに注意されたい。

{% alert tip %}
リンクのエンゲージメントの指標を追跡するには、リンクの前にHTTPまたはHTTPSのいずれかがあることを確認する。特定のリンクのクリック追跡をオフにするには、[ユニバーサルリンクとアプリリンクを]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis)参照のこと。
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

### アクションベースのフィルター
 
あらゆるリンク（トラッキング済み、未トラッキング）をターゲットにアクションベースのメッセージを作成したり、あらゆるメールキャンペーンやキャンバスコンポーネントのエイリアスをクリックしたかどうかに基づいてユーザーをリターゲティングすることができる。

![キャンバスコンポーネントのエイリアスをクリックしたユーザーやキャンペーンに参加したユーザーをターゲットにするアクションベースオプション。]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### セグメンテーションフィルター

Brazeでは、メールにリンクエイリアスを設定し、ユーザーがそれをクリックすると、そのイベントがエイリアスを持つユーザープロファイルに記録される。

任意のキャンペーンまたはキャンバスステップでクリックされたエイリアス」セグメンテーションフィルターを使用し、後でこのリンクエイリアスの名前を変更することにした場合、ユーザープロファイルの以前のクリックデータは更新さ**れず**、以前のリンクエイリアスとして表示される。そのため、新しいリンクエイリアスに基づいてユーザー群をターゲットにした場合、以前のリンクエイリアスのデータは含まれない。

キャンペーンでエイリアスをクリックした」または「キャンバスでエイリアスをクリックした」セグメンテーションフィルターを使用する場合、特定のキャンペーンまたはキャンバスで特定のエイリアスをクリックしたかどうかでユーザーをフィルタリングする。複数のユーザーが同じメールアドレスを共有し、リンクエイリアスをクリックした場合、そのメールアドレスを共有する他のすべてのユーザーのユーザープロファイルが更新される。 

以下のセグメンテーションフィルターは、イベント処理時にトラッキングされたクリックイベントに適用される。つまり、トラッキングされていないリンクが既存のデータを削除することはなく、トラッキング, 追跡がデータを埋め戻すこともない。詳しくは「[セグメンテーションフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters)」を参照してください。

#### リンクの追跡を解除する

リンクのトラッキングを解除しても、そのフィルターを持つ既存のセグメントは、トラッキングされていないエイリアスに再割り当てされない。古いデータは、新しいデータに置き換わるまでユーザープロファイルに残る。 

アーカイブされたメッセージのリンクは自動的に追跡解除される。しかし、アーカイブされたメッセージがアーカイブされない場合、リンクを再度追跡する必要がある。リンクエイリアスが追跡される場合、リンクレポートはトップレベルドメインや完全なURLではなく、エイリアスによってインデックスされる。

![3つのリンクエイリアスとその合計クリック数を表示するキャンペーン分析タブ。]({% image_buster /assets/img/link_aliasing_click_table.png %})

### 電子メールのクリック・イベント

Currentsでエンゲージメントデータをエクスポートする場合、リンクエイリアスを有効にしていると、メールのクリックイベントが若干異なる。リンクエイリアスがオンになっている場合、[メールクリックイベントの]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/)ために2つの追加フィールドを持つことになる：`link_id` と`link_alias` 。

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

## コンテンツブロックのリンクエイリアス

新しいコンテンツブロックのリンクが変更され、Braze は該当する各リンクに `lid={{placeholder}}` を追加します。このプレースホルダーの値は、Eメールメッセージバリアントに挿入されると解決される。

Brazeがリンクエイリアスを有効にする前に作成された既存のコンテンツブロック内のリンクを修正するには、既存のコンテンツブロックを複製し、複製したコンテンツブロック内のリンクを修正する。

`lid` 値を持たないコンテンツブロックを新しいメッセージに挿入した場合、そのコンテンツブロックからのリンクはエイリアスで追跡されない。新しいコンテンツブロックが「古い」メッセージバリアントに挿入されると、そのメッセージバリアントからのリンクはリンクエイリアスによって認識されます。コンテンツブロックからのリンクも認識される。ただし、「古い」コンテントブロックが「新しい」コンテントブロックをネストすることはできません。

{% alert tip %}
Braze では、コンテンツブロックについては、既存のコンテンツブロックのコピーを作成し、新しいメッセージで使用することをお勧めします。これは、新規メッセージ内でリンクエイリアスが有効になっていないコンテンツブロックを参照してしまう可能性を回避するために、一括複製によって行うことができます。
{% endalert %}

## Liquid が生成する URL のリンクエイリアス

HTMLやコンテンツブロックの`assign` ステートメントなど、Liquidによって生成されるURLについては、Liquidタグにクエスチョンマーク(`?`)を追加する必要がある。これにより Braze は、リンクエイリアスが正しく機能するように、クエリパラメーター (`lid = somevalue`) を追加することができます。クエリパラメータを追加する場所を特定しなければ、リンクエイリアスはこれらの URL を認識せず、リンクテンプレートは適用されません。

### 例

リンクの推奨フォーマットについては、リンクエイリアスの例をチェックしてほしい：

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


