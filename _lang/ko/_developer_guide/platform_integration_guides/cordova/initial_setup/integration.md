---
nav_title: 통합
article_title: Cordova Braze SDK 통합
page_order: 0
---

# Cordova Braze SDK 통합

> Cordova Braze SDK를 iOS 또는 Android 앱에 통합하는 방법을 알아보세요. 완료한 후에는 [SDK를 추가로 사용자 지정]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/)할 수 있습니다.

## SDK 통합

### 1단계: 프로젝트에 SDK 추가

Cordova 6 이상을 사용하는 경우 GitHub에서 직접 SDK를 추가할 수 있습니다. 또는 [GitHub 리포지토리](https://github.com/braze-inc/braze-cordova-sdk)의 ZIP 파일을 다운로드하여 SDK를 수동으로 추가할 수도 있습니다.

{% tabs local %}
{% tab 지오펜스 비활성화됨 %}
위치 수집 및 지오펜스를 사용하지 않는다면 GitHub의 `master` 브랜치를 사용합니다.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab 지오펜스 활성화됨 %}
위치 수집 및 지오펜스를 사용하려면 GitHub의 `geofence-branch`를 사용합니다.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
1단계를 반복하여 언제든지 `master` 및 `geofence-branch` 사이를 전환할 수 있습니다.
{% endalert %}

### 2단계: 프로젝트 구성

다음으로 프로젝트의 `config.xml` 파일에 있는 `platform` 요소에 다음 환경설정을 추가합니다.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

다음을 교체합니다:

| 값                 | 설명                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_KEY`       | [Braze REST API 키입니다]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | 사용자 지정 API 엔드포인트. 이 엔드포인트는 Braze 대시보드의 올바른 앱 그룹으로 Braze 인스턴스 데이터를 라우팅하는 데 사용됩니다. |

`config.xml` 파일의 `platform` 요소는 다음과 유사해야 합니다:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## 자동 세션 추적 비활성화하기(Android만 해당)

기본적으로 Android Cordova 플러그인은 세션을 자동으로 추적합니다. 자동 세션 추적을 사용하지 않으려면 프로젝트의 `config.xml` 파일에 있는 `platform` 요소에 다음 환경 설정을 추가하세요:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

세션 추적을 다시 시작하려면 `BrazePlugin.startSessionTracking()` 으로 전화하세요. 다음 `Activity.onStart()` 이후에 시작된 세션만 추적됩니다.
