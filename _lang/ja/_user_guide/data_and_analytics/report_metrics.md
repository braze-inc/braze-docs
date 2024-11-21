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

<span class="calculation-line">計算式: (バリアントの受信者数)/(固有の受信者数)</span>

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
メール、Web プッシュ、iOS プッシュ
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} これは、有効なプッシュトークンがないか、キャンペーンの起動後に登録解除されたユーザ、またはメールアドレスが不正確または非アクティブになっているために発生する可能性があります。

#### メール

SendGrid を使用する顧客のメールバウンスは、ハードバウンス、スパム(`spam_report_drops`)、および無効なアドレスに送信されたメール(`invalid_emails`) で構成されます。

E メールの場合、*Bounce %* または *Bounce Rate* は、送信に失敗したメッセージまたは " returned" または "not received" send services used または受信予定のユーザーが受信しなかったメッセージの割合です。

#### プッシュ

これらのユーザは、今後のすべてのプッシュ通知から自動的に登録解除されます。 

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>バウンス</i> :Count</li>
        <li><i>バウンス%</i>または<i>バウンス率%</i>:(センド- バウンス) / (センド)</li>
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

{% multi_lang_include metrics.md metric='クリック・トゥ・オープン率' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数) (メールの場合)</span>

{% endapi %}

{% api %}

### 確認済み配信数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmed Deliveries' %} ブレーズの顧客として、配送はSMS割り当てに対して課金されます。 

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

{% multi_lang_include metrics.md metric='Confirmation ページボタン' %}

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

{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %} この定義済みイベントは、キャンペーンの構築時にユーザーが決定します。Eメール、プッシュ、ウェブフックについては、最初の送信後にコンバージョンのトラッキングを開始する。コンテンツカードの場合、このカウントはコンテンツカードを初めて表示したときに開始されます。

#### アプリ内メッセージ

アプリ内メッセージの場合、ユーザがアプリ内メッセージキャンペーンを受信して表示した場合、変換がカウントされ、その後、メッセージをクリックしたかどうかに関係なく、定義された変換ウィンドウ内で特定の変換イベントが実行されます。

変換は、最後に受信したメッセージに起因します。再適格性が有効な場合、変換は、定義された変換ウィンドウ内で行われる限り、受信した最新のアプリ内メッセージに割り当てられます。ただし、アプリ内メッセージに変換がすでに割り当てられている場合、その新しい変換はその特定のメッセージについてログに記録できません。これは、各アプリ内メッセージ配信が1つの変換にのみ関連付けられていることを意味します。

{% endapi %}

{% api %}

### コンバージョン数合計

{% apitags %}
アプリ内メッセージ
{% endapitags %}

{% multi_lang_include metrics.md metric='合計変換数' %}

ユーザがアプリ内メッセージキャンペーンを1 回のみ表示する場合、後で変換イベントを複数回実行しても、1 つの変換のみがカウントされます。ただし、再適格性が有効になっており、ユーザがアプリ内メッセージキャンペーンを複数回表示する場合、*Total Conversions* は、ユーザがアプリ内メッセージキャンペーンの新しいインスタンスのインプレッションをログに記録するたびに1 回増加します。 

たとえば、ユーザがアプリ内メッセージを2 回トリガし、各アプリ内メッセージインプレッションの後に変換(結果として2 回の変換) した場合、*Total Conversions* は2 つ増加します。ただし、アプリ内のメッセージインプレッションが1 つしかなく、その後に2 つの変換イベントが続く場合、1 つの変換のみがログに記録され、*Total Conversions* が1 つ増加します。

{% endapi %}

{% api %}

### コンバージョン率

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Rate' %}

#### アプリ内メッセージ

毎日の合計<i>固有の印象</i>のメトリクスは、アプリ内メッセージの<i>変換レート</i>を計算するために使用されます。

アプリ内メッセージの印象は1日に1回しかカウントできません。一方、ユーザーが目的のアクションを完了する回数("conversion") は、24 時間以内に増加します。1日に複数回の変換が行われることもありますが、インプレッションはできません。したがって、ユーザが1 日に複数回変換を完了した場合、<i>変換レート</i> はそれに応じて増加することができますが、印象は1 回だけカウントされます。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b>アプリ内メッセージ</b>:(一次変換)/(独自の印象)</li>
        <li><b>その他のチャンネル</b>:(一次変換)/(一意の受信者)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### コンバージョン期間

