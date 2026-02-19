---
nav_title: 코드 사용하기
article_title: 프로모션 코드 사용하기
page_order: 0.2
description: "프로모션 코드를 사용하는 방법을 배우고 캠페인 및 캔버스의 사용량을 확인하세요."
---

# 프로모션 코드 사용하기

> 프로모션 코드를 사용하는 방법을 배우고 캠페인 및 캔버스의 사용량을 확인하세요.

## 필수 조건

프로모션 코드를 사용하기 전에 [프로모션 코드 목록 만들기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/)이 필요합니다.

## 프로모션 코드 사용하기

메시지에 프로모션 코드를 보내려면, 이전에 만든 프로모션 코드 목록 옆의 **스니펫 복사**을 선택하세요.

![메시지에 붙여넣기 위해 스니펫을 복사하는 옵션입니다.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Braze의 메시지 중 하나에 코드 스니펫을 붙여넣고, 목록에서 고유한 프로모션 코드 중 하나를 삽입하기 위해 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)을 사용하세요. 해당 코드는 전송된 것으로 표시되어, 다른 메시지가 동일한 코드를 전송하지 않도록 합니다.

![예시 메시지 "이번 봄에 우리의 독점 제안으로 자신에게 좋은 것을 선물하세요" 다음에 코드 스니펫이 옵니다.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### 캔버스 단계 전반에 걸쳐

캠페인이나 멀티채널 메시지가 있는 캔버스에서 코드 스니펫이 사용될 때, 각 사용자는 고유한 코드를 받습니다. 프로모션 코드를 참조하는 여러 단계가 있는 캔버스에서, 사용자는 들어가는 각 단계마다 새로운 코드를 받습니다.

캔버스에서 하나의 프로모션 코드를 할당하고 단계를 통해 재사용하려면:

1. 첫 번째 단계(사용자 업데이트)에서 프로모션 코드를 커스텀 속성으로 할당하세요.
2. 이후 단계에서 새로운 코드를 생성하는 대신 해당 커스텀 속성을 참조하기 위해 Liquid를 사용하세요.

사용자가 여러 채널에서 코드 자격을 갖추면, 각 채널에서 동일한 코드를 받습니다. 예를 들어, 이메일과 푸시로 메시지를 받는 경우, 동일한 코드가 두 곳에 모두 전송됩니다. 보고서 또한 단일 코드를 반영합니다.

{% alert note %}
사용 가능한 프로모션 코드가 없으면, 코드에 의존하는 테스트 또는 실시간 메시지는 전송되지 않습니다.
{% endalert %}

### 인앱 메시지 캠페인 {#promotion-codes-iam-campaigns}

After creating an [in-app message campaign]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), you can insert a [promotion code list snippet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) into your in-app message message body. 인앱 메시지에서 프로모션 코드는 사용자가 인앱 메시지 표시를 트리거할 때만 차감되고 사용됩니다.

### 테스트 메시지

테스트 전송 및 시드 그룹 이메일 전송은 요청하지 않는 한 프로모션 코드를 사용합니다. 테스트 전송 및 시드 그룹 이메일 전송 중에 프로모션 코드가 사용되지 않도록 이 기능 동작을 업데이트하려면 Braze 계정 관리자에게 문의하세요.

### 커런츠에 대한 메시지 추가 기능

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## 사용자 프로필에 프로모션 코드 저장 {#save-to-profile}

이후 메시지에서 동일한 프로모션 코드를 참조하려면 코드를 사용자 프로필에 사용자 지정 속성으로 저장해야 합니다. 이는 할인 코드를 "프로모션 코드"와 같은 사용자 정의 속성에 할당하는 [사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)를 통해 수행할 수 있습니다. 메시지 단계 바로 전에.

먼저 사용자 업데이트 단계의 각 필드에 대해 다음을 선택합니다:

- **Attribute Name:** 프로모션 코드
- **Action:** 업데이트
- **Key Value:** 프로모션 코드의 Liquid 코드 스니펫, 예: {% raw %}`{% promotion('spring25') %}`{% endraw %}

둘째, 메시지에 사용자 정의 속성(이 예에서는 {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %})을 추가합니다. 할인 코드는 템플릿에 포함되어 있습니다.

## 프로모션 코드 사용 보기

**프로모션 코드** 페이지의 프로모션 코드 목록의 **남은** 열에서 남은 코드 수를 확인할 수 있습니다.

![사용되지 않은 코드가 있는 프로모션 코드의 예입니다.]({% image_buster /assets/img/promocodes/promocode11.png %})

이 코드 수는 기존 프로모션 코드 목록 페이지를 다시 방문할 때도 확인할 수 있습니다. 사용하지 않는 코드를 CSV 파일로 내보낼 수도 있습니다. 

![992개의 남은 코드가 있는 "블랙 프라이데이 세일"이라는 이름의 프로모션 코드입니다.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## 멀티채널 및 단일 채널 전송

멀티채널 및 단일 전송 캠페인과 캔버스의 경우, 메시지의 리퀴드에 참조된 모든 프로모션 코드가 메시지 전송 **전에** 사용되지 않도록 차감되어 다음과 같은 상황이 발생합니다:

- 멀티채널 메시지에서 동일한 프로모션 코드가 여러 채널에 걸쳐 사용됩니다.
- 메시지가 실패하거나 중단되면 추가 프로모션 코드는 사용되지 않습니다.

사용자가 Liquid 조건 로직 태그로 분할된 하나의 메시지에서 두 개의 프로모션 코드 목록을 참조하는 경우, 사용자가 따르는 조건 흐름에 관계없이 모든 프로모션 코드가 여전히 차감됩니다.

사용자가 새로운 캔버스 단계를 입력하거나 캔버스를 다시 입력하고, 해당 사용자에게 메시지에 대해 프로모션 코드 Liquid 스니펫이 다시 적용되면 새로운 프로모션 코드가 사용됩니다.

### 예시

다음 예에서 두 개의 프로모션 코드 목록 `vip-deal` 및 `regular-deal`가 차감됩니다. 여기 Liquid가 있습니다.

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze는 예상보다 더 많은 프로모션 코드를 업로드할 것을 권장합니다. 프로모션 코드 목록이 만료되거나 프로모션 코드가 소진되면 후속 메시지는 중단됩니다.

{% alert tip %}
**다음은 Braze에서 프로모션 코드가 어떻게 사용되는지에 대한 비유입니다.** <br><br>메시지를 보내는 것이 우체국에서 편지를 보내는 것과 같다고 상상해 보세요. 편지를 점원에게 전달하면 편지에 쿠폰이 포함되어 있어야 한다는 것을 점원이 확인합니다. 점원은 더미에서 첫 번째 쿠폰을 꺼내 봉투에 넣습니다. 점원이 편지를 보냈지만 어떤 이유에서인지 편지가 우편물에서 분실되었습니다(쿠폰도 분실되었습니다). <br><br>이 시나리오에서 Braze는 우편 클럭이고, 당신의 프로모션 코드는 쿠폰입니다. 우리는 그것이 프로모션 코드 스택에서 꺼내진 후에는 웹훅 결과와 관계없이 그것을 검색할 수 없습니다.
{% endalert %}
