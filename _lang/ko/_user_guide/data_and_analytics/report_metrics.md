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

AMP HTML 이메일의 AMP 버전으로 클릭한 총 사용자 수.

{% endapi %}

{% api %}

### 오디언스

{% apitags %}
전체
{% endapitags %}

특정 메시지를 받은 사용자 비율. 이 숫자는 Braze에서 받았습니다.

{% endapi %}

{% api %}

### 반송 수

{% apitags %}
이메일, 웹 푸시, iOS 푸시
{% endapitags %}

실패한 메시지의 총 수. 이것은 유효한 푸시 토큰이 없거나, 이메일 주소가 잘못되었거나 비활성화되었거나, 사용자가 캠페인이 시작된 후 구독을 취소했기 때문에 발생할 수 있습니다. SendGrid를 사용하는 고객의 이메일 반송은 하드 바운스, 스팸 및 잘못된 주소로 전송된 이메일로 구성됩니다.

<span class="calculation-line">계산: (반송) / (발송)</span>

{% endapi %}

{% api %}

### 본문 클릭

{% apitags %}
iOS 푸시, Android 푸시
{% endapitags %}

푸시 스토리 알림은 알림이 클릭될 때 본문 클릭을 기록합니다. 메시지가 확장되거나 실행 버튼 클릭에 대해 기록되지 않습니다.

<span class="calculation-line">계산: (바디 클릭) / (노출)</span>

{% endapi %}

{% api %}

### 본문 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

다음 인앱 메시지 유형 중 하나를 클릭하면 발생합니다:
- 슬라이드 업
- Modal
- 버튼이 없는 전체 화면

<span class="calculation-line">계산: (바디 클릭) / (노출)</span>

{% endapi %}

{% api %}

### 버튼 1 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

메시지의 버튼 1 클릭 수 총합.

<span class="calculation-line">계산: (버튼 1 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### 버튼 2 클릭 수

{% apitags %}
인앱 메시지
{% endapitags %}

메시지의 버튼 2 클릭 수 총계.

<span class="calculation-line">계산: (버튼 2 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

### 제출된 선택

{% apitags %}
인앱 메시지
{% endapitags %}

사용자가 [간단한 설문조사]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/) 질문 페이지에서 제출 버튼을 클릭할 때 선택한 총 선택 수입니다.

{% endapi %}

{% api %}

### 클릭 후 열람률

{% apitags %}
이메일
{% endapitags %}

열린 이메일 중 클릭된 이메일의 비율. 이 메트릭은 [보고서 빌더]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)에서만 사용할 수 있습니다.

<span class="calculation-line">계산: (고유 클릭 수) / (고유 오픈 수) (for 이메일)</span>

{% endapi %}

{% api %}

### 확인된 전달 수

{% apitags %}
SMS
{% endapitags %}

통신사는 SMS가 대상 전화번호로 전달되었음을 확인했습니다. Braze 고객으로서, 배송은 SMS 할당량에 따라 청구됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 신뢰도

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

메시지의 특정 배리언트가 대조군보다 더 나은 성과를 내고 있다는 신뢰도 비율.

{% endapi %}

{% api %}

### 확인 페이지 버튼

{% apitags %}
인앱 메시지
{% endapitags %}

확인 페이지의 실행 버튼에 대한 총 클릭 수는 [간단한 설문조사]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)입니다.

{% endapi %}

{% api %}

### 확인 페이지 해제

{% apitags %}
인앱 메시지
{% endapitags %}

확인 페이지에서 닫기 (x) 버튼을 클릭한 총 횟수는 [간단한 설문조사]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)입니다.

{% endapi %}

{% api %}

### 변환 (B, C, D)

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS
{% endapitags %}

주요 전환 이벤트 이후에 추가된 전환 이벤트. Braze 캠페인에서 받은 메시지를 보고 상호작용한 후 정의된 이벤트가 발생한 횟수입니다. <br><br> 이 정의된 이벤트는 마케터가 캠페인을 구축할 때 결정됩니다. 이메일, 푸시 및 웹훅의 경우 초기 전송 후 전환 추적을 시작합니다. 콘텐츠 카드 및 인앱 메시지의 경우, 이 수치는 사용자가 콘텐츠 카드 또는 메시지를 처음 볼 때 시작됩니다.

