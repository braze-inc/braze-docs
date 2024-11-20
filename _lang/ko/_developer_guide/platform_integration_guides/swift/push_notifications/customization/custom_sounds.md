---
nav_title: 사용자 지정 사운드
article_title: iOS용 사용자 지정 푸시 알림 소리
platform: Swift
page_order: 3
description: "이 문서에서는 Swift SDK에서 iOS 커스텀 사운드를 구현하는 방법을 다룹니다."
channel:
  - push

---

# 사용자 지정 사운드

## 1단계: 앱에서 사운드 호스팅하기

사용자 지정 푸시 알림 사운드는 앱의 기본 번들 내에서 로컬로 호스팅해야 합니다. 허용되는 오디오 데이터 형식은 다음과 같습니다:

- 선형 PCM
- MA4
- µLaw
- aLaw

오디오 데이터를 AIFF, WAV 또는 CAF 파일로 패키징할 수 있습니다. Xcode에서 사운드 파일을 프로젝트에 애플리케이션 번들의 지역화되지 않은 리소스로 추가합니다.

{% alert note %}
사용자 지정 사운드는 재생 시 30초 미만이어야 합니다. 커스텀 사운드가 이 제한을 초과하면 기본 시스템 사운드가 대신 재생됩니다.
{% endalert %}

### 사운드 파일 변환

afconvert 도구를 사용하여 사운드를 변환할 수 있습니다. 예를 들어 16비트 선형 PCM 시스템 사운드 Submarine.aiff를 CAF 파일에서 IMA4 오디오로 변환하려면 터미널에서 다음 명령을 사용합니다.

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
QuickTime Player에서 사운드를 열고 **동영상** 메뉴에서 **동영상 검사기 표시를** 선택하면 사운드를 검사하여 데이터 형식을 확인할 수 있습니다.
{% endalert %}

## 2단계: 사운드에 대한 프로토콜 URL 제공

앱에서 사운드 파일의 위치로 연결되는 프로토콜 URL을 지정해야 합니다. 이를 수행하는 방법에는 두 가지가 있습니다:

* [Apple 푸시 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object)의 `sound` 매개변수를 사용하여 URL을 Braze에 전달합니다.
* 대시보드에서 URL을 지정합니다. [푸시 작성기]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android)에서 **설정**을 선택하고 **사운드** 필드에 프로토콜 URL을 입력합니다. 

![Braze 대시보드의 푸시 작성기]({% image_buster /assets/img_archive/sound_push_ios.png %})

지정한 사운드 파일이 존재하지 않거나 'default' 키워드가 입력된 경우 Braze는 기기의 기본 알림 사운드를 사용합니다. 대시보드 외에도 [메시징 API][12]를 통해 사운드를 구성할 수도 있습니다.

자세한 내용은 [사용자 지정 경고음 준비에](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) 관한 Apple 개발자 문서를 참조하세요.

