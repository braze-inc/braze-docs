---
nav_title: FAQ
article_title: 캠페인 FAQ
page_order: 10
page_type: FAQ
description: "이 페이지는 캠페인에 대한 자주 묻는 질문에 대한 답변을 제공합니다."
tool: Campaigns

---

# Frequently asked questions

> 이 기사는 캠페인에 대한 자주 묻는 질문에 대한 답변을 제공합니다.

### 멀티채널 캠페인은 어떻게 만들 수 있나요?

멀티채널 캠페인을 만들려면 **메시징** > **캠페인을** 선택합니다. 그런 다음 **캠페인 만들기** > **멀티채널을** 선택합니다. 여기에서 다음 메시징 채널 중에서 선택할 수 있습니다: 콘텐츠 카드, 이메일, LINE, 푸시 알림, SMS/MMS/RCS, 웹훅 또는 WhatsApp.

### 내 멀티채널 캠페인에 대조군을 추가할 수 있나요?

아니요, 캠페인의 통제 그룹은 이메일 A 대 이메일 B와 같은 단일 채널 메시징을 위해 설계되었습니다. 대안으로, 다른 채널, 메시징 콘텐츠 및 전달 타이밍을 테스트하기 위해 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas)를 사용해 보십시오. 

### 캠페인을 테스트하고 최적화하는 방법은 무엇입니까?

다변량 캠페인 및 여러 배리언트가 있는 캔버스 실행은 시작하기에 좋은 방법입니다! 예를 들어, 다른 복사본이나 제목 줄이 있는 하나의 메시지를 테스트하기 위해 [다변량 캠페인]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)을 실행할 수 있습니다. 여러 변형이 있는 캔버스는 전체 워크플로를 테스트하는 데 도움이 됩니다.

### 왜 내 캠페인의 열람율이 감소했습니까?

낮은 오픈율이 항상 기술적 문제와 관련이 있는 것은 아닙니다. 이메일 스크랩으로 인해 추적 픽셀이 누락될 수 있습니다. 그러나 콘텐츠나 오디언스 크기의 변화로 인해 더 적은 사용자가 이메일을 열어볼 가능성도 있습니다. 

### 캠페인 대상은 어떻게 평가됩니까?

기본값으로, 캠페인은 입장 시 오디언스 필터를 확인합니다. 지연이 있는 액션 기반 캠페인의 경우, 메시지가 전송될 때 사용자가 여전히 대상 오디언스에 속해 있는지 확인하기 위해 전송 시점에 세그먼트 기준을 재평가하는 옵션이 있습니다. 

### 특정 캠페인 또는 캔버스에 대해 고유 수신자 수와 전송 횟수에 차이가 있는 이유는 무엇인가요?

One potential explanation could be the campaign or Canvas has re-eligibility turned on, which means users who qualify for the segment and delivery settings will be able to receive the message more than once. 재인증이 켜져 있지 않은 경우 발신자와 고유 수신자 간의 차이에 대한 가능한 설명은 사용자가 프로필과 연결된 플랫폼에 여러 개의 기기를 가지고 있기 때문일 수 있습니다. 

예를 들어, iOS 및 웹 푸시 알림이 모두 포함된 캔버스가 있는 경우, 모바일 및 데스크톱 장치를 모두 사용하는 사용자는 둘 이상의 메시지를 받을 수 있습니다.

### 왜 내 캠페인이 내가 캠페인에 사용하는 세그먼트보다 도달 가능한 사용자 기반이 더 작은가요?

[글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/)이 설정되어 있는 경우, 이는 도달 가능한 오디언스의 일부가 캠페인을 받지 못하도록 방지합니다. 이는 캠페인이 동일한 세그먼트를 사용하더라도 세그먼트의 도달 가능한 사용자 수가 캠페인의 도달 가능한 사용자 수보다 많을 수 있음을 의미합니다.

### 현지 시간대 전달은 무엇을 제공하나요?

현지 시간대 전달을 통해 사용자의 개별 시간대를 기준으로 메시징 캠페인을 세그먼트에 전달할 수 있습니다. 현지 시간대 배송을 사용하지 않는 캠페인은 Braze에서 회사의 시간대 설정에 따라 예약됩니다. 

