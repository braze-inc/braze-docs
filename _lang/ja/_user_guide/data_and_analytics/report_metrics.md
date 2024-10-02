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

特定のメッセージを受け取ったユーザーの割合。この数値は Braze から受信します。

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
メール、Web プッシュ、iOS プッシュ
{% endapitags %}

失敗したメッセージの総数。これは、有効なプッシュトークンが存在しないか、メールアドレスが間違っているか、無効化されているか、キャンペーン開始後にユーザーが購読を解除したために発生する可能性がある。SendGrid を使用している顧客のメールバウンスには、ハードバウンス、スパム、および無効なアドレスに送信されたメールがあります。

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
- スライドアップ
- モーダル
- ボタンのないフルスクリーン

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 1 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

メッセージのボタン1をクリックした総数。

<span class="calculation-line">計算式: (ボタン 1 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 2 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

メッセージのボタン2をクリックした総数。

<span class="calculation-line">計算式: (ボタン 2 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### 選択肢の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

[単純なアンケートの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)質問ページで、ユーザーが送信ボタンをクリックしたときに選択された選択肢の総数。

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

[簡単なアンケートの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)確認ページにある行動喚起ボタンの総クリック数。

{% endapi %}

{% api %}

### 確認ページの却下

{% apitags %}
アプリ内メッセージ
{% endapitags %}

[簡単なアンケートの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)確認ページで、閉じる(x)ボタンをクリックした合計。

{% endapi %}

{% api %}

### コンバージョン (B、C、D)

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS
{% endapitags %}

主要なコンバージョンイベントの後に追加されるコンバージョンイベント。Braze キャンペーンから受信したメッセージの操作後または表示後に、定義されたイベントが発生した回数。<br><br> このイベントは、キャンペーンを作成するときにマーケターが決定します。Eメール、プッシュ、ウェブフックについては、最初の送信後にコンバージョンのトラッキングを開始する。コンテンツカードやアプリ内メッセージの場合、このカウントはコンテンツカードやメッセージを初めて閲覧した時点から始まる。

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

受信サーバーが受け入れたメッセージリクエスト数の合計。これは、メッセージがデバイスに届いたことを意味するのではなく、メッセージがサーバーに受け入れられたことを意味する。

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

インターネットサービスプロバイダがハードバウンスを返したため、WhatsAppメッセージは送信できなかった。ハードバウンスとは、永続的な配信の失敗です。

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

受信サーバーによって一時的に拒否されたが、Eメールサービスプロバイダ（ESP）によって再配信が試みられたリクエストの数。メールサービスプロバイダー (ESP) は、タイムアウト期間に達する (通常は 72 時間後) まで配信を再試行します。

{% endapi %}

{% api %}

### 1 次コンバージョン (A) または 1 次コンバージョンイベント

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

Braze キャンペーンから受信したメッセージの操作後または表示後に、定義されたイベントが発生した回数。このイベントは、キャンペーンを作成するときにマーケターが決定します。<br><br>Eメール、プッシュ、ウェブフックについては、最初の送信後にコンバージョンのトラッキングを開始する。コンテンツカードやアプリ内メッセージの場合、このカウントはコンテンツカードやメッセージを初めて閲覧した時点から始まる。

{% endapi %}

{% api %}

### 既読数

{% apitags %}
WhatsApp
{% endapitags %}

ユーザーがWhatsAppメッセージを読む。Brazeが読み取りを追跡するには、ユーザーの読み取りレシートが「オン」になっていなければならない。

{% endapi %}

{% api %}

### 受信済み

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、SMS、WhatsApp
{% endapitags %}

- コンテンツカード: ユーザーがアプリ内でカードを表示すると「受信済み」になります。
- プッシュ: メッセージが Braze サーバーからプッシュプロバイダーに送信されると「受信済み」になります。
- メール: メッセージが Braze サーバーからメールサービスプロバイダー (ESP) に送信されると「受信済み」になります。
- SMS/MMS: SMSプロバイダーが上流のキャリアと宛先デバイスから確認を受け取った後、"Delivered "となる。
- アプリ内メッセージ：定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。
- WhatsApp:定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。

{% endapi %}

{% api %}

### 拒否数

{% apitags %}
SMS
{% endapitags %}

SMS が通信事業者によって拒否されました。これは、キャリアのコンテンツフィルタリング、相手先デバイスの在庫状況、電話番号がサービス終了など、いくつかの理由で起こりうる。Braze のお客様の場合、拒否数は SMS 割り当てを消費します。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、WhatsApp、LINE
{% endapitags %}

*送信数*、または*送信済みメッセージ数*は、キャンペーンで送信されたメッセージの合計数です。スケジュールされたキャンペーンを開始した後、このメトリクスには、レート制限のためにまだ送信されているかどうかに関係なく、送信されたすべてのメッセージが含まれる。これは、メッセージが受信されたり、デバイスに配信されたことを意味するものではなく、メッセージが送信されたことのみを意味する。この指標は Braze によって提供されます。

{% alert tip %}
コンテンツカードの場合、この指標は \[**カードの作成**] で選択した内容に応じて異なる方法で計算されます。詳細については、「[カードの作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)」を参照してください。
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

輸送会社によって配達または配達拒否が確認されなかった、確認された配達、拒否、および送信の合計。これには、運送業者が配達確認を提供しない、あるいは発送時に提供できない場合も含まれる。

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

[簡単なアンケートの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)質問ページで、閉じる(x)ボタンをクリックした合計。

{% endapi %}

{% api %}

### 調査の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

[単純なアンケートの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)送信ボタンをクリックした総数。

{% endapi %}

{% api %}

### クリック数の合計

{% apitags %}
Eメール、コンテンツカード、SMS、LINE
{% endapitags %}

配信されたメール、カード、メッセージ内でクリックしたユーザーの総数（および割合）。LINEの場合は、1日20通のメッセージが最低閾値に達した後に追跡される。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール:</b>(クリック数の合計) / (配信数)</li>
        <li><b>コンテンツカード:</b>(クリック数の合計) / (インプレッション数の合計)</li>
        <li><b>SMS:</b>(クリック数）／（配達数）</li>
    </ul>
</span>
{:/}

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
メール, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

開封されたメッセージ数の合計。LINEの場合は、1日20通のメッセージが最低閾値に達した後に追跡される。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール:</b>(開封数) / (配信数)</li>
        <li><b>Web プッシュ:</b>(直接開封数) / (配信数)</li>
        <li><b>iOS、Android、および Kindle のプッシュ:</b>(ユニーク開封数) / (配信数)</li>
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
メール, コンテンツカード, LINE
{% endapitags %}

メッセージ内で少なくとも1回クリックした受信者の数。メールの場合、これは 7 日間にわたって追跡されます。これには、Brazeが提供する配信停止リンクのクリックも含まれる。

LINEの場合は、1日20通のメッセージが最低閾値に達した後に追跡される。 

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール:</b>(ユニーククリック数) / (配信数)</li>
        <li><b>コンテンツカード: </b>(ユニーククリック数) / (ユニークインプレッション数)</li>
    </ul>
</span>
{:/}

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
メール, LINE
{% endapitags %}

これは、配信されたメールのうち、一人のユーザーが一度でも開封したメールの総数を7日間にわたって追跡したものである。LINEの場合は、1日20通のメッセージが最低閾値に達した後に追跡される。

<span class="calculation-line">計算式: (ユニーク開封数) / (配信数)</span>

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
すべて
{% endapitags %}

1日のユニーク受信者数、つまり1日に特定のメッセージを受信したユーザーの数。この数値は Braze から受信します。

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
