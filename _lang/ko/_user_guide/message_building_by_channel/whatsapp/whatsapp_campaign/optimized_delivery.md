---
nav_title: 최적화된 전달이 포함된 WhatsApp 메시지
article_title: 최적화된 전달이 포함된 WhatsApp 메시지
page_order: 1
description: "이 참조 기사는 최적화된 전달이 포함된 WhatsApp 메시지를 작성하고 생성하는 단계에 대해 설명합니다."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# 최적화된 전달이 포함된 WhatsApp 메시지

> 동적 참여 기반 전달을 통해 WhatsApp에서 올바른 사용자에게 더 많이 도달하여 전달 가능성과 참여를 높입니다.

최적화된 전달이 포함된 WhatsApp 메시지는 Meta의 [마케팅 메시지 API for WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) (WhatsApp용 MM API)을 사용하여 전송되며, 이는 동적 참여 기반 전달을 제공합니다. 이는 귀하의 높은 참여 메시지(예: 읽히고 클릭될 가능성이 높은 메시지)가 참여할 가능성이 있는 더 많은 사용자에게 도달할 수 있음을 의미합니다. WhatsApp은 귀하의 메시지가 예상되고 관련성이 있으며 시의적절한 경우 높은 참여로 간주하며, 따라서 읽히고 클릭될 가능성이 더 높습니다. 

브랜드는 Cloud API와 비교하여 WhatsApp용 MM API로 동일하거나 더 높은 전달 가능성을 기대할 수 있습니다. 인도에서 높은 참여 마케팅 메시지는 Cloud API에 비해 최대 9% 더 많은 메시지가 전달된 것으로 나타났습니다. WhatsApp용 MM API는 여전히 100% 전달 가능성을 보장하지 않습니다.

### 지역 가용성

최적화된 전달의 가용성과 최적화 기능은 비즈니스 전화번호와 사용자 지역에 따라 다릅니다. 자세한 내용을 보려면 [기능의 지리적 가용성](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features)을 참조하십시오. 

## 최적화된 전달 설정

1. Braze에서 **파트너 통합** > **기술 파트너** > **WhatsApp**으로 이동합니다.
2. **최적화된 전달로 발송 최적화** 섹션에서 **업그레이드 설정**을 선택하여 [내장 가입 워크플로우]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)를 트리거합니다.

![최적화된 전달로 발송 최적화 옵션이 있는 WhatsApp 메시지 통합 섹션입니다.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. 최적화된 전달이 활성화되면 **WhatsApp 비즈니스 계정 관리**의 계정 세부정보에 최적화된 전달 상태가 표시됩니다.

![활성 번호 상태가 있는 구독 그룹이 나열된 WhatsApp 비즈니스 계정 관리 섹션입니다.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

또는 WhatsApp 관리자에서 직접 최적화된 전달을 활성화한 후 Braze에서 발송을 시작할 수 있습니다.

### 설정 문제 해결

- **일반 오류:** 업그레이드 중 문제가 발생하면 이 오류 배너가 표시되고 [지원팀에 문의]({{site.baseurl}}/braze_support/)하라는 안내가 표시됩니다.
- **자격 없음 오류:** Meta에 의해 제한된 경우 이 오류 배너가 표시됩니다: "최소 하나의 WhatsApp 비즈니스 계정이 Meta에 의해 제한되었습니다." 계정은 업그레이드할 수 있도록 양호한 상태여야 합니다.” 문제가 해결될 때까지 이 배너는 닫을 수 없습니다.

## 캠페인 및 캔버스에서 최적화된 전달 사용

최적화된 전달은 **마케팅 메시지**에 사용해야 합니다. Braze는 **유틸리티, 인증, 서비스 및 응답 메시지**에 대해 최적화된 전달 옵션을 자동으로 제거하며, 이는 기본 설정인 Cloud API를 통해 계속 전송되어야 합니다. 

### 전달 방법 선택

1. 캠페인 또는 캔버스 메시지 단계의 Braze WhatsApp 작성기에서 **설정** 탭으로 이동합니다.
2. **전달 방법** 섹션에서 WhatsApp 비즈니스 계정(WABA)이 활성화된 경우 **최적화된 전달(권장)**의 체크박스가 기본적으로 선택됩니다. 특정 메시지에 대해 최적화된 전달을 사용하고 싶지 않다면 체크박스를 선택 해제하세요.
- 최적화된 전달을 선택했지만 사용할 수 없는 경우, 메시지는 자동으로 Cloud API 방법으로 전환됩니다.

![최적화된 전달을 선택할 수 있는 체크박스가 있는 미리보기 탭이 있는 메시지 작성기.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### 다른 Braze 채널에서 사용자 리타겟팅 

WhatsApp의 MM API가 100% 전달 가능성을 제공하지 않기 때문에, 다른 채널에서 메시지를 받지 못한 사용자를 리타겟팅하는 방법을 이해하는 것이 중요합니다. 

사용자를 리타겟팅하려면 특정 메시지를 받지 못한 사용자로 구성된 세그먼트를 만드는 것이 좋습니다. 이를 위해 오류 코드 `131049`로 필터링합니다. 이는 WhatsApp의 사용자당 마케팅 템플릿 한도 시행으로 인해 마케팅 템플릿 메시지가 전송되지 않았음을 나타냅니다. 이 작업은 Braze 커런츠 또는 SQL 세그먼트 확장을 사용하여 수행할 수 있습니다:

- **Braze 커런츠:** Braze 커런츠를 사용하여 메시지 실패 이벤트를 내보낼 수 있습니다. 그런 다음 이 데이터를 사용하여 사용자 프로필의 커스텀 속성을 업데이트할 수 있습니다(예: `whatsapp_failed_last_msg: true`), 이를 리타겟팅 캠페인의 필터로 사용할 수 있습니다.
- **SQL 세그먼트 확장:** 이 기능에 접근할 수 있다면, SQL을 사용하여 메시지 실패 로그를 쿼리하고 해당 사용자 세그먼트를 생성한 다음, 다른 채널에서 해당 세그먼트를 타겟팅할 수 있습니다.
