---
nav_title: レポート指標用語集
article_title: レポート指標の用語集
layout: report_metrics
page_order: 0.5
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

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### AMP 開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### オーディエンス

{% apitags %}
すべて
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数) / (ユニーク受信者数)</span>

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
メール、Web プッシュ、iOS プッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} これは、有効なプッシュトークンがない、キャンペーン開始後にユーザーが配信停止した、メールアドレスが不正確または無効になっているなどの理由で発生する可能性があります。

|チャネル|追加情報|
|-------|-----------------------|
|メール|SendGrid を使用している顧客のメールバウンスには、ハードバウンス、スパム (`spam_report_drops`)、および無効なアドレスに送信されたメール (`invalid_emails`) が含まれます。<br><br>メールの場合、*バウンス率 (%)* または*バウンス率*は、使用した送信サービスが送信に失敗した、または「返送された」や「受信されなかった」と指定されたメッセージ、あるいは目的のメール可能なユーザーが受信しなかったメッセージの割合です。|
|プッシュ|これらのユーザーは、今後のすべてのプッシュ通知から自動的に配信停止されています。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>バウンス数</i>:カウント</li>
        <li><i>バウンス率 (%)</i> または<i>バウンス率</i>:(バウンス数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 本文クリック

{% apitags %}
iOS プッシュ、Android プッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### 本文クリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} 詳細については、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) と [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100) の SDK 変更ログを参照してください。

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 1 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} _ボタン 1 クリック_のレポートは、アプリ内メッセージで**レポートの識別子**を「0」に指定した場合のみ機能します。

<span class="calculation-line">計算式: (ボタン 1 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 2 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} _ボタン 2 クリック_のレポートは、アプリ内メッセージで**レポートの識別子**を「1」に指定した場合のみ機能します。

<span class="calculation-line">計算式: (ボタン 2 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### キャンペーン分析

{% apitags %}
フィーチャーフラグ
{% endapitags %}

さまざまなチャネルにわたるメッセージのパフォーマンス。表示される指標は、選択したメッセージングチャネルや、[フィーチャーフラグ実験]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics)が多変量テストであるかどうかによって異なります。

{% endapi %}

{% api %}

### 選択肢の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### クリック開封率

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数) (メールの場合)</span>

{% endapi %}

{% api %}

### RCS 確認済み配信数または SMS 確認済み配信数

{% apitags %}
SMS/MMS、RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Braze の顧客として、配信は SMS 割り当てに対して課金されます。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>確認済み配信数</i>:カウント</li>
        <li><i>確認済み配信率 (%)</i>:(確認済み配信数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 信頼度

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 確認ページのボタン

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### 確認ページの却下

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### コンバージョン (B、C、D)

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} この定義済みイベントは、キャンペーンを構築する際に設定します。

|チャネル|追加情報|
|-------|-----------------------|
|メール、プッシュ、Webhook|コンバージョンは初回送信後に追跡されます。|
|コンテンツカード|ユーザーが初めてコンテンツカードを表示したときに、コンバージョンがカウントされます。|
|アプリ内メッセージ|ユーザーがアプリ内メッセージキャンペーンを受信して表示し、その後定義されたコンバージョン期間内に特定のコンバージョンイベントを実行した場合、メッセージをクリックしたかどうかに関係なく、コンバージョンがカウントされます。<br><br>コンバージョンは、最後に受信したメッセージに帰属します。再適格性が有効な場合、定義されたコンバージョン期間内にコンバージョンが発生する限り、コンバージョンは最後に受信したアプリ内メッセージに割り当てられます。ただし、アプリ内メッセージにすでにコンバージョンが割り当てられている場合、その特定のメッセージに対して新しいコンバージョンを記録することはできません。つまり、各アプリ内メッセージ配信は1つのコンバージョンにのみ関連付けられます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### コンバージョン数合計

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

