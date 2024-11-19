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

{% multi_lang_include metrics.md metric='Eメール可能' %}

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### オーディエンス (%)

{% apitags %}
パーセンテージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">計算式: (バリアントの受信者数)/(固有の受信者数)</span>

{% endapi %}

{% api %}

### ユニーク受信者数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %} この番号は、Braze から受け取ります。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} このメトリクスはBraze によって提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 送信済みメッセージ

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %} このメトリクスはBraze によって提供されます。

<span class="calculation-line">計算式: カウント</span>

{% endapi %}

{% api %}

### 配信数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} メールの場合、*Deliveries* は、メール利用可能な相手に正常に送受信されたメッセージ(送信)の総数です。

<span class="calculation-line">計算式: (センド) - (バウンス) </span>

{% endapi %}

{% api %}

### 配信 (%)

{% apitags %}
パーセンテージ
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">計算式: (センド- バウンス) / (センド) </span>

{% endapi %}

{% api %}

### バウンス数

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='バウンス' %} 

E メールの場合、*Bounce %* または *Bounce Rate* は、送信に失敗したメッセージまたは " returned" または "not received" send services used または受信予定のユーザーが受信しなかったメッセージの割合です。

SendGrid を使用する顧客のメールバウンスは、ハードバウンス、スパム(`spam_report_drops`)、および無効なアドレスに送信されたメール(`invalid_emails`) で構成されます。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>バウンス</i>:</b>カウント</li>
        <li><b><i>バウンス%</i>または<i>バウンス率%</i>:</b>(バウンス)/(センド)</li>
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

{% multi_lang_include metrics.md metric='Soft Bounce' %} メールがソフトバウンスを受信した場合、通常は72 時間以内に再試行されますが、再試行回数は受信者によって異なります。

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
        <li><b><i>Spam %</i>または<i>Spam Rate %</i>:</b>(スパムとしてマーク)/(送信)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### ユニーク開封数

{% apitags %}
カウント、パーセント
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} メールの場合、これは7 日間で追跡されます。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>Unique Opens</i>:</b>カウント</li>
        <li><b><i>Unique %</i>または<i>Unique Open Rate</i>:</b>(ユニーク開封数) / (配信数)</li>
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
        <li><b><i>ユニーククリック</i>:</b>カウント</li>
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

{% multi_lang_include metrics.md metric='Unsubscribers またはUnsub' %}

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>Unsubscribers</i>または<i>Unsub</i>:</b>カウント</li>
        <li><b><i>Unsubscribers %</i>または<i>Unsub Rate</i>:</b>(契約解除)/(配信)</li>
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

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} メール、プッシュ、およびウェブフックの場合、最初の送信後に変換の追跡を開始します。

{::nomarkdown}
<span class="calculation-line">
    計算式: 
    <ul>
        <li><b><i>プライマリ変換(A)</i>または<i>プライマリ変換イベント</i>:</b>カウント</li>
        <li><b><i>プライマリ変換(A) %</i> または<i>プライマリ変換イベントレート</i>:</b>(一次変換)/(一意の受信者)</li>
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
  
{% multi_lang_include metrics.md metric='Machine Opens' %} このメトリクスは、SendGrid の場合は2021年11 月11 日、SparkPost の場合は2021年12 月2 日から追跡されます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### その他の開封数

{% apitags %}
カウント
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} ユーザは、<i>Machine Opens</i> カウントが記録される前に、メールを開くこともできます(<i>Other Opens</i> に対するオープンカウントなど)。あるユーザーが、マシン開封イベント後に Apple Mail 以外の受信トレイメールを 1 回 (またはそれ以上) 開封した場合、ユーザーによるメール開封数が<i>その他の開封数</i>に加算され、<i>ユニーク開封数</i>には 1 回のみが加算されます。

<span class="calculation-line">計算式: カウント </span>

{% endapi %}

{% api %}

### クリック開封率

{% apitags %}
パーセンテージ
{% endapitags %}

{% multi_lang_include metrics.md metric='クリック・トゥ・オープン率' %}

<span class="calculation-line">計算式: (ユニーククリック数) / (ユニーク開封数) (メールの場合)</span>

{% endapi %}