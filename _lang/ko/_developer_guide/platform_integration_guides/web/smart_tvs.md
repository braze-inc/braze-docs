---
nav_title: 스마트 TV 통합
article_title: 웹용 스마트 TV 통합
platform: Web
page_order: 20
description: "이 문서에서는 Braze 웹 SDK를 사용하여 스마트 TV(삼성 및 LG)와 통합하는 방법을 다룹니다."

---

# 스마트 TV 통합

> Braze 웹 SDK를 사용하면 분석을 수집하고 리치 서식의 인앱 메시지와 콘텐츠 카드 메시지를 [삼성 Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) 및 [LG TV(webOS)](https://webostv.developer.lge.com/discover)를 포함한 스마트 TV 사용자에게 표시할 수 있습니다. 이 문서에서는 Braze 웹 SDK를 사용하여 스마트 TV와 통합하는 방법을 다룹니다.

전체 기술 참조는 [JavaScript 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)를 참조하세요. 또는 TV에서 실행되는 웹 SDK를 확인하려면 [샘플 앱](https://github.com/Appboy/smart-tv-sample-apps)을 참조하세요.

## Braze SDK 설치

시작하려면 웹 SDK에 대한 [초기 SDK 설정]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) 가이드를 따르세요.

스마트 TV와 통합할 때는 두 가지 변경 사항이 필요합니다:

1. 웹 SDK를 다운로드하거나 가져올 때는 반드시 '코어' 번들(https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js에서 사용 가능, 여기서 x.y는 원하는 버전)을 사용해야 합니다. NPM 버전은 기본 ES 모듈로 작성되는 반면 CDN 버전은 ES5로 변환되므로 웹 SDK의 CDN 버전을 사용하는 것이 좋습니다. [NPM 버전을](https://www.npmjs.com/package/@braze/web-sdk) 사용하려면 사용하지 않는 코드를 제거하는 웹팩과 같은 번들러를 사용하고 있는지, 코드가 ES5로 트랜스파일되었는지 확인하세요.
2. 웹 SDK를 초기화할 때 `disablePushTokenMaintenance` 및 `manageServiceWorkerExternally` 초기화 옵션을 `true`로 설정해야 합니다.

## 분석

분석을 위한 모든 동일한 웹 SDK 메서드는 스마트 TV에서도 사용할 수 있습니다.

커스텀 이벤트, 커스텀 속성 등을 추적하는 방법에 대한 전체 가이드는 [분석]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/) 설명서를 참조하세요.

## 인앱 메시지 및 콘텐츠 카드

Braze 웹 SDK는 스마트 TV에서 [인앱 메시지]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/) 및 [콘텐츠 카드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/)를 모두 지원합니다. 인앱 메시지 및 콘텐츠 카드 렌더링은 표준 UI 표시로는 지원되지 않아 대신 앱에서 TV 앱 경험에 맞게 사용자 지정해야 하므로 ['코어' 웹 SDK](https://www.npmjs.com/package/@braze/web-sdk)를 사용해야 합니다.

스마트 TV 앱에서 인앱 메시지를 수신하고 표시하는 방법에 대한 자세한 내용은 [수동 인앱 메시지 표시]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display)를 참조하세요.


