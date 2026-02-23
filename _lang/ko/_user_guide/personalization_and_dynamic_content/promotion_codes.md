---
nav_title: 프로모션 코드
article_title: 프로모션 코드
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "프로모션 코드 목록에 대해 알아보세요. 이를 캠페인과 캔버스에 추가할 수 있습니다."
---

# 프로모션 코드

> 프로모션 코드 목록에 대해 알아보세요. 이를 캠페인과 캔버스에 추가할 수 있습니다.

## 프로모션 코드 정보

프로모션 코드는 메시지에 고유하고 시간 제한이 있는 값을 삽입하여 전환을 유도할 수 있게 해줍니다. 각 목록은 최대 2천만 개의 코드를 보유할 수 있으며, 모든 코드는 만료되기 전에 최대 6개월 동안 유효할 수 있습니다.

Braze가 프로모션 코드가 포함된 메시지를 보낼 때, 코드는 메시지가 발송되기 전에 차감됩니다. 코드가 일관되고 고유하며 재사용되지 않도록 하려면:

- 실패한 메시지도 코드를 소모합니다.
- 다채널 전송에서는 동일한 코드가 모든 채널에 적용됩니다.
- 조건부 Liquid를 사용하면 참조된 모든 목록에서 코드가 차감되며, 단지 하나의 분기만 표시되더라도 마찬가지입니다.
- 캔버스 단계를 입력하거나 다시 입력하면 새로운 코드가 소모됩니다.

같은 목록에서 여러 스니펫을 하나의 메시지에 배치하면, Braze는 모든 스니펫에 동일한 코드를 적용합니다. 소진되지 않도록 예상 사용량보다 더 많은 코드를 업로드하는 것이 좋습니다.

{% tabs local %}
{% tab Example %}
프로모션 코드를 우체국의 쿠폰처럼 생각하세요. 직원이 귀하의 편지를 위해 스택에서 쿠폰을 꺼내면, 그것은 사라집니다. 편지가 도착하지 않더라도 말입니다.  

예를 들어, 다음 조건부 Liquid에서는 두 목록(`vip-deal` 및 `regular-deal`)의 코드가 차감되며, 각 사용자는 단지 하나의 분기만 보게 됩니다:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
프로모션 코드는 캔버스의 인앱 메시지로 전송될 수 없습니다.
{% endalert %}

## 다음 단계

다음 단계가 필요하신가요? 여기서 시작하세요:

- [프로모션 코드 목록 만들기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/)
- [프로모션 코드 사용하기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes)
- [프로모션 코드 사용 현황 보기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#viewing-promotion-code-usage)

## Frequently asked questions

### 프로모션 코드와 함께 사용할 수 있는 메시징 채널은 무엇인가요?

프로모션 코드는 현재 이메일, 모바일 푸시, 웹 푸시, 콘텐츠 카드, 웹훅, SMS 및 WhatsApp에서 지원됩니다. Braze 거래 이메일 캠페인과 인앱 메시지는 현재 프로모션 코드를 지원하지 않습니다.

### 테스트 및 시드 전송이 사용량에 포함되나요?

기본적으로 테스트 전송 및 시드 그룹 이메일 전송에는 사용자별, 테스트 전송당 프로모션 코드가 사용됩니다. 그러나 테스트 중에 프로모션 코드를 사용하지 않도록 이 동작을 업데이트하려면 Braze 계정 매니저에게 문의할 수 있습니다.

### 여러 메시징 채널이 동일한 프로모션 코드 스니펫을 사용할 때 어떤 일이 발생합니까?

특정 사용자가 여러 채널을 통해 코드를 받을 수 있는 경우, 각 채널을 통해 동일한 코드를 받게 됩니다. 수신된 채널에 관계없이 하나의 프로모션 코드만 사용됩니다.

### 하나의 메시지에서 동일한 프로모션 코드 목록을 참조하기 위해 여러 Liquid 스니펫을 사용할 수 있습니까?

예. Braze는 메시지의 해당 스니펫의 모든 인스턴스에 동일한 프로모션 코드를 적용하여 사용자가 고유한 코드를 하나만 받도록 보장합니다.

### 프로모션 코드 목록이 만료되었거나 비어 있으면 어떻게 되나요?

만료된 코드는 6개월 후에 삭제됩니다.

메시지에 비어 있거나 만료된 목록의 프로모션 코드가 포함되어 있어야 하는 경우 메시지가 취소됩니다. 

메시지에 조건부로 프로모션 코드를 삽입하는 Liquid 로직이 포함된 경우, 메시지에 프로모션 코드가 포함되어 있어야 하는 경우에만 메시지가 취소됩니다. 메시지에 프로모션 코드가 포함되지 않아야 하는 경우, 메시지는 정상적으로 전송됩니다.

### 잘못된 프로모션 코드를 업로드한 경우, 이를 업데이트할 수 있습니까?

예. 전체 목록을 사용 중단하거나 플레이스홀더를 사용하여 목록을 삭제하여 이 문제를 해결할 수 있습니다. 자세한 내용은 [프로모션 코드 목록 업데이트]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#updating-a-promotion-code-list)를 참조하십시오.

### 향후 메시지를 위해 프로모션 코드를 사용자의 프로필에 저장할 수 있습니까?

예. 사용자 업데이트 단계를 통해 사용자의 프로필에 프로모션 코드를 저장할 수 있습니다. 자세한 내용은 [사용자 프로필에 프로모션 코드 저장]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#save-to-profile)을 참조하십시오.
