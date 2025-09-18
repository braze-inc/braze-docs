---
nav_title: mParticle for Currents
article_title: mParticle for Currents
alias: /partners/mparticle_for_currents/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 mParticle과 Braze 커런츠 간의 파트너십을 간략히 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle for Currents

> [mParticle](https://www.mparticle.com)은 여러 소스로부터 정보를 수집하여 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼입니다.

Braze와 mParticle의 통합을 통해 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다. [Currents를]({{site.baseurl}}/user_guide/data/braze_currents/) 사용하면 전체 성장 스택에서 데이터를 mParticle에 연결하여 실행 가능한 데이터로 만들 수도 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 커런츠 | 데이터를 mParticle로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
| mParticle 계정 | 이 파트너십을 활용하려면 [mParticle 계정](https://app.mparticle.com/login)이 필요합니다. |
| m파티클 서버 간 키 및 암호 | 이러한 데이터는 mParticle 대시보드로 이동하여 mParticle이 iOS, Android 및 웹 플랫폼용 Braze 상호 작용 데이터를 수신할 수 있도록 [필요한 피드](#step-1-create-feeds)를 생성하여 얻을 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 엠파티클 자격 증명 정보

이벤트 전송 방식에 영향을 주는 앱 수준 및 워크스페이스 수준의 자격 증명이 mParticle에 있습니다.

- **앱 수준:** mParticle은 각 개별 앱별로 이벤트를 분리하므로 iOS 앱에 제공하는 앱 수준 자격 증명은 iOS 전용 이벤트를 전송하는 데만 사용할 수 있습니다.
- **작업 공간 수준:** mParticle은 모든 이벤트를 함께 그룹화하므로 앱 그룹에 제공하는 작업 공간 수준 자격 증명을 사용하여 앱에 특정되지 **않은** 모든 이벤트를 전송할 수 있습니다.

이를 각 개별 앱을 기반으로 mParticle이 '피드'를 수집하는 것으로 생각하면 됩니다. 예를 들어 iOS용 앱이 하나, Android용 앱이 하나, 웹용 앱이 하나 있는 경우 이벤트가 분리됩니다. 즉, 각 앱에 대해 동일한 자격 증명을 제공하면 중복 없이 모든 앱의 모든 데이터를 수신하는 데 하나의 mParticle 피드가 사용됩니다.

## 통합

### 1단계: 피드 만들기

mParticle 관리자 계정에서 **설정 > 입력으로** 이동합니다. mParticle **디렉토리**에서 **Braze**를 찾아 피드 통합을 추가합니다.

Braze 피드 통합은 iOS, Android, 웹, 언바운드와 같은 네 가지 개별 피드를 지원합니다. 언바운드 피드는 플랫폼에 연결되지 않은 이메일과 같은 이벤트에 사용할 수 있습니다. 각 주요 플랫폼 피드에 대한 입력을 만들어야 합니다. **피드 구성** 탭의 **설정 > 입력**에서 추가 입력을 생성할 수 있습니다.

![][1]

각 피드에 대해 **플랫폼으로 작동** 아래 목록에서 일치하는 플랫폼을 선택합니다. **act-as** 피드를 선택하는 옵션이 표시되지 않으면 데이터는 언바운드로 처리되지만 여전히 데이터 웨어하우스 출력으로 전달할 수 있습니다.

![구성 이름을 제공하고 피드 상태를 결정하며 작동할 플랫폼을 선택하라는 프롬프트를 표시하는 첫 번째 통합 대화 상자.][2]{: style="max-width:40%;"}  ![서버 간 키와 서버 간 비밀을 보여주는 두 번째 통합 대화상자.][3]{: style="max-width:37%;"}

각 입력을 생성할 때 mParticle에서 키와 비밀을 제공합니다. 이러한 자격 증명을 복사하고 각 자격 증명 쌍이 어떤 피드에 해당하는지 기록해 두세요.

### 2단계: 현재 만들기

Braze에서 **커런츠 > + 커런츠 생성 > mParticle 내보내기 생성**으로 이동합니다. 각 플랫폼에 대한 통합 이름, 연락처 이메일, mParticle API 키 및 mParticle 비밀 키를 제공합니다. 다음으로, 추적하려는 이벤트를 선택하면 사용 가능한 이벤트 목록이 제공됩니다. 마지막으로, **커런츠 시작**을 클릭합니다.

![Braze의 mParticle Currents 페이지입니다. 여기에서 통합 이름, 연락처 이메일, API 키 및 비밀 키 필드를 찾을 수 있습니다.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지하므로 mParticle API 키와 mParticle 비밀 키를 최신 상태로 유지하는 것이 중요합니다. 이 상태가 **48시간** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

mParticle에 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 `customerid`로 포함됩니다. 현재 Braze는 `external_user_id` 설정이 없는 사용자에 대해서는 이벤트 데이터를 전송하지 않습니다. `external_user_id`를 기본 `customerid`가 아닌 다른 ID에 매핑하려면 Braze CSM에게 문의하세요. 

## 지원되는 커런츠 이벤트

Braze는 커런츠 [사용자 행동]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 이벤트 용어집에 나열된 다음 데이터를 mParticle로 내보낼 수 있도록 지원합니다:

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
- 이메일(중단, 반송, 클릭, 전달, 스팸 설정, 열람, 전송, 소프트 반송, 탈퇴)
- 인앱 메시지(중단, 클릭, 노출 횟수)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- 푸시 알림(중단, 반송, 열기, 보내기)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


mParticle 통합에 대한 자세한 내용은 [여기](http://docs.mparticle.com/integrations/braze/feed) 설명서를 참조하세요.

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}
