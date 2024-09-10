---
nav_title: カード作成
article_title: カード作成
alias: /card_creation/
description: "この記事では、キャンペーン開始時やキャンバスステップエントリー時とファーストインプレッション時のコンテンツカード作成の違いについて説明する。"
page_order: 1
tool: Campaigns
channel:
  - content cards
---

# カード作成

> Brazeが新しいコンテンツカードキャンペーンとキャンバスのステップでオーディエンスの適格性とパーソナライズを評価するタイミングは、カードが作成されるタイミングを指定することで選択できる。

## 前提条件

この機能を利用するには、以下の最小SDKバージョンにアップグレードする必要がある：

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

SDKをアップグレードしたら、モバイルユーザーはアプリをアップグレードしなければならない。キャンペーンまたはキャンバスのオーディエンスをフィルタリングして、[これらの最小アプリバージョンのユーザーのみをターゲットにする]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)ことができる。

## 概要

{% tabs %}
{% tab キャンペーン %}

Brazeは、スケジュール配信で新しい[コンテンツカードキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)作成する際に、**配信**ステップでカードを作成するタイミングを選択できる。

![]({% image_buster /assets/img_archive/card_creation.png %})

以下のオプションがある：

- **キャンペーン発表会にて：**以前のコンテンツカードのデフォルト動作。Brazeは、キャンペーン開始時にオーディエンスの適格性とパーソナライズを計算し、その後カードを作成し、ユーザーがアプリを開くまで保存する。 
- **第一印象で（推奨）：**ユーザーが次にアプリを開いたとき（つまり、新しい[セッションを](https://www.braze.com/resources/articles/whats-an-app-session-anyway)開始したとき）、Brazeはそのユーザーがどのコンテンツカードが適用可能かを判断し、リキッドやコネクテッドコンテンツのようなパーソナライゼーションをテンプレート化し、カードを作成する。このオプションは通常、カード配送でより良いパフォーマンスを発揮する。

選択したオプションにかかわらず、キャンペーン開始時にコンテンツカードの有効期限カウントダウンが始まる。

{% endtab %}
{% tab キャンバス %}

Brazeがカードを作成するタイミングは、[コンテンツカードメッセージステップの]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) **Messaging Channels**タブで選択できる。

![]({% image_buster /assets/img_archive/card_creation_canvas.png %})

以下のオプションがある：

