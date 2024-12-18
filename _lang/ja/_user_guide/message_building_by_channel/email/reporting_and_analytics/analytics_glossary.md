---
nav_title: 電子メール分析用語集
article_title: 電子メール分析用語集
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "この用語集には、起動後にメール キャンペーンまたはキャンバスの分析の項に記載されている用語が含まれています。この用語集には、Currents測定基準は含まれていません。"
channel: 
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### バリエーション

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### メール可能

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### オーディエンス (%)

{% apitags %}
パーセンテージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数)/(ユニーク受信者数)</span>

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %} この数値は Braze から受信します。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %}  この指標は Braze によって提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %}  この指標は Braze によって提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} メールの場合、*Deliveries* は、メール利用可能な相手に正常に送受信されたメッセージ(送信)の総数です。

<span class="calculation-line">計算式: (送信数) - (バウンス数) </span>

{% endapi %}

{% api %}

### 配信 (%)

{% apitags %}
パーセンテージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">計算式: (送信数 - バウンス数) / (送信数) </span>

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} 

メールの場合、[*バウンス率 (%)*] または [*バウンス率*] は、使用した送信サービスが送信に失敗した、または「返送された」や「受信されなかった」が示されたメッセージ、あるいは目的のメール可能なユーザーが受信しなかったメッセージの割合です。

SendGrid を使用している顧客のメールバウンスには、ハードバウンス、スパム (`spam_report_drops`)、および無効なアドレスに送信されたメール (`invalid_emails`) があります。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>バウンス数</i>:</b>カウント</li>
        <li><b><i>バウンス%</i>または<i>バウンス率%</i>:</b>(バウンス数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ハードバウンス

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### ソフトバウンス

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} メールがソフトバウンスを受信した場合、通常は72時間以内に再試行されますが、再試行回数は受信側ごとに異なります。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}
  
### スパム

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>スパム</i>:</b>カウント</li>
        <li><b><i>スパム率</i><i> (%)</i>:</b>(スパムとしてマークされた数) / (送信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### ユニーク開封数

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %}メールの場合、これは7日間にわたって追跡されます。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>ユニーク開封数</i>:</b>カウント</li>
        <li><b><i>ユニーク開封率 (%)</i> または<i>ユニーク開封率</i>:</b>(ユニーク開封数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### ユニーククリック数

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} これは、メールの7 日間にわたって追跡され、<a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> によって測定されます。これには、Brazeが提供する配信停止リンクのクリックも含まれる。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>ユニーククリック数</i>:</b>カウント</li>
        <li><b><i>一意のクリック%</i>または<i>クリック率</i>:</b>(ユニーククリック数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### 配信停止数

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>配信</i><i>停止数</i>:</b>カウント</li>
        <li><b><i>配信</i><i>停止率 (%)</i>:</b>(配信停止数) / (配信数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 収益

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='収益' %}

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### 1 次コンバージョン (A) または 1 次コンバージョンイベント

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} メール、プッシュ、Webhook については、最初の送信後にコンバージョンのトラッキングを開始します。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>1次コンバージョン (A)</i> または <i>1次コンバージョンイベント</i>:</b>カウント</li>
        <li><b><i>1次コンバージョン (A) %</i> または<i>1次コンバージョンイベント率</i>:</b>(1次コンバージョン数) / (ユニーク受信者数)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 信頼度

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### マシン開封数
  
{% multi_lang_include metrics.md metric='Machine Opens' %} この指標の追跡は、SendGrid の場合は 2021年11月11日から、SparkPost の場合は 2021年12月2日から開始されます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### その他の開封数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} ユーザーは、<i>マシン開封数</i>が記録される前に、メールも開封できることに注意してください (<i>その他の開封数</i>にカウントされる開封数など)。あるユーザーが、マシン開封イベント後に Apple Mail 以外の受信トレイメールを 1 回 (またはそれ以上) 開封した場合、ユーザーによるメール開封数が<i>その他の開封数</i>に加算され、<i>ユニーク開封数</i>には 1 回のみが加算されます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### クリック開封率

{% apitags %}
パーセンテージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数) (メールの場合)</span>

{% endapi %}