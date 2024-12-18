---
nav_title: 보고서 측정기준 용어집
article_title: 보고서 측정기준 용어집
layout: report_metrics
page_order: 0
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

{% multi_lang_include metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### AMP 열람 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### 오디언스

{% apitags %}
전체
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">계산: (변형의 수신자 수) / (고유 수신자 수)</span>

{% endapi %}

{% api %}

### 반송 수

{% apitags %}
이메일, 웹 푸시, iOS 푸시
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} 유효한 푸시 토큰이 없거나, 사용자가 캠페인이 시작된 후 구독을 취소했거나, 이메일 주소가 부정확하거나 비활성화되어 있기 때문에 발생할 수 있습니다.

#### 이메일

SendGrid를 사용하는 고객의 이메일 반송은 하드 반송, 스팸(`spam_report_drops`) 및 잘못된 주소로 전송된 이메일(`invalid_emails`)로 구성됩니다.

이메일의 경우 반송 *%* 또는 *반송률은* 이메일 수신 가능 사용자가 사용하거나 수신하지 않은 전송 서비스에서 전송에 실패하거나 '반송' 또는 '미수신'으로 지정된 메시지의 백분율입니다.

#### 푸시

이러한 사용자는 향후 모든 푸시 알림에서 자동으로 수신 거부되었습니다. 

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>바운스</i>:카운트</li>
        <li><i>이탈률</i><i>%</i> 또는 <i>이탈률 %</i>: (전송 - 반송) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 본문 클릭

{% apitags %}
iOS 푸시, Android 푸시
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Click' %}

<span class="calculation-line">계산: (본문 클릭) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 본문 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Clicks' %} 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) 및 [Android용]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100) SDK 변경 로그를 참조하세요.

<span class="calculation-line">계산: (본문 클릭) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 버튼 1 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 1 Clicks' %}

<span class="calculation-line">계산: (버튼 1 클릭) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 버튼 2 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 2 Clicks' %}

<span class="calculation-line">계산: (버튼 2 클릭) / (노출 횟수)</span>

{% endapi %}

{% api %}

### 제출된 선택

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### 클릭 후 열람률

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">계산: (고유 클릭 수) / (고유 열람 수) (이메일용)</span>

{% endapi %}

{% api %}

### 확인된 전달 수

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmed Deliveries' %} Braze 고객은 SMS 할당량에 따라 배달 요금이 청구됩니다. 

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 신뢰도

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 확인 페이지 버튼

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### 확인 페이지 해제

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### 변환 (B, C, D)

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %} 이 정의된 이벤트는 캠페인을 구축할 때 사용자가 결정합니다. 이메일, 푸시 및 웹훅의 경우 초기 전송 후 전환 추적을 시작합니다. 콘텐츠 카드의 경우 이 횟수는 콘텐츠 카드를 처음 볼 때부터 시작됩니다.

#### 인앱 메시지

인앱 메시지의 경우, 사용자가 인앱 메시지 캠페인을 수신하고 확인한 후 메시지를 클릭했는지 여부에 관계없이 정의된 전환 기간 내에 특정 전환 이벤트를 수행하면 전환이 카운트됩니다.

전환은 가장 최근에 수신한 메시지에 기인합니다. 재자격이 활성화된 경우, 정의된 전환 기간 내에 발생한 경우 가장 최근에 수신한 인앱 메시지에 전환이 할당됩니다. 그러나 인앱 메시지에 이미 전환이 할당된 경우에는 해당 특정 메시지에 대해 새 전환을 기록할 수 없습니다. 즉, 각 인앱 메시지 전달은 단 하나의 전환과만 연결됩니다.

{% endapi %}

{% api %}

### 총 전환 수

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Conversions' %}

사용자가 인앱 메시지 캠페인을 한 번만 조회하면 나중에 전환 이벤트를 여러 번 수행하더라도 전환은 한 번만 계산됩니다. 그러나 재적격성이 켜져 있고 사용자가 인앱 메시지 캠페인을 여러 번 보는 경우, 사용자가 인앱 메시지 캠페인의 새 인스턴스에 대한 노출을 기록할 때마다 *총 전환* 수가 한 번씩 증가할 수 있습니다. 

