---
nav_title: 보고서 측정기준 용어집
article_title: 보고서 측정기준 용어집
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

### AMP 열람 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### 오디언스

{% apitags %}
전체
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">계산: (배리언트의 수신자 수) / (고유 수신자 수)</span>

{% endapi %}

{% api %}

### 반송 수

{% apitags %}
이메일, 웹 푸시, iOS 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 이는 유효한 푸시 토큰이 없거나, 캠페인 시작 후 사용자가 구독을 취소했거나, 이메일 주소가 부정확하거나 비활성화된 경우 발생할 수 있습니다.

|채널|추가 정보|
|-------|-----------------------|
|이메일|SendGrid를 사용하는 고객의 이메일 반송은 하드바운스, 스팸(`spam_report_drops`) 및 잘못된 주소로 전송된 이메일(`invalid_emails`)로 구성됩니다.<br><br>이메일의 경우 *반송 %* 또는 *반송률*은 전송 서비스에서 전송에 실패하거나 '반송' 또는 '미수신'으로 지정된 메시지, 또는 이메일 수신 가능 사용자에게 수신되지 않은 메시지의 백분율입니다.|
|푸시|이러한 사용자는 향후 모든 푸시 알림에서 자동으로 수신 거부 처리되었습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>반송 수</i>: 카운트</li>
        <li><i>반송 %</i> 또는 <i>반송률 %</i>: (반송 수) / (발송 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 본문 클릭

{% apitags %}
iOS 푸시, Android 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">계산: (본문 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 본문 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) 및 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100)의 SDK 체인지로그를 참조하십시오.

<span class="calculation-line">계산: (본문 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 버튼 1 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} _버튼 1 클릭 수_에 대한 보고는 인앱 메시지에서 **보고용 식별자**를 "0"으로 지정할 때만 작동합니다.

<span class="calculation-line">계산: (버튼 1 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 버튼 2 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} _버튼 2 클릭 수_에 대한 보고는 인앱 메시지에서 **보고용 식별자**를 "1"로 지정할 때만 작동합니다.

<span class="calculation-line">계산: (버튼 2 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 캠페인 분석

{% apitags %}
기능 플래그
{% endapitags %}

다양한 채널에 걸친 메시지의 성과입니다. 표시되는 측정기준은 선택한 메시징 채널과 [기능 플래그 실험]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics)이 다변량 테스트인지 여부에 따라 달라집니다.

{% endapi %}

{% api %}

### 제출된 선택

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### 클릭 후 열람률

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">계산: (고유 클릭 수) / (고유 열람 수) (이메일용)</span>

{% endapi %}

{% api %}

### RCS 확인된 전달 또는 SMS 확인된 전달

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Braze 고객으로서, 전달은 귀하의 SMS 할당량에 포함됩니다. 

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>확인된 전달</i>: 카운트</li>
        <li><i>확인된 전달률</i>: (확인된 전달) / (발송 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 신뢰도

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 확인 페이지 버튼

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### 확인 페이지 해제

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### 전환 (B, C, D)

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} 이 정의된 이벤트는 캠페인을 구축할 때 사용자가 결정합니다. 

|채널|추가 정보|
|-------|-----------------------|
|이메일, 푸시, 웹훅|전환은 최초 발송 이후 추적됩니다.|
|콘텐츠 카드|전환은 사용자가 콘텐츠 카드를 처음 조회할 때 계산됩니다.|
|인앱 메시지|사용자가 인앱 메시지 캠페인을 수신하고 조회한 후, 메시지를 클릭했는지 여부와 관계없이 정의된 전환 기간 내에 특정 전환 이벤트를 수행하면 전환이 계산됩니다.<br><br>전환은 가장 최근에 수신한 메시지에 귀속됩니다. 재자격이 활성화된 경우, 정의된 전환 기간 내에 발생하면 가장 최근에 수신한 인앱 메시지에 전환이 할당됩니다. 그러나 인앱 메시지에 이미 전환이 할당된 경우에는 해당 특정 메시지에 대해 새 전환을 기록할 수 없습니다. 즉, 각 인앱 메시지 전달은 단 하나의 전환과만 연결됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### 총 전환 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

사용자가 인앱 메시지 캠페인을 한 번만 조회하면 나중에 전환 이벤트를 여러 번 수행하더라도 전환은 한 번만 계산됩니다. 그러나 재자격이 켜져 있고 사용자가 인앱 메시지 캠페인을 여러 번 보는 경우, 사용자가 인앱 메시지 캠페인의 새 인스턴스에 대한 노출을 기록할 때마다 *총 전환 수*가 한 번씩 증가할 수 있습니다. 

예를 들어, 사용자가 인앱 메시지를 두 번 트리거하고 각 인앱 메시지 노출 후 전환하면(결과적으로 두 번의 전환이 발생하면) *총 전환 수*가 두 개 증가합니다. 그러나 인앱 메시지 노출이 한 번만 발생한 후 전환 이벤트가 두 번 발생한 경우에는 전환이 한 번만 기록되고 *총 전환 수*가 한 개 증가합니다.

{% endapi %}

{% api %}

### 메시지 닫기

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### 전환율

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|채널|추가 정보|
|-------|-----------------------|
|인앱 메시지|일일 총 <i>고유 노출 수</i> 측정기준은 인앱 메시지의 <i>전환율</i>을 계산하는 데 사용됩니다.<br><br>인앱 메시지의 노출 수는 하루에 한 번만 계산할 수 있습니다. 반면에 사용자가 원하는 동작('전환')을 완료하는 횟수는 24시간 이내에 증가할 수 있습니다. 전환은 하루에 여러 번 발생할 수 있지만, 노출은 한 번만 계산됩니다. 따라서 사용자가 하루에 여러 번 전환을 완료하는 경우 <i>전환율</i>은 그에 따라 증가할 수 있지만 노출 횟수는 한 번만 계산됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>인앱 메시지</b>: (주요 전환) / (고유 노출 수)</li>
        <li><b>기타 채널</b>: (주요 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 전환 기간

{% apitags %}
전체
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### 전달 수

{% apitags %}
이메일, 웹 푸시, iOS 푸시, Android 푸시, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|채널|추가 정보|
|-------|-----------------------|
|이메일|이메일 수신 가능 대상에게 성공적으로 발송되고 수신된 총 메시지(발송 수) 수를 나타냅니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>전달 수</i>: 카운트</li>
        <li><i>전달률 %</i>: (발송 수 - 반송 수) / (발송 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### RCS 전달 실패 또는 SMS 전달 실패

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

전달 실패의 원인을 파악하는 데 도움이 필요하면 <a href="/docs/braze_support/">Braze 고객지원</a>에 문의하십시오.

<span class="calculation-line">계산: (발송 수) - (이동통신사로 발송 수)</span>

{% endapi %}

{% api %}

### 전달 실패 수

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

전달 실패의 원인을 파악하는 데 도움이 필요하면 <a href="/docs/braze_support/">Braze 고객지원</a>에 문의하십시오.

<span class="calculation-line">계산: (발송 수) - (이동통신사로 발송 수)</span>

{% endapi %}

{% api %}

### 전달 실패율

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

전달 실패의 원인을 파악하는 데 도움이 필요하면 <a href="/docs/braze_support/">Braze 고객지원</a>에 문의하십시오.

<span class="calculation-line">계산: (전달 실패 수) / (발송 수)</span>

{% endapi %}

{% api %}

### 직접 열람 수

{% apitags %}
iOS 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">계산: (직접 열람 수) / (전달 수)</span>

{% endapi %}

{% api %}

### 이메일 수신 가능

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 오류 수

{% apitags %}
웹훅
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} 오류는 <i>발송 수</i>에 포함되지만 <i>고유 수신자</i> 수에는 포함되지 않습니다.

{% endapi %}

{% api %}

### 추정 실제 열람 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### 실패 수

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} 실패는 <i>발송 수</i>에 포함되지만 <i>전달 수</i>에는 포함되지 않습니다.</td>

<span class="calculation-line">계산 (<i>실패율</i>): (실패 수) / (발송 수)</span>

{% endapi %}

{% api %}

### 기능 플래그 실험 성과

{% apitags %}
기능 플래그
{% endapitags %}

기능 플래그 실험에서 메시지의 성과 측정기준입니다. 표시되는 구체적인 측정기준은 메시징 채널과 실험이 다변량 테스트인지 여부에 따라 달라집니다.

{% endapi %}

{% api %}

### 하드바운스

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

이 경우 Braze는 이메일 주소를 유효하지 않은 것으로 표시하지만 사용자의 [구독 상태]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)는 업데이트하지 않습니다. 이메일이 하드바운스되면 해당 이메일 주소에 대한 향후 요청이 중지됩니다.

