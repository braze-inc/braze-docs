---
nav_title: リンクエイリアシング
article_title: リンクエイリアシング
alias: /link_aliasing/
page_order: 3
description: "この記事では、リンク エイリアスの仕組みとリンクの外観について説明します。"
channel:
  - email

---

# リンクエイリアシング
 
> リンク エイリアスを使用して、Braze から電子メール メッセージで送信されたリンクを識別するための、認識可能なユーザー生成名を作成します。これらのリンクは、セグメンテーション リターゲティング、アクション ベースのトリガー、リンク分析に使用できます。リンク エイリアスを使用すると、特定のリンクをクリックしたユーザーを再ターゲットできるため、ユーザーが特定のエイリアス リンクをクリックしたときにアクション ベースのトリガーを作成できます。

## リンクエイリアスの作成

リンク エイリアスは、電子メール チャネル内のリンクに Braze によって生成されたクエリ パラメータを装飾することによって機能します。リンク エイリアスを作成するには、次の手順に従います。 

1. メール本文を開きます。
2. **[リンク管理]** タブをクリックします。
3. Braze は、リンクごとに一意のデフォルトのリンク エイリアスを自動的に生成します。
4. エイリアスに名前を付けます。エイリアスは、電子メール キャンペーン バリアントまたは Canvas コンポーネントごとに一意の名前を付ける必要があります。 

レポートやセグメンテーションを処理するときに特定のリンクを参照するために使用されるエイリアスを設定することもできます。 

![][2]

リンクエイリアスは、 `href` クエリ パラメータを追加しても安全な HTML アンカー タグ内の属性。Brazeが簡単にリンクを追加できるように、リンクの最後に疑問符（？）を含めることをお勧めします。 `lid` 価値。追加せずに `lid` 値がない場合、Braze はリンク エイリアスの URL を認識しません。

### リンクエイリアスの管理

追跡したリンク エイリアスをすべて表示するには、次の手順に従います。

1. **ワークスペース設定**の下にある **設定** > **メール設定** に移動します。
2. **[リンク エイリアス設定]** タブをクリックします。

{% alert important %}
[古いナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)を使用している場合、これらの設定は **「設定の管理」**にあります。
{% endalert %}

ここでは、すべてのリンク エイリアスを並べ替えたり検索したりすることもできます。

![Canvas ステップのアクティブな部分である「test」という名前のリンク エイリアスを表示する [追跡されたリンク エイリアス] ページ。][8]

#### リンクエイリアスの追跡解除

**[リンク エイリアス設定]** タブでは、リンク エイリアスの追跡をオフにすることができます。

1. リンクエイリアスを選択します。
2. **[追跡をオフにする]**をクリックします。  

#### リンクエイリアスとユーザープロファイルデータ

Braze では、アプリまたは Web サイトにリンク エイリアスがあり、ユーザーがそれをクリックすると、そのイベントがエイリアスとともにユーザーのプロフィールに記録されます。後でこのリンク エイリアスの名前を変更する場合、ユーザー プロファイル内の以前のクリック データは更新さ **れず** 、以前のリンク エイリアスとして引き続き表示されます。したがって、新しいリンク エイリアスに基づいてユーザーをターゲットにすると、以前のリンク エイリアスのデータは含まれません。

### ワークフローの確認

Braze では、電子メール内のリンクを評価し、リンク テンプレートを追加し、セグメンテーションとレポート作成の目的に適した命名規則を提供することを推奨しています。これにより、すべてのリンクを追跡できるようになります。

リンク エイリアスが有効になっている場合、メッセージ、コンテンツ ブロック、およびリンク テンプレートは変更されません。リンク テンプレートまたはコンテンツ ブロックを使用する既存のメッセージは同じになります。ただし、メッセージを更新すると、リンク エイリアス マークアップがすべてのリンクに適用されるため、リンクを表示するにはリンク テンプレートを再度適用する必要があります。

### データの抽出

[キャンペーンのリストリンクエイリアス][3]と[キャンバスのリストリンクエイリアス][4]エンドポイントを使用して、 `alias` キャンペーン内の各メッセージ バリアントまたは電子メール固有の Canvas コンポーネントに設定されます。

