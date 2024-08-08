---
nav_title: カードの作成
article_title: カードの作成
alias: /card_creation/
description: "この記事では、キャンペーン開始時またはキャンバスステップエントリ時のコンテンツカード作成と第一印象時の違いについて説明します。"
page_order: 1
tool: Campaigns
channel:
  - content cards
---

# カードの作成

> カードを作成するタイミングを指定することで、Brazeが新しいコンテンツカードキャンペーンとキャンバスステップのオーディエンスの適格性とパーソナライゼーションを評価するタイミングを選択できます。

## 前提 条件

この機能を利用するには、次の最小 SDK バージョンにアップグレードする必要があります。

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

SDK をアップグレードした後、モバイル ユーザーはアプリをアップグレードする必要があります。キャンペーンまたはキャンバスのオーディエンスをフィルタリングして、 [これらの最小アプリバージョンのユーザー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)のみをターゲットにすることができます。

## 概要

{% tabs %}
{% tab Campaign %}

配信スケジュールを設定した新しい[コンテンツカードキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)を作成する際に、Brazeが**配信**ステップでカードを作成するタイミングを選択できます。

![Content Card Controls section when editing the delivery of a scheduled Content Card.]({% image_buster /assets/img_archive/card_creation.png %})

次のオプションを使用できます。