예를 들어, 사용자가 인앱 메시지를 두 번 트리거하고 각 인앱 메시지 노출 후 전환하는 경우(결과적으로 두 번의 전환이 발생) *총 전환 수가* 두 개 증가합니다. 그러나 인앱 메시지 노출이 한 번만 발생한 후 전환 이벤트가 두 번 발생한 경우에는 전환이 한 번만 기록되고 *총 전환 수가* 한 개 증가합니다.

{% endapi %}

{% api %}

### 전환율

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Rate' %}

#### 인앱 메시지

일일 총 <i>고유 노출</i> 수 측정지표는 인앱 메시지의 <i>전환율을</i> 계산하는 데 사용됩니다.

인앱 메시지의 노출 수는 하루에 한 번만 계산할 수 있습니다. 반면에 사용자가 원하는 작업('전환')을 완료하는 횟수는 24시간 이내에 증가할 수 있습니다. 전환은 하루에 한 번 이상 발생할 수 있지만, 노출은 하루에 한 번만 발생할 수 있습니다. 따라서 사용자가 하루에 여러 번 전환을 완료하는 경우 <i>전환율은</i> 그에 따라 증가할 수 있지만 노출 횟수는 한 번만 계산됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>인앱 메시지</b>: (기본 전환) / (고유 노출)</li>
        <li><b>기타 채널</b>: (기본 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 전환 기간

{% apitags %}
전체
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### 전달 수

{% apitags %}
이메일, 웹 푸시, iOS 푸시, Android 푸시, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} 이메일의 경우 *배달* 건수는 이메일 가능 상대방이 성공적으로 주고받은 총 메시지(보내기) 수입니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>배송</i>: 카운트</li>
        <li><i>배송 %</i>: (전송 - 반송) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 전달 실패 수

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Delivery Failures' %}

배달 실패의 원인을 파악하는 데 도움이 필요하면 <a href="/docs/braze_support/">Braze 지원팀에</a> 문의하세요.

<span class="calculation-line">계산: (보냄) - (운송업체에 보냄)</span>

{% endapi %}

{% api %}

### 직접 열람 수

{% apitags %}
iOS 푸시
{% endapitags %}

{% multi_lang_include metrics.md metric='Direct Opens' %}

<span class="calculation-line">계산: (직접 열람 수) / (전달 수)</span>

{% endapi %}

{% api %}

### 이메일 가능

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 오류

{% apitags %}
웹훅
{% endapitags %}

{% multi_lang_include metrics.md metric='Errors' %} 오류는 <i>발신자</i> 수에는 포함되지만 <i>고유 수신자</i> 수에는 포함되지 않습니다.

{% endapi %}

{% api %}

### 추정된 실제 열람

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### 실패 수

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Failures' %} 실패는 <i>전송</i> 횟수에는 포함되지만 <i>배달</i> 횟수에는 포함되지 않습니다.</td>

<span class="calculation-line">계산<i>(실패율</i>): (실패) / (전송)</span>

{% endapi %}

{% api %}

### 하드바운스

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

이 경우 Braze는 이메일 주소를 유효하지 않은 것으로 표시하지만 사용자의 [구독 상태]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)는 업데이트하지 않습니다. 이메일이 하드 반송되면 해당 이메일 주소에 대한 향후 요청이 중지됩니다.

{% endapi %}

{% api %}

### 도움말

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Help' %} 사용자 답장은 사용자가 메시지를 받은 후 4시간 이내에 인바운드 메시지를 보낼 때마다 측정됩니다.

{% endapi %}

{% api %}

### 영향받은 열람 수

{% apitags %}
iOS 푸시, Android 푸시
{% endapitags %}

{% multi_lang_include metrics.md metric='Influenced Opens' %}

<span class="calculation-line">계산: (영향을 받은 열람) / (전달)</span>

{% endapi %}

{% api %}

### 생애주기 매출

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### 사용자별 생애주기 가치

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### 일일 평균 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### 일일 구매 수

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### 사용자당 일일 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, 안드로이드 푸시, 웹훅, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### 기계 열람

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Machine Opens' %} 이 지표는 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다.

{% endapi %}

{% api %}

### 열람 수

{% apitags %}
웹 푸시, iOS 푸시, Android 푸시
{% endapitags %}

