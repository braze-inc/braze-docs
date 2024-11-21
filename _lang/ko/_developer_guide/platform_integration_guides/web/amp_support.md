---
nav_title: AMP 지원
article_title: 웹용 AMP 지원
platform: Web
page_order: 5
page_type: reference
description: "이 참조 문서에서는 웹에 대한 AMP 지원과 AMP 페이지에서 Braze를 통합하는 방법을 설명합니다."

---

# AMP 지원

{% alert note %}
AMP 페이지에서 Braze를 통합하려는 경우가 아니라면 이 섹션은 통합할 필요가 없습니다.
{% endalert %}

> 이 참조 문서에서는 웹에 대한 AMP 지원과 AMP 페이지에서 Braze를 통합하는 방법을 설명합니다. 가속 모바일 페이지(AMP)는 JavaScript 사용 제한 등 특정 표준을 적용하여 모바일 기기에서 페이지 로드 시간을 개선하도록 설계된 Google의 지원 프로젝트입니다.

따라서 Braze SDK는 AMP 페이지에 로드할 수 없습니다. 하지만 AMP 프로젝트는 웹 푸시를 지원하는 구성요소를 제공합니다. [다음 지침](https://www.ampproject.org/docs/reference/components/amp-web-push)에서는 해당 구성요소를 설정하는 방법을 자세히 설명합니다. `amp-web-push` 구성요소에 대해서는 다음 설명서를 참조하세요.

## 1단계: AMP 웹 푸시 스크립트 포함

다음 비동기 스크립트 태그를 기억합니다.

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## 2단계: 구독 및 구독 취소 위젯 추가하기

사용자가 푸시에서 가입 및 탈퇴할 수 있는 위젯을 추가해야 합니다. 이것은 HTML 본문 안에 있어야 하며 원하는 대로 스타일을 지정할 수 있습니다.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

## 3단계: 도우미 iFrame 다운로드 및 권한 대화 상자

AMP 웹 푸시 컴포넌트는 푸시 구독을 처리하는 팝업을 생성하는 방식으로 작동합니다. 따라서 프로젝트에 몇 개의 헬퍼 파일을 포함해야 합니다. [helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) 파일 및 [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) f파일을 다운로드하고 사이트에 대해 저장합니다.

## 4단계: 서비스 워커 파일 만들기

다음 내용으로 `service-worker.js` 파일을 만들어 웹사이트의 루트 디렉터리에 넣습니다:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## 5단계: AMP 웹 푸시 HTML 요소 구성

이제 페이지에 `amp-web-push` HTML 요소를 추가해야 합니다. 문서 본문에 다음 HTML 코드를 붙여넣습니다:

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```

특히 `service-worker-URL`에는 `apiKey` 및 `baseUrl`(https://dev.appboy.com/api/v3)을 쿼리 매개변수로 추가해야 합니다.

이제 AMP 페이지에서 푸시 가입 및 탈퇴를 구성할 수 있습니다.
