---
nav_title: レポート指標の用語集
article_title: レポート指標の用語集
layout: report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "この用語集では、Braze アカウントのレポートに表示される用語の定義を示します。"
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### AMP クリック数

{% apitags %}
メール
{% endapitags %}

AMP HTML メールの AMP バージョンをクリックしたユーザーの総数。

{% endapi %}

{% api %}

### オーディエンス

{% apitags %}
すべて
{% endapitags %}

特定のメッセージを受信したユーザーの割合。この数値は Braze から受信します。

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
メール、Web プッシュ、iOS プッシュ
{% endapitags %}

失敗したメッセージの総数。原因として、有効なプッシュトークンがない、メールアドレスが間違っているか無効になっている、またはキャンペーンの開始後にユーザーが配信停止した、などがあります。SendGrid を使用している顧客のメールバウンスには、ハードバウンス、スパム、および無効なアドレスに送信されたメールがあります。

<span class="calculation-line">計算式: (バウンス数) / (送信数)</span>

{% endapi %}

{% api %}

### 本文クリック数 (1 回)

{% apitags %}
iOSプッシュ、Androidプッシュ
{% endapitags %}

ストーリーのプッシュ通知では、通知がクリックされたときに本文クリック数 (1 回) として記録されます。メッセージが展開されたとき、またはアクションボタンがクリックされたときには記録されません。

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### 本文クリック数 (複数回)

{% apitags %}
アプリ内メッセージ
{% endapitags %}

次のアプリ内メッセージタイプのいずれかがクリックされると発生します。
\- スライドアップ
\- モーダル
\- ボタンのない全画面表示

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 1 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

メッセージのボタン 1 の合計クリック数。

<span class="calculation-line">計算式: (ボタン 1 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 2 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

メッセージのボタン 2 の合計クリック数。

<span class="calculation-line">計算式: (ボタン 2 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### 選択肢の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

ユーザーが [簡単な調査]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)の質問ページで送信ボタンをクリックしたときに選択されていた選択肢の合計数。

{% endapi %}

{% api %}

### クリック開封率

{% apitags %}
メール
{% endapitags %}

開封されたメールのうちクリックされた割合。この指標は、[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)でのみ使用できます。

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数) (メールの場合)</span>

{% endapi %}

{% api %}

### 確認済み配信数

{% apitags %}
SMS
{% endapitags %}

通信事業者が、ターゲットの電話番号に SMS が配信されたことを確認しました。Braze のお客様の場合、配信数は SMS 割り当てを消費します。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 信頼度

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

メッセージの特定のバリアントのパフォーマンスがコントロールグループよりも優れているという信頼度の割合。

{% endapi %}

{% api %}

### 確認ページのボタン

{% apitags %}
アプリ内メッセージ
{% endapitags %}

[簡単な調査]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)の確認ページにあるアクション呼び出しボタンのクリック数の合計。

{% endapi %}

{% api %}

### 確認ページの却下

{% apitags %}
アプリ内メッセージ
{% endapitags %}

[簡単な調査]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)の確認ページにある [閉じる] (x) ボタンのクリック数の合計。

{% endapi %}

{% api %}

### コンバージョン (B、C、D)

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS
{% endapitags %}

1 次コンバージョン後に追加された追加のコンバージョンイベント。Braze キャンペーンから受信したメッセージの操作後または表示後に、定義されたイベントが発生した回数。このイベントは、キャンペーンを作成するときにマーケターが決定します。メール、プッシュ、および Webhook の場合、最初の送信後にコンバージョンの追跡が開始されます。コンテンツカードとアプリ内メッセージの場合、このカウントは、コンテンツカードまたはメッセージが初めて表示されたときに開始されます。

{% endapi %}

{% api %}

### コンバージョン率

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS
{% endapitags %}

送信されたメッセージのすべての受信者数に対して、定義されたイベントが発生した回数の割合。キャンペーンを作成するときに、このイベントを決定します。

<span class="calculation-line">計算式: (1 次コンバージョン) / (ユニーク受信者数)</span>