{% multi_lang_include metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### 옵트아웃

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Opt-Ou' %} 사용자 답장은 사용자가 메시지를 받은 후 4시간 이내에 인바운드 메시지를 보낼 때마다 측정됩니다.

{% endapi %}

{% api %}

### 기타 열람 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} 사용자가 컴퓨터 열기 횟수가 기록되기 전에 이메일을 열 수도 있습니다(예: 기타 열기에 대한 열기 횟수). 사용자가 Apple Mail이 아닌 받은 편지함에서 컴퓨터 열기 이벤트가 발생한 후 이메일을 한 번 이상 여는 경우, 사용자가 이메일을 여는 횟수는 기타 열기 횟수에 대해 계산되고 고유 열기 횟수에 대해서는 한 번만 계산됩니다.

{% endapi %}

{% api %}

### 보류 중 재시도

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### 주요 전환(A) 또는 주요 전환 이벤트

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 이메일, 푸시, 웹훅의 경우 최초 전송 이후 전환 추적을 시작합니다. 콘텐츠 카드 및 인앱 메시지의 경우, 이 수치는 사용자가 콘텐츠 카드 또는 메시지를 처음 볼 때 시작됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>기본 전환(A) 또는 기본 전환 이벤트</i>: 카운트</li>
        <li><i>기본 전환(A) %</i> 또는 <i>기본 전환 이벤트율</i>: (기본 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 읽기 수

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### 수신

{% apitags %}
이메일, 콘텐츠 카드, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Received' %} 

- 콘텐츠 카드: 사용자가 앱에서 카드를 볼 때 수신됩니다.
- 푸시: Braze 서버에서 푸시 제공자에게 메시지가 전송될 때 수신됩니다.
- 이메일: Braze 서버에서 이메일 서비스 제공업체로 메시지가 전송될 때 수신됩니다.
- SMS/MMS: SMS 제공업체가 업스트림 이동 통신사 및 대상 디바이스로부터 확인을 받은 후 "배달됨".
- 인앱 메시지: 트리거 동작에 따라 정의된 디스플레이 시점에 수신됨.
- WhatsApp: 트리거 동작에 따라 정의된 디스플레이 시점에 수신됨.

{% endapi %}

{% api %}

### 거부 수

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rejections' %} Braze 고객의 경우, 거부 건수는 SMS 할당량으로 청구됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 매출

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### 발송됨

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sent' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송 수

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} 이 메트릭은 Braze에서 제공합니다. 예약된 캠페인을 시작하면 이 지표에는 전송률 제한으로 인해 아직 발송되지 않았는지 여부와 관계없이 발송된 모든 메시지가 포함됩니다.

{% alert tip %}
콘텐츠 카드의 경우 이 지표는 [카드 생성을]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) 위해 선택한 항목에 따라 다르게 계산됩니다:

- **출시 또는 단계 진입 시:** 생성되어 볼 수 있는 카드의 수입니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.
- **첫인상:** 사용자에게 표시되는 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 메시지 발송됨

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %} 이 지표는 Braze에서 제공합니다. 예약된 캠페인을 시작하면 이 지표에는 전송률 제한으로 인해 아직 발송되지 않았는지 여부와 관계없이 발송된 모든 메시지가 포함됩니다.

{% alert tip %}
콘텐츠 카드의 경우 이 지표는 [카드 생성을]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) 위해 선택한 항목에 따라 다르게 계산됩니다:

- **출시 또는 단계 진입 시:** 생성되어 볼 수 있는 카드의 수입니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.
- **첫인상:** 사용자에게 표시되는 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 이동통신사로 발송

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends to Carrier' %} 

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 소프트바운스

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} 이메일이 소프트 반송을 받으면 일반적으로 72시간 이내에 재시도하지만, 재시도 횟수는 수신자마다 다릅니다.

{% endapi %}

{% api %}

