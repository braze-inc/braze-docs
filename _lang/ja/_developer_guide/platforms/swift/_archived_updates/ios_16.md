---
nav_title: iOS 16アップグレードガイド
article_title: iOS 16アップグレードガイド
page_order: 7
platform: 
  - iOS
description: "この参考記事では、iOS 16、アップグレード方法、SDK アップデートなどについて説明します。"
hidden: true
noindex: true
---

# iOS 16 SDK アップグレードガイド

> このガイドでは、iOS 16 (2022) で導入された関連する変更と、Braze iOS SDK 統合への影響について説明します。完全な移行ガイドについては、[iOS 16リリースノート](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes)を参照してください。

## iOS 16での変更点

### Safari Web プッシュ {#safari-web-push}

Apple は、Web プッシュ機能に対する2つの変更を発表しました。

#### デスクトップ Web プッシュ (MacOS) {#macos-push}

以前、Apple は独自の Safari プッシュ API を使用して macOS (デスクトップ) でのプッシュ通知をサポートしていました。

macOS Ventura (2022年10月24日リリース) 以降、[Safari には、Safari プッシュに加えて Web プッシュ API のサポートが追加されました](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos)。これは、他の一般的なブラウザで使用されている既存のクロスブラウザー API 標準です。

すでに Braze 経由で Safari 用 Web プッシュを送信している場合は、変更する必要はありません。

#### モバイル Web プッシュ (iOS および iPadOS) {#ios-push}

以前は、iPhone および iPad の Safari はプッシュ通知の受信をサポートしていませんでした。

2023年に、Apple は Safari を介した iPhone および iPad デバイスでの Web プッシュのサポートを追加する予定です。

Braze は、追加の変更やアップグレードを必要とせずに、この新しい iOS および iPadOS の Web プッシュをサポートします。

## iOS 16への準備 {#next-steps}

Braze iOS SDK を iOS 16用にアップグレードする必要はありませんが、他に 2 つの興味深い更新があります。

1. Braze は [新しい Swift SDK](https://github.com/braze-inc/braze-swift-sdk)をリリースしました。これにより、パフォーマンスの向上、新機能、および多くの改善がもたらされます。
2. 当社の Braze Swift SDK は、新しい[「コードなし」プッシュプライマー機能]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)をサポートしています。

