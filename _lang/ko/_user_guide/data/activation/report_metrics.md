---
nav_title: 보고서 메트릭 용어집
article_title: 보고서 메트릭 용어집
layout: report_metrics
page_order: 0.5
excerpt_separator: ""
page_type: glossary
description: "이 용어집은 Braze 계정의 보고서에서 찾을 수 있는 용어를 정의합니다."
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### AMP 클릭 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### AMP 열기

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### 청중

{% apitags %}
모두
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">계산: (변형의 수신자 수) / (고유 수신자 수)</span>

{% endapi %}

{% api %}

### 반송

{% apitags %}
이메일, 웹 푸시, iOS 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 이는 유효한 푸시 토큰이 없거나, 캠페인이 시작된 후 사용자가 구독을 취소했거나, 이메일 주소가 부정확하거나 비활성화된 경우 발생할 수 있습니다.

|채널|추가 정보|
|-------|-----------------------|
|이메일|SendGrid를 사용하는 고객의 이메일 반송은 하드 반송, 스팸 (`spam_report_drops`) 및 잘못된 주소로 전송된 이메일 (`invalid_emails`)로 구성됩니다.<br><br>이메일의 경우, *Bounce %* 또는 *Bounce Rate*는 전송 서비스에서 성공적으로 전송되지 않았거나 "반송됨" 또는 "수신되지 않음"으로 지정된 메시지의 비율입니다.|
|푸시|이 사용자들은 모든 향후 푸시 알림에서 자동으로 구독 해지되었습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>Bounces</i>: 수량</li>
        <li><i>Bounce %</i> 또는 <i>Bounce Rate %</i>: (Bounce) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 본문 클릭

{% apitags %}
iOS 푸시, 안드로이드 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">계산: (본문 클릭) / (노출)</span>

{% endapi %}

{% api %}

### 본문 클릭 수

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) 및 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100)의 SDK 변경 로그를 참조하십시오.

<span class="calculation-line">계산: (본문 클릭) / (노출)</span>

{% endapi %}

{% api %}

### 버튼 1 클릭 수

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} _버튼 1 클릭 수_에 대한 보고는 앱 내 메시지에서 **보고를 위한 식별자**를 "0"으로 지정할 때만 작동합니다.

<span class="calculation-line">계산: (버튼 1 클릭 수) / (노출)</span>

{% endapi %}

{% api %}

### 버튼 2 클릭 수

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} _버튼 2 클릭 수_에 대한 보고는 앱 내 메시지에서 **보고를 위한 식별자**를 "1"로 지정할 때만 작동합니다.

<span class="calculation-line">계산: (버튼 2 클릭 수) / (노출)</span>

{% endapi %}

{% api %}

### 캠페인 분석

{% apitags %}
기능 플래그
{% endapitags %}

메시지의 성능이 다양한 채널에서 나타납니다. 표시된 메트릭은 선택한 메시징 채널과 [기능 플래그 실험]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics)이 다변량 테스트인지 여부에 따라 달라집니다.

{% endapi %}

{% api %}

### 제출된 선택사항

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### 클릭-오픈 비율

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">계산: (고유 클릭 수) / (고유 오픈 수) (이메일)</span>

{% endapi %}

{% api %}

### RCS 확인된 배달 또는 SMS 확인된 배달

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Braze 고객으로서, 배달은 귀하의 SMS 할당량에 청구됩니다. 

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>확인된 배달</i>: 수량</li>
        <li><i>확인된 배달 비율</i>: (확인된 배달) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 신뢰도

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 확인 페이지 버튼

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### 확인 페이지 해제

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### 전환 (B, C, D)

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} 이 정의된 이벤트는 캠페인을 구축할 때 귀하에 의해 결정됩니다. 

|채널|추가 정보|
|-------|-----------------------|
|이메일, 푸시, 웹훅|전환은 초기 전송 후 추적됩니다.|
|콘텐츠 카드|사용자가 콘텐츠 카드를 처음 볼 때 전환이 계산됩니다.|
|앱 내 메시지|사용자가 앱 내 메시지 캠페인을 수신하고 보고, 정의된 전환 기간 내에 특정 전환 이벤트를 수행하면 전환이 계산됩니다. 메시지를 클릭했는지 여부는 관계없습니다.<br><br>전환은 가장 최근에 수신한 메시지에 귀속됩니다. 재자격이 활성화된 경우, 전환은 정의된 전환 기간 내에 수신한 최신 앱 내 메시지에 할당됩니다. 그러나 앱 내 메시지에 이미 전환이 할당된 경우, 해당 특정 메시지에 대해 새로운 전환을 기록할 수 없습니다. 이는 각 앱 내 메시지 전달이 오직 하나의 전환과만 연관되어 있음을 의미합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### 총 전환

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

