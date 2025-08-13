---
nav_title: Amplitude for Currents
article_title: Amplitude for Currents
page_order: 0
description: "이 참조 문서에서는 제품 분석 및 비즈니스 인텔리전스 플랫폼인 Amplitude와 Braze 커런츠 간의 파트너십을 간략히 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude for Currents

> [Amplitude](https://amplitude.com/)는 제품 분석 및 비즈니스 인텔리전스 플랫폼입니다.

Braze와 Amplitude의 양방향 통합을 통해 [Amplitude 코호트]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/), 사용자 특성 및 이벤트를 Braze로 동기화하고 Braze 커런츠를 활용하여 [Braze 이벤트를 Amplitude로 내보내](#data-export-integration) 제품 및 마케팅 데이터에 대한 심층 분석을 수행할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Amplitude 계정 | 이 파트너십을 활용하려면 이 [Amplitude 계정](https://amplitude.com/)이 필요합니다. |
| 커런츠 | 데이터를 Amplitude로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## 데이터 내보내기 통합

Braze에서 Amplitude로 내보낼 수 있는 이벤트 및 이벤트 속성의 전체 목록은 다음 섹션에서 확인할 수 있습니다. 모든 이벤트는 Amplitude에 전송되며 사용자의 `external_user_id`가 Amplitude 사용자 ID로 포함됩니다. Braze 특정 이벤트 속성정보는 Amplitude에 전송되는 데이터의 `event_properties` 키 아래에 전송됩니다.

{% alert important %}
이 기능을 사용하려면, Amplitude 사용자 ID가 Braze 외부 ID와 일치해야 합니다.
{% endalert %}

Braze는 `external_user_id`가 설정된 사용자 또는 `device_id`가 설정된 익명 사용자에 대해서만 이벤트 데이터를 전송합니다. 익명 사용자의 경우 Amplitude 기기 ID를 SDK의 Braze 기기 ID와 동기화해야 합니다. 예를 들어, 다음과 같습니다.

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Amplitude에 두 가지 유형의 이벤트를 내보낼 수 있습니다. [메시지 인게이지먼트 이벤트](#supported-currents-events)는 메시지 전송과 직접적으로 관련된 Braze 이벤트 및 플랫폼을 통해 추적된 세션, 커스텀 이벤트, 구매 등 기타 앱 또는 웹사이트 활동을 포함한 [고객 행동 이벤트](#supported-currents-events)로 구성됩니다. 모든 일반 이벤트에는 `[Appboy]`가 접두사로 붙고, 모든 커스텀 이벤트에는 `[Appboy] [Custom Event]`가 접두사로 붙습니다. 커스텀 이벤트 및 구매 이벤트 속성정보에는 각각 `[Custom event property]` 및 `[Purchase property]`의 접두사가 붙습니다.

이름이 지정되어 Braze로 가져온 모든 코호트에는 `[Amplitude]`가 접두사로 붙고 `cohort_id`가 접미사로 붙습니다. 즉, 'TEST_COHORT' 이름이 `cohort_id` 'abcd1234"인 코호트는 Braze 필터에서 제목이 `[Amplitude] TEST_COHORT: abcd1234`입니다.

추가 이벤트 자격에 대한 액세스가 필요한 경우 계정 매니저에게 문의하거나 [지원 티켓][support]을 개설하세요.

### 1단계: Braze에서 Amplitude 통합 구성 

Amplitude에서 Amplitude 내보내기 API 키를 찾습니다.

{% alert warning %}
Amplitude API 키를 최신 상태로 유지합니다. 커넥터의 자격 증명이 만료되면, 커넥터는 이벤트 전송을 중지합니다. **48시간** 넘게 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

### 2단계: Braze 커런츠 생성

Braze에서 **커런츠 > + 커런츠 생성 > Amplitude 내보내기 생성**으로 이동합니다. 제공된 필드에 통합 이름, 연락처 이메일, Amplitude 내보내기 API 키 및 Amplitude 리전을 제공합니다. 다음으로, 추적하려는 이벤트를 선택하면 사용 가능한 이벤트 목록이 제공됩니다. 마지막으로, **커런츠 시작**을 클릭합니다.

{% alert note %}
Braze 커런츠에서 Amplitude로 전송된 이벤트는 Amplitude 이벤트 볼륨 할당량에 포함됩니다.
{% endalert %}

![Braze Amplitude 커런츠 페이지. 이 페이지에는 통합 이름, 연락처 이메일, API 비밀번호 및 미국 리전에 대한 필드가 포함되어 있습니다. 커런츠 페이지 하단에는 보낼 수 있는 커런츠 이벤트가 나열되어 있습니다.]({% image_buster /assets/img/amplitude4.png %})

{% tab 참고 %}
자세한 내용은 Amplitude의 [통합 설명서](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration)를 참조하세요.
{% endtab %}

## 사용량 제한

커런츠는 Amplitude의 HTTP API에 연결됩니다. 이 경우 기기마다 초당 30개의 이벤트와 같은 [사용량 제한](https://developers.amplitude.com/docs/http-api-v2#upload-limit) 그리고 기기마다 일당 500,000개의 이벤트와 같은 문서화되지 않은 제한이 있습니다. 이 임계치를 초과하면, Amplitude는 커런츠를 통해 기록된 이벤트를 제한합니다. 통합에서 기기가 이 사용량 제한을 초과하면 모든 기기의 이벤트가 Amplitude에 나타나는 데 지연이 발생할 수 있습니다.

기기는 정상적인 상황에서 초당 30개의 이벤트 또는 일당 500,000개의 이벤트를 초과하여 보고해서는 안 되며, 이 이벤트 패턴은 잘못 구성된 통합으로 인해서만 발생해야 합니다. 이러한 유형의 지연을 피하려면 SDK 통합 지침에 명시된 대로 SDK 통합이 정상적인 속도로 이벤트를 보고하고 단일 기기에 대해 많은 이벤트를 생성하는 자동화된 테스트를 실행하지 않도록 합니다.

## 지원되는 커런츠 이벤트

Braze는 Amplitude로 커런츠 [사용자 행동]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 인게이지먼트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 이벤트 용어집에 나열된 다음 데이터 내보내기를 지원합니다.

### 동작
- 커스텀 이벤트: `users.behaviors.CustomEvent`
- 설치 경로: `users.behaviors.InstallAttribution`
- 위치: `users.behaviors.Location`
- 구매: `users.behaviors.Purchase`
- 제거: `users.behaviors.Uninstall`
- 앱(첫 번째 세션, 세션 종료, 세션 시작)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- 가입(글로벌 상태 변경): `users.behaviors.subscription.GlobalStateChange`
- 구독 그룹(상태 변경): `users.behaviors.subscriptiongroup.StateChange`
  
### 캠페인
- Abort: `users_campaigns_abort`
- Conversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### 캔버스
- Abort: `users_canvas_abort`
- Conversion: `users.canvas.Conversion`
- 진입: `users.canvas.Entry`
- 종료(일치하는 오디언스, 수행된 이벤트)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 실험 단계(전환, 분할 항목)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### 메시지
- 콘텐츠 카드(중단, 클릭, 해제, 노출 횟수, 전송)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- 이메일(중단, 반송, 클릭, 전달, 스팸 설정, 열람, 전송, 소프트 반송, 탈퇴)
- 인앱 메시지(중단, 클릭, 노출 횟수)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- 푸시 알림(중단, 반송, iOSforeground, 열람, 전송)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS(중단, 이동통신사 전송, 전달, 전달 실패, 인바운드 수신, 거부, 전송, 짧은 링크 클릭)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- 웹훅(중단, 전송)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp(중단, 전달, 실패, 인바운드 수신, 읽기, 전송)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`
  
[support]: {{site.baseurl}}/braze_support/
