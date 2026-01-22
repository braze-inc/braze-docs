---
nav_title: 최적화된 전송으로 WhatsApp 메시지
article_title: 최적화된 전송으로 WhatsApp 메시지
page_order: 1
description: "이 참조 기사는 최적화된 전송으로 WhatsApp 메시지를 작성하고 생성하는 과정에 대해 설명합니다."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# 최적화된 전송으로 WhatsApp 메시지

> 메타의 고급 AI 시스템을 활용하여 마케팅 메시지를 참여할 가능성이 높은 더 많은 사용자에게 전달하여 전송 가능성과 메시지 참여를 크게 향상시킵니다.

최적화된 전송으로 WhatsApp 메시지는 메타의 새로운 [마케팅 메시지 라이트 API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/)를 사용하여 전송되며, 이는 전통적인 클라우드 API에 비해 우수한 성능을 제공합니다. 이 새로운 전송 파이프라인은 메시지를 받고 싶어하는 사용자에게 더 잘 도달할 수 있도록 도와줍니다.

최적화된 전송을 사용할 때의 이점은 다음과 같습니다:

- **동적 메시징 한도:** 새로운 API는 사용자당 더 동적인 메시징 한도를 제공하여 높은 참여율의 마케팅 메시지(읽히거나 클릭될 가능성이 높은 메시지)가 더 많은 사용자에게 도달할 수 있도록 합니다.
- **최적화된 전송 가능성:** 메타의 고급 AI가 메시지를 가치 있게 여기고 참여할 것으로 예상되는 사용자에게 최적화하므로, 전달된 메시지의 전송률은 낮지만 참여율은 높을 것으로 기대할 수 있습니다. 
- **검증된 결과:** 인도에서 읽히거나 클릭될 가능성이 높은 메시지는 클라우드 API를 통해 전송한 것에 비해 최대 9% 더 많은 메시지가 전달되었습니다.
- **타겟 전송:** 메타의 고급 AI는 높은 참여율의 메시지를 식별하고 이를 더 많은 사용자에게 전달하여 WhatsApp에서 더 많은 적합한 사람들에게 올바른 메시지를 전달할 수 있도록 합니다.

### 지역 가용성

최적화된 전송의 가용성과 최적화 기능은 비즈니스 전화번호와 사용자의 지역에 따라 다릅니다. 자세한 내용을 보려면 [기능의 지리적 가용성](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features)을 참조하십시오. 

## 최적화된 전송 설정하기

1. Braze에서 **파트너 통합** > **기술 파트너** > **WhatsApp**으로 이동합니다.
2. **최적화된 전송으로 전송 최적화** 섹션에서 **업그레이드 설정**을 선택하여 [내장된 가입 워크플로우]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거합니다.

\![WhatsApp 메시지 통합 섹션으로, 최적화된 전송을 위한 최적화된 배달 옵션이 있습니다.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. 최적화된 배달이 활성화되면, **WhatsApp 비즈니스 계정 관리**의 계정 세부정보에 최적화된 배달 상태가 표시됩니다.

\![WhatsApp 비즈니스 계정 관리 섹션으로, 활성 번호 상태가 있는 구독 그룹이 나열되어 있습니다.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

대안으로, WhatsApp 관리자에서 직접 최적화된 배달을 활성화한 후 Braze에서 전송을 시작할 수 있습니다.

### 설정 문제 해결

- **일반 오류:** 업그레이드 중에 문제가 발생하면, 이 오류 배너가 표시되고 [지원팀에 문의]({{site.baseurl}}/braze_support/)하라는 안내가 표시됩니다.
- **자격 없음 오류:** Meta에 의해 제한된 경우, 이 오류 배너가 표시됩니다: "최소한 하나의 WhatsApp 비즈니스 계정이 Meta에 의해 제한되었습니다. 계정은 업그레이드하기 위해 양호한 상태여야 합니다.” 문제가 해결될 때까지 이 메시지는 닫을 수 없습니다.

## 캠페인 및 캔버스에서 최적화된 배달 사용

최적화된 배달은 **마케팅 메시지**에 사용해야 합니다. Braze는 **유틸리티, 인증, 서비스 및 응답 메시지**에 대해 최적화된 배달 옵션을 자동으로 제거하며, 이는 기본 설정인 Cloud API를 통해 계속 전송되어야 합니다. 

### 전송 방법 선택

1. 캠페인 또는 캔버스 메시지 단계의 Braze WhatsApp 작성기에서 **설정** 탭으로 이동합니다.
2. **전송 방법** 섹션에서, WhatsApp 비즈니스 계정(WABA)이 활성화된 경우 **최적화된 배달(권장)**의 체크박스가 기본적으로 선택됩니다. 특정 메시지에 대해 최적화된 전송을 사용하고 싶지 않다면 체크박스를 선택 해제하세요.
- 최적화된 전송을 선택했지만 사용할 수 없는 경우, 메시지는 자동으로 Cloud API 방법으로 전환됩니다.

\![최적화된 전송을 선택할 수 있는 체크박스가 있는 미리보기 탭이 있는 메시지 작성기.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})