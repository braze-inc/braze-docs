---
nav_title: HTML 인-앱 메시지
article_title: 커스텀 HTML 인-앱 메시지
page_order: 0
page_type: reference
description: "이 문서에서는 사용자 지정 코드 인앱 메시지의 개요, JavaScript 메서드, 버튼 추적 및 Braze에서 대화형 HTML 미리보기를 사용하는 방법에 대해 설명합니다."
channel:
  - in-app messages
---

# 커스텀 HTML 인-앱 메시지 {#custom-html-messages}

> 표준 인앱 메시지는 다양한 방식으로 사용자 정의할 수 있지만, HTML, CSS 및 JavaScript를 사용하여 설계되고 구축된 메시지를 사용하면 캠페인의 모양과 느낌을 더욱 세밀하게 제어할 수 있습니다. 간단한 구성으로 커스텀 기능과 브랜딩을 필요에 맞게 사용할 수 있습니다. 

HTML 인앱 메시지는 메시지의 모양과 느낌을 더 잘 제어할 수 있게 해줍니다. 다음을 포함합니다.

- 커스텀 글꼴 및 스타일
- 비디오
- 다중 이미지
- 클릭 시 동작
- 대화형 구성 요소
- 커스텀 애니메이션

커스텀 HTML 메시지는 [JavaScript Bridge](#javascript-bridge) 메서드를 사용하여 이벤트를 기록하고, 커스텀 속성을 설정하고, 메시지를 닫는 등의 작업을 수행할 수 있습니다! Check out our [GitHub repository](https://github.com/braze-inc/in-app-message-templates) that contains detailed instructions on how to use and customize HTML in-app messages for your needs, and for a set of HTML5 in-app messages templates to help you get started.

{% alert note %}
웹 SDK를 통해 인앱 메시지에 HTML을 사용하려면 Braze에 초기화 `allowUserSuppliedJavascript`옵션을 제공해야 합니다. 예를 들어, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. 이는 보안상의 이유로, HTML 인앱 메시지는 JavaScript를 실행할 수 있으므로 사이트 관리자가 이를 활성화해야 합니다.
{% endalert %}

## JavaScript 브리지 {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## 링크 기반 작업

커스텀 JavaScript 외에도, Braze SDK는 이러한 편리한 URL 바로 가기를 사용하여 분석 데이터를 보낼 수 있습니다. 이 쿼리 매개변수와 URL 스킴은 모두 대소문자를 구분합니다.

### 버튼 클릭 추적 (사용되지 않음)

{% alert warning %}
`abButtonID`의 사용은 [미리보기]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) 메시지 유형의 HTML에서 지원되지 않습니다. 자세한 내용은 [업그레이드 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes)를 참조하십시오.
{% endalert %}

인앱 메시지 분석을 위해 버튼 클릭을 기록하려면 `abButtonId`를 쿼리 매개변수로 딥링크, 리디렉션 URL 또는 앵커 요소 `<a>`에 추가할 수 있습니다. `?abButtonId=0`을 사용하여 "버튼 1" 클릭을 기록하고, `?abButtonId=1`을 사용하여 "버튼 2" 클릭을 기록합니다.

다른 URL 매개변수와 마찬가지로 첫 번째 매개변수는 물음표`?`로 시작해야 하며, 이후 매개변수는 앰퍼샌드`&`로 구분해야 합니다.

#### 예제 URL

- `https://example.com/?abButtonId=0` - 버튼 1 클릭
- `https://example.com/?abButtonId=1` - 버튼 2 클릭
- `https://example.com/?utm_source=braze&abButtonId=0` - 다른 기존 URL 매개변수와 함께 버튼 1 클릭
- `myApp://deep-link?page=home&abButtonId=1` - 모바일 딥링크와 버튼 2 클릭
- `<a href="https://example.com/?abButtonId=1">` - 앵커 요소 `<a>` 버튼 2 클릭

{% alert note %}
인앱 메시지는 버튼 1 및 버튼 2 클릭만 지원합니다. 이 두 버튼 ID 중 하나를 지정하지 않은 URL은 일반 "본문 클릭"으로 기록됩니다.
{% endalert %}

### 새 창에서 링크 열기 (모바일 전용)

링크를 새 창에서 열려면 `?abExternalOpen=true`를 설정하세요. 메시지는 링크를 열기 전에 해제됩니다.

딥링킹의 경우 Braze는 `abExternalOpen`의 값에 관계없이 사용자의 URL을 엽니다.

### 딥링크로 열기 (모바일 전용)

Braze가 HTTP 또는 HTTPS 링크를 딥링크로 처리하도록 하려면 `?abDeepLink=true`를 설정하세요.

이 쿼리 문자열 매개변수가 없거나 `false`로 설정된 경우, Braze는 호스트 앱 내부의 웹 브라우저에서 웹 링크를 열려고 합니다.

### 인앱 메시지 닫기

인앱 메시지를 닫으려면 `brazeBridge.closeMessage()` JavaScript 메서드를 사용할 수 있습니다.