{% endapi %}

{% api %}

### コンバージョン期間

{% apitags %}
すべて
{% endapitags %}

メッセージを受信してから、ユーザーのアクションが追跡されてコンバージョンイベントに関連付けられるまでの日数。この期間の後に発生したコンバージョンは、コンバージョンイベントに起因するものとは見なされません。

{% endapi %}

{% api %}

### 配信数

{% apitags %}
メール、Web プッシュ、iOS プッシュ、Android プッシュ、WhatsApp
{% endapitags %}

受信サーバーが受け入れたメッセージリクエスト数の合計。これはメッセージがデバイスに配信されたことを意味するのではなく、メッセージがサーバーによって受け入れられたことのみを意味します。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信失敗数

{% apitags %}
SMS
{% endapitags %}

キューのオーバーフロー (ロングコードまたはショートコードで処理できる速度よりも高いレートで SMS を送信している) のため、SMS を送信できませんでした。

<span class="calculation-line">計算式: (送信数) - (通信事業者への送信数)</span>

{% endapi %}

{% api %}

### 直接開封数

{% apitags %}
iOS プッシュ
{% endapitags %}

プッシュから直接開封されたプッシュ通知の合計数 (および割合)。

<span class="calculation-line">計算式: (直接開封数) / (配信数)</span>

{% endapi %}

{% api %}

### エラー数

{% apitags %}
Webhook
{% endapitags %}

Webhook イベントによって返されたエラーの数 (送信プロセス中に増加)。

{% endapi %}

{% api %}

### 失敗数

{% apitags %}
WhatsApp
{% endapitags %}

インターネットサービスプロバイダーがハードバウンスを返したため、WhatsApp メッセージを送信できませんでした。ハードバウンスは、配信到達性の永続的なエラーを意味します。

{% endapi %}

{% api %}

### 誘発された開封数

{% apitags %}
iOSプッシュ、Androidプッシュ
{% endapitags %}

プッシュ通知の送信後に、プッシュを直接開封せずにアプリを開いたユーザーの総数 （および割合）。

<span class="calculation-line">計算式: (誘発された開封数) / (配信数)</span>

{% endapi %}

{% api %}

### 再試行保留中

{% apitags %}
メール
{% endapitags %}

受信サーバーから一時的に拒否されたが、メールサービスプロバイダー (ESP) によって再配信が試行されたリクエストの数。メールサービスプロバイダー (ESP) は、タイムアウト期間に達する (通常は 72 時間後) まで配信を再試行します。

{% endapi %}

{% api %}

### 1 次コンバージョン (A) または 1 次コンバージョンイベント

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

Braze キャンペーンから受信したメッセージの操作後または表示後に、定義されたイベントが発生した回数。このイベントは、キャンペーンを作成するときにマーケターが決定します。メール、プッシュ、および Webhook の場合、最初の送信後にコンバージョンの追跡が開始されます。コンテンツカードとアプリ内メッセージの場合、このカウントは、コンテンツカードまたはメッセージが初めて表示されたときに開始されます。

{% endapi %}

{% api %}

### 既読数

{% apitags %}
WhatsApp
{% endapitags %}

WhatsApp メッセージがエンドユーザーによって既読になった時点。Braze が既読数を追跡するには、エンドユーザーの既読受信者が「オン」になっている必要があります。

{% endapi %}

{% api %}

### 受信済み

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、SMS、WhatsApp
{% endapitags %}

- コンテンツカード: ユーザーがアプリ内でカードを表示すると「受信済み」になります。
- プッシュ: メッセージが Braze サーバーからプッシュプロバイダーに送信されると「受信済み」になります。
- メール: メッセージが Braze サーバーからメールサービスプロバイダー (ESP) に送信されると「受信済み」になります。
- SMS/MMS: SMS プロバイダーが上流通信事業者と宛先デバイスから確認を受信すると、「配信済み」になります。
- アプリ内メッセージ: 定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。
- WhatsApp:定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。