- キャンペーン開始時コンテンツ カードの以前の既定の動作。Brazeは、キャンペーンの開始時にオーディエンスの適格性とパーソナライゼーションを計算し、カードを作成して、ユーザーがアプリを開くまで保存します。
- **第一印象(推奨):**ユーザーが次にアプリを開くと(つまり、新しい [セッション](https://www.braze.com/resources/articles/whats-an-app-session-anyway)を開始すると)、Brazeはユーザーがどのコンテンツカードに適格であるかを判断し、Liquidやコネクテッドコンテンツなどのパーソナライゼーションをテンプレート化してから、カードを作成します。このオプションを使用すると、通常、カード配信のパフォーマンスが向上します。

{% endtab %}
{% tab Canvas %}

Brazeがカードを作成するタイミングは、コンテンツカード[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)の**「メッセージングチャネル**」タブで選択できます。

![Content Card Controls section when editing the delivery of a scheduled Content Card.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

次のオプションを使用できます。

- **ステップエントリ時:**コンテンツ カードの以前の既定の動作。Brazeは、ユーザーがキャンバスステップに入ったときにオーディエンスの適格性を計算し、カードを作成して、ユーザーがアプリを開くまで保存します。
- **第一印象(推奨):**Braze は、ユーザーが Canvas ステップに入ったときにオーディエンスの適格性を計算します。ユーザーが次にアプリを開くと(つまり、新しい [セッション](https://www.braze.com/resources/articles/whats-an-app-session-anyway)を開始すると)、BrazeはLiquidやコネクテッドコンテンツなどのパーソナライゼーションをテンプレート化し、カードを作成します。このオプションを使用すると、カード配信のパフォーマンスが向上し、最新のパーソナライゼーションが強化されます。

{% endtab %}
{% endtabs %}

{% alert note %}
どちらのオプションでも、カードの作成後、Brazeはオーディエンスの適格性やパーソナライゼーションを再計算しません。
{% endalert %}

### カード作成時のカード作成と、ローンチ時やエントリー時と第一印象時の違い

このセクションでは、キャンペーンの開始時またはステップ入力時のカード作成と、第一印象時のカード作成の主な違いについて説明します。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">キャンペーン開始時/キャンバスステップ入力時</th>
    <th class="tg-0pky">最初のインプレッション発生時</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">使用に適しているケース</td>
    <td class="tg-0pky">特定の時間(起動時間)にコンテンツのスナップショットを作成する必要がある場合。</td>
    <td class="tg-0pky"><ul><li>ローンチ後にセグメントに入力する可能性のある新規ユーザーまたは匿名ユーザーにカードを表示する必要がある場合(<a href="#campaign_note">キャンペーンのみ*</a>)。</li><li>パーソナライゼーションを使用していて、最新のコンテンツをカードで利用できるようにする場合。</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">オーディエンス</td>
    <td class="tg-0pky">Brazeは、キャンペーンの送信時にオーディエンスのメンバーシップを評価します。<br><br>新規ユーザーまたは匿名ユーザーは、キャンペーンの送信後にカードを表示しようとしても、適格性は評価されません。定期的なキャンペーンの場合、これは次の繰り返し間隔になります。</td>
    <td class="tg-0pky">Brazeは、ユーザーが次にアプリを開いたとき(セッションの開始、 <a href="#campaign_note">キャンペーンのみ*</a>)にメンバーシップを評価します。<br><br> この設定では、新規ユーザーまたは匿名ユーザーがカードを表示しようとすると、常に適格性が評価されるため、対象ユーザーのリーチが広くなります。また、レート制限(キャンペーンを受け取る人数を制限する)は、第一印象時(<a href="#campaign_note">キャンペーンのみ*</a>)に設定されている場合は適用されません。</td>
  </tr>
  <tr>
    <td class="leftHeader">パーソナライゼーション</td>
    <td class="tg-0pky">Brazeは、Liquid、コネクテッドコンテンツ、コンテンツブロックを、キャンペーンの開始時、またはユーザーがキャンバスステップに入ったときに評価します。定期的なキャンペーンの場合、これは次の繰り返し間隔になります。</td>
    <td class="tg-0pky">Brazeは、Liquid、コネクテッドコンテンツ、コンテンツブロックを、最初のインプレッション時または次の繰り返し間隔の後に評価します。</td>
  </tr>
  <tr>
    <td class="leftHeader">分析</td>
    <td class="tg-0pky"><em>送信されたメッセージ</em> とは、作成され、表示可能なカードの数を指します。これは、ユーザーがカードを表示したかどうかはカウントされません。</td>
    <td class="tg-0pky"><em>送信されたメッセージ</em> とは、ユーザーに表示されるカードの数を指します。<br><br>リーチ可能なユーザー数とインプレッション数は変わりませんが、キャンペーンのローンチ時やキャンバスステップの入力時に同じカードを作成した場合と比較して、ファーストインプレッション時にカードを作成した場合の送信量(<em>送信メッセージ数</em>)は減少することが予想されます。</td>
  </tr>
  <tr>
    <td class="leftHeader">処理時間</td>
    <td class="tg-0pky">カードは、ローンチ時にセグメント内の対象ユーザーごとに作成されます。オーディエンスが多い場合は、カードがローンチ後より迅速に利用可能になるため、[ <b>第一印象時</b>]を選択することをお勧めします。</td>
    <td class="tg-0pky">カードは、ユーザーが初めてカードを表示しようとしたときに作成されるため、最初のインプレッションに表示されるまでに 1 秒から 2 秒かかる場合があります。</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* このシナリオはキャンペーンにのみ適用され、キャンバスオーディエンスはステップレベルではなくキャンバスエントリで評価されます。</sup></p>

## 考慮 事項

### 起動後のカード作成の変更

Brazeは、キャンペーン開始後にカードの作成方法を変更しないことを推奨しています。2つのカード作成タイプでは送信メッセージの計算方法が異なるため、キャンペーンの開始後にカードの作成方法を変更すると、送信量の精度に影響を与える可能性があります。

### 処理時間の可能性

オーディエンスが多いキャンペーンでは、キャンペーン開始後、カードがより迅速に利用可能になるため、第一印象でカードを作成するオプションを選択することをお勧めします。セッションの開始時にトリガーされるキャンペーンでは、パフォーマンスの向上を実現するために、第一印象でカードを作成する(配信日時指定で利用可能)ように移行することも検討してください。

第一印象でカードが作成されると、カードが処理されるまでに1〜2秒かかる場合があります。この処理時間の長さは、カードのサイズやメッセージテンプレートオプションの複雑さなど、さまざまな要因によって異なります。たとえば、コネクテッド コンテンツを使用するカードの処理時間は、少なくともコネクテッド コンテンツの応答時間と同じになります。

### 以前のバージョンの SDK

ユーザーのアプリが以前のバージョンの SDK を実行している場合でも、指定したカード作成で送信されたコンテンツ カードを受信します。ただし、これらのユーザーにカードが表示されるまでに時間がかかり、次回のコンテンツ カードの同期まで表示されない場合があります。

[1]: {% image_buster /assets/img_archive/card_creation.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/
[3]: https://www.braze.com/resources/articles/whats-an-app-session-anyway