ユーザーがアプリ内メッセージキャンペーンを1回だけ表示した場合、後でコンバージョンイベントを複数回実行しても、カウントされるのは1つのコンバージョンのみです。ただし、再適格性が有効になっており、ユーザーがアプリ内メッセージキャンペーンを複数回表示した場合、*コンバージョン数合計*は、ユーザーが新しいアプリ内メッセージキャンペーンインスタンスのインプレッションを記録するたびに1つずつ増加します。

例えば、ユーザーがアプリ内メッセージを2回トリガーし、各アプリ内メッセージインプレッションの後にコンバージョンした場合 (結果として2回のコンバージョン)、*コンバージョン数合計*は2つ増加します。ただし、アプリ内メッセージのインプレッションが1回のみで、その後に2つのコンバージョンイベントが続いた場合、記録されるコンバージョンは1つのみで、*コンバージョン数合計*は1つ増加します。

{% endapi %}

{% api %}

### メッセージを閉じる

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### コンバージョン率

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|チャネル|追加情報|
|-------|-----------------------|
|アプリ内メッセージ|毎日の<i>ユニークインプレッション数</i>の指標が、アプリ内メッセージの<i>コンバージョン率</i>の計算に使用されます。<br><br>アプリ内メッセージのインプレッションは1日あたり1回のみカウントされます。一方、ユーザーが目的のアクション (「コンバージョン」) を完了する回数は、24時間以内に増加する可能性があります。1日に複数回のコンバージョンが発生することはありますが、インプレッションは複数回カウントされません。したがって、ユーザーが1日に複数回コンバージョンを完了した場合、<i>コンバージョン率</i>はそれに応じて増加しますが、インプレッションは1回のみカウントされます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b>アプリ内メッセージ</b>:(1次コンバージョン数) / (ユニークインプレッション数)</li>
        <li><b>その他のチャネル</b>:(1次コンバージョン数) / (ユニーク受信者数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### コンバージョン期間

{% apitags %}
すべて
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### 配信数

{% apitags %}
メール、Web プッシュ、iOS プッシュ、Android プッシュ、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|チャネル|追加情報|
|-------|-----------------------|
|メール|メール可能な相手に正常に送受信されたメッセージ (送信) の総数です。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>配信数</i>:カウント</li>
        <li><i>配信率 (%)</i>:(送信数 - バウンス数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### RCS 配信失敗数または SMS 配信失敗数

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

配信失敗の原因究明については、<a href="/docs/braze_support/">Braze サポート</a>にお問い合わせください。

<span class="calculation-line">計算式: (送信数) - (通信事業者への送信数)</span>

{% endapi %}

{% api %}

### 配信失敗数

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

配信失敗の原因究明については、<a href="/docs/braze_support/">Braze サポート</a>にお問い合わせください。

<span class="calculation-line">計算式: (送信数) - (通信事業者への送信数)</span>

{% endapi %}

{% api %}

### 配信失敗率

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

配信失敗の原因究明については、<a href="/docs/braze_support/">Braze サポート</a>にお問い合わせください。

<span class="calculation-line">計算式: (配信失敗数) / (送信数)</span>

{% endapi %}

{% api %}

### 直接開封数

{% apitags %}
iOS プッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">計算式: (直接開封数) / (配信数)</span>

{% endapi %}

{% api %}

### メール可能

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### エラー数

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} エラーは<i>送信</i>数には含まれますが、<i>ユニーク受信者</i>数には含まれません。

{% endapi %}

{% api %}

### 推定実質開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### 失敗数

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} 失敗は<i>送信</i>数には含まれますが、<i>配信</i>数には含まれません。</td>

<span class="calculation-line">計算式 (<i>失敗率</i>):(失敗数) / (送信数)</span>

{% endapi %}

{% api %}

### フィーチャーフラグ実験パフォーマンス

{% apitags %}
フィーチャーフラグ
{% endapitags %}

フィーチャーフラグ実験におけるメッセージのパフォーマンス指標。表示される具体的な指標は、メッセージングチャネルや、実験が多変量テストであるかどうかによって異なります。

{% endapi %}

{% api %}

### ハードバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

