---
nav_title: HTML 인앱 메시지
article_title: 커스텀 HTML 인앱 메시지
page_order: 0
page_type: reference
description: "이 문서에서는 JavaScript 메서드, 버튼 추적, Braze의 대화형 HTML 미리보기 사용 등 사용자 지정 코드 인앱 메시지에 대한 개요를 제공합니다."
channel:
  - in-app messages
---

# 커스텀 HTML 인앱 메시지 {#custom-html-messages}

> 표준 인앱 메시지는 다양한 방식으로 커스텀할 수 있지만 HTML, CSS, JavaScript를 사용하여 디자인하고 구축한 메시지를 사용하면 캠페인의 모양과 느낌을 훨씬 더 효과적으로 제어할 수 있습니다. 간단한 구성을 통해 필요에 맞는 커스텀 기능과 브랜딩을 구현할 수 있습니다. 

HTML 인앱 메시지를 사용하면 다음과 같이 메시징의 모양과 느낌을 더욱 효과적으로 제어할 수 있습니다:

- 커스텀 글꼴 및 스타일
- 동영상
- 여러 이미지
- 클릭 시 동작
- 대화형 구성 요소
- 커스텀 애니메이션

커스텀 HTML 메시지는 [자바스크립트 브리지](#javascript-bridge) 메서드를 사용하여 이벤트를 기록하고, 커스텀 속성을 설정하고, 메시지를 닫는 등의 작업을 수행할 수 있습니다! 필요에 따라 HTML 인앱 메시지를 사용하고 커스텀하는 방법에 대한 자세한 지침과 시작하는 데 도움이 되는 HTML5 인앱 메시지 템플릿 세트가 포함된 [GitHub 리포지토리를](https://github.com/braze-inc/in-app-message-templates) 확인하세요.

{% alert note %}
웹 소프트웨어 개발 키트를 통해 HTML 인앱 메시지를 인에이블하려면 `allowUserSuppliedJavascript` 초기화 옵션을 Braze에 제공해야 합니다(예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`). 이는 HTML 인앱 메시지가 JavaScript를 실행할 수 있기 때문에 보안상의 이유로 사이트 관리자가 인에이블먼트해야 합니다.
{% endalert %}

## 자바스크립트 브리지 {#javascript-bridge}

웹, Android, iOS 및 Swift SDK용 HTML 인앱 메시지는 사용자가 링크가 있는 요소를 클릭하거나 다른 방식으로 콘텐츠에 참여할 때 Braze SDK와 인터페이스하는 JavaScript "브릿지"를 지원하므로 커스텀 Braze 동작을 트리거할 수 있습니다. 이러한 메서드는 글로벌 `brazeBridge` 또는 `appboyBridge` 변수와 함께 존재합니다.

{% alert important %}
Braze는 글로벌 `brazeBridge` 변수를 사용할 것을 권장합니다. 글로벌 `appboyBridge` 변수는 더 이상 사용되지 않지만 기존 사용자에게는 계속 작동합니다. `appboyBridge` 을 사용 중인 경우 `brazeBridge` 으로 마이그레이션하는 것이 좋습니다. <br><br> `appboyBridge` 는 다음 소프트웨어 개발 키트 버전에서 더 이상 사용되지 않습니다:
- 웹: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

예를 들어 커스텀 속성 및 커스텀 이벤트를 기록한 다음 메시지를 닫으려면 HTML 인앱 메시지 내에서 다음 JavaScript를 사용할 수 있습니다:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close this in-app message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### 자바스크립트 브리지 메서드 {#bridge}

Braze HTML 인앱 메시지에서 지원되는 자바스크립트 메서드는 다음과 같습니다:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Liquid를 참조하여 JavaScript Bridge 메서드에 <code>customAttributes를</code> 삽입할 수 없습니다.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## 링크 기반 작업

커스텀 자바스크립트 외에도 Braze SDK는 이러한 편리한 URL 바로가기를 통해 분석 데이터를 전송할 수 있습니다. 이러한 쿼리 매개변수와 URL 체계는 모두 대소문자를 구분한다는 점에 유의하세요.

### 버튼 클릭 추적(사용 중단됨)

{% alert warning %}
[미리보기]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) 메시지 유형이 [있는 HTML에서는]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) `abButtonID` 사용이 지원되지 않습니다. 자세한 내용은 [업그레이드 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes) 참조하세요.
{% endalert %}

인앱 메시지 분석을 위해 버튼 클릭을 기록하려면 딥링크, 리디렉션 URL 또는 앵커 요소 `<a>` 에 `abButtonId` 를 쿼리 파라미터로 추가하면 됩니다. '버튼 1' 클릭을 기록하려면 `?abButtonId=0`, '버튼 2' 클릭을 기록하려면 `?abButtonId=1` 을 사용하세요.

다른 URL 매개변수와 마찬가지로 첫 번째 매개변수는 물음표 `?` 로 시작해야 하며, 이후 매개변수는 앰퍼샌드 `&` 로 구분해야 합니다.

#### URL 예시

- `https://example.com/?abButtonId=0` - 버튼 1 클릭
- `https://example.com/?abButtonId=1` - 버튼 2 클릭
- `https://example.com/?utm_source=braze&abButtonId=0` - 다른 기존 URL 매개변수와 함께 버튼 1 클릭
- `myApp://deep-link?page=home&abButtonId=1` - 버튼 2번 클릭으로 모바일 디링크하기
- `<a href="https://example.com/?abButtonId=1">` - 앵커 요소 `<a>`, 버튼 2 클릭

{% alert note %}
인앱 메시지는 버튼 1과 버튼 2 클릭만 지원합니다. 이 두 가지 버튼 ID 중 하나를 지정하지 않은 URL은 일반적인 '본문 클릭'으로 기록됩니다.
{% endalert %}

### 새 창에서 링크 열기(모바일 전용)

앱 외부의 링크를 새 창에서 열려면 `?abExternalOpen=true` 을 설정합니다. 링크를 열기 전에 메시징이 해제됩니다.

딥링킹의 경우, Braze는 `abExternalOpen` 의 값에 관계없이 URL을 엽니다.

### 딥링크로 열기(모바일 전용)

Braze가 HTTP 또는 HTTPS 링크를 딥링킹으로 처리하도록 하려면 `?abDeepLink=true` 을 설정하세요.

이 쿼리 문자열 매개변수가 없거나 `false` 로 설정되어 있으면 Braze는 호스트 앱 내부의 웹 브라우저에서 웹 링크를 열려고 시도합니다.

### 인앱 메시지 닫기

인앱 메시지를 닫으려면 `brazeBridge.closeMessage()` 자바스크립트 메서드를 사용할 수 있습니다.

예를 들어 `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` 은 인앱 메시지를 닫습니다.

## 미리보기 기능이 있는 HTML 업로드

커스텀 HTML 인앱 메시지를 제작할 때 Braze에서 바로 인터랙티브 콘텐츠를 미리 볼 수 있습니다. 

편집기의 메시지 미리보기 패널에는 메시징에 포함된 JavaScript를 렌더링하는 사실적인 미리보기가 표시됩니다. 미리보기 패널에서 페이지 매김, 양식 또는 설문조사 제출, 자바스크립트 애니메이션 시청 등을 클릭하여 커스텀 메시지를 미리 보고 상호작용할 수 있습니다!

페이지를 스와이프하여 HTML 미리 보기와 상호 작용하기.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
HTML에서 사용하는 `brazeBridge` JavaScript 메서드는 대시보드에서 미리 보는 동안 고객 프로필을 업데이트하지 않습니다.
{% endalert %}

### 소프트웨어 개발 키트 요구 사항 {#supported-sdk-versions}

인앱 메시징에 HTML 미리 보기를 사용하려면 다음 최소 Braze 소프트웨어 개발 키트 버전으로 업그레이드해야 합니다:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
이 메시지 유형은 특정 이후 소프트웨어 개발 키트 버전에서만 수신할 수 있으므로 지원되지 않는 SDK 버전을 사용하는 사용자는 메시지를 수신할 수 없습니다. 사용자 기반의 상당 부분에 도달할 수 있게 된 후에 이 메시지 유형을 채택하거나 앱 버전이 요구 사항보다 최신 버전인 사용자만 타겟팅하는 것을 고려하세요. [최신 앱 버전별 필터링에]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) 대해 자세히 알아보세요.
{% endalert %}

### 캠페인 만들기 {#instructions}

모바일 앱 사용자가 **사용자 지정 코드** 인앱 메시지를 받으려면 지원되는 소프트웨어 개발 키트 버전으로 업그레이드해야 합니다. 최신 Braze 소프트웨어 개발 키트 버전에 의존하는 캠페인을 시작하기 전에 [사용자에게]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) 모바일 앱을 [업그레이드하도록 넛지하는]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) 것이 좋습니다.