사용자가 앱 내 메시지 캠페인을 한 번만 볼 때, 전환 이벤트를 나중에 여러 번 수행하더라도 오직 하나의 전환만 계산됩니다. 그러나 재자격이 활성화되고 사용자가 앱 내 메시지 캠페인을 여러 번 보는 경우, *총 전환*은 사용자가 앱 내 메시지 캠페인의 새로운 인스턴스에 대한 노출을 기록할 때마다 한 번씩 증가할 수 있습니다. 

예를 들어, 사용자가 앱 내 메시지를 두 번 트리거하고 각 앱 내 메시지 노출 후에 전환을 수행하면(결과적으로 두 개의 전환이 발생함), *총 전환*은 두 번 증가합니다. 그러나 앱 내 메시지 노출이 하나만 있었고 그 뒤에 두 개의 전환 이벤트가 발생한 경우, 오직 하나의 전환만 기록되며, *총 전환*은 한 번 증가합니다.

{% endapi %}

{% api %}

### 메시지 닫기

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### 전환율

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|채널|추가 정보|
|-------|-----------------------|
|앱 내 메시지|총 일일 <i>고유 노출</i> 지표는 앱 내 메시지의 <i>전환율</i>을 계산하는 데 사용됩니다.<br><br>앱 내 메시지의 노출은 하루에 한 번만 계산될 수 있습니다. 반면, 사용자가 원하는 행동("전환")을 완료하는 횟수는 24시간 이내에 증가할 수 있습니다. 전환은 하루에 여러 번 발생할 수 있지만, 노출은 그렇지 않습니다. 따라서 사용자가 하루에 여러 번 전환을 완료하면 <i>전환율</i>이 그에 따라 증가할 수 있지만, 노출은 한 번만 계산됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>앱 내 메시지</b>: (주요 전환) / (고유 노출 수)</li>
        <li><b>기타 채널</b>: (주요 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 전환 창

{% apitags %}
모두
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### 전송 수

{% apitags %}
이메일, 웹 푸시, iOS 푸시, 안드로이드 푸시, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|채널|추가 정보|
|-------|-----------------------|
|이메일|이메일 수신 가능 당사자에게 성공적으로 전송되고 수신된 메시지(전송)의 총 수를 나타냅니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>전송 수</i>: 수량</li>
        <li><i>전송 수 %</i>: (전송 - 반송) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### RCS 전송 실패 또는 SMS 전송 실패

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

전송 실패의 이유를 이해하는 데 도움을 받으려면 <a href="/docs/braze_support/">브레이즈 지원</a>에 문의하십시오.

<span class="calculation-line">계산: (전송) - (운영자에게 전송된 전송)</span>

{% endapi %}

{% api %}

### 전송 실패

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

전송 실패의 이유를 이해하는 데 도움을 받으려면 <a href="/docs/braze_support/">브레이즈 지원</a>에 문의하십시오.

<span class="calculation-line">계산: (전송) - (운영자에게 전송된 전송)</span>

{% endapi %}

{% api %}

### 실패한 전송 비율

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

전송 실패의 이유를 이해하는 데 도움을 받으려면 <a href="/docs/braze_support/">브레이즈 지원</a>에 문의하십시오.

<span class="calculation-line">계산: (전송 실패) / (전송)</span>

{% endapi %}

{% api %}

### 직접 열기

{% apitags %}
iOS 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">계산: (직접 열기) / (전송)</span>

{% endapi %}

{% api %}

### 이메일 가능

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">계산: 수</span>

{% endapi %}

{% api %}

### 오류

{% apitags %}
웹훅
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} 오류는 <i>Sends</i> 수에 포함되지만 <i>고유 수신자</i> 수에는 포함되지 않습니다.

{% endapi %}

{% api %}

### 추정 실제 열기

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### 실패

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} 실패는 <i>Sends</i> 수에 포함되지만 <i>전송</i> 수에는 포함되지 않습니다.</td>

<span class="calculation-line">계산 (<i>실패율</i>): (실패) / (전송)</span>

{% endapi %}

{% api %}

### 기능 플래그 실험 성과

{% apitags %}
기능 플래그
{% endapitags %}

기능 플래그 실험에서 메시지에 대한 성과 지표. 표시된 특정 지표는 메시징 채널 및 실험이 다변량 테스트인지 여부에 따라 달라집니다.

{% endapi %}

{% api %}