この場合、Braze はメールアドレスを無効としてマークしますが、ユーザーの[サブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)は更新しません。メールがハードバウンスされた場合、このメールアドレスへの今後のリクエストは停止されます。

{% endapi %}

{% api %}

### ヘルプ

{% apitags %}
SMS/MMS、RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} ユーザーからの返信は、メッセージを受け取ってから4時間以内にユーザーがインバウンドメッセージを送信した場合に測定されます。

{% endapi %}

{% api %}

### 誘発された開封数

{% apitags %}
iOS プッシュ、Android プッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">計算式: (誘発された開封数) / (配信数)</span>

{% endapi %}

{% api %}

### 生涯収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### ユーザーあたりの生涯価値

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### 平均日次収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### 日次購入数

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### ユーザーあたりの日次収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### マシン開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} この指標は、SendGrid では2021年11月11日から、SparkPost では2021年12月2日からトラッキングされています。Amazon SES の場合、分析は_開封数_として表示されます。ただし、クリックに対するボットフィルタリングはサポートされます。

{% endapi %}

{% api %}

### 開封数

{% apitags %}
Web プッシュ、iOS プッシュ、Android プッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### オプトアウト

{% apitags %}
SMS/MMS、RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} ユーザーからの返信は、メッセージを受け取ってから4時間以内にユーザーがインバウンドメッセージを送信した場合に測定されます。

{% endapi %}

{% api %}

### その他の開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} マシン開封数が記録される前に、ユーザーがメールを開封する場合もあります（その開封数はその他の開封数にカウントされます）。あるユーザーが、マシン開封イベント後に Apple Mail 以外の受信トレイからメールを1回 (またはそれ以上) 開封した場合、そのユーザーによるメール開封回数がその他の開封数に加算され、ユニーク開封数には1回のみ加算されます。

{% endapi %}

{% api %}

### 再試行保留中

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### 1次コンバージョン (A) または1次コンバージョンイベント

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|チャネル|追加情報|
|-------------|----------------------|
|メール、プッシュ、Webhook|初回送信後。|
|コンテンツカード、アプリ内メッセージ|ユーザーがコンテンツカードまたはメッセージを初めて閲覧したとき。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>1次コンバージョン (A) または1次コンバージョンイベント</i>:カウント</li>
        <li><i>1次コンバージョン (A) %</i> または<i>1次コンバージョンイベント率</i>:(1次コンバージョン数) / (ユニーク受信者数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 既読数

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### 既読率

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">計算式: (既読通知付きの既読数) / (送信数)</span>

{% endapi %}

{% api %}

### 受信済み

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|チャネル|追加情報|
|-------|-------|
|コンテンツカード|ユーザーがアプリ内でカードを表示すると「受信済み」になります。|
|プッシュ|メッセージが Braze サーバーからプッシュプロバイダーに送信されると「受信済み」になります。|
|メール|メッセージが Braze サーバーからメールサービスプロバイダー (ESP) に送信されると「受信済み」になります。|
|SMS/MMS|SMS プロバイダーが上流の通信事業者と宛先デバイスから確認を受け取ると「配信済み」になります。|
|アプリ内メッセージ|定義されたトリガーアクションに基づいて表示されたときに「受信済み」になります。|
|WhatsApp|定義されたトリガーアクションに基づいて表示されたときに「受信済み」になります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### RCS 拒否数または SMS 拒否数

{% apitags %}
SMS/MMS、RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Braze の顧客として、拒否は SMS 割り当てに対して課金されます。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>拒否数</i>:カウント</li>
        <li><i>拒否率</i>:(拒否数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 収益

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### 送信済み

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、RCS、WhatsApp、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} この指標は Braze が提供しています。スケジュールされたキャンペーンを起動すると、この指標には、レート制限のためにまだ送信されていないものも含め、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、この指標は、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)で選択した内容に応じて異なる方法で計算されます。

