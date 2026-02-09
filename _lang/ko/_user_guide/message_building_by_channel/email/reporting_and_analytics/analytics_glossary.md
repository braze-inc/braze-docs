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

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 이메일 가능

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 오디언스 %

{% apitags %}
백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">계산: (변형의 수신자 수) / (고유 수신자 수)</span>

{% endapi %}

{% api %}

### 고유 수신자

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} 이 번호는 Braze에서 받은 번호입니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송 수

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  이 측정기준은 Braze에서 제공합니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### Messages Sent

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  이 측정기준은 Braze에서 제공합니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 전달 수

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} 이메일의 경우 *전달* 건수는 이메일 수신 가능 상대방이 성공적으로 주고받은 총 메시지(전송)의 수입니다.

<span class="calculation-line">계산: (전송) - (반송) </span>

{% endapi %}

{% api %}

### 전달 %

{% apitags %}
백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">계산: (전송 - 반송) / (전송) </span>

{% endapi %}

{% api %}

### 반송 수

{% apitags %}
개수, 백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

이메일의 경우 반송 *%* 또는 *반송률은* 이메일 수신 가능 사용자가 사용하거나 수신하지 않은 전송 서비스에서 전송에 실패하거나 '반송' 또는 '미수신'으로 지정된 메시지의 백분율입니다.

SendGrid를 사용하는 고객의 이메일 반송은 하드 반송, 스팸(`spam_report_drops`) 및 잘못된 주소로 전송된 이메일(`invalid_emails`)로 구성됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>바운스</i>:</b> 카운트</li>
        <li><b><i>반송률 %</i> 또는 <i>반송률 %</i>:</b> (바운스) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 하드바운스

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">계산: Count </span>

{% endapi %}

{% api %}

### 소프트바운스

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 이메일이 소프트 바운스를 받으면 일반적으로 72시간 이내에 재시도하지만 재시도 시도 횟수는 수신자마다 다릅니다. 

소프트 반송은 캠페인 분석에서 추적되지 않지만, [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에서 소프트 반송을 모니터링하거나 [소프트 반송 세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)를 사용하여 이러한 사용자를 발송에서 제외할 수 있습니다. 메시지 활동 로그에서 소프트 반송의 이유를 확인하고 이메일 캠페인의 "발송"과 "전달" 간의 가능한 불일치를 이해할 수 있습니다.

<span class="calculation-line">계산: Count </span>

{% endapi %}

{% api %}
  
### 스팸

{% apitags %}
개수, 백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>스팸:</i></b> 카운트</li>
        <li><b><i>스팸 %</i> 또는 <i>스팸 비율 %</i>:</b> (스팸으로 표시) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### 고유 열람

{% apitags %}
개수, 백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} 이메일의 경우 7일 동안 추적됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>고유 열람</i>:</b> 카운트</li>
        <li><b><i>고유 열람 %</i> 또는 <i>고유 열람율</i>:</b> (고유 열람 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 클릭 수

{% apitags %}
개수, 백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} 이는 이메일의 경우 7일 동안 추적되며 측정은 <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. This includes clicks on Braze-provided unsubscribe links.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>고유 클릭 수</i>:</b> 카운트</li>
        <li><b><i>고유 클릭 수 %</i> 또는 <i>클릭률</i>:</b> (고유 클릭 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### 구독 취소 또는 구독 취소

{% apitags %}
개수, 백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>구독자 탈퇴</i> 또는 <i>구독</i> <i>취소</i>:</b> 카운트</li>
        <li><b><i>구독 취소자 수 %</i> 또는 <i>탈퇴율입니다</i>:</b> (구독 취소) / (배송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Revenue

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">계산: Count </span>

{% endapi %}

{% api %}

### 주요 전환(A) 또는 주요 전환 이벤트

{% apitags %}
개수, 백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 이메일, 푸시, 웹훅의 경우 최초 전송 후 전환 추적을 시작합니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>주요 전환(A)</i> 또는 <i>주요 전환 이벤트</i>:</b> 카운트</li>
        <li><b><i>주요 전환(A) %</i> 또는 <i>주요 전환 이벤트율입니다</i>:</b> (기본 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 신뢰도

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 기계 열람
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} 이 측정기준은 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다.

<span class="calculation-line">계산: Count </span>

{% endapi %}

{% api %}

### 기타 열람 수

{% apitags %}
카운트
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} <i>컴퓨터 열기</i> 횟수가 기록되기 전에 사용자가 이메일(예: <i>기타 열기에</i> 대한 열기 횟수)을 열 수도 있다는 점에 유의하세요. 사용자가 Apple Mail이 아닌 받은 편지함에서 컴퓨터 열기 이벤트가 발생한 후 이메일을 한 번 이상 여는 경우, 사용자가 이메일을 여는 횟수는 <i>기타 열기</i> 횟수에 대해 계산되고 <i>고유 열기</i> 횟수에 대해서는 한 번만 계산됩니다.

<span class="calculation-line">계산: Count </span>

{% endapi %}

{% api %}

### 클릭 후 열람률

{% apitags %}
백분율
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">계산: (고유 클릭 수) / (고유 열람 수) (이메일용)</span>

{% endapi %}