### 스팸

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>스팸:</i> 카운트</li>
        <li><i>스팸 %</i> 또는 <i>스팸 비율 %</i>: (스팸으로 표시) / (전송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 설문조사 페이지 해제

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### 설문조사 제출

{% apitags %}
인앱 메시지
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### 총 클릭 수

{% apitags %}
이메일, Content Cards, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Clicks' %} LINE의 경우, 하루 최소 임계치인 20개 메시지에 도달한 후 추적됩니다. AMP 이메일의 경우, HTML 및 일반 텍스트 버전의 총 클릭 수입니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (총 클릭 수) / (배송)</li>
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

{% multi_lang_include metrics.md metric='Total Dismissals' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 총 노출 수

{% apitags %}
인앱 메시지, 콘텐츠 카드
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Impressions' %} 이 숫자는 Braze가 SDK로부터 받은 노출 이벤트 수를 합산한 것입니다. 콘텐츠 카드의 경우, 특정 콘텐츠 카드에 대해 기록된 총 노출 횟수입니다. 동일한 사용자에 대해 여러 번 증가시킬 수 있습니다.

인앱 메시지의 경우, 여러 디바이스가 있고 재인증이 꺼져 있는 경우 사용자는 인앱 메시지를 한 번만 볼 수 있습니다. 사용자가 여러 디바이스를 사용하더라도 타겟팅된 첫 번째 디바이스에서만 볼 수 있습니다. 여기서는 프로필에 통합된 디바이스가 있고 사용자가 여러 디바이스에서 로그인하는 하나의 사용자 ID를 가지고 있다고 가정합니다. 사용자가 인앱 메시지를 볼 때마다 노출에 재적격 여부가 기록됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 총 열람 수

{% apitags %}
이메일, iOS 푸시, Android 푸시, 웹 푸시, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Opens' %} LINE의 경우, 하루 최소 임계치인 20개 메시지에 도달한 후 추적됩니다. AMP 이메일의 경우, HTML 및 일반 텍스트 버전의 총 열람 수입니다. 

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (열림) / (배달)</li>
        <li><b>웹 푸시:</b> (직접 열람 수) / (전달 수)</li>
        <li><b>iOS, Android, and Kindle push:</b> (고유 열람 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Revenue' %} 이 지표는 <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>보고서 빌더를</a> 통한 캠페인 비교 보고서에서만 사용할 수 있습니다.

{% endapi %}

{% api %}

### 고유 클릭 수

{% apitags %}
이메일, Content Cards, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} 이메일의 경우 7일 동안 추적됩니다. 여기에는 Braze에서 제공한 탈퇴 링크를 클릭하는 것이 포함됩니다. LINE의 경우 하루에 최소 20개의 메시지가 도달한 후에 추적됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 클릭 수</i>: 카운트</li>
        <li><b>콘텐츠 카드</b> <i>고유 클릭 수 %</i> 또는 <i>고유 클릭률</i>: (고유 클릭 수) / (고유 노출 횟수)</li>
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

{% multi_lang_include metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">계산: (고유 무시 수) / (고유 노출 횟수)</span>

{% endapi %}

{% api %}

### 고유 노출 수

{% apitags %}
인앱 메시지, 콘텐츠 카드
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Impressions' %} 인앱 메시지의 경우, 재적격성이 켜져 있고 사용자가 트리거 액션을 수행하면 24시간 후에 고유 노출 수가 다시 증가할 수 있습니다. 재자격이 켜져 있으면 <i>고유 노출</i> <i>수</i>= <i>고유 수신자 수입니다</i>. <br><br>콘텐츠 카드의 경우 사용자가 카드를 두 번째로 볼 때마다 카운트가 증가해서는 안 됩니다. 

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 고유 열람

{% apitags %}
이메일, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} 이메일의 경우, 이는 7일 동안 추적됩니다. LINE의 경우 하루에 최소 20개의 메시지가 도달한 후에 추적됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 열기</i>: 카운트</li>
        <li><i>고유 오픈 %</i> 또는 <i>고유 오픈율</i>: (고유 열람 수) / (전달 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 수신자

{% apitags %}
전체
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %}

시청자는 매일 고유한 수신자가 될 수 있으므로, <i>고유 노출 수</i>보다 더 높을 것으로 예상해야 합니다. 이 번호는 Braze에서 받은 것으로 `user_id` 을 기준으로 합니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 구독 취소 또는 구독 취소

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>구독 취소</i> 또는 <i>구독</i> <i>취소</i>: 카운트</li>
        <li><i>구독 취소자 %</i> 또는 <i>구독 취소율</i>: (구독 취소) / (배송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 구독취소 수

{% apitags %}
이메일
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribes' %}

<span class="calculation-line">계산: (구독 취소 수) / (전달 수)</span>

{% endapi %}

{% api %}

### 변형

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}