예를 들어, 런던에 본사를 둔 회사가 오후 12시에 캠페인을 보내면 미국 서부 해안의 사용자에게 새벽 4시에 도달하게 됩니다. If your app is only available in certain countries, this may not be a risk for you. Otherwise, we highly recommend avoiding sending early morning push notifications to your user base.

### Braze는 사용자의 시간대를 어떻게 인식합니까?

Braze는 사용자의 기기에서 자동으로 사용자의 시간대를 결정합니다. 이것은 시간대 정확성과 사용자의 완전한 커버리지를 보장합니다. 사용자 API를 통해 생성된 사용자 또는 표준 시간대가 없는 사용자는 SDK에서 앱에서 인식할 때까지 회사의 표준 시간대가 기본 시간대로 사용됩니다. 

You can check your company's time zone in your [company settings]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) on the dashboard.

### Braze는 현지 시간대 전달을 위해 사용자를 언제 평가합니까?

현지 시간대 배달의 경우 Braze는 다음 두 경우에 사용자의 진입 자격을 평가합니다.

- 예정일의 사모아 시간(UTC+13) 기준
- 예정된 날짜의 현지 시간 기준

사용자가 참가 자격을 얻으려면 두 가지 검사를 모두 통과해야 합니다. 예를 들어 캔버스가 2021년 8월 7일 오후 2시(현지 시간 기준)에 출시될 예정인 경우 뉴욕에 위치한 사용자를 타겟팅하려면 다음과 같은 자격 요건을 확인해야 합니다.

- 2021년 8월 6일 오후 9시에 뉴욕
- 2021년 8월 7일 오후 2시 뉴욕

사용자는 출시 24시간 전에 세그먼트에 있어야 합니다. 사용자가 첫 번째 검사에서 자격이 없는 경우 Braze는 두 번째 검사를 시도하지 않습니다.

예를 들어, 캠페인이 오후 7시 UTC에 전달되도록 예약된 경우, 시간대(예: 사모아)가 식별되면 캠페인 전송을 즉시 대기열에 추가하기 시작합니다. 이는 캠페인을 보내는 것이 아니라 메시지를 보낼 준비를 하고 있다는 의미입니다. If users don't match any filters when we check eligibility, they won't fall into the target audience.

또 다른 예로, 같은 날 발송될 두 개의 캠페인을 만들고 싶다고 가정해 보겠습니다. 하나는 아침에, 하나는 저녁에 발송되며, 사용자가 첫 번째 캠페인을 이미 받은 경우에만 두 번째 캠페인을 받을 수 있도록 필터를 추가합니다. 현지 시간대 전달을 사용하면 일부 사용자가 두 번째 캠페인을 받지 못할 수 있습니다. 이는 사용자의 시간대가 확인될 때 자격을 확인하기 때문에 해당 시간대에 아직 예약된 시간이 발생하지 않았다면 첫 번째 캠페인을 받지 못한 것이므로 두 번째 캠페인에 참여할 수 없습니다.

### 로컬 시간대 캠페인을 어떻게 예약하나요?

캠페인을 예약할 때 지정된 시간에 캠페인을 보내도록 선택한 다음 **현지 시간대의 사용자에게 캠페인 보내기를** 선택합니다.

Braze highly recommends that all local time zone campaigns be scheduled 24 hours in advance. Since such a campaign needs to send over an entire day, scheduling it 24 hours in advance ensures that your message will reach your entire segment. 그러나 필요한 경우 24시간 전에 이러한 캠페인을 예약할 수 있습니다. Keep in mind that Braze will not send messages to any users who have missed the send time by more than 1 hour. 

For example, if it is 1 pm and you schedule a local time zone campaign for 3 pm, then the campaign will immediately send to all users whose local time is between 3 pm and 4 pm, but not to users whose local time is 5 pm. 또한 캠페인에 대해 선택한 전송 시간은 회사 시간대에 아직 발생하지 않은 시간이어야 합니다.