## コンテンツブロック内のリンクエイリアス

新しいコンテンツブロックのリンクはBrazeによって変更され、 `lid={{placeholder}}` 該当する場合は各リンクへ。このプレースホルダー値は、電子メール メッセージのバリアントに挿入されたときに解決されます。

Braze がリンク エイリアスを有効にする前に作成された既存のコンテンツ ブロック内のリンクを変更するには、既存のコンテンツ ブロックを複製し、複製したコンテンツ ブロック内のリンクを変更します。

コンテンツブロックに `lid` 値が新しいメッセージに挿入されると、そのコンテンツ ブロックからのリンクはエイリアスで追跡されません。新しいコンテンツ ブロックが「古い」メッセージ バリアントに挿入されると、そのメッセージ バリアントからのリンクはリンク エイリアシングによって認識されます。コンテンツ ブロックからのリンクも認識されます。ただし、「古い」コンテンツ ブロックは「新しい」コンテンツ ブロックをネストすることはできません。

{% alert tip %}
コンテンツ ブロックについては、Braze では、新しいメッセージで使用するために既存のコンテンツ ブロックのコピーを作成することをお勧めします。これは、一括複製によって実行でき、新しいメッセージでリンク エイリアスが有効になっていないコンテンツ ブロックを参照するシナリオを防ぐことができます。
{% endalert %}

## 例

次の表は、電子メール本文内のリンクの例、リンク エイリアスの結果、およびリンク エイリアスによって元のリンクがどのように更新されるかの説明を示しています。

| メール本文のリンク | エイリアス付きリンク | ロジック |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Braze inserts a question mark (?) and adds the first query parameter into the URL. |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze detects other query parameters and appends `lid=`URL の末尾に追加します。 |
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%}| {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%}| Braze はこれが URL であり、すでに疑問符 (?) が含まれていることを認識します。次に、 `lid` 疑問符の後のクエリ パラメータ。 |
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email | Braze expects the URL to use a standard structure where anchors (#) are present after a question mark (?). Because Braze reads from left to right, we will append the question mark and `lid` アンカーの前の値。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Liquid 経由で生成された URL のリンク エイリアス

生成されたURLの場合 `assign` HTML またはコンテンツ ブロックにステートメントがある場合は、アンカー タグに疑問符 (?) を追加することをお勧めします。これにより、Brazeはクエリパラメータを追加できるようになります（`lid = somevalue`) により、リンク エイリアシングが適切に機能します。クエリ パラメータを追加する場所を指定しないと、リンク エイリアシングではこれらの URL が認識されません。

### 例:

アンカー タグの推奨フォーマットについては、次のリンク エイリアスの例を確認してください。

