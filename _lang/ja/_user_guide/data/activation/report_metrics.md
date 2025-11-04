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

### AMPが開く

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

<span class="calculation-line">計算式: (バリアントの受信者数)/(ユニーク受信者数)</span>

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
メール、Web プッシュ、iOS プッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} これは、有効なプッシュトークンがない、キャンペーン開始後にユーザーが配信停止した、メールアドレスが不正確または無効になっているなどの理由で発生する可能性がある。

|チャネル|追加情報|
|-------|-----------------------|
|メール|SendGrid を使用している顧客のメールバウンスには、ハードバウンス、スパム (`spam_report_drops`)、および無効なアドレスに送信されたメール (`invalid_emails`) があります。<br><br>メールの場合、[*バウンス率 (%)*] または [*バウンス率*] は、使用した送信サービスが送信に失敗した、または「返送された」や「受信されなかった」が示されたメッセージ、あるいは目的のメール可能なユーザーが受信しなかったメッセージの割合です。|
|プッシュ|これらのユーザーに対し、今後のすべてのプッシュ通知が自動的に配信停止されています。|
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

### 本文クリック数 (1 回)

{% apitags %}
iOSプッシュ、Androidプッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### 本文クリック数 (複数回)

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} 詳細については、[iOSと]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) [Androidの]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100)SDK変更履歴を参照のこと。

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 1 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} _ボタン1クリックの_レポートは、アプリ内メッセージで**レポートの識別子を**「0」に指定した場合のみ機能する。

<span class="calculation-line">計算式: (ボタン 1 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 2 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} _ボタン2クリックの_レポートは、アプリ内メッセージで**レポートの識別子を**「1」に指定した場合のみ機能する。

<span class="calculation-line">計算式: (ボタン 2 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### キャンペーン分析

{% apitags %}
フィーチャーフラグ
{% endapitags %}

さまざまなチャネルにわたるメッセージのパフォーマンス。表示されるメトリックは、選択したメッセージングチャネルによって異なり、[Feature Flag experiment]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) が多変量検定であるかどうかによって異なります。

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

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Brazeの顧客として、配達はSMS割り当てに課金される。 

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>確認済み配信数</i>:カウント</li>
        <li><i>確認済み配信率 (%)</i>(確認済み配信)/(送信)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 信頼度

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、WhatsApp
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
コンテンツカード、電子メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webフック、SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} この定義されたイベントは、キャンペーンを構築する際にあなたが決定する。 

|チャネル|追加情報|
|-------|-----------------------|
|電子メール、プッシュ、Webhook|コンバージョンは初回送信後に追跡されます。|
|コンテンツカードによって促進された|ユーザーが初めてコンテンツカードを表示したときに、変換がカウントされます。|
|アプリ内メッセージ|ユーザーがアプリ内メッセージキャンペーンを受信して表示し、その後定義されているコンバージョン期間内に特定のコンバージョンイベントを実行した場合、メッセージをクリックしたかどうかに関係なく、コンバージョンがカウントされます。<br><br>変換は、最後に受信したメッセージに起因します。再適格性が有効な場合、定義されているコンバージョン期間内にコンバージョンが行われる限り、コンバージョンは受信した最新のアプリ内メッセージに割り当てられます。ただし、アプリ内メッセージに変換がすでに割り当てられている場合、その新しい変換はその特定のメッセージについてログに記録できません。これは、各アプリ内メッセージ配信が1つのコンバージョンにのみ関連付けられていることを意味します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### コンバージョン数合計

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

ユーザーがアプリ内メッセージキャンペーンを1回だけ表示する場合、後でコンバージョンイベントを複数回実行しても、カウントされるのは1つのコンバージョンのみです。ただし、再適格性が有効になっており、ユーザーに対してアプリ内メッセージキャンペーンが複数回表示される場合、［*コンバージョン数合計*] は、ユーザーが新しいアプリ内メッセージキャンペーンインスタンスのインプレッションをログに記録するたびに1つ増加します。 

