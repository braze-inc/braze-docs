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

{% multi_lang_include metrics.md metric='AMPクリック' %}

{% endapi %}

{% api %}

### AMPが開く

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### オーディエンス

{% apitags %}
すべて
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数)/(ユニーク受信者数)</span>

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
メール、Web プッシュ、iOS プッシュ
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} これは、有効なプッシュトークンが存在しないか、キャンペーン開始後にユーザーが配信停止したか、メールアドレスが間違っているかまたは無効化されているために発生する可能性があります。

#### メール

SendGrid を使用している顧客のメールバウンスには、ハードバウンス、スパム (`spam_report_drops`)、および無効なアドレスに送信されたメール (`invalid_emails`) があります。

メールの場合、[*バウンス率 (%)*] または [*バウンス率*] は、使用した送信サービスが送信に失敗した、または「返送された」や「受信されなかった」が示されたメッセージ、あるいは目的のメール可能なユーザーが受信しなかったメッセージの割合です。

#### プッシュ

これらのユーザーに対し、今後のすべてのプッシュ通知が自動的に配信停止されています。 

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

{% multi_lang_include metrics.md metric='Body Click' %}

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### 本文クリック数 (複数回)

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Clicks' %} 詳細については、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310)および[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100)のSDK 変更点を参照してください。

<span class="calculation-line">計算式: (本文クリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 1 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='ボタン1クリック' %}

<span class="calculation-line">計算式: (ボタン 1 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### ボタン 2 のクリック数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='ボタン2クリック' %}

<span class="calculation-line">計算式: (ボタン 2 のクリック数) / (インプレッション数)</span>

{% endapi %}

{% api %}

### 選択肢の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### クリック開封率

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数) (メールの場合)</span>

{% endapi %}

{% api %}

### 確認済み配信数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmed Deliveries' %} Braze を利用する顧客の場合、配信数は SMS 割り当てに対して請求されます。 

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 信頼度

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 確認ページのボタン

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### 確認ページの却下

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### コンバージョン (B、C、D)

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %} この定義済みイベントは、キャンペーンを作成するときにあなたが決定します。Eメール、プッシュ、ウェブフックについては、最初の送信後にコンバージョンのトラッキングを開始する。コンテンツカードの場合、このカウントはコンテンツカードを初めて閲覧した時点から始まります。

#### アプリ内メッセージ

アプリ内メッセージの場合、ユーザーがアプリ内メッセージキャンペーンを受信して表示し、その後定義されているコンバージョン期間内に特定のコンバージョンイベントを実行した場合、メッセージをクリックしたかどうかに関係なく、コンバージョンがカウントされます。

変換は、最後に受信したメッセージに起因します。再適格性が有効な場合、定義されているコンバージョン期間内にコンバージョンが行われる限り、コンバージョンは受信した最新のアプリ内メッセージに割り当てられます。ただし、アプリ内メッセージに変換がすでに割り当てられている場合、その新しい変換はその特定のメッセージについてログに記録できません。これは、各アプリ内メッセージ配信が1つのコンバージョンにのみ関連付けられていることを意味します。

{% endapi %}

{% api %}

### コンバージョン数合計

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Conversions' %}

ユーザーがアプリ内メッセージキャンペーンを1回だけ表示する場合、後でコンバージョンイベントを複数回実行しても、カウントされるのは1つのコンバージョンのみです。ただし、再適格性が有効になっており、ユーザーに対してアプリ内メッセージキャンペーンが複数回表示される場合、［*コンバージョン数合計*] は、ユーザーが新しいアプリ内メッセージキャンペーンインスタンスのインプレッションをログに記録するたびに1つ増加します。 

例えばユーザーがアプリ内メッセージを2回トリガーし、各アプリ内メッセージインプレッションの後にコンバージョンすると (結果として2回のコンバージョン)、［*コンバージョン数合計*] は2つ増加します。ただし、アプリ内のメッセージインプレッションが1 つしかなく、その後に2 つの変換イベントが続く場合、1 つの変換のみがログに記録され、*Total Conversions* が1 つ増加します。

{% endapi %}

{% api %}

### コンバージョン率

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Rate' %}

#### アプリ内メッセージ

毎日の<i>ユニークインプレッション数</i>の指標は、アプリ内メッセージの<i>コンバージョン率</i>を計算するために使用されます。

アプリ内メッセージのインプレッションは1日あたり1回だけカウントできます。一方、ユーザーが目的のアクションを完了する回数("conversion") は、24 時間以内に増加します。1日に複数回のコンバージョンが発生することもありますが、インプレッションはこのように発生することはありません。したがって、ユーザが1 日に複数回変換を完了した場合、<i>変換レート</i> はそれに応じて増加することができますが、印象は1 回だけカウントされます。

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

