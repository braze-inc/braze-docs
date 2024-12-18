---
nav_title: 리치 알림
article_title: iOS용 리치 푸시 알림
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 애플리케이션에서 리치 푸시 알림을 구현하는 방법에 대해 설명합니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS 10 리치 알림

iOS 10에서는 이미지, GIF 및 비디오를 포함하는 푸시 알림을 보낼 수 있는 기능이 도입되었습니다. 이 기능을 활성화하려면 클라이언트는 푸시 페이로드를 표시하기 전에 이를 수정할 수 있는 새로운 유형의 확장인 `Service Extension`을 생성해야 합니다.

## 서비스 확장 만들기

[`Notification Service Extension`](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension)을 생성하려면 Xcode에서 **파일 > 새로 만들기 > 대상**으로 이동하여 **알림 서비스 확장**을 선택합니다.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

**애플리케이션에 임베드**가 애플리케이션에 확장을 임베드하도록 설정되었는지 확인합니다.

## 서비스 확장 설정

`Notification Service Extension`은 앱과 함께 번들로 제공되는 자체 바이너리입니다. [Apple 개발자 포털에서](https://developer.apple.com) 자체 앱 ID 및 프로비저닝 프로필을 사용하여 설정해야 합니다.

`Notification Service Extension`의 번들 ID는 기본 앱 대상의 번들 ID와 구별되어야 합니다. 예를 들어 앱의 번들 ID가 `com.company.appname`인 경우 서비스 확장에 `com.company.appname.AppNameServiceExtension`을 사용할 수 있습니다.

### Braze와 함께 작동하도록 서비스 확장 구성하기

Braze는 `ab` 키 아래 APN 페이로드에 리치 콘텐츠를 구성, 다운로드 및 표시하는 데 사용하는 첨부 파일 페이로드를 전송합니다. 예를 들어, 다음과 같습니다.

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

관련 페이로드 값은 다음과 같습니다:

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Braze 페이로드가 포함된 푸시를 수동으로 표시하려면 `AppboyAPNSDictionaryAttachmentURLKey` 아래의 값에서 콘텐츠를 다운로드하고 `AppboyAPNSDictionaryAttachmentTypeKey` 키 아래에 저장된 파일 형식으로 파일로 저장한 다음, 알림 첨부 파일에 추가합니다.

### 코드 예제

서비스 확장은 Objective-C 또는 Swift로 작성할 수 있습니다.

Objective-C 샘플 코드를 사용하려면 `Notification Service Extension` 대상에서 자동 생성된 `NotificationService.m`의 콘텐츠를 Appboy [`NotificationService.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m)으로 바꿉니다.

Swift 샘플 코드를 사용하려면 `Notification Service Extension` 대상에서 자동 생성된 `NotificationService.swift`의 콘텐츠를 Appboy [`NotificationService.swift`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift)로 바꿉니다.

## 대시보드에서 리치 알림 만들기

Braze 대시보드에서 리치 알림을 만들려면 iOS 푸시를 만들고, 이미지 또는 GIF를 첨부하거나, 이미지, GIF 또는 동영상을 호스팅하는 URL을 입력합니다. 푸시 알림을 받으면 자산이 다운로드되므로 콘텐츠를 호스팅하는 경우 요청이 동시에 급증하는 상황에 대비해야 합니다.

지원되는 파일 형식 및 크기 목록은 [`unnotificationattachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment) 에서 지원되는 파일 유형 및 크기 목록을 확인하세요.