{% apitags %}
すべて
{% endapitags %}

{% multi_lang_include metrics.md metric='変換ウィンドウ' %}

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
        <li><i>デリバリー</i>:カウント</li>
        <li><i>デリバリー%</i>:(センド- バウンス) / (センド)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 配信失敗数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='配信失敗' %}

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

{% multi_lang_include metrics.md metric='Eメール可能' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### エラー数

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include metrics.md metric='Errors' %} エラーは<i>送信</i>カウントに含まれますが、<i>一意の受信者</i>カウントには含まれません。

{% endapi %}

{% api %}

### 推定実質オープン

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='推定実質オープン' %}

{% endapi %}

{% api %}

### 失敗数

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Failures' %} 失敗は<i>Sends</i>カウントに含まれますが、<i>Deliveries</i>カウントには含まれません。</td>

<span class="calculation-line">計算(<i>故障率</i>):(失敗)/(送信)</span>

{% endapi %}

{% api %}

### ハードバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

この場合、Braze はメールの住所を不正なものとしてマークしますが、ユーザーの[サブスクリプション ステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) と更新しません。メールがハードバウンスを受信した場合、このメールアドレスへの今後のリクエストは停止されます。

{% endapi %}

{% api %}

### ヘルプ

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Help' %} ユーザがメッセージを受信してから4 時間以内に受信メッセージを送信するたびに、ユーザの応答が測定されます。

{% endapi %}

{% api %}

### 誘発された開封数

{% apitags %}
iOSプッシュ、Androidプッシュ
{% endapitags %}

{% multi_lang_include metrics.md metric='影響を受けるオープン' %}

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

{% multi_lang_include metrics.md metric='ユーザあたりの寿命値' %}

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

{% multi_lang_include metrics.md metric='Machine Opens' %} このメトリクスは、SendGrid の場合は2021年11 月11 日、SparkPost の場合は2021年12 月2 日から追跡されます。

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

{% multi_lang_include metrics.md metric='Opt-Out' %} ユーザがメッセージを受信してから4時間以内に受信メッセージを送信するたびに、ユーザの応答が測定されます。

{% endapi %}

{% api %}

### その他の開封数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} マシンオープン数がログに記録される前に、ユーザがメールを開くこともできます(その他のオープン数など)。Apple Mail 以外の受信トレイからマシンが開いているイベントの後に、ユーザがメールを1 回(または複数回)開いた場合、ユーザがメールを開いた回数は「その他の開く」に向かって計算され、一度だけ「一意の開く」に向かって計算されます。

{% endapi %}

{% api %}

### 再試行保留中

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='保留中の再試行' %}

{% endapi %}

{% api %}

### 1 次コンバージョン (A) または 1 次コンバージョンイベント

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Web プッシュ、iOS プッシュ、Android プッシュ、Webhook、SMS、WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} メール、プッシュ、およびウェブフックの場合、最初の送信後に変換の追跡を開始します。コンテンツカードやアプリ内メッセージの場合、このカウントはコンテンツカードやメッセージを初めて閲覧した時点から始まる。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>一次変換(A)または一次変換イベント</i>:カウント</li>
        <li><i>プライマリ変換(A) %</i> または<i>プライマリ変換イベントレート</i>:(一次変換)/(一意の受信者)</li>
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
- SMS/MMS: SMSプロバイダがアップストリームキャリアと宛先デバイスから確認を受信した後に「配信済み」になります。
- アプリ内メッセージ：定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。
- WhatsApp:定義されたトリガーアクションに基づいて表示したときに「受信済み」になります。

{% endapi %}

{% api %}

### 拒否数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rejections' %} ブレーズの顧客として、拒否はSMS割り当てに対して課金されます。

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

{% multi_lang_include metrics.md metric='Sends' %} このメトリクスはBraze によって提供されます。スケジュールされた キャンペーンを起動すると、このメトリクスには、レート制限のためにまだ送信されたかどうかに関係なく、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、このメトリクスは、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) で選択した内容に応じて異なる方法で計算されます。

