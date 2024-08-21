---
nav_title: 9月
page_order: 3
noindex: true
page_type: update
description: "この記事には2021年9月のリリースノートが含まれています。"
---

# 2021年9月

## iOS 15

### アップルメールプライバシー保護 

AppleのMailプライバシー保護（MPP）は、iOS 15、iPadOS 15、MacOS Monterey、およびwatchOS 8のApple Mailアプリのユーザーが利用できるプライバシー更新であり、9月中旬にリリースされます。MPPにオプトインしたユーザーの場合、メールはプロキシサーバーを使用して事前に読み込まれ、画像がキャッシュされ、[開封トラッキング]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel)のようなメトリクスのためのトラッキングピクセルを活用する能力が妨げられます。MPPおよびメール配信メトリクスに関する問題、既存のキャンペーンおよびこれらのメトリクスに基づいてトリガーされるキャンバスに関する問題の詳細については、当社の[ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/)をご覧ください。

### 機能をプッシュ

iOS 15は、ユーザーが集中力を維持し、1日を通して頻繁な中断を避けるのに役立つ新しい通知機能を導入しました。これらの新機能、特に[中断レベルと関連性スコア]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)のサポートを提供できることを嬉しく思います。

## 連絡先カード

連絡先カードは、アドレス帳や連絡先帳に簡単にインポートできるビジネスおよび連絡先情報を送信するための標準化されたファイル形式です。これで、SMSおよびMMSメッセージ用の連絡先カードをアップロードして作成できるようになりました。組み込みの連絡先カードジェネレーターで連絡先カードの作成方法について詳しく読むには、私たちの[ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)をご覧ください。

## デフォルトコンテンツカードのカスタマイズ

`ABKContentCardsTableViewController` を拡張してすべての UI 要素とコンテンツカードの動作をカスタマイズすることで、独自のコンテンツカードインターフェイスを作成できます。コンテンツカードフィードのカスタマイズ方法の詳細については、[ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization/customizing_feed/)をご覧ください。 

## APIレート制限

[レート制限]({{site.baseurl}}/api/basics/#api-limits/)は、2021年9月16日以降にオンボードされたすべての顧客に適用されます。 

## AndroidおよびFireOS開発者ガイドの更新

AndroidとFireOSの開発者ガイドが1つの場所に統合されました。専用のFireOS記事は、この[新しいAndroidセクション]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/)で利用可能になります。

## ファネルおよびリテンションレポートの更新

[ファンネルレポート]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/)と[リテンションレポート]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/)は、SMSキャンペーンで利用できるようになりました。