24시간 전에 예약된 현지 시간대 캠페인을 수정해도 메시지의 일정은 변경되지 않습니다. 현지 시간대 캠페인을 편집하여 나중에 전송하기로 결정한 경우(예: 오후 6시 대신 오후 7시), 원래 전송 시간을 선택할 때 타겟 세그먼트에 있던 사용자는 여전히 원래 시간(오후 6시)에 메시지를 받게 됩니다. 현지 시간대를 편집하여 더 이른 시간(예: 오후 5시 대신 오후 4시)에 전송하는 경우 캠페인은 여전히 원래 시간(오후 5시)에 모든 세그먼트 멤버에게 전송됩니다. 

{% alert note %}
캔버스 구성 요소의 경우 사용자는 현지 시간대 전달을 위해 사용자 여정의 다음 구성 요소를 받기 위해 구성 요소에 24시간 동안 있을 필요가 없습니다.
{% endalert %}

사용자가 캠페인에 다시 참여할 수 있도록 허용한 경우 원래 시간(오후 5시)에 다시 캠페인을 받게 됩니다. 그러나 이후의 모든 캠페인에 대해서는 업데이트된 시간에만 메시지가 전송됩니다.

### 현지 시간대 캠페인의 변경 사항은 언제 적용됩니까?

현지 시간대 캠페인의 타겟 세그먼트에는 모든 시간 기반 필터에 최소 48시간의 기간이 포함되어야 전체 세그먼트에 전달이 보장됩니다. 예를 들어 다음 필터를 사용하여 둘째 날 사용자를 타겟팅하는 세그먼트를 생각해 보겠습니다:

- 앱을 처음 사용한 지 1일 이상 경과
- 앱을 처음 사용한 지 2일 미만

현지 시간대 배송은 배송 시간과 사용자의 현지 시간대에 따라 이 구간에 있는 사용자를 놓칠 수 있습니다. 이는 사용자가 자신의 시간대가 전달을 트리거하는 시간까지 세그먼트를 떠날 수 있기 때문입니다.

### 출시 전에 예약된 캠페인에 어떤 변경을 할 수 있습니까?

캠페인이 예약되면 전송할 메시지를 대기열에 추가하기 전에 메시지 구성 이외의 내용을 수정해야 합니다. 모든 캠페인과 마찬가지로, 전환 이벤트는 시작된 후에 편집할 수 없습니다.

### 저는 예정된 캠페인을 업데이트했습니다. 왜 출시되지 않았습니까?

이것은 캠페인이 업데이트된 정확한 시간에 시작되도록 예약된 경우 발생할 수 있습니다. 예를 들어 현재 오후 3시 10분인데 캠페인을 오후 3시 10분에 시작하도록 변경하고 **캠페인 업데이트를** 선택했다면 이제 오후 3시 10분이 지났으므로 시작 예정 시간이 지났음을 의미합니다. 동일한 시간에 캠페인을 예약하는 대신, **캠페인 시작 시 즉시 발송**을 선택하십시오.

### 예약된 캠페인에서 메시지가 대기열에 추가되기 전의 "안전 구역"은 무엇입니까?

We recommend making changes to messages within the following times:

- **One-time scheduled campaigns:** Edit up until the scheduled send time.
- **Recurring scheduled campaigns:** Edit up until the scheduled send time.
- **Local send time campaigns:** Edit up to 24 hours before the scheduled send time.
- **Optimal send time campaigns:** Edit up to 24 hours before the day the campaign is scheduled to send.

If you make changes to your message outside of these recommendations, you may not see the updates reflected in the message sent. For example, if you edit the send time three hours before a campaign is scheduled to send at 12 pm local time, the following may occur:

- Braze는 발송 시간이 1시간 이상 지난 사용자에게 메시지를 보내지 않습니다.
- Pre-enqueued messages may still be sent at the originally enqueued time, rather than the adjusted time.

If you need to make changes, we recommend stopping the current campaign (this will cancel any enqueued messages). 그런 다음 캠페인을 복제하고 필요에 따라 변경한 다음 새 캠페인을 시작할 수 있습니다. 이미 첫 번째 캠페인을 받은 사용자를 이 캠페인에서 제외해야 할 수도 있습니다. 시간대 전송이 가능하도록 캠페인 일정 시간을 다시 조정해야 합니다.

### 캠페인에 참여하는 사용자 수가 예상 수와 일치하지 않는 이유는 무엇입니까?

