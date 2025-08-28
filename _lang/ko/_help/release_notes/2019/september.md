---
nav_title: 9월
page_order: 4
noindex: true
page_type: update
description: "이 문서에는 2019년 9월의 릴리스 노트가 포함되어 있습니다."
---

# 2019년 9월

## OneLogin 내 Braze 앱

고객은 SP 또는 IdP 시작 로그인을 위해 [원로그인]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) 내에서 Braze를 간단히 검색하고 선택할 수 있습니다. 즉, 고객은 OneLogin 내에서 커스텀 애플리케이션을 추가할 필요가 없습니다. 그 결과, SAML SSO를 시작한 이후 나타난 속성 등의 특정 설정이 미리 채워집니다.

## Rokt 캘린더 파트너십

[Rokt 캘린더는]({{site.baseurl}}/partners/home/) Braze 고객에게 개인화된 마케팅 이니셔티브를 조정하고 개인화된 콘텐츠를 최종 사용자의 캘린더로 확장할 수 있는 기능을 제공합니다. 이를 통해 최종 사용자에게 보다 원활한 경험을 제공하고 고객 서비스와의 밀착도를 더욱 높일 수 있습니다. 고객은 다음을 수행할 수 있습니다.

- Braze 플랫폼을 통해 캘린더 초대를 보내 "날짜 저장"을 하고 커뮤니케이션을 확장하세요
- 이벤트 내용이 변경된 경우 기존 초대를 업데이트합니다.

## Passkit 파트너십

Braze 고객은 [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/)을 통해 모바일 지갑으로 고객 참여를 확대할 수 있습니다. Braze의 강력한 세분화 기능을 사용하여 개인화된 지갑 캠페인을 진행하고 푸시, 인앱 메시지 등의 채널과 함께 오케스트레이션할 수 있습니다.

## 메시징 엔드포인트를 통한 디스패치 ID 값 반환

메시지의 `dispatch_id` 은 다음 메시징 엔드포인트 응답에 포함됩니다:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

이렇게 하면 트랜잭션 메시징을 사용하는 고객이 커런츠를 통해 콜백을 추적할 수 있습니다.

## 캔버스 변경 로그

계정에서 캔버스 작업을 하는 사람에 대한 세부 정보가 더 궁금하신가요? 더 이상 궁금해하지 마세요! 이제 캔버스 변경 로그에 액세스할 수 있습니다.

![캔버스 변경 로그]({% image_buster /assets/img/canvas-changelog1.png %})
![캔버스 변경 로그]({% image_buster /assets/img/canvas-changelog2.png %})