例えばユーザーがアプリ内メッセージを2回トリガーし、各アプリ内メッセージインプレッションの後にコンバージョンすると (結果として2回のコンバージョン)、［*コンバージョン数合計*] は2つ増加します。ただし、アプリ内のメッセージインプレッションが1 つしかなく、その後に2 つの変換イベントが続く場合、1 つの変換のみがログに記録され、*Total Conversions* が1 つ増加します。

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
コンテンツカード、電子メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webフック、SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|チャネル|追加情報|
|-------|-----------------------|
|アプリ内メッセージ|毎日の<i>ユニークインプレッション数</i>の指標は、アプリ内メッセージの<i>コンバージョン率</i>を計算するために使用されます。<br><br>アプリ内メッセージのインプレッションは1日あたり1回だけカウントできます。一方、ユーザーが目的のアクションを完了する回数("conversion") は、24 時間以内に増加します。1日に複数回のコンバージョンが発生することもありますが、インプレッションはこのように発生することはありません。したがって、ユーザが1 日に複数回変換を完了した場合、<i>変換レート</i> はそれに応じて増加することができますが、印象は1 回だけカウントされます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>アプリ内メッセージ</b>:(1次コンバージョン数) / (ユニークインプレッション数)</li>
        <li><b>その他のチャンネル</b>:(1次コンバージョン数) / (ユニーク受信者数)</li>
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
|メール|メール可能な相手に正常に送受信されたメール (送信) の総数です。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>配信数</i>:カウント</li>
        <li><i>配信 (%)</i>:(送信数 - バウンス数) / (送信数)</li>
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

<a href="/docs/braze_support/">Braze Support</a>に連絡し、配送失敗の理由を理解するための支援を行ってください。

<span class="calculation-line">計算式: (送信数) - (通信事業者への送信数)</span>

{% endapi %}

{% api %}

### 配信失敗数

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

<a href="/docs/braze_support/">Braze Support</a>に連絡し、配送失敗の理由を理解するための支援を行ってください。

<span class="calculation-line">計算式: (送信数) - (通信事業者への送信数)</span>

{% endapi %}

{% api %}

### 配信失敗率

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

<a href="/docs/braze_support/">Braze Support</a>に連絡し、配送失敗の理由を理解するための支援を行ってください。

<span class="calculation-line">計算式: (配信失敗)/(送信)</span>

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

{% multi_lang_include analytics/metrics.md metric='Errors' %} エラーは<i>送信</i>数には含まれるが、<i>ユニーク受信者</i>数には含まれない。

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

{% multi_lang_include analytics/metrics.md metric='Failures' %} 失敗は<i>送信</i>回数には含まれるが、<i>配達</i>回数には含まれない。</td>

<span class="calculation-line">計算(<i>故障率</i>):(失敗数) / (送信数)</span>

{% endapi %}

{% api %}

### 特徴フラグ実験性能

{% apitags %}
フィーチャーフラグ
{% endapitags %}

Feature Flag 実験でのメッセージのパフォーマンスメトリクス。表示される特定のメトリクスは、メッセージングチャネル、および実験が多変量検定であるかどうかによって異なります。

{% endapi %}

{% api %}

### ハードバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

この場合、Braze はメールの住所を不正なものとしてマークしますが、ユーザーの[サブスクリプション ステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) と更新しません。メールがハードバウンスされた場合、このメールアドレスへの今後のリクエストは停止されます。

{% endapi %}

{% api %}

### ヘルプ

{% apitags %}
SMS/MMS、RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} ユーザーからの返信は、あなたのメッセージを受け取ってから4時間以内にユーザーがインバウンドメッセージを送信した場合に測定される。

{% endapi %}

{% api %}

### 誘発された開封数

{% apitags %}
iOSプッシュ、Androidプッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">計算式: (誘発された開封数) / (配信数)</span>

{% endapi %}

{% api %}

### 生涯収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### ユーザーあたりの生涯価値

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### 平均日次収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### 日々の購入

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### ユーザーあたりの日割り収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### マシン開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} この指標は、SendGridでは2021年11月11日から、SparkPostでは2021年12月2日からトラッキング 追跡される。Amazon SES の場合、分析は_開封数_として表示されます。ただし、クリックに対するボットフィルターはサポートされる予定です。

{% endapi %}

{% api %}

### 開封数

{% apitags %}
Webプッシュ、iOSプッシュ、Androidプッシュ
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### オプトアウト

{% apitags %}
SMS/MMS、RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} ユーザーからの返信は、あなたのメッセージを受け取ってから4時間以内にユーザーがインバウンドメッセージを送信した場合に測定される。

{% endapi %}

{% api %}

### その他の開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} マシン開封カウントが記録される前に、ユーザーがメールを開封することも可能であることに注意すること（その他の開封に向けた開封カウントなど）。あるユーザーが、マシン開封イベント後に Apple Mail 以外の受信トレイメールを1回 (またはそれ以上) 開封した場合、ユーザーによるメール開封数がその他の開封数に加算され、ユニーク開封数には1回のみが加算されます。

{% endapi %}

