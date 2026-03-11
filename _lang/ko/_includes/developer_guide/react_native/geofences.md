{% alert important %}
지오펜스는 React Native SDK에서 **iOS와 Android** 모두에서 지원됩니다. `requestLocationInitialization` 메소드는 Android 전용이며 iOS에서는 필요하지 않습니다. `requestGeofences` 메소드는 두 플랫폼 모두에서 사용할 수 있습니다. 기본적으로 SDK는 위치가 사용 가능할 때 지오펜스를 자동으로 요청하고 모니터링할 수 있습니다. 이 자동 구성을 신뢰하거나 `requestGeofences`를 호출하여 수동으로 요청할 수 있습니다.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} Android에서는 지오펜스 동기화를 위해 [조용한 푸시 알림 설정]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)이 필요합니다.

## 지오펜스 설정 {#setting-up-geofences}

### 1단계: Braze에서 활성화

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### 2단계: 네이티브 Android 설정 완료

React Native SDK가 네이티브 Braze Android SDK를 사용하므로, 프로젝트에 대한 네이티브 Android 지오펜스 설정을 완료하십시오. 이 단계의 iOS에 해당하는 내용은 네이티브 Swift SDK 지오펜스 가이드([단계 2.2에서 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module))에 포함되어 있습니다. 단계 2.1(브레이즈 위치 모듈 추가)은 BrazeLocation이 Braze React Native SDK에 이미 암묵적으로 포함되어 있기 때문에 React Native에서는 필요하지 않습니다.

1. **업데이트 `build.gradle`:** `android-sdk-location` 및 Google Play 서비스 위치를 추가하십시오. [Android 지오펜스]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)를 참조하십시오.
2. **매니페스트 업데이트:** 위치 권한 및 Braze 부트 수신기를 추가하십시오. [Android 지오펜스]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)를 참조하십시오.
3. **Braze 위치 수집 활성화:** `braze.xml` 파일을 업데이트하십시오. [Android 지오펜스]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)를 참조하십시오.

### 3단계: 네이티브 iOS 설정 완료

React Native SDK는 네이티브 Braze iOS SDK를 사용하므로, 프로젝트에 대한 네이티브 iOS 지오펜스 설정을 완료하려면 2.2단계부터 시작하여 네이티브 Swift SDK 지침을 따르십시오: `Info.plist`에 위치 사용 설명을 업데이트하고(2.2단계), Braze 구성에서 지오펜스를 활성화하십시오 `automaticGeofenceRequests = true`(3단계); 선택적으로 백그라운드 보고를 활성화하십시오(3.1단계). 2.1단계(브레이즈 위치 모듈 추가)는 필요하지 않습니다. BrazeLocation은 이미 Braze React Native SDK에 암묵적으로 포함되어 있습니다. [iOS 지오펜스, 2.2단계에서 3.1단계까지]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)를 참조하십시오.

### 4단계: JavaScript에서 지오펜스 요청하기

**Android에서:** 사용자가 위치 권한을 부여한 후, `requestLocationInitialization()`를 호출하여 Braze 위치 기능을 초기화하고 Braze 서버에서 지오펜스를 요청하십시오. 이 메서드는 iOS에서 지원되지 않으며 iOS에 필요하지 않습니다.

**iOS에서:** 동등한 것은 네이티브 Swift 또는 Objective-C Braze 구성에서 `automaticGeofenceRequests` 구성을 활성화하는 것입니다(3단계 참조). 그것이 활성화되면, SDK는 위치가 사용 가능할 때 자동으로 지오펜스를 요청하고 모니터링합니다. `requestLocationInitialization`에 해당하는 JavaScript 호출은 필요하지 않습니다.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### 5단계: 지오펜스를 수동으로 요청하기(선택 사항)

iOS와 Android 모두에서, `requestGeofences`을 사용하여 특정 GPS 좌표에 대한 지오펜스 업데이트를 수동으로 요청할 수 있습니다. 기본적으로 Braze는 장치의 위치를 자동으로 검색하고 지오펜스를 요청합니다. 대신 좌표를 수동으로 제공하려면:

1. 자동 지오펜스 요청 비활성화. Android에서는 `com_braze_automatic_geofence_requests_enabled`을 `false`로 설정하십시오 `braze.xml`에서. iOS에서는 Braze 구성에서 `automaticGeofenceRequests`를 `false`로 설정하십시오.
2. 원하는 위도와 경도로 `requestGeofences`을 호출하십시오:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
지오펜스는 세션당 한 번만 요청할 수 있으며, SDK를 통해 자동으로 요청하거나 이 메서드를 사용하여 수동으로 요청할 수 있습니다.
{% endalert %}