{% endapi %}

{% api %}

### 도움말

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} 사용자의 답장은 메시지를 수신한 후 4시간 이내에 인바운드 메시지를 보낼 때 측정됩니다.

{% endapi %}

{% api %}

### 영향받은 열람 수

{% apitags %}
iOS 푸시, Android 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">계산: (영향받은 열람 수) / (전달 수)</span>

{% endapi %}

{% api %}

### 생애주기 매출

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### 사용자별 생애주기 가치

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### 일일 평균 매출

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### 일일 구매 수

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### 사용자당 일일 매출

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### 기계 열람

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} 이 측정기준은 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다. Amazon SES의 경우 분석은 _열람 수_로 표시됩니다. 그러나 클릭에 대한 봇 필터링은 지원됩니다.

{% endapi %}

{% api %}

### 열람 수

{% apitags %}
웹 푸시, iOS 푸시, Android 푸시
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### 옵트아웃

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} 사용자의 답장은 메시지를 수신한 후 4시간 이내에 인바운드 메시지를 보낼 때 측정됩니다.

{% endapi %}

{% api %}

### 기타 열람 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} 사용자가 기계 열람 수가 기록되기 전에 이메일을 열 수도 있습니다(예: 기타 열람 수에 포함되는 열람). 사용자가 Apple Mail이 아닌 받은편지함에서 기계 열람 이벤트가 발생한 후 이메일을 한 번 이상 여는 경우, 사용자가 이메일을 여는 횟수는 기타 열람 수로 계산되고 고유 열람 수에 대해서는 한 번만 계산됩니다.