- **起動時またはステップエントリ時:**作成され、閲覧可能なカードの数。ユーザーがカードを閲覧したかどうかはカウントされません。
- **最初のインプレッション発生時:**ユーザーに表示されたカードの数。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、WhatsApp、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} この指標は Braze が提供しています。スケジュールされたキャンペーンを起動すると、この指標には、レート制限のためにまだ送信されていないものも含め、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、この指標は、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)で選択した内容に応じて異なる方法で計算されます。

- **起動時またはステップエントリ時:**作成され、閲覧可能なカードの数。ユーザーがカードを閲覧したかどうかはカウントされません。
- **最初のインプレッション発生時:**ユーザーに表示されたカードの数。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### キャリアへの送信数

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>キャリアへの送信数</i>:カウント</li>
        <li><i>キャリアへの送信率</i>:(キャリアへの送信数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ソフトバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} _ソフトバウンス_は_延期_とは異なることに注意してください。この再試行期間中にメールが正常に配信されなかった場合、Braze は送信を試みたキャンペーンごとに1つのソフトバウンスイベントを送信します。2025年2月25日以前は、これらの再試行は1回のキャンペーン送信に対して複数のソフトバウンスとしてカウントされていました。

ソフトバウンスはキャンペーン分析では追跡されませんが、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)で監視できます。また、これらのユーザーを送信から除外したり、[ソフトバウンスのセグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)で過去30日間のソフトバウンス数を確認したりすることもできます。メッセージアクティビティログでは、ソフトバウンスの理由を確認し、メールキャンペーンの「送信」と「配信」の間に生じる可能性のある差異を把握することもできます。

{% endapi %}

{% api %}

### スパム

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
スパムの苦情は、メールサービスプロバイダーによって直接処理され、フィードバックループを通じて Braze に中継されます。ほとんどのフィードバックループは実際の苦情の一部のみを報告するため、_スパム_指標は多くの場合、実際の合計の一部を表しています。メールサービスプロバイダーのみがスパム苦情の実際のボリュームを確認できるため、_スパム_はすべてを網羅する指標ではなく、参考指標として捉える必要があります。
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>スパム</i>:カウント</li>
        <li><i>スパム率 (%)</i>:(スパムとしてマークされた数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 調査ページの却下数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### 調査の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### クリック数の合計

{% apitags %}
メール、コンテンツカード、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|チャネル|追加情報|
|-------|-------|
|LINE|1日20通の最小しきい値に達した後に追跡されます。AMP メールには、HTML とプレーンテキストの両方のバージョンで記録されたクリックが含まれます。この数値は、スパム対策ツールによって人為的に膨らむ可能性があります。|
|バナー|同じユーザーが複数回クリックしたかどうかに関係なく、配信されたメッセージ内でクリックしたユーザーの総数 (およびパーセンテージ)。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b>メール:</b> (クリック数の合計) / (配信数)</li>
        <li><b>コンテンツカード:</b> (クリック数の合計) / (インプレッション数の合計)</li>
        <li><b>SMS:</b> (クリック開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 却下数の合計

{% apitags %}
コンテンツカード
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} ユーザーが同じキャンペーンから2つの異なるカードを受け取り、両方を却下した場合、このカウントは2つ増えます。再適格性により、ユーザーがカードを受け取るたびに_却下数の合計_を1つずつ増やすことができます。各カードは異なるメッセージです。

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>却下数の合計:</i> カウント</li>
        <li><i>却下率の合計:</i> 却下数の合計 / インプレッション数の合計</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### インプレッション数の合計

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} この数値は、Braze が SDK から受け取るインプレッションイベント数の合計です。

|チャネル|追加情報|
|-------|-----------------------|
|コンテンツカード|特定のコンテンツカードについて記録されたインプレッションの合計数。同じユーザーに対して複数回インクリメントされる場合があります。|
|アプリ内メッセージ|複数のデバイスがあり、再適格性が無効になっている場合、ユーザーに対してアプリ内メッセージは1回だけ表示されます。ユーザーが複数のデバイスを使用している場合でも、ターゲットとなる最初のデバイスでのみ表示されます。これは、プロファイルによりデバイスが統合されており、ユーザーが1つのユーザー ID でこれらのデバイスにログインしていることを前提としています。再適格性が有効になっている場合、ユーザーがアプリ内メッセージを表示するたびにインプレッションが記録されます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 開封数の合計

