---
nav_title: 9月
page_order: 3
noindex: true
page_type: update
description: "この記事には2021年9月のリリースノートが含まれている。"
---

# 2021年9月

## iOS 15

### アップル・メールのプライバシー保護 

アップルのMail Privacy Protection（MPP）は、9月中旬にリリースされるiOS 15、iPadOS 15、macOS Monterey、watchOS 8のApple Mailアプリのユーザー向けに提供されるプライバシーアップデートだ。MPPをオプトインしたユーザーは、プロキシサーバーを使用してメールがプリロードされ、画像がキャッシュされ、[開封トラッキングなどの]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel)指標にトラッキングピクセルを活用することができなくなる。MPPの詳細や、メール配信メトリクスの問題、既存のキャンペーンやCanvaseがこれらのメトリクスのトリガーとなる問題については、当社の[ドキュメントを]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/)ご覧ください。

### プッシュ機能

iOS15は、ユーザーが集中力を維持し、一日中頻繁な中断を避けるための新しい通知機能を導入した。[中断レベルや関連性スコアなど]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)、これらの新機能のサポートを提供できることをうれしく思う。

## 連絡先カード

コンタクトカードは、ビジネスや連絡先情報を送信するための標準化されたファイルフォーマットで、アドレス帳や連絡帳に簡単にインポートできる。SMSやMMSメッセージに連絡先カードをアップロードして作成できるようになった。内蔵のコンタクト・カード・ジェネレーターでコンタクト・カードを作成する方法については、[ドキュメントを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)参照されたい。

## デフォルト・コンテンツ・カードのカスタマイズ

`ABKContentCardsTableViewController` を拡張してすべての UI 要素とコンテンツカードの動作をカスタマイズすることで、独自のコンテンツカードインターフェイスを作成できます。コンテンツ・カード・フィードのカスタマイズ方法の詳細については、[ドキュメントを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization/customizing_feed/)ご覧いただきたい。 

## APIレート制限

[料金制限は]({{site.baseurl}}/api/basics/#api-limits/)2021年9月16日以降に搭乗するすべての顧客に適用される。 

## AndroidとFireOSの開発者向けガイドを更新

AndroidとFireOSの開発者ガイドは1つの場所に統合された。FireOSの記事は、この[新しいAndroidセクションで]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/)読むことができる。

## ファネルとリテンションレポートの更新

[ファネルレポートと]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/) [リテンションレポートが]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/)SMSキャンペーンで利用可能になった。
