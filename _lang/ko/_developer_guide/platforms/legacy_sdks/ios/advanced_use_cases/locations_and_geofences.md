---
nav_title: 위치 및 지오펜스
article_title: iOS용 위치 및 지오펜스
platform: iOS
page_order: 6
description: "이 참조 문서에서는 iOS 애플리케이션에서 위치 및 지오펜스를 구현하는 방법에 대해 설명합니다."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 위치 및 지오펜스

iOS용 지오펜스를 지원하기 위한 조건:

1. 통합은 백그라운드 푸시 알림을 지원해야 합니다.
2. Braze 지오펜스는 SDK를 통해 위치 수집을 활성화하여 암시적으로 또는 지오펜스 수집을 활성화하여 명시적으로 [활성화해야 합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/#enabling-automatic-location-tracking). 기본적으로 활성화되어 있지 않습니다.

{% alert important %}
iOS 14부터 지오펜스는 대략적인 위치 권한을 제공하는 사용자의 경우 안정적으로 작동하지 않습니다.
{% endalert %}

## 1단계: 백그라운드 푸시 사용

지오펜스 동기화 전략을 완전히 사용하려면 표준 푸시 통합을 완료하는 것 외에도 [백그라운드 푸시를]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work) 사용하도록 설정해야 합니다.

## 2단계: 지오펜스 활성화

기본적으로 지오펜스는 자동 위치 수집의 활성화 여부에 따라 활성화됩니다. `Info.plist` 파일을 사용하여 지오펜스를 활성화할 수 있습니다. `Info.plist` 파일에 `Braze` 사전을 추가합니다. `Braze` 사전 내에서 `EnableGeofences` 부울 하위 항목을 추가하고 값을 `YES`로 설정합니다. Braze iOS SDK v4.0.2 이전 버전에서는 `Braze` 대신 `Appboy`의 사전 키를 사용해야 합니다.

앱 시작 시 지오펜스를 사용하도록 설정할 수도 있습니다. [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) 메서드를 사용하여 지오펜스를 활성화할 수도 있습니다. `appboyOptions` 사전에서 `ABKEnableGeofencesKey` 을 `YES` 으로 설정합니다. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## 3단계: Braze 백그라운드 푸시 확인

Braze는 백그라운드 푸시 알림을 사용하여 지오펜스를 기기와 동기화합니다. 애플리케이션이 Braze 지오펜스 동기화 알림을 수신할 때 원치 않는 조치를 취하지 않도록 하려면 [iOS 사용자 지정]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/) 문서를 참조하세요.

## 4단계: NSLocationAlwaysUsageDescription을 추가하십시오. Info.plist

`NSLocationAlwaysUsageDescription` 및 `NSLocationAlwaysAndWhenInUseUsageDescription` 키를 `String` 값으로 `info.plist`에 추가합니다. 이 값에는 애플리케이션에서 위치를 추적해야 하는 이유에 대한 설명이 포함되어 있습니다. iOS 11 이상에서는 두 키가 모두 필요합니다.
이 설명은 시스템 위치 프롬프트가 승인을 요청할 때 표시되며, 사용자에게 위치 추적의 이점을 명확하게 설명해야 합니다.

## 5단계: 사용자로부터 권한 부여 요청

지오펜스 기능은 `Always` 위치 권한이 부여된 상태에서만 작동합니다.

`Always` 위치 인증을 요청하려면 다음 코드를 사용하세요:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## 6단계: 대시보드에서 지오펜스 활성화

iOS에서는 특정 앱에 대해 최대 20개의 지오펜스만 저장하도록 허용합니다. 위치를 사용하면 사용 가능한 지오펜스 슬롯 20개 중 일부가 소진됩니다. 앱의 다른 지오펜스 관련 기능이 실수로 또는 원치 않게 중단되는 것을 방지하려면 대시보드에서 개별 앱에 대해 위치 지오펜스를 활성화해야 합니다.

위치가 올바르게 작동하려면 앱이 사용 가능한 모든 지오펜스 지점을 사용하고 있지 않은지도 확인해야 합니다.

### 위치 페이지에서 지오펜스를 활성화합니다.

![Braze 위치 페이지의 지오펜스 옵션]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### 설정 페이지에서 지오펜스를 활성화합니다.

![지오펜스 확인란은 Braze 설정 페이지에 있습니다.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## 자동 지오펜스 요청 비활성화하기

iOS SDK 버전 3.21.3부터 지오펜스의 자동 요청을 비활성화할 수 있습니다. `Info.plist` 파일을 사용하여 이 작업을 수행할 수 있습니다. `Info.plist` 파일에 `Braze` 사전을 추가합니다. `Braze` 사전 내에서 `DisableAutomaticGeofenceRequests` 부울 하위 항목을 추가하고 값을 `YES`로 설정합니다.

앱 시작 시 [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) 메서드를 통해 자동 지오펜스 요청을 비활성화할 수도 있습니다. `appboyOptions` 사전에서 `ABKDisableAutomaticGeofenceRequestsKey` 을 `YES` 으로 설정합니다. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

이 옵션을 사용하려는 경우 기능이 작동하도록 지오펜스를 수동으로 요청해야 합니다.

## 지오펜스 수동 요청

Braze SDK가 백엔드에서 모니터링하도록 지오펜스를 요청하면 사용자의 현재 위치를 보고하고 보고된 위치를 기반으로 최적의 관련성이 있는 것으로 판단되는 지오펜스를 수신합니다. 지오펜스 새로 고침 사용량 제한은 세션당 한 번입니다.

가장 관련성이 높은 지오펜스를 수신하기 위해 SDK가 보고하는 위치를 제어하도록 iOS SDK 버전 3.21.3부터 위치의 위도와 경도를 제공하여 지오펜스를 수동으로 요청할 수 있습니다. 이 방법을 사용할 때는 자동 지오펜스 요청을 비활성화하는 것이 좋습니다. 이렇게 하려면 다음 코드를 사용하세요:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}


