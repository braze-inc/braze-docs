---
nav_title: Google 태그 관리자
article_title: 웹용 Google Tag Manager
platform: Web
page_order: 20
description: "이 문서에서는 Google Tag Manager를 사용하여 웹사이트에 Braze를 배포하는 방법을 다룹니다."

---

# Google 태그 관리자

> 이 문서에서는 Google Tag Manager(GTM)를 사용하여 웹사이트에 Braze 웹 SDK를 추가하는 방법에 대한 단계별 가이드를 제공합니다. [Google 태그 관리자를](https://support.google.com/tagmanager/answer/6103696) 사용하면 프로덕션 코드 릴리스나 엔지니어링 리소스 없이도 웹사이트에 원격으로 태그를 추가, 제거, 편집할 수 있습니다.

Braze에서 만든 두 가지 Google 태그 관리자 템플릿은 [초기화 태그와](#initialization-tag) [작업 태그입니다](#actions-tag).

두 태그 모두 [Google의 커뮤니티 갤러리에서](https://tagmanager.google.com/gallery/#/?filter=braze) 또는 커뮤니티 템플릿에서 새 태그를 추가할 때 Braze를 검색하여 작업 공간에 추가할 수 있습니다.

![갤러리 검색 이미지]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## 업데이트된 Google EU 사용자 동의 정책

{% alert important %}
Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html) 개정 사항에 따라 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트하고 있습니다. 이 새로운 변경 사항에 따라 광고주는 EEA 및 영국 최종 사용자에게 특정 정보를 공개하고 해당 사용자로부터 필요한 동의를 얻어야 합니다. 자세한 내용은 다음 문서를 참조하세요.
{% endalert %}

Google의 EU 사용자 동의 정책의 일환으로 다음 부울 커스텀 속성을 고객 프로필에 기록해야 합니다.

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 통합을 통해 설정하는 경우 커스텀 속성을 사용하려면 커스텀 HTML 태그를 생성해야 합니다. 다음은 이러한 값을 문자열이 아닌 부울 데이터 유형으로 기록하는 방법의 예시입니다:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

자세한 내용은 [Google에 오디언스 동기화]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/)를 참조하세요.

## 초기화 태그 템플릿 {#initialization-tag}

초기화 태그를 사용하여 웹사이트에 Braze 웹 SDK를 추가합니다.

### 1단계: 푸시 설정(선택 사항)

선택적으로 Google Tag Manager를 통해 푸시를 보낼 수 있도록 하려면 먼저 [푸시 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/) 지침에 따라 다음을 수행합니다.
1. 사이트의 서비스 종사자를 사이트의 루트 디토리에 배치하여 구성
2. 브라우저 등록 설정 - 서비스 종사자가 구성된 후에는 해당 앱에서 기본적으로 또는 커스텀 HTML 태그를 통해(GTM 대시보드 사용) `braze.requestPushPermission()` 메서드를 설정해야 합니다. 또한 SDK가 초기화된 후 태그가 실행되는지 확인해야 합니다.

### 2단계: 초기화 태그 선택

커뮤니티 템플릿 갤러리에서 Braze를 검색하고 **Braze 초기화 태그**를 선택합니다.

![Braze 초기화 태그 구성 설정을 보여주는 대화 상자. 포함된 설정은 "태그 유형", "API 키", "API 엔드포인트", "SDK 버전", "외부 사용자 ID" 및 "Safari 웹 푸시 ID"입니다.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### 3단계: 설정 구성

대시보드의 **설정 관리** 페이지에서 찾을 수 있는 Braze API 앱 식별자 키와 SDK 엔드포인트를 입력합니다. 웹 SDK의 최신 버전( `major.minor` )을 입력합니다. 예를 들어 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. SDK 버전 목록은 [변경 로그에서](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) 확인할 수 있습니다.

### 4단계: 초기화 옵션 선택

초기 설정]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) 가이드)에 설명된 추가 초기화 옵션 중에서 선택합니다.

### 5단계: 검증 및 QA

이 태그를 배포한 후에는 두 가지 방법으로 제대로 통합되었는지 확인할 수 있습니다.

1. Google 태그 관리자의 [디버깅 도구를](https://support.google.com/tagmanager/answer/6107056?hl=en) 사용하면 구성된 페이지 또는 이벤트에서 Braze 초기화 태그가 트리거된 것을 확인할 수 있습니다.
2. 이제 Braze에 대한 네트워크 요청이 표시되어야 하며, 글로벌 `window.braze` 라이브러리가 웹 페이지에 정의되어 있어야 합니다.

## 작업 태그 템플릿 {#actions-tag}

Braze 액션 태그 템플릿을 사용하면 사용자 지정 이벤트를 트리거하고, 구매를 추적하고, 사용자 ID를 변경하고, 개인정보 보호 요건에 따라 추적을 중지하거나 재개할 수 있습니다.

![]({% image_buster /assets/img/web-gtm/gtm-actions-tag.png %})

### 사용자 외부 ID 변경 {#external-id}

**사용자 변경** 태그 유형은 [`changeUser` 메서드](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)를 호출합니다. 

사용자가 로그인하거나 고유한 `external_id` 식별자로 식별될 때마다 이 태그를 사용합니다.

일반적으로 웹사이트에서 전송한 데이터 레이어 변수를 사용하여 채워지는 **외부 사용자 ID** 필드에 현재 사용자의 고유 ID를 입력해야 합니다.

![Braze 작업 태그 구성 설정을 보여주는 대화상자. 포함된 설정은 '태그 유형'과 '외부 사용자 ID'입니다.]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})