- **ステップエントリ時:**以前のコンテンツカードのデフォルト動作。Brazeは、ユーザーがCanvasステップに入った時点で視聴資格を計算し、カードを作成して、ユーザーがアプリを開くまで保存する。
- **第一印象で（推奨）：**Brazeは、ユーザーがCanvasステップに入った時点で視聴者資格を計算する。ユーザーが次にアプリを開く（つまり、新しい[セッションを](https://www.braze.com/resources/articles/whats-an-app-session-anyway)開始する）と、BrazeはLiquidやConnected Contentのようなパーソナライズをテンプレート化し、カードを作成する。このオプションでは、カード配送のパフォーマンスが向上し、より最新のパーソナライズが可能になる。

選択したオプションにかかわらず、コンテンツカードの有効期限のカウントダウンは、ユーザーがキャンバスのステップに入ったときに開始される。

{% endtab %}
{% endtabs %}

{% alert note %}
どちらのオプションでも、カード作成後、Brazeは視聴資格やパーソナライズを再計算しない。
{% endalert %}

### ローンチ時やエントリー時と第一印象時のカード作成の違い

このセクションでは、キャンペーン開始時やステップエントリー時とファーストインプレッション時のカード作成の主な違いについて説明する。

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
    <th class="tg-0pky">キャンペーン開始時／キャンバスステップエントリー時</th>
    <th class="tg-0pky">第一印象</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">いつこれを使うか</td>
    <td class="tg-0pky">特定の時間（ローンチタイム）にスナップショットされるコンテンツが必要な場合。</td>
    <td class="tg-0pky"><ul><li>ローンチ後にセグメントに入る可能性のある新規ユーザーや匿名ユーザーにカードを表示する必要がある場合<a href="#campaign_note">（キャンペーンのみ*）。</a></li><li>パーソナライゼーションを使用していて、最新のコンテンツをカードで利用できるようにしたい場合。</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">オーディエンス</td>
    <td class="tg-0pky">Brazeは、キャンペーン送信時にオーディエンスのメンバーシップを評価する。<br><br>新規または匿名のユーザーが、キャンペーン送信後にカードを閲覧しようとしても、適格性は評価されない。定期的なキャンペーンの場合、これは次回の更新間隔となる。</td>
    <td class="tg-0pky">Brazeは、ユーザーが次にアプリを開く（セッションを開始する、<a href="#campaign_note">キャンペーンのみ*）</a>ときにメンバーシップを評価する。<br><br> この設定は、新規ユーザーや匿名ユーザーがカードを閲覧しようとする際に、常に適格性が評価されるため、より多くのオーディエンスにリーチすることができる。また、ファーストインプレッション<a href="#campaign_note">（キャンペーンのみ*）に</a>設定した場合、レート制限（キャンペーンを受け取る人数を制限すること）は適用されない。</td>
  </tr>
  <tr>
    <td class="leftHeader">パーソナライゼーション</td>
    <td class="tg-0pky">Brazeは、リキッド、コネクテッドコンテンツ、コンテンツブロックを、キャンペーン開始時またはユーザーがキャンバスステップに入った時点で評価する。定期的なキャンペーンの場合、これは次回の更新間隔となる。</td>
    <td class="tg-0pky">Brazeは、リキッド、コネクテッド・コンテンツ、コンテンツ・ブロックを、最初のインプレッション時、または次の再発間隔後に評価する。</td>
  </tr>
  <tr>
    <td class="leftHeader">分析</td>
    <td class="tg-0pky"><em>Messages Sentは</em>、作成され、閲覧可能なカードの数を指す。ユーザーがカードを見たかどうかはカウントされない。</td>
    <td class="tg-0pky"><em>Messages Sentは</em>、ユーザーに表示されたカードの数を指す。<br><br>リーチ可能なユーザーとインプレッションは変わらないが、ファーストインプレッションでカードを作成した場合、キャンペーン開始時やキャンバスステップエントリー時に同じカードを作成した場合と比べて、送信量<em>（メッセージ送信</em>数）が減少することが予想される。</td>
  </tr>
  <tr>
    <td class="leftHeader">処理時間</td>
    <td class="tg-0pky">カードは、立ち上げ時にセグメント内の対象ユーザー全員に作成される。大人数の観客には、発売後すぐにカードが入手できる<b>At First Impressionを</b>選択することをお勧めする。</td>
    <td class="tg-0pky">カードは、ユーザーが最初に表示しようとしたときに作成されるため、ファーストインプレッションで表示されるまで1～2秒かかることがある。</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* キャンバスのオーディエンスは、ステップレベルではなく、キャンバスのエントリーで評価されるため、このシナリオはキャンペーンにのみ適用される。</sup></p>

## 考慮事項

### ローンチ後にカード作成を変更する

Brazeは、キャンペーン開始後にカードの作成方法を変更しないことを推奨している。2つのカード作成タイプで送信メッセージの計算方法が異なるため、キャンペーン開始後にカードの作成方法を変更すると、送信ボリュームの精度に影響する可能性がある。

### 潜在的な処理時間

キャンペーン開始後、より早くカードが利用できるようになるため、オーディエンス数が多いキャンペーンでは、ファーストインプレッションでカードを作成するオプションを選択することをお勧めする。セッション開始時にトリガーされるキャンペーンも、パフォーマンス向上を実現するために、ファーストインプレッション時にカードを作成する（スケジュール配信で利用可能）ように移行することを検討するとよいだろう。

第一印象でカードを作成した場合、カードの処理に1～2秒かかることがある。この処理時間の長さは、カードサイズやメッセージテンプレートのオプションの複雑さなど、様々な要因に依存する。例えば、コネクテッド・コンテンツを使用するカードの処理時間は、少なくともコネクテッド・コンテンツのレスポンス・タイムと同じくらいかかる。

### 以前のSDKバージョン

ユーザーのアプリが以前のバージョンのSDKを実行している場合でも、指定されたカード作成で送信されたコンテンツ・カードを受け取ることができる。ただし、これらのユーザーにはカードが表示されるまでに時間がかかり、次回のコンテンツカード同期まで表示されないこともある。

[1]: {% image_buster /assets/img_archive/card_creation.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/
[3]: https://www.braze.com/resources/articles/whats-an-app-session-anyway