### 하드 바운스

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

이 경우 Braze는 이메일 주소를 유효하지 않은 것으로 표시하지만 사용자의 [구독 상태]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)는 업데이트하지 않습니다. 이메일이 하드 바운스를 받으면 이 이메일 주소에 대한 모든 향후 요청을 중지합니다.

{% endapi %}

{% api %}

### 도움

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} 사용자가 귀하의 메시지를 받은 후 4시간 이내에 수신 메시지를 보낼 때마다 사용자 응답이 측정됩니다.

{% endapi %}

{% api %}

### 영향을 받은 열기

{% apitags %}
iOS 푸시, 안드로이드 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">계산: (영향을 받은 열기) / (전송)</span>

{% endapi %}

{% api %}

### 평생 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### 사용자당 평생 가치

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### 평균 일일 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### 일일 구매

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### 사용자당 일일 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### 기계 열기

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} 이 지표는 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다. Amazon SES의 경우 분석은 _열기_로 표시됩니다. 그러나 클릭에 대한 봇 필터링이 지원됩니다.

{% endapi %}

{% api %}

### 열기

{% apitags %}
웹 푸시, iOS 푸시, 안드로이드 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### 옵트아웃

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} 사용자가 귀하의 메시지를 받은 후 4시간 이내에 수신 메시지를 보낼 때마다 사용자 응답이 측정됩니다.

{% endapi %}

{% api %}

### 기타 열기

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} 사용자가 기계 열기 수가 기록되기 전에 이메일을 열 수 있다는 점에 유의하십시오(예: 열기 수는 기타 열기로 계산됨). 사용자가 비 애플 메일 수신함에서 기계 열기 이벤트 후에 이메일을 한 번(또는 그 이상) 열면, 사용자가 이메일을 여는 횟수는 기타 열기로 계산되며 고유 열기로는 한 번만 계산됩니다.

{% endapi %}

{% api %}

### 대기 중 재시도

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### 주요 전환 (A) 또는 주요 전환 이벤트

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|채널|추가 정보|
|-------------|----------------------|
|이메일, 푸시, 웹훅|초기 전송 후.|
|콘텐츠 카드, 앱 내 메시지|사용자가 콘텐츠 카드 또는 메시지를 처음 볼 때.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>주요 전환 (A) 또는 주요 전환 이벤트</i>: 수량</li>
        <li><i>주요 전환 (A) %</i> 또는 <i>주요 전환 이벤트 비율</i>: (주요 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 읽기

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### 읽기 비율

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">계산: (읽기 영수증이 있는 읽기) / (전송)</span>

{% endapi %}

{% api %}

### 수신됨

{% apitags %}
이메일, 콘텐츠 카드, 앱 내 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|채널|추가 정보|
|-------|-------|
|콘텐츠 카드|사용자가 앱에서 카드를 볼 때 수신됨.|
|푸시|메시지가 Braze 서버에서 푸시 제공업체로 전송될 때 수신됨.|
|이메일|메시지가 Braze 서버에서 이메일 서비스 제공업체로 전송될 때 수신됨.|
|SMS/MMS|“전송됨”은 SMS 제공업체가 상위 통신사 및 목적지 장치로부터 확인을 받을 때입니다.|
|앱 내 메시지|정의된 트리거 작업에 따라 표시 시점에 수신됨.|
|WhatsApp|정의된 트리거 작업에 따라 표시 시점에 수신됨.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### RCS 거부 또는 SMS 거부

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Braze 고객으로서, 거부는 귀하의 SMS 할당량에 포함됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>거부</i>: 수량</li>
        <li><i>거부율</i>: (거부) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 수익

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### 보내기

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">계산: 수량</span>

{% endapi %}

{% api %}

### 보내기

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} 이 지표는 Braze에서 제공됩니다. 예약된 캠페인을 시작할 때, 이 지표는 전송된 모든 메시지를 포함하며, 비율 제한으로 인해 아직 전송되지 않은 메시지도 포함됩니다.

{% alert tip %}
콘텐츠 카드의 경우, 이 지표는 [카드 생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)에 대해 선택한 내용에 따라 다르게 계산됩니다:

- **출시 또는 단계 진입 시:** 생성된 카드 수와 볼 수 있는 카드 수입니다. 사용자가 카드를 보았는지 여부는 포함되지 않습니다.
- **첫 인상 시:** 사용자에게 표시된 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 수량</span>

{% endapi %}

{% api %}