### 커스텀 이벤트 기록 {#custom-events}

**커스텀 이벤트** 태그 유형은 [`logCustomEvent` 메서드](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)를 호출합니다.

이 태그를 사용하여 선택적으로 커스텀 이벤트 속성정보를 포함한 커스텀 이벤트를 Braze에 전송합니다.

변수를 사용하거나 이벤트 이름을 입력하여 이벤트 **이름**을 입력합니다.

**행 추가** 버튼을 사용하여 이벤트 속성을 추가합니다.

![Braze 작업 태그 구성 설정을 보여주는 대화상자. 포함된 설정은 '태그 유형'(사용자 지정 이벤트), '이벤트 이름'(버튼 클릭), '이벤트 속성'입니다.]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})

### 전자 상거래 이벤트 {#ecommerce}

사이트에서 표준 [전자상거래 이벤트](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) 데이터 레이어 항목을 사용하여 Google 태그 매니저에 구매를 기록하는 경우 **전자상거래 구매** 태그 유형을 사용할 수 있습니다. 이 작업 유형은 `items`의 목록에 전송된 각 항목에 대한 별도의 '구매'를 Braze에 기록합니다.

구매 속성정보 목록에서 키를 지정하여 구매 속성정보로 포함할 추가 속성정보 이름을 지정할 수도 있습니다. Braze는 목록에 추가하는 모든 구매 자산에 대해 기록 중인 개별 `item` 내에서 확인합니다.

예를 들어, 이커머스 페이로드에 다음 `items`가 포함되어 있다고 가정합니다.

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

`item_brand` 및 `item_name`만 구매 속성정보로 전달하려면 구매 속성정보 테이블에 이 두 필드를 추가하면 됩니다. 속성을 제공하지 않으면 구매 속성이 전송되지 않습니다. [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) 호출로 전송되지 않습니다.

### 구매 추적 {#purchases}

**구매** 태그 유형은 [`logPurchase` 메서드](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)를 호출합니다.

이 태그를 사용하여 선택적으로 구매 속성정보를 포함한 Braze에 대한 구매를 추적합니다.

**제품 ID** 및 **가격** 필드는 필수 입력 사항입니다.

**행 추가** 버튼을 사용하여 구매 속성을 추가합니다.

![Braze 작업 태그 구성 설정을 보여주는 대화상자. 포함된 설정은 '태그 유형', '외부 ID', '가격', '통화 코드', '수량', '구매 속성' 등입니다.]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})

### 추적 중지 및 재개 {#stop-tracking}

예를 들어 사용자가 개인정보 보호를 위해 웹 추적을 사용하지 않겠다고 표시한 후 웹사이트에서 Braze 추적을 비활성화하거나 다시 활성화해야 하는 경우가 있습니다.

**추적 비활성화** 또는 **추적 재개** 태그 유형을 사용하여 각각 웹 추적을 비활성화하거나 다시 활성화합니다. 이 두 가지 옵션은 [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) 및 [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)를 호출합니다.

### 사용자 지정 사용자 속성 {#custom-attributes}

Google 태그 관리자의 스크립팅 언어 제한으로 인해 사용자 지정 사용자 속성을 사용할 수 없습니다. 사용자 지정 속성을 기록하려면 다음 내용으로 사용자 지정 HTML 태그를 만듭니다:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTM 템플릿은 이벤트 또는 구매에 중첩된 속성을 지원하지 않습니다. 앞의 HTML을 사용하여 중첩된 속성이 필요한 이벤트 또는 구매를 기록할 수 있습니다.
{% endalert %}

### 표준 사용자 속성 {#standard-attributes}

