---
nav_title: 통합
article_title: 웹용 푸시 통합
platform: Web
channel: push
page_order: 0
page_type: reference
description: "이 문서에서는 Braze SDK를 통해 Braze 웹 푸시를 통합하는 방법을 설명합니다."

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# 푸시 알림 통합

> 푸시 알림은 중요한 업데이트가 발생하면 사용자 화면에 표시되는 알림입니다. 사용자의 브라우저에서 웹 페이지가 현재 열려 있지 않은 경우에도 푸시 알림을 받을 수 있습니다. 푸시 알림은 사용자에게 시의적절하고 관련성 높은 콘텐츠를 제공하거나 사이트에 다시 참여하도록 유도할 수 있는 유용한 방법입니다. 이 참조 문서에서는 Braze 웹 푸시를 Braze SDK와 통합하는 방법을 다룹니다.

더 많은 리소스는 [푸시 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)를 참조하세요.

![]({{site.baseurl}}/assets/img_archive/web_push2.png)

웹 푸시 알림은 대부분의 주요 브라우저에서 지원하는 [W3C 푸시 표준](http://www.w3.org/TR/push-api/)을 사용하여 구현됩니다.

푸시 프로토콜 표준 및 브라우저 지원에 대한 자세한 내용은 [Apple사파리](https://developer.apple.com/notifications/safari-push-notifications/ "푸시 알림") [모질라모질라](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "푸시 API 브라우저 호환성") 및 [마이크로소프트마이크로소프트](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "푸시 API에서") 리소스를 검토할 수 있습니다.

{% multi_lang_include archive/web-v4-rename.md %}

## 통합

### 1단계: 사이트의 서비스 종사자 구성

- 아직 서비스 워커가 없는 경우 다음 스니펫을 사용하여 `service-worker.js` 이라는 이름의 새 파일을 만들어 웹사이트의 루트 디렉터리에 넣습니다.
- 그렇지 않으면 사이트에 이미 서비스 종사자가 등록된 경우 서비스 종사자 파일에 다음 스니펫을 추가하고 웹 SDK를 초기화할 때 [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 초기화 옵션을 `true`로 설정합니다.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

서비스 종사자 파일 이름이 `service-worker.js`가 아닌 경우 `serviceWorkerLocation` [초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)을 사용해야 합니다.

{% alert important %}
웹 서버는 서비스 종사자 파일을 제공할 때 `Content-Type: application/javascript`를 반환해야 합니다.
{% endalert %}

#### 루트 디렉터리에 서비스 워커를 등록할 수 없으면 어떻게 하나요?

기본적으로 서비스 종사자는 등록된 동일한 디렉토리 내에서만 사용할 수 있습니다. 예를 들어 서비스 종사자 파일이 `/assets/service-worker.js`에 있는 경우 `example.com/assets/*` 또는 `assets` 폴더의 하위 디렉토리에만 등록할 수 있으며 홈 페이지(`example.com/`)에는 등록할 수 없습니다. 따라서 서비스 종사자를 루트 디렉토리(예: `https://example.com/service-worker.js`)에 호스팅하고 등록하는 것이 좋습니다.

루트 도메인에 서비스 종사자를 등록할 수 없는 경우 다른 방법은 서비스 종사자 파일을 제공할 때 [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) HTTP 헤더를 사용하는 것입니다. 서비스 워커에 대한 응답으로 `Service-Worker-Allowed: /` 을 반환하도록 서버를 구성하면 브라우저가 범위를 넓혀 다른 디렉토리 내에서 사용할 수 있도록 지시합니다.

#### Tag Manager를 사용하여 서비스 종사자를 생성할 수 있나요?

아니요, 서비스 워커는 웹사이트의 서버에서 호스팅되어야 하며 태그 관리자를 통해 로드할 수 없습니다.

### 2단계: 브라우저 등록

브라우저에서 푸시 알림을 받으려면 `braze.requestPushPermission()`을 호출하여 푸시 기능에 등록해야 합니다. 그러면 즉시 사용자에게 푸시 권한을 요청합니다. 

푸시 권한을 요청하기 전에 사용자에게 푸시 관련 UI를 표시하려는 경우(소프트 푸시 프롬프트라고 함), `braze.isPushSupported()`를 사용하여 사용자의 브라우저에서 푸시가 지원되는지 테스트할 수 있습니다. 인앱 메시지를 사용한 [소프트 푸시 프롬프트 예시를]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) 참조하세요.

사용자를 탈퇴하려면 `braze.unregisterPush()`를 호출하여 탈퇴할 수 있습니다.

{% alert important %}
최신 버전의 Safari 및 Firefox에서는 버튼 클릭 핸들러 또는 소프트 푸시 프롬프트와 같이 수명이 짧은 이벤트 핸들러에서 이 메서드를 호출해야 합니다. 이는 푸시 등록에 대한 [Chrome의 사용자 환경 모범 사례](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE)와 일관됩니다.
{% endalert %}

### 3단계: Safari 푸시 구성(선택 사항) {#safari}

{% alert important %}
이 단계는 macOS 13의 Safari 16부터 더 이상 필요하지 않습니다. 이전 macOS Safari 버전을 지원하려는 경우에만 이 단계를 완료하세요.
{% endalert %}

Mac OS X에서 Safari에 푸시 알림을 지원하려면 다음 추가 지침을 따르세요.

- [Apple에 등록하기](https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33) 지침에 따라 Safari 푸시 인증서를 생성합니다.
- Braze 대시보드의 **설정** 페이지(API 키가 있는 곳)에서 웹 앱을 선택합니다. **Safari 푸시 구성**을 클릭하고 지침에 따라 방금 생성한 푸시 인증서를 업로드합니다.
- `braze.initialize` 으로 전화할 때 선택 사항인 `safariWebsitePushId` 구성 옵션에 Safari 푸시 인증서를 생성할 때 사용한 웹사이트 푸시 ID를 입력합니다. 예를 들면 `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`과 같습니다.

## Safari 모바일 푸시 {#safari-mobile}

iOS 및 iPadOS의 Safari 16.4 이상에서는 [홈 화면에 추가되고](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) [웹 애플리케이션 매니페스트](https://developer.mozilla.org/en-US/docs/Web/Manifest) 파일이 있는 앱에 대한 웹 푸시를 지원합니다. 웹 푸시 알림을 통합하는 단계를 완료한 후에는 Safari용 모바일 푸시에 대한 지원도 제공할 수 있습니다. 

모바일 Safari 웹 푸시를 지원하려면 [여기에서 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/) 참조하세요.

## 소프트 푸시 프롬프트

소프트 푸시 프롬프트('푸시 프라이머'라고도 함)는 권한을 요청할 때 옵트인 비율을 최적화하는 데 도움이 됩니다.

소프트 푸시 프롬프트 설정에 대해 자세히 알아보려면 [소프트 푸시 프롬프트]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) )를 방문하세요.

## HTTPS 요구 사항

웹 표준에서는 푸시 알림 권한을 요청하는 도메인의 보안을 요구합니다.

### 안전한 사이트의 정의는 무엇인가요?

다음 보안 출처 패턴 중 하나와 일치하면 사이트가 안전한 것으로 간주됩니다.

- (https, , \*)
- (wss, \*, \*)
- (, localhost, )
- (, .localhost, \*)
- (, 127/8, )
- (, ::1/128, \*)
- (file, \*, —)
- (chrome-extension, \*, —)

Braze 웹 푸시의 기반이 되는 개방형 표준 사양의 이 보안 요구 사항은 중간자 공격을 방지합니다.

### 보안 사이트를 사용할 수 없는 경우 어떻게 하나요?

업계 모범 사례는 전체 사이트를 보안하는 것이지만, 사이트 도메인을 보안할 수 없는 고객은 보안 Modal을 사용하여 요구 사항을 해결할 수 있습니다. 대체 푸시 도메인 사용 가이드]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) 또는 [작동 중인 데모](http://appboyj.com/modal-test.html) 보기)에서 자세히 알아보세요.

## 서비스 종사자 고급 설정

서비스 종사자 파일은 설치 시 자동으로 `skipWaiting`을 호출합니다. 이 문제를 방지하려면 Braze를 가져오기 전에 서비스 종사자 파일에 다음 코드를 추가합니다.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## 문제 해결

**통합 지침을 따랐지만 여전히 푸시 알림을 받지 못하고 있습니다.**
- 웹 푸시 알림을 사용하려면 사이트가 HTTPS여야 합니다.
- 모든 브라우저에서 푸시 메시지를 수신할 수 있는 것은 아닙니다. 브라우저에서 `braze.isPushSupported()` 이 `true` 으로 반환되는지 확인합니다.
- 사용자가 사이트 푸시 액세스를 거부한 경우 브라우저 환경설정에서 거부 상태를 제거하지 않는 한 다시 권한을 요청하는 메시지가 표시되지 않습니다.

