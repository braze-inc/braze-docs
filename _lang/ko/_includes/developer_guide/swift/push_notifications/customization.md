{% multi_lang_include developer_guide/prerequisites/swift.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 합니다.

## 동작 버튼 사용자 지정 {#push-action-buttons-integration}

Braze Swift SDK는 푸시 액션 버튼에 대한 URL 처리 지원을 제공합니다. Braze 기본 푸시 카테고리에는 네 가지 기본 푸시 실행 버튼 세트(`Accept/Decline`, `Yes/No`, `Confirm/Cancel`, `More`)가 있습니다.

![푸시 메시지를 아래로 당겨서 두 개의 사용자 지정 가능한 작업 버튼을 표시하는 GIF.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### 수동으로 작업 버튼 등록하기

{% alert important %}
푸시 동작 버튼을 수동으로 등록하는 것은 권장하지 않습니다.
{% endalert %}

`configuration.push.automation` 구성 옵션을 사용하여 [푸시 알림을 설정하면]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) Braze는 기본 푸시 카테고리에 대한 액션 버튼을 자동으로 등록하고 푸시 액션 버튼 클릭 분석 및 URL 라우팅을 처리합니다.

그러나 대신 푸시 동작 버튼을 수동으로 등록하도록 선택할 수 있습니다.

#### 1단계: Braze 기본 푸시 카테고리 추가하기 {#registering}

[푸시 등록]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) 시 다음 코드를 사용하여 기본 푸시 카테고리에 등록하세요:

{% tabs %}
{% tab swift %}
a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
백그라운드 활성화 모드에서 푸시 동작 버튼을 클릭하면 알림만 해제되고 앱은 열리지 않습니다. 다음에 사용자가 앱을 열면 이 작업에 대한 버튼 클릭 분석이 서버로 플러시됩니다.
{% endalert %}

#### 2단계: 대화형 푸시 처리 활성화 {#enable-push-handling}

클릭 분석 및 URL 라우팅을 포함한 푸시 액션 버튼 처리를 활성화하려면 앱의 `didReceive(_:completionHandler:)` 델리게이트 메서드에 다음 코드를 추가하세요:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

`UNNotification` 프레임워크를 사용하고 Braze [알림 방법을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) 구현한 경우 이 방법이 이미 통합되어 있을 것입니다. 

## 푸시 카테고리 사용자 지정 {#customizing-push-categories}

Braze는 기본 푸시 카테고리 세트를 제공할 뿐만 아니라 커스텀 알림 카테고리 및 작업을 지원합니다. 애플리케이션에 카테고리를 등록한 후 Braze 대시보드를 사용하여 이러한 사용자 지정 알림 카테고리를 사용자에게 보낼 수 있습니다.

다음은 기기에 표시되는 `LIKE_CATEGORY`를 활용하는 예제입니다.

!['싫어요' 및 '좋아요' 푸시 동작 버튼 두 개를 표시하는 푸시 메시지]({% image_buster /assets/img_archive/push_example_category.png %})

### 1단계: 카테고리 등록

앱에 카테고리를 등록하려면 다음과 유사한 방법을 사용합니다:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
`UNNotificationAction`을 생성할 때 작업 옵션 목록을 지정할 수 있습니다. 예를 들어 `UNNotificationActionOptions.foreground`는 사용자가 실행 버튼을 탭한 후 앱을 열도록 합니다. '앱 열기' 및 '애플리케이션으로 딥 링크'와 같은 탐색 관련 클릭 시 동작에 필요합니다. 자세한 내용은 [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions)를 참조하세요.
{% endalert %}

### 2단계: 카테고리 선택

카테고리를 등록한 후 Braze 대시보드를 사용하여 해당 유형의 알림을 사용자에게 발송합니다.

{% alert tip %}
앱으로 딥링킹하거나 URL을 여는 등 _특별한 동작이_ 있는 액션 버튼에 대해서만 사용자 지정 알림 카테고리를 정의하면 됩니다. 알림을 해제하기만 하는 실행 버튼에 대해서는 정의할 필요가 없습니다.
{% endalert %}

1. Braze 대시보드에서 **메시징** > **푸시 알림**을 선택한 다음, iOS [푸시 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)을 선택합니다.
2. **푸시 알림 작성에서** **작업 버튼을** 켭니다.
3. **iOS 알림 카테고리** 드롭다운에서 **미리 등록한 커스텀 iOS 카테고리 입력**을 선택합니다.
4. 마지막으로 앞서 만든 카테고리 중 하나를 입력합니다. 다음 예에서는 사용자 지정 카테고리를 사용합니다: `LIKE_CATEGORY`.

![사용자 지정 카테고리를 설정할 수 있는 푸시 알림 캠페인 대시보드]({% image_buster /assets/img_archive/ios-notification-category.png %})

## 배지 사용자 지정

배지는 사용자의 관심을 끌기에 적합한 작은 아이콘입니다. 배지 개수를 지정할 수 있습니다. [**설정**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) 탭에서 브레이즈 대시보드를 사용하여 푸시 알림을 작성할 때 배지 개수를 지정할 수 있습니다. 애플리케이션의 [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) 속성정보 또는 [원격 알림 페이로드](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1)를 통해 배지 수를 수동으로 업데이트할 수도 있습니다. 