{% raw %}
\`\`\`liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">{{link1}}</a>
\`\`\`
{% endraw %}

## リンクテンプレート

新しいメッセージ バリアントの場合は、**[リンク管理]** タブから既存の [リンク テンプレートを]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/) 使用できます。リンク テンプレートを使用して開始されたメッセージについては、引き続き適用されます。既存のメッセージが変更された場合は、**[リンク管理]** タブからリンク テンプレートを再適用する必要があります。 

{% alert note %}
リンク テンプレートは、**[リンク管理]** タブに表示されるリンクにのみ適用できます。つまり、 `lid`「古い」コンテンツ ブロックやマークアップできないリンクなどの URL パラメータは、リンク テンプレートに適格ではありません。これを修正するには、「古い」コンテンツブロックをコピーするか、疑問符（？）またはアンパサンド（＆）を `href` URL の属性。
{% endalert %}

## リンクのセグメンテーション

エイリアス フィルターのリターゲティングを使用すると、電子メール キャンペーンまたは Canvas コンポーネントから特別に追跡されたエイリアスをクリックした顧客に基づいてセグメンテーション フィルターを作成できます。このフィルターは、追跡されたエイリアスが存在するキャンペーンまたはキャンバスでのみ使用できます。

### トラッキングリンク

[ **リンク管理]** タブで、セグメンテーションの目的で「追跡」し、セグメンテーション フィルターに表示するエイリアスを選択します。追跡されるエイリアスはセグメンテーション目的のみであり、レポート目的で追跡されるリンクには影響しないことに注意してください。

{% alert tip %}
リンクエンゲージメント指標を追跡するには、リンクの前に HTTP または HTTPS が付いていることを確認してください。
{% endalert %}

Braze では、追跡するリンクを無制限に選択できますが、ユーザーが開いた最新のリンクに対してのみ、ユーザーをリターゲティングできます。ユーザー プロファイルには、最近クリックした 100 個のリンクが含まれます。たとえば、500 個のリンクを追跡し、ユーザーがその 500 個すべてをクリックした場合、最近クリックされた 100 個のリンクに基づいてリターゲティングまたはセグメントを作成できます。

{% tabs local %}
{% tab Drag-And-Drop Editor %}

![Link Management tab of the Drag-and-Drop email editor.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTML editor %}

![Link Management tab of the HTML email editor.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze は、プロファイル レベルで最後にクリックされた 100 個のリンク エイリアスのみを追跡します。
{% endalert %}

### 追跡解除リンク

リンクの追跡を解除しても、フィルターを含む既存のセグメントは追跡解除されたエイリアスに再割り当てされません。古いデータは、新しいデータに置き換えられるまでユーザー プロファイルに残ります。次のセグメンテーション フィルターは引き続き存在しますが、そのフィルターを使用して新しいセグメントを作成することはできません。

セグメンテーションの目的で、デフォルトではワークスペースごとに 100 個のリンクのみを追跡できます。アーカイブされたメッセージ内のリンクは自動的に追跡解除されます。ただし、アーカイブされたメッセージをアーカイブ解除した場合は、リンクを再度追跡する必要があります。リンク エイリアスが追跡されると、リンク レポートはトップレベル ドメインや完全な URL ではなくエイリアスによってインデックス化されます。

![][1]

### セグメントフィルター

次のセグメント フィルターは、イベントの処理時に追跡されるクリック イベントに適用されます。つまり、リンクの追跡を解除しても既存のデータは削除されず、リンクの追跡によってデータがバックフィルされることはありません。

#### キャンペーンでクリックされたエイリアス

キャンペーンでクリックされた特定のエイリアスに基づいてユーザーをリターゲティングします。追跡されたエイリアスを持つキャンペーンのみがここに反映されます。

#### キャンバスステップでクリックされたエイリアス

Canvas コンポーネントでクリックされた特定のエイリアスに基づいてユーザーを再ターゲットします。パイプ区切りのフィルター オプションでは、Canvas と Canvas コンポーネントが表示され、その後に Canvas コンポーネント内のエイリアスが表示されます。追跡されたエイリアスを持つ Canvas ステップのみがここに表示されます。

#### キャンペーンまたはキャンバスでクリックされたエイリアス

キャンペーンまたはキャンバス コンポーネントでクリックされたエイリアスに基づいてユーザーを再ターゲットします。エイリアスは「グローバル」とみなされるため、グローバル エイリアスはすべてのキャンペーンとキャンバス ステップからのリンク クリックをターゲットにします。

![][5]

### アクションベースのフィルター
 
任意のリンク（追跡対象または追跡対象外）をターゲットとするアクションベースのメッセージを作成したり、電子メール キャンペーンまたは Canvas コンポーネント全体でエイリアスをクリックしたかどうかに基づいてユーザーを再ターゲットしたりできます。 

![][6]

### メールクリックイベント

[メールクリックイベント][7]は、ユーザーがメールをクリックしたときに発生します。ユーザーがメールを複数回クリックしたり、メール内の異なるリンクをクリックしたりすると、同じキャンペーンに対して複数のイベントが生成されることがあります。リンク エイリアスが有効になっている場合、電子メール クリック イベントには次の 2 つの追加フィールドがあります。 `link_id` そして `link_alias`。

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
の行動 `dispatch_id` Braze は、Canvas ステップ (スケジュール可能なエントリ ステップを除く) を、たとえ「スケジュール」されている場合でもトリガーされたイベントとして扱うため、Canvas とキャンペーンでは異なります。詳細はこちら [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) キャンバスとキャンペーンでの動作。

_2019 年 8 月に更新が記録されました。_
{% endalert %}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/
[8]: {% image_buster /assets/img/tracked_aliases.png %}