### 전송된 메시지

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} 이 지표는 Braze에서 제공됩니다. 예약된 캠페인을 시작할 때, 이 지표는 전송된 모든 메시지를 포함하며, 비율 제한으로 인해 아직 전송되지 않은 메시지도 포함됩니다.

{% alert tip %}
콘텐츠 카드의 경우, 이 지표는 [카드 생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)에 대해 선택한 내용에 따라 다르게 계산됩니다:

- **출시 또는 단계 진입 시:** 생성된 카드 수와 볼 수 있는 카드 수입니다. 사용자가 카드를 보았는지 여부는 포함되지 않습니다.
- **첫 인상 시:** 사용자에게 표시된 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 수량</span>

{% endapi %}

{% api %}

### 운송사에 전송

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>운송업체로 전송</i>: 수량</li>
        <li><i>운송업체 요금</i>: (운송업체로 전송) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 소프트 바운스

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} _소프트 바운스_는 _연기_와 다릅니다. 이 재시도 기간 동안 이메일이 성공적으로 배달되지 않으면, Braze는 시도된 캠페인 전송당 하나의 소프트 바운스 이벤트를 보냅니다. 2025년 2월 25일 이전에는 이러한 재시도가 1회 캠페인 전송에 대해 여러 소프트 바운스로 계산되었습니다.

소프트 바운스는 캠페인 분석에서 추적되지 않지만, [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에서 소프트 바운스를 모니터링할 수 있습니다. 이 사용자들을 전송에서 제외하거나, [소프트 바운스 세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)를 사용하여 지난 30일 동안의 소프트 바운스 수를 확인할 수 있습니다. 메시지 활동 로그에서 소프트 바운스의 이유를 확인하고 이메일 캠페인에서 '전송'과 '배달' 간의 가능한 불일치를 이해할 수 있습니다.

{% endapi %}

{% api %}

### 스팸

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
스팸 불만은 이메일 서비스 제공업체에 의해 직접 처리되며, 이후 피드백 루프를 통해 Braze에 전달됩니다. 대부분의 피드백 루프는 실제 불만의 일부만 보고하므로, _스팸_ 지표는 종종 실제 총량의 일부를 나타냅니다. 오직 이메일 서비스 제공업체만이 스팸 불만의 실제 양을 볼 수 있으므로, _스팸_은 지표로서 참고용으로만 보아야 합니다.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>스팸</i>: 수량</li>
        <li><i>스팸 %</i> 또는 <i>스팸 비율 %</i>: (스팸으로 표시됨) / (전송됨)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 설문조사 페이지 해제

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### 설문조사 제출

{% apitags %}
앱 내 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### 총 클릭 수

{% apitags %}
이메일, 콘텐츠 카드, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|채널|추가 정보|
|-------|-------|
|LINE|하루 최소 20개의 메시지가 도달한 후 추적됩니다. AMP 이메일은 HTML 및 일반 텍스트 버전 모두에서 기록된 클릭을 포함합니다. 이 숫자는 스팸 방지 도구에 의해 인위적으로 부풀려질 수 있습니다.|
|배너|전달된 메시지 내에서 클릭한 사용자 수(및 비율)의 총 수로, 동일한 사용자가 여러 번 클릭하더라도 상관없습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (총 클릭 수) / (전달 수)</li>
        <li><b>콘텐츠 카드:</b> (총 클릭 수) / (총 노출 수)</li>
        <li><b>SMS:</b> (클릭 오픈) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 해제 수

{% apitags %}
콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} 사용자가 동일한 캠페인에서 두 개의 서로 다른 카드를 받고 둘 다 해제하면, 이 수치는 두 개 증가합니다. 재자격 부여는 사용자가 카드를 받을 때마다 _총 해제 수_를 한 번 증가시킬 수 있게 해줍니다. 각 카드는 다른 메시지입니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>총 해제 수:</i> 수량</li>
        <li><i>총 해제 비율:</i> 총 해제 수 / 총 노출 수</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 노출 수

{% apitags %}
앱 내 메시지, 콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 이 숫자는 Braze가 SDK로부터 받는 노출 이벤트 수의 합계입니다.

|채널|추가 정보|
|-------|-----------------------|
|콘텐츠 카드|주어진 콘텐츠 카드에 대해 기록된 총 노출 수입니다. 이것은 동일한 사용자에 대해 여러 번 증가할 수 있습니다.|
|앱 내 메시지|여러 장치가 있고 재자격 부여가 꺼져 있으면, 사용자는 앱 내 메시지를 한 번만 봐야 합니다. 사용자가 여러 장치를 사용하더라도, 타겟팅된 첫 번째 장치에서만 볼 수 있습니다. 이것은 프로필이 장치를 통합하고 사용자가 장치 간에 로그인한 하나의 사용자 ID를 가지고 있다고 가정합니다. 재자격 부여가 켜져 있으면, 사용자가 앱 내 메시지를 볼 때마다 노출이 기록됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">계산: 수량</span>