#### 자산 파일

HTML 업로드로 사용자 지정 코드 인앱 메시지를 만들 때 [미디어 라이브러리에]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) 캠페인 자산을 업로드하여 메시지에서 참조할 수 있습니다.

업로드에 지원되는 파일 형식은 다음과 같습니다:

| 파일 유형        | 파일 확장자                    |
| :--------------- | :-------------------------------- |
| 글꼴 파일       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG 이미지       | `.svg`                            |
| 자바스크립트 파일 | `.js`                             |
| CSS 파일        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze는 두 가지 이유로 미디어 라이브러리에 자산 업로드를 권장합니다:

1. 미디어 라이브러리를 통해 캠페인에 자산을 추가하면 사용자가 오프라인 상태이거나 인터넷 연결 상태가 좋지 않은 경우에도 메시지를 표시할 수 있습니다.
2. Braze에 업로드한 자산은 여러 캠페인에서 재사용할 수 있습니다.

##### 자산 파일 추가하기

캠페인에 새 자산 또는 기존 자산을 추가할 수 있습니다.

캠페인에 새 자산을 추가하려면 드래그 앤 드롭 섹션을 사용하여 파일을 업로드하세요. 이 섹션에서 추가한 자산은 미디어 라이브러리에도 자동으로 추가됩니다. 미디어 라이브러리에 이미 업로드한 자산을 추가하려면 **미디어 라이브러리에서 추가를** 선택합니다.

