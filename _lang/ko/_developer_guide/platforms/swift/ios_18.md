---
nav_title: iOS 18로 업그레이드
article_title: iOS 18로 업그레이드
page_order: 7.1
platform: 
  - iOS
description: "이 문서에서는 SDK를 원활하게 업그레이드하는 데 도움이 되는 iOS 18 릴리스에 대한 인사이트를 다룹니다."
---

# iOS 18로 업그레이드

> Braze가 곧 출시될 iOS 버전을 어떻게 준비하고 있는지 궁금하신가요? 이 문서에는 사용자와 사용자의 고객에게 원활한 경험을 제공하는 데 도움이 되는는 iOS 18 릴리스에 대한 인사이트를 요약하여 제공합니다.

Apple의 [WWDC](https://developer.apple.com/wwdc24/)는 2024년 6월 9일부터 11일까지 진행되었습니다. [블로그 게시물](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18)에서 해당 발표 내용을 자세히 알아보세요. 또는 Braze에서 iOS 18을 활용하는 방법을 읽어보세요.

## iOS 18의 변경 사항

### Apple Watch의 실시간 활동

[라이브 활동](https://www.braze.com/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift)은 watchOS 11에서 지원됩니다. 추가 설정이 필요하지 않습니다. 그러나 Apple은 시계 인터페이스를 사용자 정의할 수 있는 옵션을 제공합니다.

### Apple Vision Pro

현재 중국, 일본, 싱가포르, 호주, 캐나다, 프랑스, 독일, 영국에서 Vision Pro를 사용할 수 있습니다. [Braze가 비전OS를 지원하는 방법](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support)은 Braze 블로그에서 확인하세요.

### macOS의 iPhone 알림

Apple의 새로운 [iPhone 미러링](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) 기능을 사용하면 macOS 기기에서 iPhone 알림을 받을 수 있습니다. 푸시 스토리 이미지 및 GIF와 같은 일부 미디어 유형은 macOS 알림으로 렌더링할 수 없으므로 지원되지 않습니다.

### Apple 인텔리전스

[Apple 인텔리전스](https://developer.apple.com/documentation/Updates/Apple-Intelligence)는 이제 iOS 18.1 이상을 실행하는 기기에서 사용할 수 있습니다.

Braze 사용자로서 가장 중요한 새로운 기능은 [알림 요약](https://support.apple.com/en-us/108781)입니다. 이 기능은 장치 내 처리 기능을 사용하여 단일 앱에서 전송된 관련 푸시 알림에 대한 텍스트 요약을 자동으로 그룹화하고 생성합니다. 최종 사용자는 요약을 탭하여 확장하고 원래 전송된 각 푸시 알림을 볼 수 있습니다.

이 요약이 생성되는 방식 때문에 특정 동작이나 생성된 텍스트에 대한 제어권이 없습니다. 그러나 이는 푸시 클릭 추적과 같은 분석 또는 보고 기능에 영향을 미치지 않습니다.

![푸시 알림 미리보기 요약의 샘플 스크린샷.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})