사용자의 이름과 같은 표준 사용자 속성은 커스텀 사용자 속성과 동일한 방식으로 기록해야 합니다. 표준 속성으로 전달하는 값이 [사용자 클래스](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 문서에 지정된 예상 형식과 일치하는지 확인합니다.

예를 들어 성별 속성은 다음 중 하나를 값으로 사용할 수 있습니다. `"m" | "f" | "o" | "u" | "n" | "p"`. 따라서 사용자의 성별을 여성으로 설정하려면 다음 내용으로 사용자 지정 HTML 태그를 만드세요:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## 콘텐츠 카드 통합

Google 태그 관리자를 사용하여 [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) 메시징 채널을 통합하는 몇 가지 추가 단계가 있습니다. Google 태그 매니저는 웹사이트 코드에 [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (웹 SDK 버전)을 직접 삽입하는 방식으로 작동하므로 콘텐츠 카드를 구현할 때를 제외하고는 Google 태그 매니저 없이 SDK를 통합한 것처럼 모든 SDK 방법을 사용할 수 있습니다.

### 옵션 1: GTM을 사용하여 통합

콘텐츠 카드 피드의 표준 통합을 위해 Google 태그 관리자에서 **사용자 정의 HTML** 태그를 사용할 수 있습니다. 표준 콘텐츠 카드 피드를 활성화하는 사용자 정의 HTML 태그에 다음을 추가합니다:

```html
<script>
   window.braze.showContentCards();
</script>
```

![콘텐츠 카드 피드를 표시하는 사용자 지정 HTML 태그의 Google 태그 관리자에서 태그 구성]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})

### 옵션 2: 웹사이트에 직접 통합

콘텐츠 카드의 모양과 피드를 보다 자유롭게 사용자 지정하려는 경우 콘텐츠 카드를 기본 웹사이트에 직접 통합할 수 있습니다. 표준 피드 UI를 사용하거나 커스텀 피드 UI를 생성하는 두 가지 접근 방식이 있습니다.

#### 표준 피드

[표준 피드 UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui)를 구현할 때 Braze 메서드는 메서드 시작 부분에 `window.`를 추가해야 합니다. 예를 들어 `braze.showContentCards`는 `window.braze.showContentCards`가 되어야 합니다.

#### 사용자 지정 피드 UI

[커스텀 피드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling) 스타일의 경우, 단계는 GTM 없이 SDK를 통합한 경우와 동일합니다. 예를 들어 콘텐츠 카드 피드의 너비를 사용자 지정하려면 다음을 CSS 파일에 붙여넣으면 됩니다:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## 템플릿 업그레이드 및 업데이트 {#upgrading}

Braze 웹 SDK의 최신 버전으로 업그레이드하려면Google Tag Manager 대시보드에서 다음 세 단계를 수행합니다.

1. **태그 템플릿 업데이트**<br>워크스페이스 내의 **템플릿** 페이지로 이동합니다. 여기에 업데이트를 사용할 수 있음을 나타내는 아이콘이 표시됩니다.<br><br>![업데이트를 보여주는 템플릿 페이지]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>해당 아이콘을 클릭하고 변경 사항을 검토한 후 **업데이트 수락**을 클릭합니다.<br><br>!['업데이트 수락' 버튼이 있는 이전 태그 템플릿과 새 태그 템플릿을 비교하는 화면]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **업데이트 버전 번호**<br>태그 템플릿이 업데이트되면 Braze 초기화 태그를 편집하고 SDK 버전을 최신 `major.minor` 버전으로 업데이트합니다. 예를 들어 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. SDK 버전 목록은 [변경 로그에서](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) 확인할 수 있습니다.<br><br>![SDK 버전 변경을 위한 입력 필드가 있는 Braze 초기화 템플릿]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA 및 게시**<br>태그 컨테이너에 업데이트를 게시하기 전에 Google 태그 관리자의 [디버깅 도구를](https://support.google.com/tagmanager/answer/6107056?hl=en) 사용하여 새 SDK 버전이 작동하는지 확인합니다.

## 문제 해결 단계 {#troubleshooting}

### 태그 디버깅 사용 {#debugging}

각 Braze 태그 템플릿에는 웹 페이지의 JavaScript 콘솔에 디버그 메시지를 기록하는 데 사용할 수 있는 **GTM 태그 디버깅** 체크박스(선택 사항)가 있습니다.

![Google 태그 관리자의 디버그 도구]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

### 디버그 모드로 전환

Google 태그 관리자 연동 디버깅에 도움이 되는 또 다른 방법은 Google의 [미리보기 모드](https://support.google.com/tagmanager/answer/6107056) 기능을 사용하는 것입니다.

이렇게 하면 웹 페이지의 데이터 레이어에서 트리거된 각 Braze 태그로 전송되는 값을 식별하는 데 도움이 되며, 어떤 태그가 트리거되었는지 또는 트리거되지 않았는지도 설명할 수 있습니다.

![Braze 초기화 태그 요약 페이지에서는 트리거된 태그에 대한 정보를 포함하여 태그에 대한 개요를 확인할 수 있습니다.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

### 상세 로깅 활성화

테스트하는 동안 Braze 기술 지원팀이 로그에 액세스할 수 있도록 하려면 Google Tag Manager 통합에서 상세 로깅을 활성화하면 됩니다. 이러한 로그는 브라우저 [개발자 도구의](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) **콘솔** 탭에 표시됩니다.

Google Tag Manager 통합에서 Braze 초기화 태그로 이동하고 **웹 SDK 로깅 활성화**를 선택합니다.

![웹 SDK 로깅 활성화 옵션이 켜져 있는 Braze 초기화 태그 요약 페이지.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