Braze는 앱이 포그라운드에 있는 상태에서 Braze 알림을 받으면 배지 수를 자동으로 지웁니다. 배지 수를 0으로 설정하면 알림 센터의 알림도 지워집니다. 

정상적인 앱 작동의 일부로 배지를 지우거나 배지를 지우는 푸시를 전송하여 배지를 지우려는 계획이 없는 경우 앱의 `applicationDidBecomeActive:` 위임 메서드에 다음 코드를 추가하여 앱이 활성화되면 배지를 지워야 합니다.

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## 사운드 사용자 지정

### 1단계: 앱에서 사운드 호스팅

사용자 지정 푸시 알림 사운드는 앱의 기본 번들 내에서 로컬로 호스팅해야 합니다. 허용되는 오디오 데이터 형식은 다음과 같습니다:

- 선형 PCM
- MA4
- µLaw
- aLaw

오디오 데이터를 AIFF, WAV 또는 CAF 파일로 패키징할 수 있습니다. Xcode에서 사운드 파일을 프로젝트에 애플리케이션 번들의 지역화되지 않은 리소스로 추가합니다.

{% alert note %}
사용자 지정 사운드는 재생 시 30초 미만이어야 합니다. 커스텀 사운드가 이 제한을 초과하면 기본 시스템 사운드가 대신 재생됩니다.
{% endalert %}

#### 사운드 파일 변환

afconvert 도구를 사용하여 사운드를 변환할 수 있습니다. 예를 들어 16비트 선형 PCM 시스템 사운드 Submarine.aiff를 CAF 파일에서 IMA4 오디오로 변환하려면 터미널에서 다음 명령을 사용합니다.

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
QuickTime Player에서 사운드를 열고 **동영상** 메뉴에서 **동영상 검사기 표시를** 선택하면 사운드를 검사하여 데이터 형식을 확인할 수 있습니다.
{% endalert %}

### 2단계: 사운드에 대한 프로토콜 URL 제공

앱에서 사운드 파일의 위치로 연결되는 프로토콜 URL을 지정해야 합니다. 이를 수행하는 방법에는 두 가지가 있습니다:

* [Apple 푸시 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object)의 `sound` 매개변수를 사용하여 URL을 Braze에 전달합니다.
* 대시보드에서 URL을 지정합니다. [푸시 작성기]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android)에서 **설정**을 선택하고 **사운드** 필드에 프로토콜 URL을 입력합니다. 

![Braze 대시보드의 푸시 작성기]({% image_buster /assets/img_archive/sound_push_ios.png %})

지정한 사운드 파일이 존재하지 않거나 'default' 키워드가 입력된 경우 Braze는 기기의 기본 알림 사운드를 사용합니다. 대시보드 외에도 [메시징 API][12]를 통해 사운드를 구성할 수도 있습니다.

자세한 내용은 [사용자 지정 경고음 준비에](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) 관한 Apple 개발자 문서를 참조하세요.

## 설정

대시보드를 통해 푸시 캠페인을 만들 때 **작성** 단계의 **설정** 탭을 클릭하면 사용 가능한 고급 설정을 볼 수 있습니다.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### 키-값 쌍

Braze에서는 커스텀 정의 문자열 키-값 페어(`extras`)를 푸시 알림과 함께 애플리케이션에 전송할 수 있습니다. 추가 항목은 대시보드 또는 API를 통해 정의할 수 있으며, 푸시 위임 구현에 전달되는 `notification` 사전 내에서 키-값 페어로 사용할 수 있습니다.

### 경고 옵션

**경고 옵션** 확인란을 선택하여 알림이 기기에 표시되는 방식을 조정할 수 있는 키-값 드롭다운을 확인합니다.

### 콘텐츠 가용 플래그 추가

**콘텐츠 가용 플래그 추가** 확인란을 선택하여 기기가 백그라운드에서 새 콘텐츠를 다운로드하도록 지시합니다. 가장 일반적으로 [무음 알림을]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) 보내고 싶은 경우 이 옵션을 선택할 수 있습니다.

### 변경 가능한 콘텐츠 플래그 추가

고급 수신기 사용자 지정을 사용하려면 **변경 가능한 콘텐츠 플래그 추가** 확인란을 선택합니다. 이 플래그는 이 확인란의 값에 관계없이 [리치 알림을]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift) 작성할 때 자동으로 전송됩니다.

### 접기 ID

축소 ID를 지정하여 유사한 알림을 결합합니다. 동일한 축소 ID로 여러 알림을 발송한 경우, 기기에는 가장 최근 수신된 알림만 표시됩니다. [통합 알림에](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) 대한 Apple의 문서를 참조하세요.

### 만료 

**만료** 확인란을 선택하면 메시지의 만료 시간을 설정할 수 있습니다. 사용자 기기와 연결이 끊어지면 Braze는 지정된 시간까지 계속해서 메시지 발송을 시도합니다. 이 옵션을 설정하지 않으면 플랫폼은 기본적으로 30일 만료로 설정됩니다. 배달 전에 만료되는 푸시 알림은 실패로 간주되지 않으며 반송으로 기록되지 않습니다.