{% api %}

### 再試行保留中

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### 1 次コンバージョン (A) または 1 次コンバージョンイベント

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|チャネル|追加情報|
|-------------|----------------------|
|電子メール、プッシュ、Webhook|初回送信後。|
|コンテンツカード、アプリ内メッセージ|ユーザーがコンテンツカードまたはメッセージを初めて閲覧したとき。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>1次コンバージョン (A) または 1次コンバージョンイベント</i>:カウント</li>
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

### 読み取り率

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">計算式: (既読通知付きで読む) / (送信)</span>

{% endapi %}

{% api %}

### 受信済み

{% apitags %}
Eメール、コンテンツカード、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|チャネル|追加情報|
|-------|-------|
|コンテンツカードによって促進された|ユーザーがアプリ内でカードを表示すると「受信済み」になります。|
|プッシュ|メッセージが Braze サーバーからプッシュプロバイダーに送信されると「受信済み」になります。|
|メール|メッセージが Braze サーバーからメールサービスプロバイダー (ESP) に送信されると「受信済み」になります。|
|SMS/MMS|SMS プロバイダーが上流の通信事業者と宛先デバイスから確認を受け取ると「配信済み」になります。|
|アプリ内メッセージ|定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。|
|WhatsApp|定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### RCS 拒否数または SMS 拒否数

{% apitags %}
SMS/MMS、RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Brazeの顧客として、拒否はあなたのSMS割り当てに課金される。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>拒否数</i>:カウント</li>
        <li><i>拒否率</i>:(拒否)/(送信)</li>
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
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、RCS、WhatsApp、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} この指標はBrazeが提供している。スケジュールされた キャンペーンを起動すると、このメトリクスには、レート制限のためにまだ送信されたかどうかに関係なく、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、このメトリクスは、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) で選択した内容に応じて異なる方法で計算されます。

- **開始時またはステップエントリ時：**作成され、見ることができるカードの数。ユーザーがカードを見たかどうかはカウントされない。
- **最初のインプレッション発生時:**ユーザーに表示されるカードの数。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、WhatsApp、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  この指標はBrazeが提供している。スケジュールされた キャンペーンを起動すると、このメトリクスには、レート制限のためにまだ送信されたかどうかに関係なく、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、このメトリクスは、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) で選択した内容に応じて異なる方法で計算されます。

- **開始時またはステップエントリ時：**作成され、見ることができるカードの数。ユーザーがカードを見たかどうかはカウントされない。
- **最初のインプレッション発生時:**ユーザーに表示されるカードの数。
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
        <li><i>キャリアへ送信</i>:カウント</li>
        <li><i>キャリアレートへ送信</i>:(キャリアへ送信)/(送信)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ソフトバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} _ソフトバウンスは_ _延期とは_異なることに注意。この再試行期間中にメールが正常に配信されなかった場合、Brazeは送信されたキャンペーンごとに1つのソフトバウンスイベントを送信する。2025年2月25日以前は、これらの再試行は1回のキャンペーン送信に対して複数のソフトバウンスとしてカウントされていた。

ソフトバウンスはキャンペーン分析では追跡されませんが、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)で監視できます。また、これらのユーザーを送信から除外したり、[ソフトバウンスのセグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)で過去30日間のソフトバウンスの量を確認することもできます。メッセージアクティビティログでは、ソフトバウンスの理由を確認し、メールキャンペーンの「送信」と「配信」の間に発生する可能性のある不一致を理解することもできます。

{% endapi %}

{% api %}

### スパム

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
スパムの苦情は、電子メールサービスプロバイダによって直接処理され、フィードバックループを通じてBraze に中継されます。ほとんどのフィードバックループは、実際の苦情の一部のみを報告するため、_Spam_メトリクスは、多くの場合、実際の合計の割合を表します。メールサービスプロバイダのみがスパム苦情の本当のボリュームを表示できます。つまり、_スパム_ は、すべてを網羅するメトリックではなく、指標と見なす必要があります。
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>スパム</i>:カウント</li>
        <li><i>スパム率</i><i> (%)</i>(スパムとしてマークされた数) / (送信数)</li>
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
電子メール、コンテンツカード、SMS/MMS、LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|チャネル|追加情報|
|-------|-------|
|LINE|1日20通の最小しきい値に達した後に追跡されます。AMPの電子メールには、HTMLとプレーンテキストの両方のバージョンで記録されたクリックが含まれます。この数字は、スパム対策ツールによって人為的に膨らませる可能性があります。|
|バナー|同じユーザーが複数回クリックしたかどうかに関係なく、配信されたメッセージ内でクリックしたユーザーの総数 (およびパーセンテージ)。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール: </b>(クリック数の合計) / (配信数)</li>
        <li><b>コンテンツカード: </b>(クリック数の合計) / (インプレッション数の合計)</li>
        <li><b>SMS:</b>(クリック開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 却下数の合計

{% apitags %}
コンテンツカード
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} ユーザーが同じキャンペーンから2つの異なるカードを受け取り、両方を却下した場合、このカウントは2つ増える。再適格性により、ユーザーがカードを受け取るたびに_却下数の合計_を増やすことができます。各カードは異なるメッセージです。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>却下数の合計</i>カウント</li>
        <li><i>却下率の合計</i>却下数の合計/インプレッション数の合計</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### インプレッション数の合計

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} この数値は、BrazeがSDKから受け取るインプレッションイベント数の合計である。