{% endapi %}

{% api %}

### 拒否数

{% apitags %}
SMS
{% endapitags %}

SMS が通信事業者によって拒否されました。これは、キャリアコンテンツへのフィルター適用、宛先デバイスの可用性、電話番号が使用されていないなど、さまざまな理由で発生する可能性があります。Braze のお客様の場合、拒否数は SMS 割り当てを消費します。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 受信者あたりの収益

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ
{% endapitags %}

直接収益の合計をユニーク受信者数で除算した値。この指標は、[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)を介したキャンペーン比較レポートでのみ使用できます。

<span class="calculation-line">計算式: (直接収益の合計) / (ユニーク受信者数)</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

*送信数*、または*送信済みメッセージ数*は、キャンペーンで送信されたメッセージの合計数です。スケジュールされたキャンペーンを開始すると、レート制限によりメッセージが送信されたかどうかに関係なく、この指標にはすべての送信済みメッセージの数が含まれます。これは、メッセージがデバイスに受信された、または配信されたことを意味せず、メッセージが送信されたことのみを意味します。この指標は Braze によって提供されます。

{% alert tip %}
コンテンツカードの場合、この指標は [**カードの作成**] で選択した内容に応じて異なる方法で計算されます。詳細については、「[カードの作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)」を参照してください。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### キャリアへの送信数

{% apitags %}
SMS
{% endapitags %}

{% alert note %}
*キャリアへの送信数*は非推奨になりましたが、すでにそれをお持ちのユーザーについては引き続きサポートされます。
{% endalert %}

この統計値は、確認済み配信数、拒否数、および通信事業者によって配信または拒否が確認されなかった送信数の合計です。通信事業者が配信または拒否の確認を提供しないことがあります。通信事業者によってはこの確認を提供していない場合、また送信時に確認を提供できなかった場合があります。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### スパム

{% apitags %}
メール
{% endapitags %}

「スパム」としてマークされたメール配信数の合計。

<span class="calculation-line">計算式: (スパムとしてマークされた数) / (送信数)</span>

{% endapi %}

{% api %}

### 調査ページの却下数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

[簡単な調査]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)の質問ページにある [閉じる] (x) ボタンのクリック数の合計。

{% endapi %}

{% api %}

### 調査の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

[簡単な調査]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)の送信ボタンをクリックした回数の合計。

{% endapi %}

{% api %}

### クリック数の合計

{% apitags %}
メール、コンテンツカード
{% endapitags %}

配信されたメールまたはカード内をクリックしたユーザーの総数 （および割合）。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール:</b> (クリック数の合計) / (配信数)</li>
        <li><b>コンテンツカード:</b> (クリック数の合計) / (インプレッション数の合計)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 直接購入数の合計

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ
{% endapitags %}

最終クリックアトリビューション* に基づく、購入の合計数。この指標は、1 人のユーザーからの複数の購入をカウントします。例えば、1 人のユーザーが 2 回購入すると、カウントは 2 増加します。この指標は、[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)を介したキャンペーン比較レポートでのみ使用できます。

\*最終クリックアトリビューションとは、収益が特定のキャンペーンに起因したと見なされるために、そのキャンペーンが以下の要件を満たす必要があることを意味します。

1. ユーザーが購入前にクリックした最後のキャンペーンである。かつ
2. 購入前 3 日以内にユーザーがクリックする。

<span class="calculation-line">計算式: (直接購入数の合計)</span>

{% endapi %}

{% api %}

### 直接収益の合計

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ
{% endapitags %}

最終クリックアトリビューション* に基づいて、このキャンペーンによって生み出された収益額。この指標は、[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)を介したキャンペーン比較レポートでのみ使用できます。

\*最終クリックアトリビューションとは、収益が特定のキャンペーンに起因したと見なされるために、そのキャンペーンが以下の要件を満たす必要があることを意味します。

1. ユーザーが購入前にクリックした最後のキャンペーンである。かつ
2. 購入前 3 日以内にユーザーがクリックする。

