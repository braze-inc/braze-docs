{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 마지막으로 알려진 위치 설정

사용자의 마지막으로 알려진 위치를 수동으로 설정하려면 `setLastKnownLocation` 메서드를 사용하십시오. 이것은 Braze SDK 외부에서 위치 데이터를 수집하는 경우 유용합니다.

```javascript
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);
```

- Android에서는 `latitude` 및 `longitude`가 필요합니다. `altitude`, `horizontalAccuracy` 및 `verticalAccuracy`는 선택 사항입니다.
- iOS에서는 `latitude`, `longitude` 및 `horizontalAccuracy`이 필요합니다. `altitude` 및 `verticalAccuracy`는 선택 사항입니다.

크로스 플랫폼 호환성을 위해 최소한 `latitude`, `longitude` 및 `horizontalAccuracy`을 제공하십시오.

## 사용자 정의 위치 속성 설정

사용자 프로필에 사용자 정의 위치 속성을 설정하려면 `setLocationCustomAttribute` 메서드를 사용하십시오.

```javascript
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);
```

## 위치 초기화 요청 (Android 전용)

사용자가 위치 권한을 부여한 후 `requestLocationInitialization`을 호출하여 Android에서 Braze 위치 기능을 초기화하십시오. 이 메서드는 iOS에서 지원되지 않으며 iOS 지오펜스 또는 위치 기능에 필요하지 않습니다.

```javascript
Braze.requestLocationInitialization();
```

## 지오펜스

지오펜스는 iOS와 Android 모두에서 지원됩니다. 기본적으로 Braze SDK는 위치가 사용 가능할 때 지오펜스를 자동으로 요청하고 모니터링할 수 있습니다. 대부분의 통합에 대해 이 자동 구성을 신뢰할 수 있습니다.

### 지오펜스 수동 요청

특정 GPS 좌표에 대한 지오펜스 업데이트를 수동으로 요청하려면 `requestGeofences`을 사용하십시오. 이것은 iOS와 Android 모두에서 사용할 수 있습니다. 이 메서드를 사용하는 경우 SDK가 수동 요청을 덮어쓰지 않도록 기본 구성에서 자동 지오펜스 요청을 비활성화하십시오.

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