{% multi_lang_include metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### 配信数

{% apitags %}
メール、Web プッシュ、iOS プッシュ、Android プッシュ、WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} メールの場合、*Deliveries* は、メール利用可能な相手に正常に送受信されたメッセージ(送信)の総数です。

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

### 配信失敗数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Delivery Failures' %}

<a href="/docs/braze_support/">Braze Support</a>に連絡し、配送失敗の理由を理解するための支援を行ってください。

<span class="calculation-line">計算式: (送信数) - (通信事業者への送信数)</span>

{% endapi %}

{% api %}

### 直接開封数

{% apitags %}
iOS プッシュ
{% endapitags %}

{% multi_lang_include metrics.md metric='Direct Opens' %}

<span class="calculation-line">計算式: (直接開封数) / (配信数)</span>

{% endapi %}

{% api %}

### メール可能

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### エラー数

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include metrics.md metric='Errors' %} エラーは<i>送信数</i>カウントに含まれますが、<i>ユニーク受信者数</i>カウントには含まれません。

{% endapi %}

{% api %}

### 推定実質開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### 失敗数

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Failures' %} 失敗は<i>Sends</i>カウントに含まれますが、<i>Deliveries</i>カウントには含まれません。</td>

<span class="calculation-line">計算(<i>故障率</i>):(失敗数) / (送信数)</span>

{% endapi %}

{% api %}

### ハードバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

この場合、Braze はメールの住所を不正なものとしてマークしますが、ユーザーの[サブスクリプション ステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) と更新しません。メールがハードバウンスされた場合、このメールアドレスへの今後のリクエストは停止されます。

{% endapi %}

{% api %}

### ヘルプ

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Help' %} ユーザー返信は、メッセージ受信から 4 時間以内にユーザーがインバウンドメッセージを送信するたびに測定されます。

{% endapi %}

{% api %}

### 誘発された開封数

{% apitags %}
iOSプッシュ、Androidプッシュ
{% endapitags %}

{% multi_lang_include metrics.md metric='Influenced Opens' %}

<span class="calculation-line">計算式: (誘発された開封数) / (配信数)</span>

{% endapi %}

{% api %}

### 生涯収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### ユーザーあたりの生涯価値

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### 平均日次収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='平均日次収益' %}

{% endapi %}

{% api %}

### 日々の購入

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### ユーザーあたりの日割り収益

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='ユーザーあたりの日次収益' %}

{% endapi %}

{% api %}

### マシン開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Machine Opens' %}この指標の追跡は、SendGrid の場合は 2021年11月11日から、SparkPost の場合は 2021年12月2日から開始されます。

{% endapi %}

{% api %}

### 開封数

{% apitags %}
Webプッシュ、iOSプッシュ、Androidプッシュ
{% endapitags %}

{% multi_lang_include metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### オプトアウト

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Opt-Out' %} ユーザー返信は、メッセージ受信から 4 時間以内にユーザーがインバウンドメッセージを送信するたびに測定されます。

{% endapi %}

{% api %}

### その他の開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %}ユーザーは、マシン開封数が記録される前に、メールも開封できることに注意してください (その他の開封数にカウントされる開封数など)。あるユーザーが、マシン開封イベント後に Apple Mail 以外の受信トレイメールを1回 (またはそれ以上) 開封した場合、ユーザーによるメール開封数がその他の開封数に加算され、ユニーク開封数には1回のみが加算されます。

{% endapi %}

{% api %}

### 再試行保留中

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### 1 次コンバージョン (A) または 1 次コンバージョンイベント

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}メール、プッシュ、Webhook については、最初の送信後にコンバージョンのトラッキングを開始します。コンテンツカードやアプリ内メッセージの場合、このカウントはコンテンツカードやメッセージを初めて閲覧した時点から始まる。

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

{% multi_lang_include metrics.md metric='読み取り' %}

{% endapi %}

{% api %}

### 受信済み

{% apitags %}
メール、コンテンツカード、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、SMS、WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Received' %} 

- コンテンツカード:ユーザーがアプリ内でカードを表示すると「受信済み」になります。
- プッシュ: メッセージが Braze サーバーからプッシュプロバイダーに送信されると「受信済み」になります。
- メール: メッセージが Braze サーバーからメールサービスプロバイダー (ESP) に送信されると「受信済み」になります。
- SMS/MMS: SMS プロバイダーが上流の通信事業者と宛先デバイスから確認を受け取ると「配信済み」になります。
- アプリ内メッセージ：定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。
- WhatsApp:定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。

{% endapi %}

{% api %}

### 拒否数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rejections' %}Braze を利用する顧客の場合、拒否数は SMS 割り当てに対して請求されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 収益

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='収益' %}