<span class="calculation-line">計算式: (直接収益の合計)

{% endapi %}

{% api %}

### 却下数の合計

{% apitags %}
コンテンツカード
{% endapitags %}

キャンペーンのコンテンツカードが却下された回数。あるユーザーがメッセージを 2 回無視しても、1 回のみカウントされます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### インプレッション数の合計

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

アプリ内メッセージが表示された回数。あるユーザーがメッセージを 2 回表示した場合、2 回カウントされます。この値は、Braze が SDK から受け取ったインプレッションイベント数の合計です。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 開封数の合計

{% apitags %}
メール、iOS プッシュ、Android プッシュ、Web プッシュ
{% endapitags %}

開封されたメッセージ数の合計。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール:</b> (開封数) / (配信数)</li>
        <li><b>Web プッシュ</b>:(直接開封数) / (配信数)</li>
        <li><b>iOS、Android、および Kindle のプッシュ:</b> (ユニーク開封数) / (配信数)</li>
    </ul>
</span>
{:/}


{% endapi %}

{% api %}

### 総収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

設定された 1 次コンバージョン期間内のキャンペーン受信者からのドル単位の総収益。この指標は、[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)を介したキャンペーン比較レポートでのみ使用できます。

{% endapi %}

{% api %}

### ユニーククリック数

{% apitags %}
メール、コンテンツカード
{% endapitags %}

メッセージ内を少なくとも 1 回クリックしたユニーク受信者の数。メールの場合、これは 7 日間にわたって追跡されます。Braze が提供する配信停止リンクのクリックは、ユニーククリック数としてカウントされることに注意してください。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール:</b> (ユニーククリック数) / (配信数)</li>
        <li><b>コンテンツカード: </b>(ユニーククリック数) / (ユニークインプレッション数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーク直接購入数

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ
{% endapitags %}

最終クリックアトリビューション* に基づく、購入ユーザー数。この指標は、[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder)を介したキャンペーン比較レポートでのみ使用できます。

\*最終クリックアトリビューションとは、収益が特定のキャンペーンに起因したと見なされるために、そのキャンペーンが以下の要件を満たす必要があることを意味します。

1. ユーザーが購入前にクリックした最後のキャンペーンである。かつ
2. 購入前 3 日以内にユーザーがクリックする。

{% endapi %}

{% api %}

### ユニーク却下数

{% apitags %}
コンテンツカード
{% endapitags %}

キャンペーンからコンテンツカードを却下したユーザーの数。あるユーザーがキャンペーンからコンテンツカードを複数回却下すると、ユニークな却下 1 回になります。

<span class="calculation-line">計算式: (ユニーク却下数) / (ユニークインプレッション数)</span>

{% endapi %}

{% api %}

### ユニークインプレッション数

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

1 日に特定のアプリ内メッセージまたはカードを受信して表示したユーザーの総数。アプリ内メッセージのユニークインプレッション数は、再適格性が有効で、かつユーザーがトリガーアクションを実行した場合、24 時間後に再び加算できます。反対に、ユーザーがコンテンツカードを 2 回目に表示したときには、カウントは増加しません。この数値は Braze から受信します。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### ユニーク開封数

{% apitags %}
メール
{% endapitags %}

1 人のユーザーが 1 回以上開封した配信済みメール数の合計。メールの場合、これは 7 日間にわたって追跡されます。

<span class="calculation-line">計算式: (ユニーク開封数) / (配信数)</span>

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
すべて
{% endapitags %}

日次ユニーク受信者数。1 日に特定のメッセージを受信したユーザー数。この数値は Braze から受信します。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信停止数

{% apitags %}
メール
{% endapitags %}

Braze が提供する配信停止 URL をクリックした結果、サブスクリプション状態が配信停止に変更された受信者の数。

<span class="calculation-line">計算式: (配信停止数) / (配信数)</span>

{% endapi %}

{% api %}

### バリエーション

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

キャンペーンのバリエーション。作成者の定義によって異なります。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}
