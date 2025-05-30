---
nav_title: 콘텐츠 보안 정책 헤더
article_title: 웹을 위한 콘텐츠 보안 정책 헤더
platform: Web
page_order: 21
page_type: reference
description: "이 문서에서는 Braze 웹 SDK에 필요한 콘텐츠 보안 정책 헤더를 다룹니다."

---

# 콘텐츠 보안 정책 헤더

> Content-Security-Policy는 콘텐츠가 웹사이트에 로드되는 방식과 위치를 제한하여 추가 보안을 제공합니다. 이 참조 문서에서는 웹 SDK에 필요한 콘텐츠 보안 정책 헤더를 다룹니다.

{% alert important %}
이 문서는 CSP 규칙을 적용하고 Braze와 통합하는 웹사이트에서 작업하는 개발자를 대상으로 합니다. 보안 접근 방식에 대한 조언으로 의도된 것은 아닙니다.
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Nonce 속성 {#nonce}

`nonce` 값을 `script-src` 또는 `style-src` 지시문에서 사용하는 경우 해당 값을 `contentSecurityNonce` 초기화 옵션에 전달하여 SDK에서 생성하는 새로 만든 스크립트 및 스타일에 전파합니다.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## 지시 사항 {#directives}

### `connect-src`{#connect-src}

{% alert warning %}
URL은 선택한 `baseUrl` 초기화 옵션의 [API SDK 엔드포인트와]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) 일치해야 합니다.
{% endalert %}

|URL|정보|
|---|-----------|
|`connect-src https://sdk.iad-01.braze.com`|SDK가 Braze API와 통신할 수 있도록 허용합니다. 선택한 `baseUrl` 초기화 옵션의 [API SDK 엔드포인트와]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) 일치하도록 이 URL을 변경합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### `script-src`{#script-src}

|URL|정보|
|---|-----------|
|`script-src https://js.appboycdn.com`|CDN 호스팅 통합을 사용할 때 필요합니다.|
|`script-src 'unsafe-eval'`|`appboyQueue` 에 대한 참조가 포함된 통합 코드 조각을 사용할 때 필요합니다. 이 지시어를 사용하지 않으려면 대신 [NPM을 사용하여 SDK를 통합하세요]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=package%20manager).|
|`script-src 'nonce-...'`<br>또는<br>`script-src 'unsafe-inline'`|사용자 지정 HTML과 같은 특정 인앱 메시지에 필요합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### `img-src`{#img-src}

|URL|정보|
|---|-----------|
|`img-src: appboy-images.com braze-images.com cdn.braze.eu`|Braze CDN 호스팅 이미지를 사용할 때 필요합니다. 호스트 이름은 대시보드 클러스터에 따라 다를 수 있습니다.<br><br>**중요 사항:** 사용자 정의 글꼴을 사용하는 경우 `font-src` 도 포함해야 합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Font Awesome {#font-awesome}

자동으로 Font Awesome을 포함하지 않으려면 `doNotLoadFontAwesome` 초기화 옵션을 사용하십시오:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Font Awesome을 사용하기로 선택한 경우 다음 CSP 지침이 필요합니다:

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` 또는 `style-src 'unsafe-inline'`