{% endapi %}

{% api %}

### 전환율

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS
{% endapitags %}

보낸 메시지의 모든 수신자와 비교하여 정의된 이벤트가 발생한 비율입니다. 이 정의된 이벤트는 캠페인을 구축할 때 결정됩니다.

<span class="calculation-line">계산: (기본 전환) / (고유 수신자)</span>

{% endapi %}

{% api %}

### 전환 기간

{% apitags %}
전체
{% endapitags %}

사용자 행동이 전환 이벤트로 추적되고 반환되는 동안 메시지를 수신한 이후의 일수입니다. 이 기간 이후에 발생하는 전환은 전환 이벤트로 인해 발생한 것이 아닙니다.

{% endapi %}

{% api %}

### 전달 수

{% apitags %}
이메일, 웹 푸시, iOS 푸시, Android 푸시, WhatsApp
{% endapitags %}

수신 서버에서 수락한 메시지 요청의 총 수. 이것은 메시지가 기기에 전달되었다는 것을 의미하지 않으며, 메시지가 서버에 의해 수락되었다는 것만을 의미합니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 전달 실패 수

{% apitags %}
SMS
{% endapitags %}

SMS는 대기열 오버플로로 인해 전송되지 않았습니다(긴 코드 또는 짧은 코드가 처리할 수 있는 속도보다 높은 속도로 SMS를 전송하는 경우).

<span class="calculation-line">계산: (보냄) - (운송업체에 보냄)</span>

{% endapi %}

{% api %}

### 직접 열람 수

{% apitags %}
iOS 푸시
{% endapitags %}

푸시 알림의 총 수(및 비율)는 해당 푸시에서 직접 열렸습니다.

<span class="calculation-line">계산: (직접 열기) / (배달)</span>

{% endapi %}

{% api %}

### 오류

{% apitags %}
웹훅
{% endapitags %}

웹훅 이벤트에 의해 반환된 오류 수(전송 과정에서 증가됨).

{% endapi %}

{% api %}

### 실패 수

{% apitags %}
WhatsApp
{% endapitags %}

WhatsApp 메시지를 보낼 수 없었습니다. 인터넷 서비스 공급자가 하드 바운스를 반환했습니다. 하드 바운스는 영구적인 전달 가능성 실패를 의미합니다.

{% endapi %}

{% api %}

### 영향받은 열람 수

{% apitags %}
iOS 푸시, Android 푸시
{% endapitags %}

푸시 알림이 전송된 후 푸시를 직접 열지 않고 앱을 연 사용자 수(및 비율)

<span class="calculation-line">계산: (영향을 받은 오픈) / (배달)</span>

{% endapi %}

{% api %}

### 보류 중 재시도

{% apitags %}
이메일
{% endapitags %}

수신 서버에 의해 일시적으로 거부되었지만 이메일 서비스 공급자(ESP)에 의해 재전달이 시도된 요청 수입니다. 이메일 서비스 공급자는 타임아웃 기간에 도달할 때까지 전달을 재시도합니다 (일반적으로 72시간 후).

{% endapi %}

{% api %}

### 주요 전환 (A) 또는 주요 전환 이벤트

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

Braze 캠페인에서 받은 메시지를 보고 상호작용한 후 정의된 이벤트가 발생한 횟수입니다. 이 정의된 이벤트는 마케터가 캠페인을 구축할 때 결정됩니다. <br><br>이메일, 푸시 및 웹훅의 경우 초기 전송 후 전환 추적을 시작합니다. 콘텐츠 카드 및 인앱 메시지의 경우, 이 수치는 사용자가 콘텐츠 카드 또는 메시지를 처음 볼 때 시작됩니다.

{% endapi %}

{% api %}

### 읽기 수

{% apitags %}
WhatsApp
{% endapitags %}

사용자가 WhatsApp 메시지를 읽을 때. 사용자의 읽음 확인이 Braze에서 읽음을 추적하려면 "켜짐" 상태여야 합니다.