{% endapi %}

{% api %}

### 送信済み

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sent' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、WhatsApp、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} この指標は Braze によって提供されます。スケジュールされた キャンペーンを起動すると、このメトリクスには、レート制限のためにまだ送信されたかどうかに関係なく、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、このメトリクスは、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) で選択した内容に応じて異なる方法で計算されます。

- **開始時またはステップエントリ時：**作成され、表示可能なカードの数。ユーザーがカードを見たかどうかはカウントされない。
- **最初のインプレッション発生時:**ユーザーに表示されるカードの数。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、WhatsApp、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %}  この指標は Braze によって提供されます。スケジュールされた キャンペーンを起動すると、このメトリクスには、レート制限のためにまだ送信されたかどうかに関係なく、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、このメトリクスは、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) で選択した内容に応じて異なる方法で計算されます。

- **開始時またはステップエントリ時：**作成され、表示可能なカードの数。ユーザーがカードを見たかどうかはカウントされない。
- **最初のインプレッション発生時:**ユーザーに表示されるカードの数。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### キャリアへの送信数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends to Carrier' %} 

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### ソフトバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} メールがソフトバウンスを受信した場合、通常は72時間以内に再試行されますが、再試行回数は受信側ごとに異なります。

{% endapi %}

{% api %}

### スパム

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

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

{% multi_lang_include metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### 調査の送信数

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### クリック数の合計

{% apitags %}
Eメール、コンテンツカード、SMS、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Clicks' %} LINE の場合、1 日あたり20 メッセージの最小しきい値に達した後、これが追跡されます。AMP メールの場合、これはHTML およびプレーンテキストバージョンのクリックの合計です。

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

{% multi_lang_include metrics.md metric='Total Dismissals' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### インプレッション数の合計

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Impressions' %}この値は、Braze が SDK から受け取ったインプレッションイベント数の合計です。コンテンツカードの場合、これは特定のコンテンツカードで記録されたインプレッションの合計数です。これは、同じユーザに対して複数回インクリメントできます。

アプリ内メッセージの場合、複数のデバイスがあり、再適格性が無効になっている場合、ユーザーに対してアプリ内メッセージが1回だけ表示されます。ユーザーが複数のデバイスを使用している場合でも、ターゲットとなる最初のデバイスでのみ表示されます。これは、プロファイルによりデバイスが統合されており、ユーザーは1つのユーザー ID でこれらのデバイスにログインすることを前提としています。再適格性が有効になっている場合、ユーザーがアプリ内メッセージを表示するたびにインプレッションが記録されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 開封数の合計

{% apitags %}
メール, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Opens' %} LINE の場合、1 日あたり20 メッセージの最小しきい値に達した後、これが追跡されます。AMP メールの場合、これはHTML およびプレーンテキストバージョンの合計オープン数です。 

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>メール: </b>(開封数) / (配信数)</li>
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

{% multi_lang_include metrics.md metric='Total Revenue' %} このメトリクスは、<a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a>を通じてキャンペーン比較レポートでのみ使用できます。

{% endapi %}

{% api %}

### ユニーククリック数

{% apitags %}
メール, コンテンツカード, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} メールの場合、これは7日間にわたって追跡されます。これには、Brazeが提供する配信停止リンクのクリックも含まれる。LINE の場合、1 日 20 通の最小しきい値に達した後、これが追跡されます。

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

{% multi_lang_include metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">計算式: (ユニーク却下数) / (ユニークインプレッション数)</span>

{% endapi %}

{% api %}

### ユニークインプレッション数

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Impressions' %} アプリ内メッセージのユニークインプレッション数は、再適格性が有効で、かつユーザーがトリガーアクションを実行した場合、24時間後に再び加算できます。再適格性が有効になっている場合は、<i>ユニークインプレッション数</i> = <i>ユニーク受信者数</i>です。<br><br>コンテンツカードの場合、ユーザーがコンテンツカードを2回目に表示したときには、カウントは増加しません。 

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### ユニーク開封数

{% apitags %}
メール, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} メールの場合、これは7日間にわたって追跡されます。LINE の場合、1 日 20 通の最小しきい値に達した後、これが追跡されます。

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

{% multi_lang_include metrics.md metric='Unique Recipients' %}

閲覧者は毎日のユニーク受信者となる可能性があるため、<i>ユニークインプレッション数</i>よりもこの数値の方が高くなると予想されます。この番号は、Braze から受信され、`user_id` に基づいています。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信停止数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

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

{% multi_lang_include metrics.md metric='Unsubscribes' %}

<span class="calculation-line">計算式: (配信停止数) / (配信数)</span>

{% endapi %}

{% api %}

### バリエーション

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}