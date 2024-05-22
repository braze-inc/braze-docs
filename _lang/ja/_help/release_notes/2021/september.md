---
nav_title: 9 月
page_order: 3
noindex: true
page_type: update
description: "この記事には、2021 年 9 月のリリース ノートが含まれています。"
---

# 2021年9月発売

## iOSの15

### Apple Mailのプライバシー保護 

Appleのメールプライバシー保護(MPP)は、9月中旬にリリースされたiOS 15、iPadOS 15、macOS Monterey、およびwatchOS 8のApple Mailアプリのユーザーが利用できるプライバシーアップデートです。MPPにオプトインしたユーザーの場合、メールはプロキシサーバーを使用してプリロードされ、画像をキャッシュし、 [オープントラッキング]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel)などの指標にトラッキングピクセルを活用する機能が妨げられます。MPPとメール配信品質指標に関する問題、およびこれらの指標に基づいてトリガーされる既存のキャンペーンとキャンバスの問題の詳細については、 [ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/)をご覧ください。

### プッシュ機能

iOS 15 では、ユーザーが集中力を維持し、一日中頻繁に中断されるのを避けるのに役立つ新しい通知機能が導入されました。中断 [レベルや関連性スコア]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)など、これらの新機能のサポートを提供できることを嬉しく思います。

## 連絡先カード

連絡先カードは、勤務先情報や連絡先情報を送信するための標準化されたファイル形式で、アドレス帳や連絡帳に簡単にインポートできます。SMSおよびMMSメッセージの連絡先カードをアップロードして作成できるようになりました。組み込みの連絡先カードジェネレーターで連絡先カードを作成する方法の詳細については、 [ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)をご覧ください。

## 既成のコンテンツカードのカスタマイズ

拡張 `ABKContentCardsTableViewController` してすべての UI 要素とコンテンツ カードの動作をカスタマイズすることで、独自のコンテンツ カード インターフェイスを作成できます。コンテンツカードフィードをカスタマイズする方法の詳細については、 [ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization/customizing_feed/)をご覧ください。 

## API レート制限

[レート制限]({{site.baseurl}}/api/basics/#api-limits/) は、2021 年 9 月 16 日以降にオンボードされたすべてのお客様に適用されます。 

## Android および FireOS 開発者ガイドの更新

Android と FireOS の開発者ガイドが 1 か所に統合されました。FireOS に関する記事は、この新しい [Android セクションで]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/)ご覧いただけます。

## ファネルレポートとリテンションレポートの更新

[ファネルレポート]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/) と [リテンションレポート]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) がSMSキャンペーンで利用できるようになりました。