{% endapi %}

{% api %}

### 수신

{% apitags %}
이메일, Content Cards, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, SMS, WhatsApp
{% endapitags %}

- 콘텐츠 카드: 사용자가 앱에서 카드를 볼 때 수신됩니다.
- 푸시: Braze 서버에서 푸시 제공자에게 메시지가 전송될 때 수신됩니다.
- 이메일: Braze 서버에서 이메일 서비스 제공업체로 메시지가 전송될 때 수신됩니다.
- SMS/MMS: SMS 제공업체가 상위 통신사 및 대상 기기로부터 확인을 받으면 "전송됨" 상태가 됩니다.
- 인앱 메시지: 트리거 동작에 따라 정의된 디스플레이 시점에 수신됨.
- 왓츠앱: 트리거 동작에 따라 정의된 디스플레이 시점에 수신됨.

{% endapi %}

{% api %}

### 거부 수

{% apitags %}
SMS
{% endapitags %}

SMS가 통신사에 의해 거부되었습니다. 이것은 여러 가지 이유로 발생할 수 있습니다. 여기에는 통신사 콘텐츠 필터링, 대상 기기의 가용성, 전화번호가 더 이상 서비스되지 않음 등이 포함됩니다. Braze 고객의 경우 거부는 SMS 할당량에 포함됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송 수

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp, LINE
{% endapitags %}

*보냄*, 또는 *보낸 메시지*, 는 캠페인에서 보낸 총 메시지 수입니다. 예약된 캠페인을 시작한 후, 이 메트릭에는 전송된 모든 메시지가 포함되며, 속도 제한으로 인해 아직 전송되지 않은 메시지도 포함됩니다. 이것은 메시지가 기기에 수신되거나 전달되었음을 의미하지 않으며, 단지 메시지가 전송되었음을 의미합니다. 이 메트릭은 Braze에서 제공합니다.

{% alert tip %}
콘텐츠 카드의 경우, 이 메트릭은 **카드 생성**에 대해 선택한 항목에 따라 다르게 계산됩니다. 자세한 내용은 [카드 생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)을 참조하세요.
{% endalert %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 이동통신사로 발송

{% apitags %}
SMS
{% endapitags %}

{% alert note %}
*전송을 캐리어로*는 더 이상 사용되지 않지만, 이미 사용 중인 사용자에게는 계속 지원됩니다.
{% endalert %}

확인된 전달, 거부 및 전송의 합계(전달 또는 거부가 운송업체에 의해 확인되지 않은 경우). 이는 운송업체가 {delivery} 또는 거부 확인을 제공하지 않는 경우를 포함합니다. 일부 운송업체는 이 확인을 제공하지 않거나 발송 시점에 이를 제공할 수 없습니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 스팸

{% apitags %}
이메일
{% endapitags %}

전송된 이메일 중 '스팸'으로 표시된 총 수.

<span class="calculation-line">계산: (스팸으로 표시됨) / (보냄)</span>

{% endapi %}

{% api %}

### 설문조사 페이지 해제

{% apitags %}
인앱 메시지
{% endapitags %}

설문조사 질문 페이지에서 [간단한 설문조사]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)의 닫기 (x) 버튼에 대한 총 클릭 수.

{% endapi %}

{% api %}

### 설문조사 제출

{% apitags %}
인앱 메시지
{% endapitags %}

간단한 설문조사[]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/)의 제출 버튼에 대한 총 클릭 수입니다.

{% endapi %}

{% api %}

### 총 클릭 수

{% apitags %}
이메일, Content Cards, SMS, LINE
{% endapitags %}

