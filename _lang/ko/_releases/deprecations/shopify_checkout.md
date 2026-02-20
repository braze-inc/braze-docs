---
nav_title: Shopify checkout.liquid
page_order: 7
description: "이 문서에서는 Shopify 통합에 미치는 영향 및 개발자를 위한 지침을 포함하여 Shopify checkout.liquid의 사용 중단에 대해 설명합니다."
page_type: update

---

# Shopify checkout.liquid 사용 중단

Shopify는 모든 판매자에게 `checkout.liquid` 의 사용 중단과 맞춤형 결제 환경을 구축하기 위한 새로운 기반인 [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) 로의 마이그레이션에 대해 알렸습니다. 

Shopify는 `checkout.liquid` 을 두 단계에 걸쳐 사용 중단할 예정입니다:

1. **[2024년 8월 13일](#phase-one-august-13-2024):** 정보, 배송 및 결제 페이지 업그레이드 마감일입니다.
2. **[2025년 8월 28일](#phase-two-august-28-2025):** 스크립트 태그 및 추가 스크립트를 사용하여 앱을 포함한 감사 및 주문 상태 페이지를 업그레이드할 수 있는 마감일입니다.

Checkout 확장성 업그레이드에 대한 일반 정보는 [Shopify의 업그레이드 가이드](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility)를 참조하세요.

## 통합에 미치는 영향

Braze와 Shopify 통합은 [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)를 사용하여 헤드리스 사이트가 아닌 사이트에 대한 Braze 웹 SDK를 로드합니다. `checkout.liquid`가 완전히 지원 중단되기 전에 모든 고객을 지원하기 위해 2025년 마감일 이전에 새로운 버전의 통합을 출시할 계획입니다. 

2024년 8월 13일에 예정된 변경 사항에 대해 아래 세부 정보를 확인하여 개발팀에서 영향을 받는지 확인하세요.

### 1단계: 2024년 8월 13일

기본 Braze와 Shopify 통합은 결제 환경 내에서 정보, 배송 및 결제 페이지를 사용하지 않습니다. 따라서 기본 통합에는 영향을 미치지 않습니다. 

#### Shopify Plus

Shopify Plus 고객의 경우 정보, 배송 또는 결제 페이지의 `checkout.liquid` 을 수정하는 모든 사용자 지정 SDK 코드 스니펫은 이 날짜 이후에는 비활성 상태가 됩니다. 예를 들어, 이러한 페이지에서 이벤트를 기록하는 사용자 지정 코드는 더 이상 작동하지 않습니다. 사용자 지정 SDK 코드가 있는 경우 마이그레이션에 대한 [개발자 가이드를](#developer-guidance) 참조하세요.

#### 비 Shopify Plus

Shopify Plus 비사용 고객의 경우 정보, 결제 및 배송 페이지를 사용자 지정해야 하는 경우 [Shopify Plus로 업그레이드한](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) 다음 [개발자 지침](#developer-guidance)을 따라야 합니다.

### 2단계: 2025년 8월 28일

Shopify는 통합에 사용되는 `checkout.liquid` 페이지의 [스크립트 태그](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)에 대한 지원을 중단할 예정입니다. 이에 따라 2025년 8월 마감일보다 훨씬 앞서 출시할 계획인 새 버전의 Shopify 통합을 적극적으로 구축하고 있습니다. Braze 제품팀에서 더 많은 정보를 알려드릴 테니 기대해 주세요. 

## 개발자 가이드

이 지침은 `checkout.liquid` 에서 정보, 배송 또는 결제 페이지에 사용자 지정 SDK 코드 스니펫을 추가한 Shopify Plus 고객에게 적용됩니다. 이러한 사용자 지정을 수행하지 않은 경우 이 지침을 무시해도 됩니다.

더 이상 `checkout.liquid`에서 정보, 배송 또는 결제 페이지에 커스텀 SDK 코드 스니펫을 추가할 수 없습니다. 대신 감사 또는 주문 상태 페이지에 커스텀 SDK 코드 스니펫을 추가해야 합니다. 이를 통해 결제를 완료한 사용자를 조정할 수 있습니다.
1. 감사 및 주문 상태 페이지에서 Braze 웹 SDK를 로드합니다.
2. 사용자로부터 이메일을 검색합니다.
3. `setEmail` 호출.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\. Braze에서 이메일의 사용자 프로필을 병합합니다.

중복된 고객 프로필이 있는 경우 [일괄 병합 도구]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)를 사용하여 데이터를 간소화할 수 있습니다. 
