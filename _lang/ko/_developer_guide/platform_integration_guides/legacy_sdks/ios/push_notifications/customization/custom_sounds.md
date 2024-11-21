---
nav_title: 사용자 지정 사운드
article_title: iOS용 사용자 지정 푸시 알림 소리
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 푸시 알림에서 커스텀 사운드를 구현하는 방법을 다룹니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 사용자 지정 사운드

## 1단계: 앱에서 사운드 호스팅하기

사용자 지정 푸시 알림 사운드는 클라이언트 애플리케이션의 기본 번들 내에서 로컬로 호스팅해야 합니다. 허용되는 오디오 데이터 형식은 다음과 같습니다:

- 선형 PCM
- MA4
- µLaw
- aLaw

오디오 데이터를 AIFF, WAV 또는 CAF 파일로 패키징할 수 있습니다. Xcode에서 사운드 파일을 프로젝트에 애플리케이션 번들의 지역화되지 않은 리소스로 추가합니다.

afconvert 툴을 사용하여 사운드를 변환할 수 있습니다. 예를 들어 16비트 선형 PCM 시스템 사운드 Submarine.aiff를 CAF 파일에서 IMA4 오디오로 변환하려면 터미널에서 다음 명령을 사용합니다.

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

QuickTime Player에서 사운드를 열고 **동영상** 메뉴에서 **동영상 검사기 표시**를 선택해 사운드를 검사하여 데이터 형식을 확인할 수 있습니다.

사용자 지정 사운드는 재생 시 30초 미만이어야 합니다. 커스텀 사운드가 이 제한을 초과하면 기본 시스템 사운드가 대신 재생됩니다.

## 2단계: 대시보드에 사운드에 대한 프로토콜 URL 제공

사운드는 앱 내에서 로컬로 호스팅되어야 합니다. 푸시 작성기의 **사운드** 필드 내에서 앱의 사운드 파일 위치로 연결되는 프로토콜 URL을 지정해야 합니다. 이 필드에서 '기본값'을 지정하면 기기에서 기본 알림 사운드가 재생됩니다. 이는 다음 스크린샷과 같이 [메시징 API]({{site.baseurl}}/api/endpoints/messaging/) 또는 푸시 작성기의 **설정** 아래 대시보드를 통해 지정할 수 있습니다:

![]({% image_buster /assets/img_archive/sound_push_ios.png %})

지정한 사운드 파일이 존재하지 않거나 'default' 키워드가 입력된 경우 Braze는 기기의 기본 알림 사운드를 사용합니다. 대시보드 외에도 [메시징 API를]({{site.baseurl}}/api/endpoints/messaging/) 통해 사운드를 구성할 수도 있습니다. 자세한 내용은 [사용자 지정 경고음 준비에](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) 관한 Apple 개발자 문서를 참조하세요.

