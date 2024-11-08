---
nav_title: iOS 16 업그레이드 가이드
article_title: iOS 16 업그레이드 가이드
page_order: 7
platform: 
  - iOS
description: "이 참조 문서에서는 iOS 16, 업그레이드 방법, SDK 업데이트 등을 다룹니다."
hidden: true
noindex: true
---

# iOS 16 SDK 업그레이드 가이드

> 이 가이드에서는 iOS 16(2022)에 도입된 관련 변경 사항과 Braze iOS SDK 통합에 미치는 영향을 설명합니다. 전체 마이그레이션 가이드는 [iOS 16 릴리스 노트를](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes) 참조하세요.

## iOS 16의 변경 사항

### Safari 웹 푸시 {#safari-web-push}

Apple은 웹 푸시 기능에 대한 두 가지 변경 사항을 발표했습니다.

#### 데스크톱 웹 푸시(MacOS) {#macos-push}

이전에 Apple은 자체 Safari 푸시 API를 사용하여 macOS(데스크톱)에서 푸시 알림을 지원했습니다.

macOS Ventura(2022년 10월 24일 출시)부터 [Safari](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos)는 Safari 푸시 외에 웹 푸시 API에 대한 지원을 추가했습니다. 이는 다른 인기 브라우저에서 사용되는 기존의 크로스 브라우저 API 표준입니다.

이미 Braze를 통해 Safari용 웹 푸시를 전송하고 있다면 변경할 필요가 없습니다.

#### 모바일 웹 푸시(iOS 및 iPadOS) {#ios-push}

이전에는 iPhone 및 iPad의 Safari에서 푸시 알림 수신을 지원하지 않았습니다.

2023년에 Apple은 iPhone 및 iPad 기기에서 Safari를 통해 웹 푸시 지원을 추가할 예정입니다.

Braze는 추가 변경이나 업그레이드 없이 이 새로운 iOS 및 iPadOS 웹 푸시를 지원합니다.

## iOS 16 준비 {#next-steps}

iOS 16에서 Braze iOS SDK를 업그레이드할 필요는 없지만, 두 가지 흥미로운 업데이트가 있습니다.

1. Braze에서 [새로운 Swift SDK를](https://github.com/braze-inc/braze-swift-sdk) 출시했습니다. 여기에서는 향상된 성능, 새로운 기능 및 많은 개선 사항을 제공합니다.
2. Braze Swift SDK는 새로운 ['노코드' 푸시 프라이머 기능]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)을 지원합니다!