- **起動時またはステップ入力時:**作成され、表示可能なカードの数。ユーザーがカードを見たかどうかはカウントされない。
- **最初のインプレッション発生時:**ユーザーに表示されるカードの数。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
コンテンツカード、メール、アプリ内メッセージ、Webプッシュ、iOSプッシュ、Androidプッシュ、Webhook、SMS、WhatsApp、LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %} このメトリクスはBraze によって提供されます。スケジュールされた キャンペーンを起動すると、このメトリクスには、レート制限のためにまだ送信されたかどうかに関係なく、送信されたすべてのメッセージが含まれることに注意してください。

{% alert tip %}
コンテンツカードの場合、このメトリクスは、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) で選択した内容に応じて異なる方法で計算されます。

- **起動時またはステップ入力時:**作成され、表示可能なカードの数。ユーザーがカードを見たかどうかはカウントされない。
- **最初のインプレッション発生時:**ユーザーに表示されるカードの数。
{% endalert %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### キャリアへの送信数

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='キャリアに送信' %} 

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### ソフトバウンス

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} メールがソフトバウンスを受信した場合、通常は72 時間以内に再試行されますが、再試行回数は受信者によって異なります。

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
        <li><i>Spam %</i>または<i>Spam Rate %</i>:(スパムとしてマーク)/(送信)</li>
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

{% multi_lang_include metrics.md metric='Survey サブミッション' %}

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

{% multi_lang_include metrics.md metric='合計解雇数' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### インプレッション数の合計

{% apitags %}
アプリ内メッセージ、コンテンツカード
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Impressions' %} この数値は、Braze がSDK から受け取る印象イベントの数の合計です。コンテンツカードの場合、これは、特定のコンテンツカードについて記録されたインプレッションの合計数です。これは、同じユーザに対して複数回インクリメントできます。

アプリ内メッセージの場合、複数のデバイスがあり、再適格性がオフの場合、ユーザはアプリ内メッセージのみを1 回表示する必要があります。ユーザーが複数のデバイスを使用している場合でも、ターゲットとなる最初のデバイスでのみ表示されます。これは、プロファイルに統合されたデバイスがあり、ユーザーにはデバイス間でログインするユーザーID が1 つあることを前提としています。再適格性がオンの場合、ユーザーがアプリ内メッセージを表示するたびに印象が記録されます。

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

{% multi_lang_include metrics.md metric='Unique Clicks' %} これは、メールの7 日間にわたって追跡されます。これには、Brazeが提供する配信停止リンクのクリックも含まれる。LINE の場合、1 日 20 通の最小しきい値に達した後、これが追跡されます。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>固有クリック数</i>:カウント</li>
        <li><b>コンテンツカード</b><i>ユニーククリック%</i>または<i>ユニーククリック率</i>:(ユニーククリック数) / (ユニークインプレッション数)</li>
        <li><b>メール</b><i>一意のクリック%</i>または<i>一意のクリック率</i>:(ユニーククリック数) / (配信数)</li>
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

{% multi_lang_include metrics.md metric='Unique Impressions' %} アプリ内メッセージの場合、再適格がオンでユーザーがトリガーアクションを実行すると、24時間後に一意の印象を再び増やすことができます。再適格性がオンの場合、<i>固有印象</i>=<i>固有受信者</i>。<br><br>コンテンツカードの場合、ユーザがカードを表示する2 回目のカウントを増やすべきではありません。 

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### ユニーク開封数

{% apitags %}
メール, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} メールの場合、これは7 日間で追跡されます。LINE の場合、1 日 20 通の最小しきい値に達した後、これが追跡されます。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>Unique Opens</i>:カウント</li>
        <li><i>Unique %</i>または<i>Unique Open Rate</i>:(ユニーク開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
すべて
{% endapitags %}

{% multi_lang_include metrics.md metric='一意の受信者' %}

ビューアは毎日一意の受信者になる可能性があるため、これは<i>一意の印象</i>よりも高いことが期待されます。この番号は、Braze から受信され、`user_id` に基づいています。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信停止数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers またはUnsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><i>Unsubscribers</i>または<i>Unsub</i>:カウント</li>
        <li><i>Unsubscribers %</i>または<i>Unsub Rate</i>:(契約解除)/(配信)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 配信停止数

{% apitags %}
メール
{% endapitags %}

{% multi_lang_include metrics.md metric='サブスクライブ解除' %}

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