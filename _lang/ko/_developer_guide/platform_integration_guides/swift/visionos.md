---
nav_title: visionOS 지원
article_title: visionOS 지원
page_order: 7.2
platform: 
  - iOS
description: "이 문서에서는 visionOS에서 지원되는 기능에 대해 설명합니다."
---

# visionOS 지원

> [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)부터 Apple Viwion Pro용 공간 컴퓨팅 플랫폼인 [visonOS](https://developer.apple.com/visionos/)에서 Braze를 활용할 수 있습니다. Braze를 사용하는 visonOS 앱 샘플은 [샘플 앱]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sample_apps/)을 참조하세요.

## 완벽하게 지원되는 기능

iOS에서 사용할 수 있는 대부분의 기능은 visonOS에서도 사용할 수 있습니다.

- 애널리틱스(세션, 사용자 지정 이벤트, 구매 등)
- 인앱 메시징(데이터 모델 및 UI)
- 콘텐츠 카드(데이터 모델 및 UI)
- 푸시 알림(사용자가 볼 수 있는 동작 버튼 및 무음 알림)
- 피처 플래그
- 위치 분석

## 부분적으로 지원되는 기능

일부 기능이 visionOS에서 부분적으로만 지원되지만, 앞으로 Apple에서 이러한 문제를 해결할 가능성이 큽니다.

- 풍부한 푸시 알림
  - 이미지가 지원됩니다.
  - GIF 및 동영상은 미리보기 이미지로 표시되지만 재생할 수는 없습니다.
  - 오디오 재생은 지원되지 않습니다.
- 푸시 스토리
  - 푸시 스토리 페이지 스크롤 및 선택이 지원됩니다.
  - **다음을** 사용하여 푸시 스토리 페이지 간에 이동하는 기능은 지원되지 않습니다.

## 지원되지 않는 기능

- 지오펜스 모니터링은 지원되지 않습니다. Apple은 visionOS에서 지역 모니터링을 위한 핵심 위치 API를 제공하지 않습니다.
- 라이브 활동은 지원되지 않습니다. 현재 ActivityKit는 iOS 및 iPadOS에서만 사용할 수 있습니다.