|チャネル|追加情報|
|-------|-----------------------|
|コンテンツカードによって促進された|特定のコンテンツカードについて記録されたインプレッションの合計数。これは、同じユーザに対して複数回インクリメントできます。|
|アプリ内メッセージ|複数のデバイスがあり、再適格性が無効になっている場合、ユーザーに対してアプリ内メッセージが1回だけ表示されます。ユーザーが複数のデバイスを使用している場合でも、ターゲットとなる最初のデバイスでのみ表示されます。これは、プロファイルによりデバイスが統合されており、ユーザーは1つのユーザー ID でこれらのデバイスにログインすることを前提としています。再適格性が有効になっている場合、ユーザーがアプリ内メッセージを表示するたびにインプレッションが記録されます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 開封数の合計

{% apitags %}
メール, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|チャネル|追加情報|
|-------|-----------------------|
|LINE|1日20通の最小しきい値に達した後に追跡されます。|
|AMP メール|HTMLとプレーンテキストバージョンの合計が開きます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール <i>開封数の合計</i>:</b>カウント</li>
        <li><b>メール <i>合計開封率</i>:</b>(開封数) / (配信数)</li>
        <li><b>Web プッシュ <i>開封数の合計</i>:</b><i>直接開封数</i>の数</li>
        <li><b>Web プッシュ <i>合計開封率</i>:</b>(開封数の合計) / (配信数)</li>
        <li><b>iOS、Android、および Kindle のプッシュ<i>開封数の合計</i>:</b>(直接開封数) + (誘発された開封数)</li>
        <li><b>iOS、Android、およびKindle プッシュ<i>合計開放率</i>:</b>(開封数の合計) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 総収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} この指標は、<a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>レポートビルダーによる</a>キャンペーン比較レポートでのみ利用可能である。

{% endapi %}

{% api %}

### ユニーククリック数

{% apitags %}
メール, コンテンツカード, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

これには、Brazeが提供する配信停止リンクのクリックも含まれる。

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
        <li><b>コンテンツカード</b><i>ユニーククリック率 (%)</i> または<i>ユニーククリック率</i>:(ユニーククリック数) / (ユニークインプレッション数)</li>
        <li><b>メールの</b><i>ユニーククリック率 (%)</i> または<i>ユニーククリック率</i>:(ユニーククリック数) / (配信数)</li>
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
|アプリ内メッセージ|ユニークインプレッション数は、再適格性が有効になり、ユーザーがトリガーアクションを実行した場合、24時間後に再び加算できます。再適格性が有効になっている場合は、<i>ユニークインプレッション数</i> = <i>ユニーク受信者数</i>です。|
|コンテンツカードによって促進された|ユーザーがコンテンツカードを 2 回目に表示したときには、カウントは増加しません。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### ユニーク開封数

{% apitags %}
メール, LINE
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

閲覧者は毎日のユニーク受信者となる可能性があるため、<i>ユニークインプレッション数</i>よりもこの数値の方が高くなると予想されます。コンテンツカードの場合、各コンテンツカードは1回しか受信できません。そのため、同じコンテンツカードを2回目に表示しても、その日に関係なく、このカウントは増分されません。<br><br>この番号は、Braze から受信され、`user_id` に基づいています。一意の受信者は、<a href='https://braze.com/docs/api/identifier_types/#send-identifier'>送信識別子</a>レベルではなく、キャンペーンまたはキャンバスのステップレベルでカウントされます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信停止数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>配信</i><i>停止数</i>:カウント</li>
        <li><i>配信</i><i>停止率 (%)</i>:(配信停止数) / (配信数)</li>
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
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS/MMS、WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}