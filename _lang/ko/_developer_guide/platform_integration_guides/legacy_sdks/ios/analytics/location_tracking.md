---
nav_title: 위치 추적
article_title: iOS용 위치 추적
platform: iOS
page_order: 6
description: "이 문서에서는 iOS 애플리케이션의 위치 추적을 구성하는 방법을 설명합니다."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS용 위치 추적

기본값으로, Braze는 위치 추적을 비활성화합니다. 호스트 애플리케이션이 위치 추적을 옵트인하고 사용자로부터 권한을 얻은 후 위치 추적을 활성화합니다. 사용자가 위치 추적을 옵트인한 경우, Braze는 세션 시작 시 각 사용자에 대해 단일 위치를 기록합니다.

{% alert important %}
대략적인 위치 권한을 부여한 사용자에 대한 위치 추적이 iOS 14에서 안정적으로 작동하려면 SDK 버전을 `3.26.1` 이상으로 업데이트해야 합니다.
{% endalert %}

## 자동 위치 추적 활성화

Braze iOS SDK `v3.17.0`부터는 위치 추적이 기본적으로 비활성화되어 있습니다. `Info.plist` 파일을 사용하여 자동 위치 추적을 활성화할 수 있습니다. `Info.plist` 파일에 `Braze` 사전을 추가합니다. `Braze` 사전 내에서 `EnableAutomaticLocationCollection` 부울 하위 항목을 추가하고 값을 `YES`로 설정합니다. Braze iOS SDK v4.0.2 이전 버전에서는 `Braze` 대신 `Appboy`의 사전 키를 사용해야 합니다.

[`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) 메서드를 통해 앱 시작 시 자동 위치 추적을 활성화할 수도 있습니다. `appboyOptions` 사전에서 `ABKEnableAutomaticLocationCollectionKey` 을 `YES` 으로 설정합니다. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab 목표-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableAutomaticLocationCollectionKey : true ])
```

{% endtab %}
{% endtabs %}

### 위치 데이터를 Braze에 전달

다음 두 메서드를 사용하여 사용자의 마지막으로 알려진 위치를 수동으로 설정할 수 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy];

```

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy
                                                      altitude:altitude
                                              verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy)
```

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy, altitude: altitude, verticalAccuracy: verticalAccuracy)
```

{% endtab %}
{% endtabs %}

자세한 내용은 [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKUser.h)을 참조하십시오.