{% endapi %}

{% api %}

### 보류 중 재시도

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### 주요 전환(A) 또는 주요 전환 이벤트

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|채널|추가 정보|
|-------------|----------------------|
|이메일, 푸시, 웹훅|최초 발송 이후.|
|콘텐츠 카드, 인앱 메시지|사용자가 콘텐츠 카드 또는 메시지를 처음 조회할 때.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>주요 전환(A) 또는 주요 전환 이벤트</i>: 카운트</li>
        <li><i>주요 전환(A) %</i> 또는 <i>주요 전환 이벤트율</i>: (주요 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 읽기 수

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### 읽기율

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">계산: (읽음 확인이 있는 읽기 수) / (발송 수)</span>

{% endapi %}

{% api %}

### 수신

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|채널|추가 정보|
|-------|-------|
|콘텐츠 카드|사용자가 앱에서 카드를 볼 때 수신됩니다.|
|푸시|Braze 서버에서 푸시 제공자에게 메시지가 전송될 때 수신됩니다.|
|이메일|Braze 서버에서 이메일 서비스 제공업체로 메시지가 전송될 때 수신됩니다.|
|SMS/MMS|SMS 제공업체가 업스트림 이동통신사 및 대상 기기로부터 확인을 받은 후 "전달됨".|
|인앱 메시지|정의된 트리거 동작에 따라 표시 시점에 수신됩니다.|
|WhatsApp|정의된 트리거 동작에 따라 표시 시점에 수신됩니다.|
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
        <li><i>거부 수</i>: 카운트</li>
        <li><i>거부율</i>: (거부 수) / (발송 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 매출

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### 발송됨

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송 수

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} 이 측정기준은 Braze에서 제공합니다. 예약된 캠페인을 시작하면 이 측정기준에는 사용량 제한으로 인해 아직 발송되지 않은 메시지를 포함하여 발송된 모든 메시지가 포함됩니다.

{% alert tip %}
콘텐츠 카드의 경우 이 측정기준은 [카드 생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)에서 선택한 항목에 따라 다르게 계산됩니다:

- **시작 또는 단계 진입 시:** 생성되어 볼 수 있는 카드의 수입니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.
- **첫 노출 시:** 사용자에게 표시된 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송된 메시지

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} 이 측정기준은 Braze에서 제공합니다. 예약된 캠페인을 시작하면 이 측정기준에는 사용량 제한으로 인해 아직 발송되지 않은 메시지를 포함하여 발송된 모든 메시지가 포함됩니다.