전달된 이메일, 카드 또는 메시지 내에서 클릭한 사용자 수(및 비율)의 총합. LINE의 경우 하루에 최소 20개의 메시지가 도달한 후에 추적됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (총 클릭 수) / (배송)</li>
        <li><b>콘텐츠 카드:</b> (총 클릭 수) / (총 노출 수)</li>
        <li><b>문자 메시지:</b> (클릭 Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 총 무시 수

{% apitags %}
콘텐츠 카드
{% endapitags %}

캠페인에서 콘텐츠 카드가 해제된 횟수. 사용자가 메시지를 두 번 닫으면 한 번만 계산됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 총 노출 수

{% apitags %}
인앱 메시지, 콘텐츠 카드
{% endapitags %}

인앱 메시지가 조회된 횟수(사용자가 메시지를 두 번 본 경우 두 번 계산됩니다). 이 숫자는 Braze가 SDK로부터 수신하는 노출 횟수 이벤트 수의 합입니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 총 열람 수

{% apitags %}
이메일, iOS 푸시, Android 푸시, 웹 푸시, LINE
{% endapitags %}

열린 메시지의 총 수. LINE의 경우 하루에 최소 20개의 메시지가 도달한 후에 추적됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (열림) / (배달)</li>
        <li><b>웹 푸시:</b> (직접 열기) / (배달)</li>
        <li><b>iOS, Android, and Kindle push:</b> (고유 오픈) / (배송)</li>
    </ul>
</span>
{:/}


{% endapi %}

{% api %}

### 총 수익

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

설정된 주요 전환 창 내에서 캠페인 수신자로부터의 총 매출(달러 기준). 이 메트릭은 [보고서 빌더]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)를 통해 캠페인 비교 보고서에서만 사용할 수 있습니다.

{% endapi %}

{% api %}

### 고유 클릭 수

{% apitags %}
이메일, Content Cards, LINE
{% endapitags %}

적어도 한 번 메시지 내에서 클릭한 수신자의 고유한 수. 이것은 이메일에 대해 7일 동안 추적됩니다. 여기에는 Braze에서 제공한 탈퇴 링크를 클릭하는 것이 포함됩니다.

LINE의 경우 하루에 최소 20개의 메시지가 도달한 후에 추적됩니다. 

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (고유 클릭 수) / (배달 수)</li>
        <li><b>콘텐츠 카드:</b> (고유 클릭 수) / (고유 노출 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 무시 수

{% apitags %}
콘텐츠 카드
{% endapitags %}

캠페인에서 콘텐츠 카드를 해제한 사용자 수. 사용자가 캠페인에서 콘텐츠 카드를 여러 번 해제하는 것은 하나의 고유한 해제를 나타냅니다.

<span class="calculation-line">계산: (고유 해고) / (고유 노출)</span>

{% endapi %}

{% api %}

### 고유 노출 수

{% apitags %}
인앱 메시지, 콘텐츠 카드
{% endapitags %}

하루 동안 특정 인앱 메시지 또는 카드를 받은 사용자 수와 본 사용자 수. 인앱 메시지의 경우, 고유 노출 수는 재적격 상태가 켜져 있고 사용자가 트리거 동작을 수행하면 24시간 후에 다시 증가할 수 있습니다. 반대로, 사용자가 콘텐츠 카드를 두 번째로 볼 때는 카운트가 증가하지 않아야 합니다. 이 숫자는 Braze에서 받았습니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 고유 열람

{% apitags %}
이메일, LINE
{% endapitags %}

이것은 단일 사용자가 최소 한 번 열어본 이메일의 총 수이며 7일 동안 추적됩니다. LINE의 경우 하루에 최소 20개의 메시지가 도달한 후에 추적됩니다.

<span class="calculation-line">계산: (고유 오픈) / (배달)</span>

{% endapi %}

{% api %}

### 고유 수신자

{% apitags %}
전체
{% endapitags %}

하루 동안 특정 메시지를 받은 고유한 일일 수신자 또는 사용자 수. 이 숫자는 Braze에서 받았습니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 구독취소 수

{% apitags %}
이메일
{% endapitags %}

수신 상태가 Braze에서 제공한 탈퇴 URL을 클릭한 결과로 탈퇴로 변경된 수신자 수.

<span class="calculation-line">계산: (구독 취소) / (배달)</span>

{% endapi %}

{% api %}

### 변형

{% apitags %}
콘텐츠 카드, 이메일, 인앱 메시지, 웹 푸시, iOS 푸시, Android 푸시, 웹훅, SMS, WhatsApp
{% endapitags %}

크리에이터가 정의한 대로 다르게 변형된 캠페인입니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}