자산이 추가되면 **이 캠페인의 자산** 섹션에 자산이 표시됩니다. 

자산의 파일명이 로컬 HTML 자산의 파일명과 일치하면 자동으로 대체됩니다(예: `cat.png` 업로드했는데 `<img src="cat.png" />` 존재하는 경우). 

그렇지 않으면 목록에서 자산 위로 마우스를 가져간 다음 <i class="fas fa-copy"></i> **복사를** 선택하여 파일의 URL을 클립보드에 복사합니다. 그런 다음 원격 자산을 참조할 때 일반적으로 하는 것처럼 복사한 자산 URL을 HTML에 붙여넣습니다.


### HTML 편집기

HTML에서 변경한 내용은 입력할 때 미리보기 패널에 자동으로 렌더링됩니다. HTML에서 사용하는 [`brazeBridge` JavaScript](#bridge) 메서드는 대시보드에서 미리 보는 동안 고객 프로필을 업데이트하지 않습니다.

{% alert tip %}
HTML 편집기에서 <i class="fa-solid fa-magnifying-glass"></i> **검색을** 선택하여 코드 내에서 검색할 수 있습니다!
{% endalert %}

### 버튼 추적 {#button-tracking-improvements}

사용자 지정 코드 인앱 메시지 내에서 성능/성과를 추적할 수 있습니다. [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) 자바스크립트 메서드를 사용하여 성능을 추적할 수 있습니다. 이를 통해 각각 `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` 또는 `brazeBridge.logClick()` 을 사용하여 "버튼 1", "버튼 2" 및 "본문 클릭"을 프로그래밍 방식으로 추적할 수 있습니다.

| 클릭 수     | 방법                       |
| ---------- | ---------------------------- |
| 버튼 1   | `brazeBridge.logClick('0')` |
| 버튼 2   | `brazeBridge.logClick('1')` |
| 본문 클릭 | `brazeBridge.logClick()`    |
| 커스텀 버튼 추적 |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
이 버튼 추적 방법은 삭제된 이전의 자동 클릭 추적 방법(예: `?abButtonId=0`)을 대체합니다.
{% endalert %}

노출 횟수당 여러 버튼 클릭 이벤트를 추적할 수 있습니다. 예를 들어 메시지를 닫고 버튼 2 클릭을 기록하려면 다음을 사용할 수 있습니다:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

캠페인당 최대 100개의 고유한 이름을 사용하여 새로운 커스텀 버튼 이름을 추적할 수도 있습니다. 예: `brazeBridge.logClick('blue button')` 또는 `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
`onclick` 속성 내에서 JavaScript 메서드를 사용할 때는 큰따옴표로 묶인 HTML 속성과의 충돌을 피하기 위해 문자열 값을 작은따옴표로 묶어야 합니다.
{% endalert %}

#### 제한 사항

- 캠페인당 최대 100개의 고유 버튼 ID를 사용할 수 있습니다.
- 버튼 ID는 각각 최대 255자까지 입력할 수 있습니다.
- 버튼 ID에는 문자, 숫자, 공백, 대시, 밑줄만 포함할 수 있습니다.

### 이전 버전과 호환되지 않는 변경 사항 {#backward-incompatible-changes}

1. 이 새로운 메시지 유형과 가장 눈에 띄는 호환되지 않는 변경 사항은 소프트웨어 개발 키트 요구 사항입니다. 앱 소프트웨어 개발 키트 최소 [버전 요구 사항을](#supported-sdk-versions) 충족하지 않는 사용자에게는 메시지가 표시되지 않습니다.
<br>

2. 이전에 모바일 앱에서 지원되던 `braze://close` 디링크는 자바스크립트 `brazeBridge.closeMessage()` 를 위해 제거되었습니다. 웹은 딥링크를 지원하지 않으므로 크로스 플랫폼 HTML 메시징이 가능합니다.

3. 버튼 ID에 `?abButtonId=0` 을 사용하던 자동 클릭 추적과 닫기 버튼의 '본문 클릭' 추적 기능이 제거되었습니다. 다음 코드 예시는 새로운 클릭 추적 자바스크립트 메서드를 사용하도록 HTML을 변경하는 방법을 보여줍니다:

   | 이전 | 이후 |
   |:-------- |:------------|
   |<code><a href="braze://close">닫기 버튼</a></code>|<code><a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">닫기 버튼</a></code>|
   |<code><a href="braze://close?abButtonId=0">닫기 버튼</a></code>|<code><a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">닫기 버튼</a></code>|
   |<code><a href="app://deeplink?abButtonId=0">추적 버튼 1</a></code>|<code><a href="app://deeplink" onclick="brazeBridge.logClick('0')">추적 버튼 1</a></code>|
   |<code><script><br>location.href = "braze://close?abButtonId=1"<br></script></code>|<code><script><br>window.addEventListener("ab.BridgeReady", function(){<br>  brazeBridge.logClick("1");<br>  brazeBridge.closeMessage();<br>});<br></script></code>|

