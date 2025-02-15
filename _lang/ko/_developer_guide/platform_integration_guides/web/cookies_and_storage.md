---
nav_title: 쿠키 및 저장소
article_title: 웹용 쿠키 및 저장소
platform: Web
page_order: 15
page_type: reference
description: "이 참조 문서에서는 Braze 웹 SDK에서 사용하는 다양한 쿠키에 대해 설명합니다."

---

# 쿠키 및 저장

> 이 문서에서는 Braze 웹 SDK에서 사용하는 다양한 쿠키에 대해 설명합니다.

계속 읽기 전에 웹사이트가 SDK를 [초기화](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)할 때까지 Braze 웹 SDK는 브라우저에 쿠키 등의 데이터를 저장하지 않는다는 점에 유의하세요.

또한 이러한 값은 변경될 수 있으며 통합을 통해 직접 액세스해서는 안 됩니다. 대신 공개 API 인터페이스에 대한 [JavaScript 설명서를](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) 참조하세요.

{% multi_lang_include archive/web-v4-rename.md %}

## 쿠키 {#cookies}

이 섹션에서는 Braze 웹 SDK에서 쿠키를 설정하고 관리하는 방법에 대한 정보를 제공합니다. Braze 웹 SDK는 유연성, 법률 준수 및 메시징 관련성을 극대화할 수 있도록 빌드되었습니다.

Braze가 쿠키를 생성하면 400일 만료로 저장되며, 새 세션에서 자동으로 갱신됩니다.

### 쿠키 비활성화하기 {#disable-cookies}

모든 쿠키를 비활성화하려면 웹 SDK를 초기화할 때 [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) 옵션을 사용합니다.
쿠키를 비활성화하면 하위 도메인 사이에서 이동하는 익명 사용자를 연결할 수 없으며 각 하위 도메인에 새로운 사용자가 생성됩니다.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

일반적으로 Braze 추적을 중지하거나 저장된 브라우저 데이터를 모두 지우려면 [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) 및 [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata) SDK 메서드를 각각 참조하세요. 이 두 가지 메서드는 사용자가 동의를 철회하거나 SDK가 이미 초기화된 후 모든 Braze 기능을 중지하려는 경우에 유용할 수 있습니다.

### 쿠키 목록

|쿠키|설명|크기|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|현재 로그인한 사용자의 변경 여부를 확인하고 이벤트를 현재 사용자와 연결하는 데 사용됩니다.|`changeUser`에 전달된 값의 크기에 기반|
|`ab.storage.sessionId.[your-api-key]`|사용자가 메시지를 동기화하고 세션 분석을 계산하기 위해 새 세션을 시작하는지 기존 세션을 시작하는지 확인하는 데 사용되는 무작위로 생성된 문자열입니다.|~200바이트|
|`ab.storage.deviceId.[your-api-key]`|익명 사용자를 식별하고 사용자 기기를 구분하기 위해 무작위로 생성된 문자열로, 기기 기반 메시징을 활성화합니다.|~200바이트|
|`ab.optOut`|`disableSDK` 호출 시 사용자의 옵트아웃 환경설정을 저장하는 데 사용됩니다.|~40바이트|
|`ab._gd`|루트 수준 쿠키 도메인을 결정하기 위해 임시로 생성됩니다. 이를 통해 SDK가 하위 도메인에서 제대로 작동할 수 있습니다.|해당 없음|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 기기 속성정보

기본적으로 Braze는 기기, 언어, 시간대를 기반으로 메시지를 개인화할 수 있도록 다음과 같은 기기 수준 속성정보를 수집합니다.

* 브라우저
* BROWSER_VERSION
* 언어
* OS
* 해상도
* TIME_ZONE
* USER_AGENT

[`DeviceProperties`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html) 목록에 대한 `devicePropertyAllowlist` 초기화 옵션을 설정하여 수집하려는 속성정보를 지정하거나 비활성화할 수 있습니다. 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

기본적으로 모든 필드가 활성화되어 있습니다. 일부 속성이 없으면 모든 기능이 제대로 작동하지 않을 수 있습니다. 예를 들어, 현지 시간대 전달은 시간대가 없으면 작동하지 않습니다.

자동으로 수집된 기기 속성정보에 대한 자세한 내용은 [SDK 데이터 수집 옵션]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)을 참조하세요. 