{% apitags %}
メール、iOS プッシュ、Android プッシュ、Web プッシュ、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|チャネル|追加情報|
|-------|-----------------------|
|LINE|1日20通の最小しきい値に達した後に追跡されます。|
|AMP メール|HTML とプレーンテキストバージョンの合計開封数。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><b>メール <i>開封数の合計</i>:</b> カウント</li>
        <li><b>メール <i>合計開封率</i>:</b> (開封数) / (配信数)</li>
        <li><b>Web プッシュ <i>開封数の合計</i>:</b> <i>直接開封</i>数</li>
        <li><b>Web プッシュ <i>合計開封率</i>:</b> (開封数の合計) / (配信数)</li>
        <li><b>iOS、Android、および Kindle のプッシュ <i>開封数の合計</i>:</b> (直接開封数) + (誘発された開封数)</li>
        <li><b>iOS、Android、および Kindle のプッシュ <i>合計開封率</i>:</b> (開封数の合計) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 総収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} この指標は、<a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>レポートビルダー</a>によるキャンペーン比較レポートでのみ利用可能です。

{% endapi %}

{% api %}

### ユニーククリック数

{% apitags %}
メール、コンテンツカード、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

これには、Braze が提供する配信停止リンクのクリックも含まれます。

|チャネル|追加情報|
|-------|-----------------------|
|メール|7日間にわたって追跡されます。|
|LINE|1日20通の最小しきい値に達した後に追跡されます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>ユニーククリック数</i>:カウント</li>
        <li><b>コンテンツカード</b> <i>ユニーククリック率 (%)</i> または<i>ユニーククリック率</i>:(ユニーククリック数) / (ユニークインプレッション数)</li>
        <li><b>メール</b> <i>ユニーククリック率 (%)</i> または<i>ユニーククリック率</i>:(ユニーククリック数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーク却下数

{% apitags %}
コンテンツカード
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">計算式: (ユニーク却下数) / (ユニークインプレッション数)</span>

{% endapi %}

{% api %}

### ユニークインプレッション数

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|チャネル|追加情報|
|-------|-----------------------|
|アプリ内メッセージ|再適格性が有効になっており、ユーザーがトリガーアクションを実行した場合、ユニークインプレッション数は24時間後に再び加算されます。再適格性が有効になっている場合は、<i>ユニークインプレッション数</i> = <i>ユニーク受信者数</i>です。|
|コンテンツカード|ユーザーがカードを2回目に表示しても、カウントは増加しません。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### ユニーク開封数

{% apitags %}
メール、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|チャネル|追加情報|
|-------|-----------------------|
|メール|7日間にわたって追跡されます。|
|LINE|1日20通の最小しきい値に達した後に追跡されます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>ユニーク開封数</i>:カウント</li>
        <li><i>ユニーク開封率 (%)</i> または<i>ユニーク開封率</i>:(ユニーク開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
すべて
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

閲覧者は毎日ユニーク受信者としてカウントされる可能性があるため、<i>ユニークインプレッション数</i>よりもこの数値の方が高くなることが予想されます。コンテンツカードの場合、各コンテンツカードは1回しか受信できないため、同じコンテンツカードを2回目に表示しても、日付に関係なくこのカウントは増加しません。<br><br>この数値は Braze から提供され、`user_id` に基づいています。ユニーク受信者数は、<a href='https://braze.com/docs/api/identifier_types/#send-identifier'>送信識別子</a>レベルではなく、キャンペーンまたはキャンバスステップレベルでカウントされます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信停止者数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式:
    <ul>
        <li><i>配信停止者数</i>:カウント</li>
        <li><i>配信停止率 (%)</i>:(配信停止数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 配信停止数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">計算式: (配信停止数) / (配信数)</span>

{% endapi %}

{% api %}

### バリエーション

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}