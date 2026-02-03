---
nav_title: iOS 18 へのアップグレード
article_title: iOS 18 へのアップグレード
page_order: 7.1
platform: 
  - iOS
description: "この記事では、SDKをシームレスにアップグレードするのに役立つ、iOS 18リリースに関する洞察を紹介する。"
---

# iOS 18 へのアップグレード

> Brazeが次のiOSリリースに向けてどのように準備しているか気になりますか？この記事は、iOS 18のリリースに関する我々の洞察をまとめたもので、あなたとあなたのユーザーのシームレスなエクスペリエンス作りに役立つ。

Apple の [WWDC](https://developer.apple.com/wwdc24/) は、2024年6月9日～11日まで行われました。発表の詳細については、[ブログ記事](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18)をご覧ください。また、Braze で iOS 18 を活用する方法についてもご覧ください。

## iOS 18の変更点

### Apple Watchでのライブ活動

[Live Activities](https://www.braze.com/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift) は、watchOS 11 でサポートされる予定です。追加の設定は必要ありません。ただし、Apple では、ウォッチインターフェイスをカスタマイズするオプションが用意されています。

### Apple Vision Pro

Apple Vision Pro は現在、中国、日本、シンガポール、オーストラリア、カナダ、フランス、ドイツ、英国で販売されています。[Braze が visionOS どのようにサポートしているか](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support)については、弊社のブログをご覧ください。

### macOSでiPhoneの通知を受ける

アップルの新しい[iPhoneミラーリング](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/)機能により、ユーザーはmacOSデバイスでiPhoneの通知を受け取ることができる。プッシュストーリーの画像やGIFなど、一部のメディアタイプはmacOS通知としてレンダリングできないため、サポートされていないことに留意してほしい。

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) は、iOS 18.1 以降を実行しているデバイスで使用できるようになりました。

Braze ユーザーとして、知っておくべき最も重要な新機能は[通知サマリ](https://support.apple.com/en-us/108781)です。これは、デバイス上の処理を使用して、1 つのアプリから送信される関連するプッシュ通知のテキストサマリを自動的にグループ化して生成します。エンドユーザーは、タップしてサマリーを展開し、最初に送信されたときの各プッシュ通知を表示できます。

これらの要約はどのように生成されるかにより、それらの特定の動作や生成されたテキストを制御することはできません。ただし、プッシュクリックトラッキングなどの分析機能やレポート機能には影響しません。

![プッシュ通知のプレビューサマリーのサンプルスクリーンショット。]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})
