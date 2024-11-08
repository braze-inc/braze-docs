---
nav_title: 웹 SDK 추적 비활성화하기
article_title: 웹 SDK 추적 비활성화하기
platform: Web
page_order: 6
page_type: reference
description: "이 문서에서는 웹 SDK 추적을 비활성화하는 이유, 방법 및 웹에 미치는 영향 등을 자세히 설명합니다."

---

# 웹 SDK 추적 비활성화

{% multi_lang_include archive/web-v4-rename.md %}

> 데이터 프라이버시 규정을 준수하기 위해 [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) 메서드를 사용하여 웹 SDK에서 데이터 추적 활동을 완전히 중지할 수 있습니다. 

이 메서드는 `disableSDK()` 호출 이전에 기록된 모든 데이터를 동기화하며, 이 페이지 및 향후 페이지 로드에서 이후 모든 Braze 웹 SDK 호출을 무시합니다. 나중에 데이터 수집을 재개하려면 향후 [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) 메서드를 사용하여 데이터 수집을 재개할 수 있습니다.

사용자에게 추적 중지 옵션을 제공하려면 링크 또는 버튼이 두 개 있는 간단한 페이지를 구축하는 것이 좋습니다. 하나는 클릭 시 `disableSDK()`, 다른 하나는 사용자가 다시 옵트인할 수 있도록 `enableSDK()` 으로 연결되는 링크 또는 버튼이 있습니다. 이러한 컨트롤을 사용하여 다른 데이터 하위 프로세서를 통한 추적을 시작하거나 중지할 수도 있습니다.

Braze SDK는 `disableSDK()`를 호출하기 위해 초기화하지 않아도 되므로 완전한 익명의 사용자에 대한 추적을 비활성화할 수 있습니다. 반대로 `enableSDK()`는 Braze SDK를 초기화하지 않으므로 추적을 활성화하려면 나중에 `initialize()`를 호출해야 합니다.