{% alert tip %}
콘텐츠 카드의 경우 이 측정기준은 [카드 생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)에서 선택한 항목에 따라 다르게 계산됩니다:

- **시작 또는 단계 진입 시:** 생성되어 볼 수 있는 카드의 수입니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.
- **첫 노출 시:** 사용자에게 표시된 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 이동통신사로 발송

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>이동통신사로 발송</i>: 카운트</li>
        <li><i>이동통신사로 발송률</i>: (이동통신사로 발송) / (발송 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 소프트바운스

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} _소프트바운스_는 _연기_와 다릅니다. 이 재시도 기간 동안 성공적으로 전달된 이메일이 없으면, Braze는 시도된 캠페인 발송당 하나의 소프트바운스 이벤트를 전송합니다. 2025년 2월 25일 이전에는 이러한 재시도가 1개의 캠페인 발송에 대해 여러 번의 소프트바운스로 계산되었습니다.

소프트바운스는 캠페인 분석에서 추적되지 않지만, [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에서 소프트바운스를 모니터링할 수 있습니다. 또한 [소프트바운스 세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)를 사용하여 이러한 사용자를 발송에서 제외하거나 지난 30일 동안의 소프트바운스 수를 확인할 수도 있습니다. 메시지 활동 로그에서 소프트바운스의 원인을 확인하고 이메일 캠페인의 '발송 수'와 '전달 수' 간의 불일치를 파악할 수도 있습니다.

{% endapi %}

{% api %}

### 스팸

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
스팸 불만은 이메일 서비스 제공업체에서 직접 처리한 후 피드백 루프를 통해 Braze에 전달됩니다. 대부분의 피드백 루프는 실제 불만의 일부만 보고하므로 _스팸_ 측정기준은 실제 총계의 일부만 나타내는 경우가 많습니다. 이메일 서비스 제공업체만이 스팸 불만의 실제 규모를 확인할 수 있으므로, _스팸_은 포괄적인 측정기준이 아닌 참고용 측정기준으로 보아야 합니다.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>스팸:</i> 카운트</li>
        <li><i>스팸 %</i> 또는 <i>스팸 비율 %</i>: (스팸으로 표시) / (발송 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 설문조사 페이지 해제

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### 설문조사 제출

{% apitags %}
인앱 메시지
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
|LINE|하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다. AMP 이메일에는 HTML 및 일반 텍스트 버전 모두에서 기록된 클릭이 포함됩니다. 이 수치는 스팸 방지 도구에 의해 인위적으로 부풀려질 수 있습니다.|
|배너|동일한 사용자가 여러 번 클릭했는지 여부와 관계없이 전달된 메시지 내에서 클릭한 총 사용자 수(및 백분율)입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (총 클릭 수) / (전달 수)</li>
        <li><b>콘텐츠 카드:</b> (총 클릭 수) / (총 노출 수)</li>
        <li><b>SMS:</b> (클릭 열람 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 무시 수

{% apitags %}
콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} 사용자가 동일한 캠페인에서 두 개의 다른 카드를 받고 둘 다 무시하면, 이 수치는 두 개 증가합니다. 재자격을 사용하면 사용자가 카드를 받을 때마다 _총 무시 수_를 한 번씩 증가시킬 수 있습니다. 각 카드는 별도의 메시지입니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>총 무시 수:</i> 카운트</li>
        <li><i>총 무시율:</i> 총 무시 수 / 총 노출 수</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 노출 수

{% apitags %}
인앱 메시지, 콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 이 숫자는 Braze가 SDK로부터 수신하는 노출 이벤트 수의 합계입니다.

|채널|추가 정보|
|-------|-----------------------|
|콘텐츠 카드|특정 콘텐츠 카드에 대해 기록된 총 노출 수입니다. 동일한 사용자에 대해 여러 번 증가할 수 있습니다.|
|인앱 메시지|여러 기기가 있고 재자격이 꺼져 있는 경우, 사용자는 인앱 메시지를 한 번만 볼 수 있습니다. 사용자가 여러 기기를 사용하더라도 타겟팅된 첫 번째 기기에서만 볼 수 있습니다. 여기서는 프로필에 통합된 기기가 있고 사용자가 여러 기기에서 로그인하는 하나의 사용자 ID를 가지고 있다고 가정합니다. 재자격이 켜져 있으면 사용자가 인앱 메시지를 볼 때마다 노출이 기록됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 총 열람 수

{% apitags %}
이메일, iOS 푸시, Android 푸시, 웹 푸시, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|채널|추가 정보|
|-------|-----------------------|
|LINE|하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다.|
|AMP 이메일|HTML 및 일반 텍스트 버전의 총 열람 수입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일 <i>총 열람 수</i>:</b> 카운트</li>
        <li><b>이메일 <i>총 열람률</i>:</b> (열람 수) / (전달 수)</li>
        <li><b>웹 푸시 <i>총 열람 수</i>:</b> <i>직접 열람 수</i> 카운트</li>
        <li><b>웹 푸시 <i>총 열람률</i>:</b> (총 열람 수) / (전달 수)</li>
        <li><b>iOS, Android 및 Kindle 푸시 <i>총 열람 수</i>:</b> (직접 열람 수) + (영향받은 열람 수)</li>
        <li><b>iOS, Android 및 Kindle 푸시 <i>총 열람률</i>:</b> (총 열람 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 매출

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} 이 측정기준은 <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>보고서 빌더</a>를 통한 캠페인 비교 보고서에서만 사용할 수 있습니다.

{% endapi %}

{% api %}

### 고유 클릭 수

{% apitags %}
이메일, 콘텐츠 카드, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

여기에는 Braze에서 제공하는 구독 취소 링크 클릭이 포함됩니다.

|채널|추가 정보|
|-------|-----------------------|
|이메일|7일 동안 추적됩니다.|
|LINE|하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 클릭 수</i>: 카운트</li>
        <li><b>콘텐츠 카드</b> <i>고유 클릭 수 %</i> 또는 <i>고유 클릭률</i>: (고유 클릭 수) / (고유 노출 수)</li>
        <li><b>이메일</b> <i>고유 클릭 수 %</i> 또는 <i>고유 클릭률</i>: (고유 클릭 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 무시 수

{% apitags %}
콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">계산: (고유 무시 수) / (고유 노출 수)</span>

{% endapi %}

{% api %}

### 고유 노출 수

{% apitags %}
인앱 메시지, 콘텐츠 카드
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|채널|추가 정보|
|-------|-----------------------|
|인앱 메시지|재자격이 켜져 있고 사용자가 트리거 동작을 수행하면 24시간 후에 고유 노출 수가 다시 증가할 수 있습니다. 재자격이 켜져 있으면 <i>고유 노출 수</i> = <i>고유 수신자</i>입니다.|
|콘텐츠 카드|사용자가 카드를 두 번째로 조회할 때 카운트가 증가하지 않아야 합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 고유 열람 수

{% apitags %}
이메일, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|채널|추가 정보|
|-------|-----------------------|
|이메일|7일 동안 추적됩니다.|
|LINE|하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 열람 수</i>: 카운트</li>
        <li><i>고유 열람률 %</i> 또는 <i>고유 열람률</i>: (고유 열람 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 수신자

{% apitags %}
전체
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

조회자는 매일 고유 수신자가 될 수 있으므로, <i>고유 노출 수</i>보다 더 높을 것으로 예상해야 합니다. 콘텐츠 카드의 경우 각 콘텐츠 카드는 한 번만 수신할 수 있으므로, 날짜에 관계없이 동일한 콘텐츠 카드를 두 번째로 조회해도 이 카운트가 증가하지 않습니다.<br><br>이 숫자는 Braze에서 수신되며 `user_id`를 기반으로 합니다. 고유 수신자는 캠페인 또는 캔버스 단계 수준에서 계산되며, <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>발송 식별자</a> 수준에서는 계산되지 않습니다.

<span class="calculation-line">계산: 카운트</span>

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
        <li><i>구독 취소자</i> 또는 <i>구독 취소</i>: 카운트</li>
        <li><i>구독 취소자 %</i> 또는 <i>구독 취소율</i>: (구독 취소) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 구독 취소 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">계산: (구독 취소 수) / (전달 수)</span>

{% endapi %}

{% api %}

### 변형

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}