예를 들어, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` 인앱 메시지를 닫습니다.

## 미리보기가 있는 HTML 업로드

커스텀 HTML 인앱 메시지를 만들 때 Braze에서 직접 인터랙티브 콘텐츠를 미리 볼 수 있습니다. 

편집기의 메시지 미리보기 패널은 메시지에 포함된 JavaScript를 렌더링하는 현실적인 미리보기를 보여줍니다. 미리보기 패널에서 페이지 매김을 클릭하거나, 양식 또는 설문지를 제출하거나, JavaScript 애니메이션을 시청하는 등 커스텀 메시지를 미리보고 상호작용할 수 있습니다!

![페이지를 스와이프하며 HTML 미리보기와 상호작용하기.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
어떤 `brazeBridge` JavaScript 메서드를 HTML에서 사용하더라도 대시보드를 미리 보는 동안 고객 프로필이 업데이트되지 않습니다.
{% endalert %}

### SDK 요구 사항 {#supported-sdk-versions}

인앱 메시지에 대한 HTML 미리보기를 사용하려면 다음 최소 Braze SDK 버전으로 업그레이드해야 합니다.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
이 메시지 유형은 특정 최신 소프트웨어 개발 키트 버전에서만 수신할 수 있으므로, 지원되지 않는 소프트웨어 개발 키트 버전을 사용하는 사용자는 해당 메시지를 수신하지 못합니다. 사용자 기반의 상당 부분에 도달할 수 있는 경우 이 메시지 유형을 채택하거나 앱 버전이 요구 사항보다 최신인 사용자만을 대상으로 고려하세요. [최신 앱 버전별 필터링에 대해 자세히 알아보기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### 캠페인 {#instructions} 만들기

모바일 앱 사용자는 지원되는 소프트웨어 개발 키트 버전으로 업그레이드해야 **사용자 지정 코드** 인앱 메시지를 수신할 수 있습니다. 캠페인 실행 전에 사용자가 최신 Braze SDK 버전에 의존하는 모바일 앱을 [업그레이드하도록 유도]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/)하는 것을 권장합니다.

#### 자산 파일

HTML 업로드를 사용하여 앱 내 메시지에 커스텀 코드를 만들 때, 캠페인 에셋을 [미디어 라이브러리]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)에 업로드하여 메시지에서 참조할 수 있습니다.

다음 파일 형식은 업로드를 지원합니다:

| 파일 형식        | 파일 확장자                    |
| :--------------- | :-------------------------------- |
| 폰트 파일       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG 이미지       | `.svg`                            |
| JavaScript 파일 | `.js`                             |
| CSS 파일        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze는 두 가지 이유로 자산을 미디어 라이브러리에 업로드할 것을 권장합니다:

1. 미디어 라이브러리를 통해 캠페인에 추가된 자산은 사용자가 오프라인 상태이거나 인터넷 연결이 불안정한 경우에도 메시지를 표시할 수 있게 합니다.
2. Braze에 업로드된 자산은 캠페인 전반에 걸쳐 재사용할 수 있습니다.

##### 자산 파일 추가

새로운 자산이나 기존 자산을 캠페인에 추가할 수 있습니다.

새 자산을 캠페인에 추가하려면 드래그 앤 드롭 섹션을 사용하여 파일을 업로드하세요. 이 섹션에 추가된 자산은 미디어 라이브러리에도 자동으로 추가됩니다. 자산을 미디어 라이브러리에 추가하려면 **미디어 라이브러리에서 추가**를 선택하세요.

자산이 추가되면 **이 캠페인의 자산** 섹션에 나타납니다. 

자산의 파일명이 로컬 HTML 자산의 파일명과 일치하는 경우 자동으로 대체됩니다(예:`cat.png`  가 업로드되고`<img src="cat.png" />`  가 존재하는 경우). 

그렇지 않으면 목록에서 자산 위로 마우스를 이동하고 <i class="fas fa-copy"></i> **복사**를 선택하여 파일의 URL을 클립보드에 복사합니다. 그런 다음 복사한 자산 URL을 원격 자산을 참조할 때처럼 HTML에 붙여넣습니다.

### HTML 편집기

HTML에서 변경한 내용은 입력하는 즉시 미리보기 패널에 자동으로 렌더링됩니다. [`brazeBridge` JavaScript](#bridge) 메서드를 HTML에서 사용해도 대시보드에서 미리 보는 동안 고객 프로필이 업데이트되지 않습니다.

{% alert tip %}
HTML 편집기 내에서 **'검색'을**<i class="fa-solid fa-magnifying-glass"></i> 선택하여 코드 내에서 검색할 수 있습니다!
{% endalert %}

### 버튼 추적 {#button-tracking-improvements}

You can track performance within your custom code in-app message using the [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) JavaScript method. 전체 참조 사항은 위의 [JavaScript Bridge 메서드를](#bridge) 참조하십시오.

{% alert note %}
이 버튼 추적 방법은 제거된 이전 자동 클릭 추적 방법(예: `?abButtonId=0`)을 대체합니다.
{% endalert %}

### 하위 호환되지 않는 변경 사항 {#backward-incompatible-changes}

1. 이 새로운 메시지 유형과 관련된 가장 주목할 만한 비호환 변경 사항은 SDK 요구 사항입니다. 앱 SDK가 최소 [SDK 버전 요구 사항](#supported-sdk-versions)을 충족하지 않는 사용자는 메시지가 표시되지 않습니다.
2. 이전에는 모바일 앱에서 지원되었던 `braze://close` 딥링크가 JavaScript `brazeBridge.closeMessage()`로 대체되었습니다. 이것은 웹이 딥링크를 지원하지 않기 때문에 크로스 플랫폼 HTML 메시지를 허용합니다.
3. 자동 클릭 추적, `?abButtonId=0` 버튼 ID에 사용된 것, 그리고 닫기 버튼에 대한 "본문 클릭" 추적이 제거되었습니다. 다음 코드 예제는 새로운 클릭 추적 JavaScript 메서드를 사용하도록 HTML을 변경하는 방법을 보여줍니다:

   | 이전 | 이후 |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_117d7263-cbf2-48d7-a60b-a591abfff6f9/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_ca9f513f-0d6a-496f-9238-bd103e9d99c6/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_ee5ae3f7-19c9-4d56-aa15-6ef76747197d/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_d3f33266-10c9-4c92-911c-7a82cbc163b1/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_713378f4-7d05-4197-95f5-6883f12e2a95/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

