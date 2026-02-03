---
nav_title: 타사 태그와 Shopify 표준 통합
article_title: "타사 태그와 Shopify 표준 통합"
description: "이 참고 문서에서는 타사 태그 도구로 표준 Shopify 통합을 설정하는 방법을 간략하게 설명합니다."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# 타사 태그 툴과 Shopify 표준 통합

> 이 페이지에서는 Google Tag Manager와 같은 타사 도구와 [Shopify 표준 통합을]({{site.baseurl}}/shopify_standard_integration/) 사용하여 Braze 웹 SDK를 초기화하고 로드하는 방법을 안내합니다.

Shopify 온라인 스토어의 경우 Braze의 표준 통합 방법을 사용하여 사이트에서 Braze SDK를 지원하는 것이 좋습니다. 그러나 Google은 사용자가 Google Tag Manager와 같은 타사 도구를 사용하는 것을 선호할 수 있음을 이해합니다. 타사 툴을 Braze의 Shopify 커넥터와 함께 사용하기로 선택한 경우, 결제 프로세스 중에 Braze 통합 및 앱 임베드가 SDK를 관리한다는 점에 유의하세요.

## 요구 사항

- **타사 도구와 Shopify 커넥터 간의 일관된 API 키:** API 키는 Braze와 타사 도구 모두에서 일관성이 있어야 합니다. 이렇게 하면 중복 사용자가 생성되는 것을 방지하고 SDK 간 호환성을 유지할 수 있습니다. 
  - **API 키 위치:** 표준 통합 경로를 온보딩하면 통합을 통해 자동으로 "Shopify"라는 이름의 Braze 웹 앱이 생성됩니다. 통합 내에서 타사 도구 구성에 사용되는 API 키를 검색합니다. 
- **타사 도구와 Shopify 커넥터 간의 일관된 소프트웨어 개발 키트 버전:** 소프트웨어 개발 키트 버전은 타사 도구 내에서 `5.4` 이어야 합니다. 잘못된 버전 번호를 사용하면 일부 소프트웨어 개발 키트 메서드가 이전 버전에 존재하지 않을 수 있으므로 호환성 문제가 발생할 수 있습니다.
- **일관된 소프트웨어 개발 키트 초기화 타이밍:** Shopify 표준 통합 설정에서 세션 시작 시 또는 계정 로그인 시 초기화할 SDK를 선택할 수 있습니다. 이 설정은 타사 도구와 Braze 간에 일관성이 있어야 합니다. 불일치는 사용자 및 데이터 동기화에 대한 다운스트림 문제로 이어질 수 있습니다. 

{% alert note %}
타사 태그 매니저와 함께 사용하기보다는 표준 통합 방법을 단독으로 사용하는 것이 좋으며, 이는 Braze SDK와 타사 도구 간에 충돌을 일으킬 수 있습니다. 타사 도구를 사용하는 경우 모든 것이 예상대로 작동하는지 테스트하세요.
{% endalert %}

## 타사 도구와 통합 설정하기

제공된 단계를 벗어나면 예기치 않은 문제가 발생할 수 있으므로 이를 주의 깊게 따르세요.

1. [Shopify 표준 통합 설정에서]({{site.baseurl}}/shopify_standard_integration/) 제공된 단계를 따릅니다. Braze [웹 SDK를 인에이블먼트하는]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-2-enable-braze-web-sdks) 동안 타사 도구를 사용하여 Shopify 사이트에 Braze 웹 SDK를 추가하고 있음을 나타내는 확인란을 선택합니다.

!["Braze SDK 설정" 섹션에서 타사 도구를 사용하여 Braze 웹 SDK를 추가할 것임을 나타내는 확인란을 선택합니다.]({% image_buster /assets/img/Shopify/third_party_enable.png %}){: style="max-width:80%;"}

{: start="2"}
2\. **설정** > **앱 설정으로** 이동하여 **Shopify** 웹 앱을 선택한 다음 **웹용 Shopify의 API 키를** 복사합니다.
3\. 타사 도구의 웹 SDK 구성에 API 키를 붙여넣고 SDK 버전을 `5.4` 으로 설정합니다.

## Shopify 데이터 캡처 및 사용자 동기화

서드파티 도구를 통해 Shopify 사이트의 프런트엔드에서 웹 SDK에 액세스할 수 있는 경우 표준 통합을 통해 예상대로 Shopify 데이터를 캡처하고 사용자를 동기화할 수 있습니다.

## 고려 사항 및 고지 사항

- **초기화 설정:** 서드파티 도구를 통해 초기화 설정을 수정하면 사용자 및 데이터 동기화에 영향을 미칠 수 있습니다. 예를 들어, 쿠키 동의 양식을 수락할 때 소프트웨어 개발 키트를 초기화하도록 선택하면 사용자가 동의할 때까지 Braze는 익명 사용자나 데이터를 추적하지 않습니다. 
- **`dataLayer` 을 통해 직접 속성을 설정하는 것은 지원되지 않습니다:** `dataLayer` 대신 `window.braze` 을 사용하여 속성을 설정하세요.
- **잠재적 중복 사용자:** API 키가 Braze와 타사 도구 간에 일치하지 않으면 중복 사용자가 생성될 수 있습니다.
- **소프트웨어 개발 키트 비호환성:** 잘못된 버전 번호를 사용하면 소프트웨어 개발 키트 메서드에 문제가 발생할 수 있습니다.