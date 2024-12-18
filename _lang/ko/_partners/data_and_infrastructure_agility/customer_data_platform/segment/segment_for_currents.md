---
nav_title: Segment for Currents
article_title: Segment for Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Segment와 Braze 커런츠 간의 파트너십을 간략히 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment for Currents  

> [Segment](https://segment.com)는 고객 데이터를 수집, 정리 및 활성화하는 데 도움이 되는 고객 데이터 플랫폼입니다. 이 참조 문서에서는 Braze 커런츠와 Segment 간의 연결에 대한 개요와 함께 적절한 구현 및 사용을 위한 요구 사항과 프로세스를 설명합니다.

Braze와 세그먼트 통합을 통해 Braze 커런츠를 활용하여 Braze 이벤트를 세그먼트로 내보내어 전환, 유지 및 제품 사용에 대한 심층 분석을 수행할 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Segment 계정 | 이 파트너십을 활용하려면 [세그먼트 계정](https://app.segment.com/login)이 필요합니다. |
| Braze 대상 | Segment 통합에서 이미 [Braze를 대상으로 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)해야 합니다.<br><br>여기에는 [연결 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)에서 올바른 Braze 데이터 센터 및 REST API 키를 제공하는 것이 포함됩니다. |
| 커런츠 | 데이터를 Segment로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 세그먼트 쓰기 키를 얻으십시오

세그먼트 대시보드에서 세그먼트 소스를 선택하세요. 다음으로, **설정 > API 키**로 이동합니다. 여기에서 **세그먼트 쓰기 키**를 찾을 수 있습니다.

{% alert warning %}
Segment 쓰기 키를 최신 상태로 유지하는 것이 중요합니다. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지합니다. **48시간** 넘게 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

### 2단계: 새 커런츠 커넥터 생성

1. Braze에서 **파트너 통합** > **데이터 내보내기**로 이동합니다.
2. 클릭 **\+ Create New Current** > **세그먼트 데이터 Export**.
3. 다음으로, 통합 이름, 연락처 이메일, Segment 쓰기 키 및 Segment 리전을 제공합니다.

![세그먼트 커런츠 페이지 in Braze. 여기에서 통합 이름, 연락처 이메일, Segment 리전 및 API 키 필드를 찾을 수 있습니다.][3]

### 3단계: 메시지 참여 이벤트 내보내기

다음으로, 내보내려는 메시지 인게이지먼트 이벤트를 선택합니다. 다음 내보내기 이벤트 및 속성 표를 참조하십시오. 세그먼트로 전송된 모든 이벤트에는 사용자의 `external_user_id`이(가) `userId`로 포함됩니다. 현재 Braze는 `external_user_id`가 설정되지지 않은 사용자에 대해 이벤트 데이터를 전송하지 않습니다.

![Braze의 세그먼트 커런츠 페이지에서 사용 가능한 모든 메시지 참여 이벤트 목록입니다.][2]

마지막으로, **현재 실행**을 선택합니다.

{% alert warning %}
동일한 커런츠 커넥터를 두 개 이상 생성하려면(예: 두 개의 메시지 인게이지먼트 이벤트 커넥터), 다른 워크스페이스에 있어야 합니다. Braze Segment 커런츠 통합은 단일 워크스페이스에서 다른 앱별로 이벤트를 분리할 수 없기 때문에, 이를 수행하지 않으면 불필요한 데이터 중복 제거 및 데이터 손실이 발생할 수 있습니다.
{% endalert %}

자세한 내용은 Segment [설명서](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/)를 참조하세요.

## 현재 업데이트 중

{% multi_lang_include updating_currents.md %}

## 지원되는 커런츠 이벤트

Braze는 커런츠 [사용자 행동]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) 이벤트 용어집에 나열된 다음 데이터를 세그먼트로 내보내는 것을 지원합니다:
 
### 행동
- 제거: `users.behaviors.Uninstall`
- 구독 (전역 상태 변경): `users.behaviors.subscription.GlobalStateChange`
- 구독 그룹 (상태 변경): `users.behaviors.subscriptiongroup.StateChange`
  
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
- 이메일 (abort, bounce, 클릭, 전달, markasspam, open, send, softbounce, 탈퇴)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- 인앱 메시지 (중단, 클릭, 노출 횟수)
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

[1]: {% image_buster /assets/img/segment/segment_currents1.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}
[3]: {% image_buster /assets/img/segment/segment.png %}
