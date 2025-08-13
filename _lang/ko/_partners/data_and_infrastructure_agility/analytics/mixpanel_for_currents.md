---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel_for_currents/
description: "이 참조 문서에서는 향후 Braze 캠페인 또는 캔버스에서 사용자를 타겟팅하는 데 사용할 수 있는 Braze 세그먼트를 생성하기 위해 Mixpanel 코호트를 Braze로 가져올 수 있는 비즈니스 분석 플랫폼인 Braze와 Mixpanel 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> [Mixpanel](https://mixpanel.com/)은 Mixpanel에서 다른 플랫폼으로 이벤트를 내보내 보다 심층적인 분석을 수행하도록 지원하는 비즈니스 분석 플랫폼입니다. 수집된 데이터는 커스텀 보고서를 작성하고 사용자 인게이지먼트와 유지를 측정하는 데 사용할 수 있습니다.

Braze와 Mixpanel의 통합을 통해 [Mixpanel 코호트를 Braze로 가져와]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/mixpanel/) 향후 Braze 캠페인이나 캔버스에서 사용자를 타겟팅하는 데 사용할 수 있는 Braze 세그먼트를 생성할 수 있습니다. 또한 Braze 커런츠를 활용하여 [Braze 이벤트를 Mixpanel로 내보내](#data-export-integration) 전환, 유지, 제품 사용에 대한 심층적인 분석을 수행할 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Mixpanel 계정 | 이 파트너십을 이용하려면 [Mixpanel 계정이](https://mixpanel.com/) 필요합니다. |
| 커런츠 | 데이터를 Mixpanel로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## 데이터 내보내기 통합

Braze에서 Mixpanel로 내보낼 수 있는 이벤트의 전체 목록은 아래에서 확인할 수 있습니다. Mixpanel로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 Mixpanel 고유 ID로 포함됩니다. 현재 Braze는 `external_user_id` 설정이 없는 사용자에 대해서는 이벤트 데이터를 전송하지 않습니다.

두 가지 유형의 이벤트를 믹스패널로 내보낼 수 있습니다: [메시지 인게이지먼트 이벤트](#supported-currents-events)는 메시지 전송과 직접적으로 관련된 Braze 이벤트 및 플랫폼을 통해 추적된 세션, 커스텀 이벤트, 구매 등 기타 앱 또는 웹사이트 활동을 포함한 [고객 행동 이벤트](#supported-currents-events)로 구성됩니다. 모든 사용자 지정 이벤트의 접두사에는 `[Braze Custom Event]` 가 붙습니다. 커스텀 이벤트 속성정보 및 구매 이벤트 속성정보에는 각각 `[Custom event property]` 및 `[Purchase property]`의 접두사가 붙습니다.

추가 이벤트 자격에 대한 액세스가 필요한 경우 계정 매니저에게 문의하거나 [지원 티켓][support]을 개설하세요.

### 1단계: Mixpanel 자격 증명 가져오기

Mixpanel 대시보드에서 새 프로젝트 또는 기존 프로젝트의 **프로젝트 설정**을 클릭합니다. 여기에서 Mixpanel API 비밀 번호와 Mixpanel 토큰을 찾을 수 있습니다. 이 자격 증명은 다음 단계에서 커런츠 연결을 생성하는 데 사용됩니다. 

### 2단계: 브레이즈 전류 생성

Braze에서 \*\*커런츠 > **\+ 커런츠 생성** > **Mixpanel 내보내기 생성**으로 이동합니다. 나열된 필드에 통합 이름, 연락처 이메일, Mixpanel API 비밀번호 및 Mixpanel 토큰을 제공합니다. 다음으로, 추적하려는 이벤트를 선택하면 사용 가능한 이벤트 목록이 제공됩니다. 마지막으로, **커런츠 시작**을 클릭합니다.

![Braze Mixpanel 커런츠 페이지. 이 페이지에는 통합 이름, 연락처 이메일, API 비밀번호 및 Mixpanel 내보내기 토큰에 대한 필드가 포함되어 있습니다. 커런츠 페이지 하단에는 보낼 수 있는 커런츠 이벤트가 나열되어 있습니다.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab 참고 %}
자세한 내용은 Mixpanel의 [통합 문서를](https://help.mixpanel.com/hc/en-us/articles/360001243663) 참조하세요.
{% endtab %}

## 지원되는 커런츠 이벤트

Braze는 커런츠 [사용자 행동]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 이벤트 용어집에 나열된 다음 데이터를 믹스패널로 내보낼 수 있도록 지원합니다:

### 행동
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
  
[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}