캠페인에 입장하는 사용자 수는 오디언스 및 트리거가 평가되는 방식에 따라 예상되는 수와 다를 수 있습니다. Braze에서는 트리거 전에 오디언스를 평가합니다([속성 변경]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) 트리거를 사용하지 않는 한). 이렇게 하면 트리거 액션이 평가되기 전에 사용자가 처음에 선택한 오디언스에 속하지 않은 경우 캠페인에서 이탈하게 됩니다.

{% alert tip %}
캠페인 문제 해결에 대한 추가 지원이 필요한 경우, 최근 30일간의 진단 로그만 보유하고 있으므로 문제 발생일로부터 30일 이내에 Braze 지원팀에 문의하시기 바랍니다.
{% endalert %}

### 캠페인 분석 페이지에서 CSV 내보내기 사용자 데이터와 CSV 내보내기 이메일 주소 옵션의 차이점은 무엇인가요?

**CSV 내보내기 이메일 주소** 옵션을 선택하면 이메일 주소가 있는 사용자의 데이터만 다운로드됩니다. 예를 들어, 100,000명의 사용자가 있는 세그먼트가 있지만 그 중 50,000명만 이메일 주소를 가지고 있고, **CSV 이메일 주소 내보내기**를 클릭하면 CSV 파일에서 50,000개의 데이터 행만 볼 수 있습니다. 비교적으로, **CSV 내보내기 사용자 데이터**를 선택하면 모든 사용자 데이터를 내보낼 수 있습니다.

### 캠페인의 API 식별자로 검색할 수 있나요?

네, **캠페인** 페이지에서 필터 `api_id:YOUR_API_ID`을(를) 사용하여 API 식별자로 캠페인을 검색하세요. 캠페인 검색에 대해 알아보려면 [searching for campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/)를 참조하세요.

### API 캠페인과 API 트리거 캠페인의 차이점은 무엇인가요?

API 트리거 캠페인을 사용하면 자체 서버 및 시스템에서 해당 콘텐츠의 전송을 트리거하면서 Braze 대시보드 내에서 캠페인 카피, 다변량 테스트 및 재자격 규칙을 관리할 수 있습니다. 이러한 메시지에는 실시간으로 메시지에 템플릿을 적용할 추가 데이터를 포함할 수도 있습니다.

API campaigns are used to track the messages sent using the API. 대부분의 캠페인과 달리 메시지, 수신자 또는 일정을 지정하지 않고 대신 식별자를 API 호출에 전달합니다. 

### 액션 기반 캠페인과 API 트리거 캠페인의 차이점은 무엇인가요?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### 실행 기반

실행 기반 전달 캠페인 또는 이벤트 트리거 캠페인은 거래 또는 성과 기반 메시지에 매우 효과적이며 사용자가 특정 이벤트를 완료한 후 트리거하여 보낼 수 있습니다. 

| 장점 | 단점 | 
| ---- | ---- |
| • 테스트 사용자가 트리거한 이벤트인 경우 플랫폼으로 들어오는 JSON 페이로드의 가시성 **메시지 활동 로그**를 통해 확인<br><br>\- 개인화 요소는 커스텀 이벤트 속성에 포함됩니다.<br><br>\- 커스텀 이벤트를 사용하여 메시지를 받을 수 있는 사용자 세그먼트를 만들 수 있습니다. | • 데이터 포인트를 소비합니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### API 트리거됨

API 트리거 및 서버 트리거 캠페인은 자체 서버 및 시스템에서 캠페인 콘텐츠 전송을 트리거할 수 있어 고급 트랜잭션을 처리하는 데 이상적입니다. 메시지를 트리거하는 API 요청에는 실시간으로 메시지에 템플릿화할 추가 데이터를 포함할 수도 있습니다.

| Benefits | Considerations | 
| ---- | ---- |
| • 데이터 포인트를 소비하지 않습니다<br><br>\- 개인화 요소는 JSON 페이로드 속성에 포함됩니다 | • JSON 페이로드 속성에서 메시지에 적합한 사용자 세그먼트를 생성할 수 없습니다.<br><br>- **메시지 활동 로그로** 들어오는 JSON 페이로드를 볼 수 없음|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

