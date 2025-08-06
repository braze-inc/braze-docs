---
nav_title: 이메일 애널리틱스 용어집
article_title: 이메일 애널리틱스 용어집
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 출시 후 이메일 캠페인 또는 Canvas의 분석 섹션에서 찾을 수 있는 용어가 포함되어 있습니다. 이 용어집에는 전류 메트릭이 포함되어 있지 않습니다."
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

### 변형

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 이메일 가능

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 오디언스 %

{% apitags %}
백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">계산: (배리언트의 수신자 수) / (고유 수신자 수)</span>

{% endapi %}

{% api %}

### 고유 수신자

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %} 이 숫자는 Braze에서 수신됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송 수

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %}  이 메트릭은 Braze에 의해 제공됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 메시지 발송됨

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %}  이 메트릭은 Braze에서 제공됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 전달 수

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} 이메일의 경우, *Deliveries*는 emailable 당사자에게 성공적으로 전송되고 수신된 메시지(전송)의 총 수입니다.

<span class="calculation-line">계산: (보냄) - (반송) </span>

{% endapi %}

{% api %}

### 전달 %

{% apitags %}
백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">계산: (보내기 - 반송) / (보내기) </span>

{% endapi %}

{% api %}

### 반송 수

{% apitags %}
카운트, 백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} 

이메일의 경우, *반송 %* 또는 *반송률*은 발송 서비스에서 사용되었거나 의도된 이메일 사용자에게 수신되지 않은 메시지의 비율입니다.

SendGrid를 사용하는 고객의 이메일 반송은 하드 반송, 스팸 (`spam_report_drops`), 및 잘못된 주소로 전송된 이메일 (`invalid_emails`)로 구성됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>바운스</i>:</b> 카운트</li>
        <li><b><i>반송률 %</i> or <i>반송률 %</i>:</b> (바운스) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 하드바운스

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 소프트바운스

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='소프트 바운스' %} 이메일이 소프트 바운스를 받으면, 우리는 보통 72시간 이내에 재시도를 하지만, 재시도 횟수는 수신자마다 다릅니다. 

소프트 반송은 캠페인 분석에서 추적되지 않지만, [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에서 소프트 반송을 모니터링하거나 [소프트 반송 세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)로 이러한 사용자를 발송에서 제외할 수 있습니다. 메시지 활동 로그에서 소프트 반송의 이유를 확인하고 이메일 캠페인의 '발송'과 '전달' 간의 가능한 불일치를 이해할 수 있습니다.

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}
  
### 스팸

{% apitags %}
카운트, 백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>스팸</i>:</b> 카운트</li>
        <li><b><i>스팸 %</i> 또는 <i>스팸 비율 %</i>:</b> (스팸으로 표시됨) / (보냄)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### 고유 열람

{% apitags %}
카운트, 백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} 이메일의 경우, 이는 7일 동안 추적됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>고유 오픈</i>:</b> 카운트</li>
        <li><b><i>고유 열람 %</i> 또는 <i>고유 열람 비율</i>:</b> (고유 열람 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 클릭 수

{% apitags %}
카운트, 백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} 이는 이메일에 대해 7일 동안 추적되며 <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>로 측정됩니다. 여기에는 Braze에서 제공한 탈퇴 링크를 클릭하는 것이 포함됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>고유 클릭 수</i>:</b> 카운트</li>
        <li><b><i>고유 클릭 %</i> 또는 <i>클릭률</i>:</b> (고유 클릭 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### 구독 취소 또는 구독 취소

{% apitags %}
카운트, 백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>구독 취소자</i> 또는 <i>구독 취소</i>:</b> 카운트</li>
        <li><b><i>구독 취소자 %</i> 또는 <i>구독 취소율</i>:</b> (구독 취소) / (배달)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 매출

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 주요 전환(A) 또는 주요 전환 이벤트

{% apitags %}
카운트, 백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 이메일, 푸시 및 웹훅의 경우, 초기 전송 후 전환 추적을 시작합니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>주요 전환(A)</i> 또는 <i>주요 전환 이벤트</i>:</b> 카운트</li>
        <li><b><i>주요 전환 (A) %</i> 또는 <i>주요 전환 이벤트 비율</i>:</b> (주요 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 신뢰도

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 기계 열람
  
{% multi_lang_include metrics.md metric='Machine Opens' %} 이 메트릭은 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다.

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 기타 열람 수

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} 사용자가 <i>기타 열기</i>에 대한 열기 수가 기록되기 전에 이메일을 열 수 있다는 점에 유의하십시오 (예: <i>기계 열기</i> 카운트가 기록됩니다). 사용자가 Apple Mail이 아닌 받은 편지함에서 컴퓨터 열기 이벤트가 발생한 후 이메일을 한 번 이상 여는 경우, 사용자가 이메일을 여는 횟수는 <i>기타 열기</i> 횟수에 대해 계산되고 <i>고유 열기</i> 횟수에 대해서는 한 번만 계산됩니다.

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 클릭 후 열람률

{% apitags %}
백분율
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">계산: (고유 클릭 수) / (고유 열람 수) (이메일용)</span>

{% endapi %}