{% endapi %}

{% api %}

### 총 열림 수

{% apitags %}
이메일, iOS 푸시, 안드로이드 푸시, 웹 푸시, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|채널|추가 정보|
|-------|-----------------------|
|LINE|하루 최소 20개의 메시지가 도달한 후 추적됩니다.|
|AMP 이메일|HTML 및 일반 텍스트 버전의 총 열기 수입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일 <i>총 열기 수</i>:</b> 수량</li>
        <li><b>이메일 <i>총 열기 비율</i>:</b> (열기 수) / (전송 수)</li>
        <li><b>웹 푸시 <i>총 열기 수</i>:</b> <i>직접 열기 수</i> 카운트</li>
        <li><b>웹 푸시 <i>총 열기 비율</i>:</b> (총 열기 수) / (전송 수)</li>
        <li><b>iOS, Android 및 Kindle 푸시 <i>총 열기 수</i>:</b> (직접 열기 수) + (영향을 받은 열기 수)</li>
        <li><b>iOS, Android 및 Kindle 푸시 <i>총 열기 비율</i>:</b> (총 열기 수) / (전송 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} 이 지표는 <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>보고서 작성기</a>를 통해 캠페인 비교 보고서에서만 사용할 수 있습니다.

{% endapi %}

{% api %}

### 고유 클릭 수

{% apitags %}
이메일, 콘텐츠 카드, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

이것은 Braze 제공 구독 취소 링크에 대한 클릭을 포함합니다.

|채널|추가 정보|
|-------|-----------------------|
|이메일|7일 동안 추적되었습니다.|
|LINE|하루 최소 20개의 메시지가 도달한 후 추적됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 클릭 수</i>: 수량</li>
        <li><b>콘텐츠 카드</b> <i>고유 클릭 수 %</i> 또는 <i>고유 클릭 비율</i>: (고유 클릭) / (고유 노출)</li>
        <li><b>Email</b> <i>고유 클릭 %</i> 또는 <i>고유 클릭 비율</i>: (고유 클릭) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 해제

{% apitags %}
콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">계산: (고유 해제) / (고유 노출)</span>

{% endapi %}

{% api %}

### 고유 노출

{% apitags %}
앱 내 메시지, 콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|채널|추가 정보|
|-------|-----------------------|
|앱 내 메시지|고유 노출은 재자격이 활성화되어 있고 사용자가 트리거 작업을 수행하면 24시간 후에 다시 증가할 수 있습니다. 재자격이 활성화되어 있으면, <i>고유 노출</i> = <i>고유 수신자</i>.|
|콘텐츠 카드|사용자가 카드를 두 번째로 볼 때 카운트가 증가하지 않아야 합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">계산: 수량</span>

{% endapi %}

{% api %}

### 고유 열림

{% apitags %}
이메일, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|채널|추가 정보|
|-------|-----------------------|
|이메일|7일 동안 추적됨.|
|LINE|하루 최소 20개의 메시지가 도달한 후 추적됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 열림</i>: 수량</li>
        <li><i>고유 열림 %</i> 또는 <i>고유 열림 비율</i>: (고유 열림) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 수신자

{% apitags %}
모두
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

뷰어가 매일 고유 수신자가 될 수 있으므로, 이는 <i>고유 노출</i>보다 높을 것으로 예상해야 합니다. 콘텐츠 카드의 경우, 각 콘텐츠 카드는 한 번만 수신될 수 있으므로, 같은 콘텐츠 카드를 두 번째로 보는 것은 날짜에 관계없이 이 카운트를 증가시키지 않습니다.<br><br>이 숫자는 Braze에서 수신되며 `user_id`를 기반으로 합니다. 고유 수신자는 캠페인 또는 캔버스 단계 수준에서 계산되며, <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>전송 식별자</a> 수준에서는 계산되지 않습니다.

<span class="calculation-line">계산: 수량</span>

{% endapi %}

{% api %}

### 구독 취소자 또는 구독 취소

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>구독 취소자</i> 또는 <i>구독 취소</i>: 수량</li>
        <li><i>구독 취소자 %</i> 또는 <i>구독 취소율</i>: (구독 취소) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 구독 취소

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">계산: (구독 취소) / (전송)</span>

{% endapi %}

{% api %}

### 변형

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">계산: 수량</span>

{% endapi %}